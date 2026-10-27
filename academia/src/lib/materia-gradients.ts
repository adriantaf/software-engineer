/** Degradados de portada por etapa (alineados con CourseCard y SVG en public/covers/). */
export const MATERIA_GRADIENTS: Record<string, [string, string]> = {
  basica: ['#0f766e', '#134e4a'],
  disciplinaria: ['#0369a1', '#0c4a6e'],
  terminal: ['#7c3aed', '#4c1d95'],
};

export function gradientForEtapa(etapaId: string): [string, string] {
  return MATERIA_GRADIENTS[etapaId] ?? MATERIA_GRADIENTS.basica;
}
