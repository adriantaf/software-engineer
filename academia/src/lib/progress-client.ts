const STORAGE_KEY = 'academia-progress-v1';

export type MateriaProgress = {
  status: 'bloqueada' | 'disponible' | 'en_curso' | 'completada';
  practicas: Record<string, boolean>;
  proyecto: boolean;
  /** Lecciones marcadas (L01…Ln por materia). */
  lecciones: Record<string, boolean>;
  /** Pasos completados por lección: L01 → { s1: true, … }. */
  pasos?: Record<string, Record<string, boolean>>;
  /** Paso actual por lección (id del paso). */
  pasoActual?: Record<string, string>;
  completadoEn: string | null;
};

/** Check-in semanal (ritmo + retrospectiva corta). */
export type WeeklyCheckIn = {
  /** ISO date YYYY-MM-DD (día del check-in). */
  fecha: string;
  /** Horas reales estudiadas esa semana. */
  horas: number;
  hecho: string;
  bloqueo: string;
  siguiente: string;
};

/** Respuestas locales de autoevaluación de etapa. */
export type ExamenAnswers = {
  updatedAt: string;
  listo: boolean;
  answers: Record<string, string>;
  /** Checklist de rúbrica formativa (id → marcado). */
  rubrica?: Record<string, boolean>;
};

/** Ítem de repaso espaciado (quiz / terminal fallado o visto). */
export type RepasoItem = {
  id: string;
  materiaId: string;
  leccionId: string;
  pasoId: string;
  /** Pregunta o enunciado corto para la sesión. */
  prompt: string;
  /** Payload tipado mínimo para re-render (quiz/terminal). */
  kind: 'quiz' | 'terminal' | 'codigo';
  payload: Record<string, unknown>;
  ease: number;
  intervalDays: number;
  due: string;
  reps: number;
  lapses: number;
};

export type ProgressState = {
  estudiante: string;
  inicio: string;
  horasSemanalesMeta: number;
  materiaActual: string;
  /** Última ficha abierta (para Continuar). */
  lastMateriaId?: string;
  /** Última lección abierta dentro de una materia con lecciones. */
  lastLeccionId?: string;
  /** Último paso dentro de la lección (motor pasos). */
  lastPasoId?: string;
  /** XP acumulado. */
  xp?: number;
  /** Racha diaria consecutiva. */
  racha?: number;
  /** Última fecha YYYY-MM-DD con actividad de estudio. */
  ultimaFechaEstudio?: string;
  materias: Record<string, MateriaProgress>;
  /** @deprecated preferir checkIns; se conserva por compatibilidad de export. */
  notas: string[];
  /** Historial de check-ins semanales (más reciente primero). */
  checkIns: WeeklyCheckIn[];
  /** Autoevaluaciones por etapa (basica | disciplinaria | terminal). */
  examenes?: Record<string, ExamenAnswers>;
  /** Cola de repaso espaciado. */
  repaso?: RepasoItem[];
  /** Epoch ms — para merge cloud / local. */
  updatedAt?: number;
};

/** Fallback en memoria si localStorage está bloqueado (Safari privado, ITP, etc.). */
let memoryStore: ProgressState | null = null;
let storageUsable: boolean | null = null;

function canUseLocalStorage(): boolean {
  if (storageUsable !== null) return storageUsable;
  if (typeof window === 'undefined' || typeof localStorage === 'undefined') {
    storageUsable = false;
    return false;
  }
  try {
    const probe = `${STORAGE_KEY}__probe`;
    localStorage.setItem(probe, '1');
    localStorage.removeItem(probe);
    storageUsable = true;
  } catch {
    storageUsable = false;
  }
  return storageUsable;
}

function defaultMateria(): MateriaProgress {
  return {
    status: 'disponible',
    practicas: {},
    lecciones: {},
    pasos: {},
    pasoActual: {},
    proyecto: false,
    completadoEn: null,
  };
}

function emptyState(materiaId = 'M01'): ProgressState {
  return {
    estudiante: 'Adrian Tafoya',
    inicio: new Date().toISOString().slice(0, 10),
    horasSemanalesMeta: 20,
    materiaActual: materiaId,
    lastMateriaId: materiaId,
    xp: 0,
    racha: 0,
    materias: {},
    notas: [],
    checkIns: [],
    repaso: [],
  };
}

function todayISO(): string {
  return new Date().toISOString().slice(0, 10);
}

function daysBetween(a: string, b: string): number {
  const ms = Date.parse(b) - Date.parse(a);
  return Math.round(ms / 86_400_000);
}

