/**
 * Motor cliente: un paso por pantalla, Comprobar, XP y repaso.
 * Se monta sobre [data-lesson-player] con JSON embebido.
 */
import {
  commandMatches,
  fillMatches,
  type Paso,
  type PasoCodigo,
  type PasoQuiz,
  type PasoTerminal,
} from './lesson-schema';
import {
  completePaso,
  enqueueRepaso,
  getPasoProgress,
  loadProgress,
  setPasoActual,
  touchMateria,
} from './progress-client';

export type PlayerPaso = Paso & { cuerpoHtml?: string; enunciadoHtml?: string };

export type PlayerPayload = {
  materiaId: string;
  leccionId: string;
  titulo: string;
  pasos: PlayerPaso[];
  nextLeccionHref?: string | null;
  materiaHref: string;
  lecturaComplementariaHtml?: string;
};

type CheckResult = { ok: boolean; message: string };

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function runCodigoTests(paso: PasoCodigo, code: string): CheckResult {
  try {
    // Scope aislado: el alumno define funciones/vars; luego se evalúan asserts.
    const fn = new Function(
      `${code}\n; return [${paso.tests.map((t) => `(${t.assert})`).join(',')}];`,
    );
    const results = fn() as boolean[];
    const failed = paso.tests.filter((_, i) => !results[i]);
    if (failed.length) {
      return {
        ok: false,
        message:
          paso.explicacionError ||
          `Falló: ${failed.map((t) => t.nombre).join(', ')}`,
      };
    }
    return { ok: true, message: 'Todos los tests pasaron.' };
  } catch (e) {
    return {
      ok: false,
      message: `Error al ejecutar: ${e instanceof Error ? e.message : String(e)}`,
    };
  }
}

function checkQuiz(paso: PasoQuiz, answer: string | string[]): CheckResult {
  if (paso.variante === 'completar') {
    const text = Array.isArray(answer) ? answer[0] ?? '' : answer;
    const ok = fillMatches(text, paso.respuesta, paso.normalizar !== false);
    return {
      ok,
      message: ok
        ? paso.explicacionOk || 'Correcto.'
        : paso.explicacionError,
    };
  }
  const expected = Array.isArray(paso.respuesta) ? paso.respuesta : [paso.respuesta];
  const got = Array.isArray(answer) ? answer : [answer];
  const ok =
    expected.length === got.length && expected.every((id) => got.includes(id));
  return {
    ok,
    message: ok ? paso.explicacionOk || 'Correcto.' : paso.explicacionError,
  };
}

function checkTerminal(paso: PasoTerminal, input: string): CheckResult {
  const ok = commandMatches(input, paso.comandoEsperado);
  return {
    ok,
    message: ok ? 'Comando correcto.' : paso.explicacionError,
  };
}

function buildRepasoPayload(paso: PlayerPaso): {
  kind: 'quiz' | 'terminal' | 'codigo';
  prompt: string;
  payload: Record<string, unknown>;
} | null {
  if (paso.tipo === 'quiz') {
    return {
      kind: 'quiz',
      prompt: paso.pregunta,
      payload: {
        variante: paso.variante,
        opciones: paso.opciones,
        respuesta: paso.respuesta,
        explicacionError: paso.explicacionError,
        explicacionOk: paso.explicacionOk,
        normalizar: paso.normalizar,
      },
    };
  }
  if (paso.tipo === 'terminal') {
    return {
      kind: 'terminal',
      prompt: paso.enunciado,
      payload: {
        comandoEsperado: paso.comandoEsperado,
        explicacionError: paso.explicacionError,
      },
    };
  }
  if (paso.tipo === 'codigo') {
    return {
      kind: 'codigo',
      prompt: paso.enunciado,
      payload: {
        starter: paso.starter,
        tests: paso.tests,
        language: paso.language,
        explicacionError: paso.explicacionError,
      },
    };
  }
  return null;
}

