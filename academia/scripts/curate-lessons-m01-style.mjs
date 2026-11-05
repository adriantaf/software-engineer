#!/usr/bin/env node
/**
 * Re-cura lecciones al estilo M01:
 * explicación propia, 2–3 ejemplos, quizzes progresivos,
 * reto (terminal/código), resumen; última lección → proyecto con rúbrica.
 *
 * No toca M01 (curada a mano) salvo --force-m01.
 *
 * Uso:
 *   node scripts/curate-lessons-m01-style.mjs
 *   node scripts/curate-lessons-m01-style.mjs M02 M07
 *   node scripts/curate-lessons-m01-style.mjs --dry-run M03
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import { parseLeccionPasos } from '../src/lib/lesson-schema.ts';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');
const etapasRoot = path.join(repoRoot, 'curriculum/etapas');

const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const forceM01 = args.includes('--force-m01');
const filter = new Set(
  args.filter((a) => !a.startsWith('--')).map((a) => a.toUpperCase()),
);

function truncate(s, n) {
  const t = String(s || '').replace(/\s+/g, ' ').trim();
  if (t.length <= n) return t;
  return `${t.slice(0, n - 1).trim()}…`;
}

/** Truncate without collapsing newlines (for code fences). */
function truncateCode(s, n) {
  const t = String(s || '').replace(/\r/g, '').trim();
  if (t.length <= n) return t;
  return `${t.slice(0, n - 1).trimEnd()}\n…`;
}