function normalizeProgress(raw: ProgressState): ProgressState {
  const state: ProgressState = {
    ...emptyState(raw.materiaActual || 'M01'),
    ...raw,
    notas: Array.isArray(raw.notas) ? raw.notas : [],
    checkIns: Array.isArray(raw.checkIns) ? raw.checkIns : [],
    materias: raw.materias ?? {},
    examenes: raw.examenes && typeof raw.examenes === 'object' ? raw.examenes : {},
    repaso: Array.isArray(raw.repaso) ? raw.repaso : [],
    xp: Number.isFinite(raw.xp) ? Math.max(0, Number(raw.xp)) : 0,
    racha: Number.isFinite(raw.racha) ? Math.max(0, Number(raw.racha)) : 0,
  };
  if (!Number.isFinite(state.horasSemanalesMeta) || state.horasSemanalesMeta <= 0) {
    state.horasSemanalesMeta = 20;
  }
  for (const mid of Object.keys(state.materias)) {
    const m = state.materias[mid];
    if (!m.lecciones) m.lecciones = {};
    if (!m.pasos) m.pasos = {};
    if (!m.pasoActual) m.pasoActual = {};
    if (!m.practicas) m.practicas = {};
  }
  return state;
}

export function loadProgress(): ProgressState | null {
  if (canUseLocalStorage()) {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = normalizeProgress(JSON.parse(raw) as ProgressState);
        memoryStore = parsed;
        return parsed;
      }
    } catch {
      /* usar memoria */
    }
  }
  return memoryStore;
}

export function saveProgress(state: ProgressState, opts?: { emit?: boolean }) {
  const normalized = normalizeProgress({
    ...state,
    updatedAt: Date.now(),
  });
  memoryStore = normalized;
  if (canUseLocalStorage()) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(normalized));
    } catch (e) {
      console.warn('[progress] localStorage no disponible; progreso solo en memoria', e);
      storageUsable = false;
    }
  }
  if (opts?.emit === false) return;
  window.dispatchEvent(new CustomEvent('academia-progress', { detail: normalized }));
}

export function initProgressFromSeed() {
  if (loadProgress()) return;
  const el = document.getElementById('progress-seed');
  if (!el?.textContent) return;
  try {
    const seed = JSON.parse(el.textContent) as ProgressState;
    saveProgress(seed);
  } catch {
    /* ignore */
  }
}

export function ensureMateria(state: ProgressState, id: string) {
  if (!state.materias[id]) {
    state.materias[id] = defaultMateria();
  } else {
    if (!state.materias[id].lecciones) state.materias[id].lecciones = {};
    if (!state.materias[id].pasos) state.materias[id].pasos = {};
    if (!state.materias[id].pasoActual) state.materias[id].pasoActual = {};
  }
  return state.materias[id];
}

/** Actualiza racha diaria si hubo actividad hoy. */
export function bumpStreak(state: ProgressState): ProgressState {
  const today = todayISO();
  const last = state.ultimaFechaEstudio;
  if (last === today) return state;
  if (!last) {
    state.racha = 1;
  } else {
    const gap = daysBetween(last, today);
    state.racha = gap === 1 ? (state.racha ?? 0) + 1 : 1;
  }
  state.ultimaFechaEstudio = today;
  return state;
}

export function addXp(state: ProgressState, amount: number): ProgressState {
  const n = Math.max(0, Math.round(amount));
  state.xp = (state.xp ?? 0) + n;
  return bumpStreak(state);
}

/** Marca la materia como visitada (Continuar + en_curso). */
export function touchMateria(materiaId: string, leccionId?: string, pasoId?: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  if (leccionId) {
    state.lastLeccionId = leccionId;
    if (pasoId) {
      state.lastPasoId = pasoId;
      m.pasoActual = m.pasoActual ?? {};
      m.pasoActual[leccionId] = pasoId;
    }
  }
  saveProgress(state);
  return state;
}

/**
 * Destino del botón Continuar:
 * 1) última visitada (si no está completada)
 * 2) primera no completada en orden del catálogo
 * 3) M01
 */
export function resolveContinueMateriaId(catalogIds: string[]): string {
  const state = loadProgress();
  const ids = catalogIds.length ? catalogIds : ['M01'];
  const last = state?.lastMateriaId || state?.materiaActual;
  if (last && ids.includes(last)) {
    const st = state?.materias?.[last]?.status;
    if (st !== 'completada') return last;
  }
  for (const id of ids) {
    if (state?.materias?.[id]?.status !== 'completada') return id;
  }
  return ids[0] ?? 'M01';
}

