const STORAGE_KEY = 'academia-progress-v1';

export type ProgressState = {
  estudiante: string;
  inicio: string;
  horasSemanalesMeta: number;
  materiaActual: string;
  /** Última ficha abierta (para Continuar). */
  lastMateriaId?: string;
  materias: Record<
    string,
    {
      status: 'bloqueada' | 'disponible' | 'en_curso' | 'completada';
      practicas: Record<string, boolean>;
      proyecto: boolean;
      completadoEn: string | null;
    }
  >;
  notas: string[];
};

function defaultMateria() {
  return {
    status: 'disponible' as const,
    practicas: {} as Record<string, boolean>,
    proyecto: false,
    completadoEn: null as string | null,
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
  };
}

export function loadProgress(): ProgressState | null {
  if (typeof localStorage === 'undefined') return null;
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return null;
  try {
    return JSON.parse(raw) as ProgressState;
  } catch {
    return null;
  }
}

export function saveProgress(state: ProgressState) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  window.dispatchEvent(new CustomEvent('academia-progress', { detail: state }));
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
  if (!state.materias[id]) state.materias[id] = defaultMateria();
  return state.materias[id];
}

/** Marca la materia como visitada (Continuar + en_curso). */
export function touchMateria(materiaId: string) {
  const state = loadProgress() ?? emptyState(materiaId);
  const m = ensureMateria(state, materiaId);
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  state.lastMateriaId = materiaId;
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

export function exportProgressJson(): string {
  const state = loadProgress();
  return JSON.stringify(state ?? {}, null, 2);
}

export { STORAGE_KEY };
