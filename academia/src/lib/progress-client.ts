const STORAGE_KEY = 'academia-progress-v1';

export type MateriaProgress = {
  status: 'bloqueada' | 'disponible' | 'en_curso' | 'completada';
  practicas: Record<string, boolean>;
  proyecto: boolean;
  /** Lecciones marcadas (L01…Ln por materia). */
  lecciones: Record<string, boolean>;
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

export type ProgressState = {
  estudiante: string;
  inicio: string;
  horasSemanalesMeta: number;
  materiaActual: string;
  /** Última ficha abierta (para Continuar). */
  lastMateriaId?: string;
  /** Última lección abierta dentro de una materia con lecciones. */
  lastLeccionId?: string;
  materias: Record<string, MateriaProgress>;
  /** @deprecated preferir checkIns; se conserva por compatibilidad de export. */
  notas: string[];
  /** Historial de check-ins semanales (más reciente primero). */
  checkIns: WeeklyCheckIn[];
};

function defaultMateria(): MateriaProgress {
  return {
    status: 'disponible',
    practicas: {},
    lecciones: {},
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
    materias: {},
    notas: [],
    checkIns: [],
  };
}

function normalizeProgress(raw: ProgressState): ProgressState {
  const state: ProgressState = {
    ...emptyState(raw.materiaActual || 'M01'),
    ...raw,
    notas: Array.isArray(raw.notas) ? raw.notas : [],
    checkIns: Array.isArray(raw.checkIns) ? raw.checkIns : [],
    materias: raw.materias ?? {},
  };
  if (!Number.isFinite(state.horasSemanalesMeta) || state.horasSemanalesMeta <= 0) {
    state.horasSemanalesMeta = 20;
  }
  return state;
}

export function loadProgress(): ProgressState | null {
  if (typeof localStorage === 'undefined') return null;
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return null;
  try {
    return normalizeProgress(JSON.parse(raw) as ProgressState);
  } catch {
    return null;
  }
}

export function saveProgress(state: ProgressState) {
  const normalized = normalizeProgress(state);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(normalized));
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
  } else if (!state.materias[id].lecciones) {
    state.materias[id].lecciones = {};
  }
  return state.materias[id];
}

/** Marca la materia como visitada (Continuar + en_curso). */
export function touchMateria(materiaId: string, leccionId?: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
  if (leccionId) state.lastLeccionId = leccionId;
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
  if (lastL && lessonIds.includes(lastL) && !done[lastL]) {
    return `materia/${materiaId}/leccion/${lastL}`;
  }
  for (const lid of lessonIds) {
    if (!done[lid]) return `materia/${materiaId}/leccion/${lid}`;
  }
  return `materia/${materiaId}`;
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

export { STORAGE_KEY };