/**
 * Ruta relativa (sin base) para Continuar.
 * Si la materia tiene lecciones, apunta a la primera incompleta (o la última visitada incompleta).
 * Con pasos: añade ?paso=id cuando hay lastPasoId.
 */
export function resolveContinuePath(
  catalogIds: string[],
  leccionesByMateria: Record<string, string[]> = {},
): string {
  const materiaId = resolveContinueMateriaId(catalogIds);
  const lessonIds = leccionesByMateria[materiaId] ?? [];
  if (!lessonIds.length) return `materia/${materiaId}`;

  const state = loadProgress();
  const done = state?.materias?.[materiaId]?.lecciones ?? {};
  const lastL = state?.lastLeccionId;
  let lid: string | undefined;
  if (lastL && lessonIds.includes(lastL) && !done[lastL]) {
    lid = lastL;
  } else {
    lid = lessonIds.find((id) => !done[id]);
  }
  if (!lid) return `materia/${materiaId}`;

  const paso =
    state?.lastPasoId && state.lastLeccionId === lid
      ? state.lastPasoId
      : state?.materias?.[materiaId]?.pasoActual?.[lid];
  if (paso && !done[lid]) {
    return `materia/${materiaId}/leccion/${lid}?paso=${encodeURIComponent(paso)}`;
  }
  return `materia/${materiaId}/leccion/${lid}`;
}

export function togglePractica(materiaId: string, practicaId: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.practicas[practicaId] = !m.practicas[practicaId];
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  saveProgress(state);
  return state;
}

export function toggleLeccion(materiaId: string, leccionId: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.lecciones[leccionId] = !m.lecciones[leccionId];
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  state.lastLeccionId = leccionId;
  saveProgress(state);
  return state;
}

/** Fija el estado de una lección (preferible al toggle cuando el checkbox ya cambió en el DOM). */
export function setLeccion(materiaId: string, leccionId: string, done: boolean) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.lecciones[leccionId] = done;
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  state.lastLeccionId = leccionId;
  saveProgress(state);
  return state;
}

/**
 * Marca un paso completado. Si se pasan todos los stepIds, marca la lección hecha.
 * Devuelve { state, gainedXp, lessonComplete }.
 */
export function completePaso(
  materiaId: string,
  leccionId: string,
  pasoId: string,
  opts: { xp?: number; allPasoIds: string[] },
): { state: ProgressState; gainedXp: number; lessonComplete: boolean } {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.pasos = m.pasos ?? {};
  m.pasos[leccionId] = m.pasos[leccionId] ?? {};
  const already = Boolean(m.pasos[leccionId][pasoId]);
  m.pasos[leccionId][pasoId] = true;
  m.pasoActual = m.pasoActual ?? {};
  m.pasoActual[leccionId] = pasoId;
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  state.lastLeccionId = leccionId;
  state.lastPasoId = pasoId;

  let gainedXp = 0;
  if (!already && opts.xp && opts.xp > 0) {
    addXp(state, opts.xp);
    gainedXp = opts.xp;
  } else {
    bumpStreak(state);
  }

  const lessonComplete = opts.allPasoIds.every((id) => m.pasos![leccionId][id]);
  if (lessonComplete) m.lecciones[leccionId] = true;

  saveProgress(state);
  return { state, gainedXp, lessonComplete };
}

export function setPasoActual(materiaId: string, leccionId: string, pasoId: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.pasoActual = m.pasoActual ?? {};
  m.pasoActual[leccionId] = pasoId;
  state.lastMateriaId = materiaId;
  state.lastLeccionId = leccionId;
  state.lastPasoId = pasoId;
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  saveProgress(state);
  return state;
}

export function getPasoProgress(
  materiaId: string,
  leccionId: string,
): { done: Record<string, boolean>; current?: string } {
  const m = loadProgress()?.materias?.[materiaId];
  return {
    done: m?.pasos?.[leccionId] ?? {},
    current: m?.pasoActual?.[leccionId],
  };
}

function addDaysISO(iso: string, days: number): string {
  const d = new Date(iso + 'T12:00:00Z');
  d.setUTCDate(d.getUTCDate() + days);
  return d.toISOString().slice(0, 10);
}