function stripNoise(s) {
  return String(s || '')
    .replace(/\r/g, '')
    .replace(/^#+\s+.+$/m, '')
    .trim();
}

/** Original lesson body: after complementary header, or whole content. */
function extractSourceBody(content) {
  const marker = '## Lectura complementaria';
  const idx = content.indexOf(marker);
  if (idx >= 0) {
    let rest = content.slice(idx + marker.length).trim();
    // drop the helper paragraph inserted by migrator
    rest = rest.replace(
      /^Contenido original de la lección[\s\S]*?\n\n/,
      '',
    );
    // if nested H1 from original, keep from there
    return rest.trim();
  }
  return content.trim();
}

function parseSections(content) {
  const lines = content.replace(/\r/g, '').split('\n');
  const sections = {};
  let current = '_intro';
  const buf = [];
  const flush = () => {
    sections[current] = buf.join('\n').trim();
    buf.length = 0;
  };
  for (const line of lines) {
    const m = /^(#{2})\s+(.+?)\s*$/.exec(line);
    if (m) {
      flush();
      current = m[2].replace(/[*_`]/g, '').trim();
      continue;
    }
    buf.push(line);
  }
  flush();
  return sections;
}

function findSection(sections, ...names) {
  const keys = Object.keys(sections);
  for (const name of names) {
    const exact = keys.find((k) => k.toLowerCase() === name.toLowerCase());
    if (exact) return sections[exact];
    const soft = keys.find((k) => k.toLowerCase().startsWith(name.toLowerCase()));
    if (soft) return sections[soft];
  }
  return '';
}

function parseSubsteps(pasosBody) {
  if (!pasosBody) return [];
  const parts = pasosBody.split(/\n(?=###\s+)/);
  const out = [];
  for (const part of parts) {
    const m = /^###\s+(.+?)\s*\n([\s\S]*)$/.exec(part.trim());
    if (!m) continue;
    const title = m[1].replace(/\s*\([^)]*\)\s*$/, '').replace(/^\d+\.\s*/, '').trim();
    const body = m[2].trim();
    const codes = [];
    const re = /```(\w+)?\n([\s\S]*?)```/g;
    let cm;
    while ((cm = re.exec(body))) {
      codes.push({ lang: (cm[1] || 'text').toLowerCase(), code: cm[2].trim() });
    }
    const prose = body
      .replace(/```[\s\S]*?```/g, '')
      .replace(/\n{3,}/g, '\n\n')
      .trim();
    out.push({ title, body, prose, codes });
  }
  return out;
}

function listItems(text) {
  return String(text || '')
    .split('\n')
    .map((l) => l.replace(/^\s*(?:[-*]|\d+\.)\s+/, '').trim())
    .filter((l) => l && !l.startsWith('|') && !/^#/.test(l) && l.length > 3);
}

function allBashCommands(text) {
  const out = [];
  const fences = [...String(text).matchAll(/```(?:bash|sh|shell|zsh)?\n([\s\S]*?)```/gi)];
  for (const f of fences) {
    for (const raw of f[1].split('\n')) {
      const line = raw.trim().replace(/^\$\s*/, '');
      if (!line || line.startsWith('#') || line.includes('<<')) continue;
      if (line.length > 140) continue;
      if (
        /^(cd|ls|mkdir|pwd|git|npm|npx|node|cat|echo|grep|find|chmod|touch|mv|cp|rm|pnpm|yarn|docker|curl|wget|python|pip|cargo|go|make|sudo|tsc|vitest|prisma|psql|ssh)\b/.test(
          line,
        )
      ) {
        out.push(line);
      }
    }
  }
  return [...new Set(out)];
}

function codeFences(text, prefer = ['ts', 'typescript', 'js', 'javascript', 'tsx', 'json', 'sql', 'py', 'python']) {
  const fences = [...String(text).matchAll(/```(\w+)?\n([\s\S]*?)```/g)];
  const ranked = [];
  for (const lang of prefer) {
    for (const f of fences) {
      if ((f[1] || '').toLowerCase() === lang && f[2].trim().length > 8) {
        ranked.push({ lang: f[1] || 'text', code: f[2].trim() });
      }
    }
  }
  for (const f of fences) {
    const item = { lang: f[1] || 'text', code: f[2].trim() };
    if (item.code.length > 8 && !ranked.some((r) => r.code === item.code)) ranked.push(item);
  }
  return ranked;
}

function introProse(sections, titulo) {
  const objetivo = findSection(sections, 'Objetivo').trim();
  const why = findSection(
    sections,
    'Por qué empieza así',
    'Por qué importa',
    'Idea clave',
    'Conceptos',
    'Contexto',
    'Por qué existe',
  ).trim();
  const intro = (sections._intro || '')
    .split('\n')
    .filter((l) => !/^#\s/.test(l) && !/^\*\*~/.test(l) && !/^L\d{2}\b/.test(l))
    .join('\n')
    .trim();

  const parts = [];
  if (why) parts.push(why);
  else if (intro) parts.push(truncate(intro.replace(/\n+/g, '\n\n'), 900));
  if (objetivo) parts.push(`**Objetivo de esta lección:** ${objetivo}`);
  if (!parts.length) {
    parts.push(
      `En **${titulo}** practicas con criterio: lees poco, produces evidencia y compruebas que entiendes antes de avanzar.`,
    );
  }
  parts.push(
    'Los libros y el detalle largo quedan como **lectura complementaria** al final. Aquí el foco es entender y demostrar.',
  );
  return parts.join('\n\n');
}

function ejemploFromSubstep(sub, fallbackCode) {
  const title = truncate(sub?.title || 'Ejemplo práctico', 70);
  if (sub?.codes?.[0]) {
    const c = sub.codes[0];
    return {
      tipo: 'ejemplo',
      titulo: title,
      xp: 10,
      cuerpo: `\`\`\`${c.lang}\n${truncateCode(c.code, 1200)}\n\`\`\`${sub.prose ? `\n\n${truncate(sub.prose, 400)}` : ''}`,
      caption: 'Practícalo en tu entorno; no te limites a leerlo.',
    };
  }
  if (fallbackCode) {
    return {
      tipo: 'ejemplo',
      titulo: title,
      xp: 10,
      cuerpo: `\`\`\`${fallbackCode.lang}\n${truncateCode(fallbackCode.code, 1200)}\n\`\`\``,
      caption: 'Ejemplo tomado de la lección — córrelo o adáptalo.',
    };
  }
  return {
    tipo: 'ejemplo',
    titulo: title,
    xp: 10,
    cuerpo: truncate(sub?.prose || sub?.body || 'Sigue el procedimiento en la lectura complementaria y deja evidencia en `projects/`.', 1000),
  };
}

function distractorsFor(topic) {
  return [
    `Instalar herramientas al azar sin evidencia de ${truncate(topic, 40)}`,
    'Marcar la lección hecha sin producir nada verificable',
    'Saltar a otra materia dejando esta a medias',
  ];
}

function loadMateriaMeta(materiaId) {
  for (const etapa of fs.readdirSync(etapasRoot)) {
    const etapaDir = path.join(etapasRoot, etapa);
    if (!fs.statSync(etapaDir).isDirectory()) continue;
    const ficha = fs
      .readdirSync(etapaDir)
      .find((f) => f.startsWith(`${materiaId}-`) && f.endsWith('.md'));
    if (!ficha) continue;
    const { data } = matter(fs.readFileSync(path.join(etapaDir, ficha), 'utf8'));
    return {
      practicas: Array.isArray(data.practicas) ? data.practicas : [],
      proyecto: data.proyecto || null,
      titulo: data.titulo || materiaId,
      filepath: path.join(etapaDir, ficha),
    };
  }
  return { practicas: [], proyecto: null, titulo: materiaId };
}

function buildPasos({ data, source, isLast, materiaMeta }) {
  const sections = parseSections(source);
  const objetivo = findSection(sections, 'Objetivo').trim();
  const pasosBody = findSection(sections, 'Pasos (hazlos en orden)', 'Pasos');
  const substeps = parseSubsteps(pasosBody);
  const hecho = listItems(findSection(sections, 'Hecho cuando'));
  const errores = listItems(findSection(sections, 'Errores comunes'));
  const bash = allBashCommands(pasosBody || source);
  const codes = codeFences(pasosBody || source);
  const topic = String(data.titulo || 'esta lección');

  const pasos = [];
  let n = 1;
  const push = (p) => {
    pasos.push({ id: `s${n++}`, ...p });
  };

  // 1. Explicación propia
  push({
    tipo: 'explicacion',
    titulo: 'Por qué esta lección',
    xp: 10,
    cuerpo: introProse(sections, topic),
  });

  // 2–3. Ejemplos
  const ejemploSources = substeps.length
    ? substeps
    : [{ title: 'Ejemplo práctico', prose: objetivo, codes: codes.slice(0, 1), body: '' }];

  push(ejemploFromSubstep(ejemploSources[0], codes[0]));
  if (ejemploSources[1] || codes[1]) {
    push(ejemploFromSubstep(ejemploSources[1] || ejemploSources[0], codes[1] || codes[0]));
  }

  // 4. Quiz fácil — evidencia / hecho cuando
  const hecho0 = hecho[0] || data.evidencia || `Dejar evidencia concreta de: ${topic}`;
  push({
    tipo: 'quiz',
    titulo: 'Comprueba lo básico',
    xp: 10,
    variante: 'opcion_multiple',
    pregunta: `Al terminar «${truncate(topic, 60)}», ¿qué demuestra que cumpliste el criterio mínimo?`,
    opciones: [
      { id: 'a', texto: truncate(String(hecho0).replace(/\*\*/g, ''), 150) },
      { id: 'b', texto: distractorsFor(topic)[0] },
      { id: 'c', texto: distractorsFor(topic)[1] },
    ],
    respuesta: 'a',
    explicacionError: 'El criterio «Hecho cuando» / evidencia manda. Leer no basta.',
    explicacionOk: 'Bien — evidencia verificable.',
  });

  // 5. Reto: terminal, o quiz de error común, o segundo concepto
  if (bash[0]) {
    push({
      tipo: 'terminal',
      titulo: 'Reto de terminal',
      xp: 15,
      enunciado: `Escribe el comando de práctica de esta lección:\n\n\`${bash[0]}\``,
      comandoEsperado: [bash[0], ...(bash[1] ? [bash[1]] : [])].slice(0, 3),
      pistas: ['Sin el prompt `$`.', 'Respeta flags y rutas.'],
      explicacionError: `Esperado: ${bash[0]}`,
    });
  } else if (errores[0]) {
    push({
      tipo: 'quiz',
      titulo: 'Evita el error común',
      xp: 15,
      variante: 'verdadero_falso',
      pregunta: `¿Es recomendable en esta lección? “${truncate(errores[0].replace(/\*\*/g, ''), 170)}"`,
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 'f',
      explicacionError: 'Eso está listado como error común: no lo hagas.',
      explicacionOk: 'Correcto — es un anti-patrón.',
    });
  } else {
    push({
      tipo: 'quiz',
      titulo: 'Práctica deliberada',
      xp: 15,
      variante: 'verdadero_falso',
      pregunta:
        'Además de leer, debes producir algo verificable (código, nota, commit o ejercicio) antes de dar la lección por hecha.',
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 't',
      explicacionError: 'Verdadero: sin evidencia no hay progreso real.',
      explicacionOk: 'Exacto.',
    });
  }

  // 6. Quiz medio/difícil — foco / objetivo
  const focus = objetivo || `Dominar: ${topic}`;
  push({
    tipo: 'quiz',
    titulo: 'Foco (dificultad media)',
    xp: 15,
    variante: 'opcion_multiple',
    pregunta: '¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta lección?',
    opciones: [
      { id: 'a', texto: truncate(focus.replace(/\*\*/g, ''), 160) },
      { id: 'b', texto: distractorsFor(topic)[2] },
      { id: 'c', texto: 'Memorizar el índice del libro sin practicar' },
    ],
    respuesta: 'a',
    explicacionError: 'El objetivo de la lección define el foco — no el consumo pasivo.',
    explicacionOk: 'Correcto.',
  });

  // 7. Tercer ejemplo o explicación de substep avanzado (si cabe y no es última con proyecto)
  if (ejemploSources[2] && pasos.length < 7) {
    push({
      tipo: 'explicacion',
      titulo: truncate(ejemploSources[2].title, 70),
      xp: 10,
      cuerpo:
        truncate(ejemploSources[2].prose, 900) ||
        (ejemploSources[2].codes[0]
          ? `\`\`\`${ejemploSources[2].codes[0].lang}\n${truncateCode(ejemploSources[2].codes[0].code, 800)}\n\`\`\``
          : `Avanza el paso «${ejemploSources[2].title}» con evidencia en el repo.`),
    });
  } else if (bash[1] && pasos.length < 7) {
    push({
      tipo: 'terminal',
      titulo: 'Segundo comando',
      xp: 15,
      enunciado: `Ahora el siguiente comando de la secuencia:\n\n\`${bash[1]}\``,
      comandoEsperado: [bash[1]],
      explicacionError: `Esperado: ${bash[1]}`,
    });
  } else if (errores[1] && pasos.length < 7) {
    push({
      tipo: 'quiz',
      titulo: 'Segundo error común',
      xp: 10,
      variante: 'verdadero_falso',
      pregunta: `¿Debes hacer esto? “${truncate(errores[1].replace(/\*\*/g, ''), 170)}"`,
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 'f',
      explicacionError: 'No — es otro anti-patrón de la lección.',
      explicacionOk: 'Bien.',
    });
  }

  // Proyecto de cierre en la última lección
  if (isLast) {
    const entregables = [];
    for (const p of materiaMeta.practicas || []) {
      entregables.push(`${p.id.toUpperCase()}: ${p.titulo}`);
    }
    if (materiaMeta.proyecto) {
      entregables.push(`Proyecto: ${materiaMeta.proyecto.titulo}`);
    }
    if (data.evidencia) entregables.push(String(data.evidencia));
    if (!entregables.length) {
      entregables.push(`Evidencia de ${data.materia} en projects/`);
      entregables.push('Bitácora / README actualizado');
    }
    const rubrica = (hecho.length ? hecho : entregables).slice(0, 5).map((c, i) => ({
      id: `r${i + 1}`,
      criterio: truncate(String(c).replace(/\*\*/g, ''), 160),
    }));
    // ensure 5-8: replace last non-resumen slot or append before resumen
    push({
      tipo: 'proyecto',
      titulo: `Proyecto de cierre · ${data.materia}`,
      xp: 25,
      enunciado: `Cierra **${materiaMeta.titulo || data.materia}** con evidencia real en el repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no está en git, no cuenta).`,
      entregables: entregables.slice(0, 6),
      rubrica: rubrica.length
        ? rubrica
        : [
            { id: 'r1', criterio: 'Evidencia de prácticas en projects/' },
            { id: 'r2', criterio: 'README o bitácora honestos' },
            { id: 'r3', criterio: 'Puedo explicar lo esencial sin mirar apuntes' },
          ],
    });
  }

  // Resumen
  const puntos = (hecho.length ? hecho : [
    `Repasaste: ${topic}`,
    data.evidencia ? `Evidencia: ${data.evidencia}` : 'Deja evidencia en projects/',
    'Continúa al siguiente nodo del camino',
  ])
    .map((x) => truncate(String(x).replace(/\*\*/g, ''), 180))
    .slice(0, 5);

  push({
    tipo: 'resumen',
    titulo: 'Cierre',
    xp: 10,
    puntos,
    siguiente: isLast
      ? `Materia ${data.materia} lista para marcar completada cuando la rúbrica sea real.`
      : 'Sigue al siguiente nodo del camino o abre la lectura complementaria.',
  });

  // Clamp 5–8
  while (pasos.length > 8) {
    // drop a middle explicación if any, else middle quiz
    const idx = pasos.findIndex(
      (p, i) => i > 2 && i < pasos.length - 1 && p.tipo === 'explicacion',
    );
    if (idx > 0) pasos.splice(idx, 1);
    else pasos.splice(Math.floor(pasos.length / 2), 1);
  }
  while (pasos.length < 5) {
    pasos.splice(pasos.length - 1, 0, {
      id: 'pad',
      tipo: 'quiz',
      titulo: 'Comprobación',
      xp: 10,
      variante: 'verdadero_falso',
      pregunta: 'Vale la pena releer «Hecho cuando» antes de marcar la lección.',
      opciones: [
        { id: 't', texto: 'Verdadero' },
        { id: 'f', texto: 'Falso' },
      ],
      respuesta: 't',
      explicacionError: 'Sí — evita autoengaño.',
      explicacionOk: 'Correcto.',
    });
  }

  pasos.forEach((p, i) => {
    p.id = `s${i + 1}`;
  });
  return pasos;
}

function complementaryBody(source) {
  return [
    '## Lectura complementaria',
    '',
    'Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.',
    '',
    source.trim(),
  ].join('\n');
}

function curateFile(filepath, { isLast, materiaMeta }) {
  const raw = fs.readFileSync(filepath, 'utf8');
  const { data, content } = matter(raw);
  const materia = String(data.materia || '').toUpperCase();
  if (materia === 'M01' && !forceM01) {
    return { skipped: true, reason: 'm01' };
  }

  const source = extractSourceBody(content);
  const pasos = buildPasos({ data, source, isLast, materiaMeta });
  const xpLeccion = Math.min(
    120,
    Math.max(60, Math.round((Number(data.horas) || 2) * 32)),
  );

  const nextData = {
    id: String(data.id),
    materia: String(data.materia || ''),
    orden: Number(data.orden),
    titulo: String(data.titulo),
    horas: Number(data.horas ?? 0),
    semana: Number(data.semana ?? 0),
    lectura: String(data.lectura ?? ''),
    evidencia: String(data.evidencia ?? ''),
    formato: 'pasos',
    xpLeccion,
    pasos,
  };

  parseLeccionPasos(nextData);

  const out = matter.stringify(complementaryBody(source), nextData);
  if (!dryRun) fs.writeFileSync(filepath, out, 'utf8');
  return { skipped: false, pasos: pasos.length, last: isLast };
}

let migrated = 0;
let skipped = 0;
let errors = 0;

for (const etapa of fs.readdirSync(etapasRoot)) {
  const etapaDir = path.join(etapasRoot, etapa);
  if (!fs.statSync(etapaDir).isDirectory()) continue;
  for (const entry of fs.readdirSync(etapaDir)) {
    const mid = entry.match(/^(M\d{2})$/i)?.[1];
    if (!mid) continue;
    if (filter.size && !filter.has(mid.toUpperCase())) continue;

    const dir = path.join(etapaDir, mid);
    const files = fs
      .readdirSync(dir)
      .filter((f) => /^L\d{2}-.+\.md$/i.test(f))
      .sort();
    const materiaMeta = loadMateriaMeta(mid);

    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const filepath = path.join(dir, file);
      const isLast = i === files.length - 1;
      try {
        const res = curateFile(filepath, { isLast, materiaMeta });
        if (res.skipped) {
          skipped += 1;
        } else {
          migrated += 1;
          console.log(
            `OK  ${mid}/${file} (${res.pasos} pasos${res.last ? ', proyecto cierre' : ''})`,
          );
        }
      } catch (e) {
        errors += 1;
        console.error(`FAIL ${mid}/${file}`);
        console.error(e instanceof Error ? e.message : e);
      }
    }
  }
}

console.log(
  `\nCuradas=${migrated} omitidas=${skipped} errores=${errors}${dryRun ? ' (dry-run)' : ''}`,
);
if (errors) process.exit(1);