export function mountLessonPlayer(root: HTMLElement, data: PlayerPayload) {
  const { materiaId, leccionId, pasos } = data;
  const allIds = pasos.map((p) => p.id);
  const progress = getPasoProgress(materiaId, leccionId);
  let index = 0;
  if (progress.current) {
    const i = pasos.findIndex((p) => p.id === progress.current);
    if (i >= 0) index = i;
  }
  // Query ?paso=
  const params = new URLSearchParams(window.location.search);
  const qPaso = params.get('paso');
  if (qPaso) {
    const i = pasos.findIndex((p) => p.id === qPaso);
    if (i >= 0) index = i;
  }

  touchMateria(materiaId, leccionId, pasos[index]?.id);

  const bar = root.querySelector<HTMLProgressElement>('[data-step-bar]');
  const label = root.querySelector('[data-step-label]');
  const xpEl = root.querySelector('[data-xp-total]');
  const streakEl = root.querySelector('[data-streak]');
  const stage = root.querySelector('[data-step-stage]');
  const feedback = root.querySelector('[data-step-feedback]');
  const btnCheck = root.querySelector<HTMLButtonElement>('[data-step-check]');
  const btnNext = root.querySelector<HTMLButtonElement>('[data-step-next]');
  const complement = root.querySelector('[data-step-complement]');

  function syncHud() {
    const state = loadProgress();
    if (xpEl) xpEl.textContent = String(state?.xp ?? 0);
    if (streakEl) streakEl.textContent = String(state?.racha ?? 0);
    const doneCount = Object.values(progress.done).filter(Boolean).length;
    // refresh done from storage
    const fresh = getPasoProgress(materiaId, leccionId).done;
    Object.assign(progress.done, fresh);
    const completed = allIds.filter((id) => fresh[id]).length;
    const pct = Math.round(((index + 1) / pasos.length) * 100);
    if (bar) {
      bar.value = pct;
      bar.max = 100;
    }
    if (label) {
      label.textContent = `Paso ${index + 1} de ${pasos.length} · ${completed}/${pasos.length} hechos`;
    }
    void doneCount;
  }

  function showFeedback(ok: boolean, message: string) {
    if (!feedback) return;
    feedback.hidden = false;
    feedback.className = `lesson-feedback ${ok ? 'lesson-feedback--ok' : 'lesson-feedback--err'}`;
    feedback.setAttribute('role', 'status');
    feedback.setAttribute('aria-live', 'polite');
    feedback.innerHTML = `<span class="lesson-feedback__icon" aria-hidden="true">${ok ? '✅' : '❌'}</span><p class="m-0">${escapeHtml(message)}</p>`;
  }

  function clearFeedback() {
    if (!feedback) return;
    feedback.hidden = true;
    feedback.textContent = '';
  }

  function renderPaso() {
    const paso = pasos[index];
    if (!paso || !stage) return;
    clearFeedback();
    setPasoActual(materiaId, leccionId, paso.id);
    syncHud();

    const already = Boolean(progress.done[paso.id]);
    if (btnNext) {
      btnNext.hidden = !already;
      btnNext.disabled = !already;
    }
    if (btnCheck) {
      const needsCheck = !['explicacion', 'ejemplo', 'resumen'].includes(paso.tipo);
      if (paso.tipo === 'proyecto') {
        btnCheck.textContent = 'Confirmar rúbrica';
        btnCheck.hidden = already;
      } else if (needsCheck) {
        btnCheck.textContent = 'Comprobar';
        btnCheck.hidden = already;
      } else {
        btnCheck.textContent = 'Entendido';
        btnCheck.hidden = already;
      }
    }

    let body = '';
    const title = `<h2 class="font-display text-xl sm:text-2xl font-semibold m-0 mb-3">${escapeHtml(paso.titulo)}</h2>`;
    const xpBadge = `<p class="text-xs opacity-70 m-0 mb-4">+${paso.xp ?? 10} XP</p>`;

    switch (paso.tipo) {
      case 'explicacion':
      case 'ejemplo':
        body = `${title}${xpBadge}<div class="prose-academia">${paso.cuerpoHtml || escapeHtml(paso.cuerpo)}</div>`;
        if (paso.tipo === 'ejemplo' && paso.caption) {
          body += `<p class="text-sm opacity-70 mt-3 m-0">${escapeHtml(paso.caption)}</p>`;
        }
        break;
      case 'quiz': {
        body = `${title}${xpBadge}<p class="text-base font-medium mb-4">${escapeHtml(paso.pregunta)}</p>`;
        if (paso.variante === 'completar') {
          body += `<label class="form-control w-full max-w-md"><span class="label-text mb-1">Tu respuesta</span>
            <input type="text" class="input input-bordered w-full font-mono" data-answer autocomplete="off" ${already ? 'disabled' : ''} /></label>`;
        } else {
          const opts = paso.opciones ?? [];
          body += `<fieldset class="flex flex-col gap-2 m-0 p-0 border-0" ${already ? 'disabled' : ''}><legend class="sr-only">Opciones</legend>`;
          for (const o of opts) {
            body += `<label class="lesson-choice"><input type="radio" name="quiz-${paso.id}" value="${escapeHtml(o.id)}" data-answer />
              <span>${escapeHtml(o.texto)}</span></label>`;
          }
          body += `</fieldset>`;
        }
        break;
      }
      case 'terminal':
        body = `${title}${xpBadge}<div class="prose-academia mb-4">${paso.enunciadoHtml || escapeHtml(paso.enunciado)}</div>
          <label class="form-control w-full"><span class="label-text mb-1 font-mono text-xs">$</span>
          <input type="text" class="input input-bordered w-full font-mono" data-answer spellcheck="false" autocomplete="off" placeholder="escribe el comando" ${already ? 'disabled' : ''} /></label>`;
        if (paso.pistas?.length) {
          body += `<details class="mt-3 text-sm"><summary class="cursor-pointer opacity-80">Pistas</summary><ul class="mt-2">${paso.pistas.map((p) => `<li>${escapeHtml(p)}</li>`).join('')}</ul></details>`;
        }
        break;
      case 'codigo':
        body = `${title}${xpBadge}<div class="prose-academia mb-4">${paso.enunciadoHtml || escapeHtml(paso.enunciado)}</div>
          <label class="form-control w-full"><span class="label-text mb-1">Código (${paso.language})</span>
          <textarea class="textarea textarea-bordered font-mono text-sm min-h-40 w-full" data-answer spellcheck="false" ${already ? 'disabled' : ''}>${escapeHtml(paso.starter || '')}</textarea></label>
          <p class="text-xs opacity-70 mt-2 m-0">${paso.tests.length} test(s) en el navegador</p>`;
        break;
      case 'proyecto':
        body = `${title}${xpBadge}<div class="prose-academia mb-4">${paso.enunciadoHtml || escapeHtml(paso.enunciado)}</div>
          <p class="font-semibold text-sm m-0 mb-2">Entregables</p><ul class="mb-4">${paso.entregables.map((e) => `<li>${escapeHtml(e)}</li>`).join('')}</ul>
          <p class="font-semibold text-sm m-0 mb-2">Rúbrica (marca al cumplir)</p>
          <div class="flex flex-col gap-2" data-rubrica>`;
        for (const r of paso.rubrica) {
          body += `<label class="lesson-choice"><input type="checkbox" data-rubrica-item value="${escapeHtml(r.id)}" ${already ? 'checked disabled' : ''} />
            <span>${escapeHtml(r.criterio)}</span></label>`;
        }
        body += `</div>`;
        break;
      case 'resumen':
        body = `${title}${xpBadge}<ul class="flex flex-col gap-2 mb-4">${paso.puntos.map((p) => `<li class="leading-relaxed">${escapeHtml(p)}</li>`).join('')}</ul>`;
        if (paso.siguiente) {
          body += `<p class="m-0 opacity-80">${escapeHtml(paso.siguiente)}</p>`;
        }
        break;
    }

    stage.innerHTML = body;
    stage.classList.remove('lesson-stage--enter');
    void stage.offsetWidth;
    stage.classList.add('lesson-stage--enter');

    if (complement) {
      complement.hidden = index < pasos.length - 1 || !data.lecturaComplementariaHtml;
    }
  }

  function finishPaso(paso: PlayerPaso) {
    const { gainedXp, lessonComplete } = completePaso(materiaId, leccionId, paso.id, {
      xp: paso.xp ?? 10,
      allPasoIds: allIds,
    });
    progress.done[paso.id] = true;
    if (gainedXp) showFeedback(true, `+${gainedXp} XP`);
    else showFeedback(true, 'Paso completado.');
    if (btnCheck) btnCheck.hidden = true;
    if (btnNext) {
      btnNext.hidden = false;
      btnNext.disabled = false;
      btnNext.textContent = index >= pasos.length - 1
        ? lessonComplete
          ? 'Lección completa →'
          : 'Cerrar'
        : 'Continuar';
    }
    // disable inputs
    stage?.querySelectorAll<HTMLInputElement | HTMLTextAreaElement>('input, textarea').forEach((el) => {
      el.disabled = true;
    });
    syncHud();
  }

  function onCheck() {
    const paso = pasos[index];
    if (!paso || progress.done[paso.id]) return;

    if (paso.tipo === 'explicacion' || paso.tipo === 'ejemplo' || paso.tipo === 'resumen') {
      finishPaso(paso);
      return;
    }

    if (paso.tipo === 'proyecto') {
      const boxes = [...(stage?.querySelectorAll<HTMLInputElement>('[data-rubrica-item]') ?? [])];
      if (!boxes.length || boxes.some((b) => !b.checked)) {
        showFeedback(false, 'Marca todos los criterios de la rúbrica cuando los hayas cumplido de verdad.');
        return;
      }
      finishPaso(paso);
      return;
    }

    let result: CheckResult = { ok: false, message: 'Sin respuesta' };
    if (paso.tipo === 'quiz') {
      let answer: string | string[] = '';
      if (paso.variante === 'completar') {
        answer = stage?.querySelector<HTMLInputElement>('[data-answer]')?.value ?? '';
      } else {
        const checked = stage?.querySelector<HTMLInputElement>('input[data-answer]:checked');
        answer = checked?.value ?? '';
      }
      result = checkQuiz(paso, answer);
    } else if (paso.tipo === 'terminal') {
      const input = stage?.querySelector<HTMLInputElement>('[data-answer]')?.value ?? '';
      result = checkTerminal(paso, input);
    } else if (paso.tipo === 'codigo') {
      const code = stage?.querySelector<HTMLTextAreaElement>('[data-answer]')?.value ?? '';
      result = runCodigoTests(paso, code);
    }

    if (!result.ok) {
      showFeedback(false, result.message);
      const rep = buildRepasoPayload(paso);
      if (rep) {
        enqueueRepaso({
          id: `${materiaId}:${leccionId}:${paso.id}`,
          materiaId,
          leccionId,
          pasoId: paso.id,
          kind: rep.kind,
          prompt: rep.prompt,
          payload: rep.payload,
        });
      }
      return;
    }

    // Primera vez correcta: agenda repaso en +1 día (sin contar lapse).
    if (paso.tipo === 'quiz' || paso.tipo === 'terminal' || paso.tipo === 'codigo') {
      const rep = buildRepasoPayload(paso);
      const id = `${materiaId}:${leccionId}:${paso.id}`;
      const exists = (loadProgress()?.repaso ?? []).some((r) => r.id === id);
      if (rep && !exists) {
        const tomorrow = new Date();
        tomorrow.setUTCDate(tomorrow.getUTCDate() + 1);
        enqueueRepaso({
          id,
          materiaId,
          leccionId,
          pasoId: paso.id,
          kind: rep.kind,
          prompt: rep.prompt,
          payload: rep.payload,
          due: tomorrow.toISOString().slice(0, 10),
          intervalDays: 1,
          reps: 1,
          lapses: 0,
        });
      }
    }

    showFeedback(true, result.message);
    finishPaso(paso);
  }

  function onNext() {
    if (index >= pasos.length - 1) {
      if (data.nextLeccionHref) window.location.href = data.nextLeccionHref;
      else window.location.href = data.materiaHref;
      return;
    }
    index += 1;
    renderPaso();
  }

  btnCheck?.addEventListener('click', onCheck);
  btnNext?.addEventListener('click', onNext);
  stage?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && (e.target as HTMLElement).matches('input[data-answer]')) {
      e.preventDefault();
      onCheck();
    }
  });

  renderPaso();
  window.addEventListener('academia-progress', syncHud);
}