/** Encola o refuerza un ítem de repaso tras un fallo. */
export function enqueueRepaso(item: Omit<RepasoItem, 'ease' | 'intervalDays' | 'due' | 'reps' | 'lapses'> & Partial<Pick<RepasoItem, 'ease' | 'intervalDays' | 'due' | 'reps' | 'lapses'>>) {
  const state = loadProgress() ?? emptyState();
  const list = Array.isArray(state.repaso) ? [...state.repaso] : [];
  const existing = list.findIndex((r) => r.id === item.id);
  const today = todayISO();
  if (existing >= 0) {
    const prev = list[existing];
    list[existing] = {
      ...prev,
      ...item,
      lapses: (prev.lapses ?? 0) + 1,
      ease: Math.max(1.3, (prev.ease ?? 2.5) - 0.2),
      intervalDays: 1,
      due: today,
      prompt: item.prompt,
      payload: item.payload,
    };
  } else {
    list.push({
      ease: 2.5,
      intervalDays: 0,
      due: today,
      reps: 0,
      lapses: 0,
      ...item,
    });
  }
  state.repaso = list.slice(0, 200);
  saveProgress(state);
  return state;
}

/** Marca un ítem de repaso como recordado (SM-2 ligero). */
export function gradeRepaso(itemId: string, ok: boolean) {
  const state = loadProgress() ?? emptyState();
  const list = Array.isArray(state.repaso) ? [...state.repaso] : [];
  const idx = list.findIndex((r) => r.id === itemId);
  if (idx < 0) return state;
  const item = { ...list[idx] };
  const today = todayISO();
  if (ok) {
    item.reps = (item.reps ?? 0) + 1;
    if (item.reps === 1) item.intervalDays = 1;
    else if (item.reps === 2) item.intervalDays = 3;
    else item.intervalDays = Math.max(1, Math.round(item.intervalDays * item.ease));
    item.ease = Math.min(3.0, item.ease + 0.1);
    item.due = addDaysISO(today, item.intervalDays);
  } else {
    item.lapses = (item.lapses ?? 0) + 1;
    item.reps = 0;
    item.intervalDays = 1;
    item.ease = Math.max(1.3, item.ease - 0.2);
    item.due = today;
  }
  list[idx] = item;
  state.repaso = list;
  bumpStreak(state);
  saveProgress(state);
  return state;
}

export function listDueRepaso(limit = 20): RepasoItem[] {
  const state = loadProgress();
  const today = todayISO();
  const list = state?.repaso ?? [];
  return list
    .filter((r) => r.due <= today)
    .sort((a, b) => (a.due < b.due ? -1 : a.due > b.due ? 1 : 0))
    .slice(0, limit);
}

export function toggleProyecto(materiaId: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.proyecto = !m.proyecto;
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  saveProgress(state);
  return state;
}

export function markMateriaCompletada(materiaId: string, done: boolean) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  m.status = done ? 'completada' : 'en_curso';
  m.completadoEn = done ? new Date().toISOString().slice(0, 10) : null;
  state.lastMateriaId = materiaId;
  saveProgress(state);
  return state;
}

export function setHorasSemanalesMeta(horas: number) {
  const state = loadProgress() ?? emptyState();
  const n = Math.round(Number(horas));
  state.horasSemanalesMeta = Number.isFinite(n) && n > 0 ? Math.min(n, 80) : 20;
  saveProgress(state);
  return state;
}

export function addWeeklyCheckIn(input: Omit<WeeklyCheckIn, 'fecha'> & { fecha?: string }) {
  const state = loadProgress() ?? emptyState();
  const entry: WeeklyCheckIn = {
    fecha: input.fecha || new Date().toISOString().slice(0, 10),
    horas: Math.max(0, Math.round(Number(input.horas) || 0)),
    hecho: (input.hecho || '').trim(),
    bloqueo: (input.bloqueo || '').trim(),
    siguiente: (input.siguiente || '').trim(),
  };
  const prev = Array.isArray(state.checkIns) ? state.checkIns : [];
  // Un check-in por fecha: reemplaza si ya existe ese día.
  state.checkIns = [entry, ...prev.filter((c) => c.fecha !== entry.fecha)].slice(0, 52);
  saveProgress(state);
  return state;
}

export function listWeeklyCheckIns(limit = 8): WeeklyCheckIn[] {
  const state = loadProgress();
  const list = state?.checkIns ?? [];
  return list.slice(0, limit);
}

export function exportProgressJson(): string {
  const state = loadProgress();
  return JSON.stringify(state ?? {}, null, 2);
}

export { STORAGE_KEY, todayISO };
