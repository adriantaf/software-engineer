const STORAGE_KEY = 'academia-progress-v1';

export type ProgressState = {
  estudiante: string;
  inicio: string;
  horasSemanalesMeta: number;
  materiaActual: string;
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

export function togglePractica(materiaId: string, practicaId: string) {
  const state = loadProgress() ?? ({
    estudiante: 'Adrian Tafoya',
    inicio: new Date().toISOString().slice(0, 10),
    horasSemanalesMeta: 20,
    materiaActual: materiaId,
    materias: {},
    notas: [],
  } satisfies ProgressState);
  const m = ensureMateria(state, materiaId);
  m.practicas[practicaId] = !m.practicas[practicaId];
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  saveProgress(state);
  return state;
}

export function toggleProyecto(materiaId: string) {
  const state = loadProgress() ?? ({
    estudiante: 'Adrian Tafoya',
    inicio: new Date().toISOString().slice(0, 10),
    horasSemanalesMeta: 20,
    materiaActual: materiaId,
    materias: {},
    notas: [],
  } satisfies ProgressState);
  const m = ensureMateria(state, materiaId);
  m.proyecto = !m.proyecto;
  if (m.status === 'disponible' || m.status === 'bloqueada') m.status = 'en_curso';
  state.materiaActual = materiaId;
  saveProgress(state);
  return state;
}

export function markMateriaCompletada(materiaId: string, done: boolean) {
  const state = loadProgress() ?? ({
    estudiante: 'Adrian Tafoya',
    inicio: new Date().toISOString().slice(0, 10),
    horasSemanalesMeta: 20,
    materiaActual: materiaId,
    materias: {},
    notas: [],
  } satisfies ProgressState);
  const m = ensureMateria(state, materiaId);
  m.status = done ? 'completada' : 'en_curso';
  m.completadoEn = done ? new Date().toISOString().slice(0, 10) : null;
  saveProgress(state);
  return state;
}

export function exportProgressJson(): string {
  const state = loadProgress();
  return JSON.stringify(state ?? {}, null, 2);
}

export { STORAGE_KEY };
