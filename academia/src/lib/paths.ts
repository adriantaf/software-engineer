/** Prefijo de GitHub Pages (siempre termina en /). */
export const baseUrl = import.meta.env.BASE_URL.endsWith('/')
  ? import.meta.env.BASE_URL
  : `${import.meta.env.BASE_URL}/`;

/** Une una ruta al base, p. ej. pathTo('materia/M01') → '/software-engineer/materia/M01/' */
export function pathTo(path = ''): string {
  const cleaned = String(path).replace(/^\/+/, '');
  return `${baseUrl}${cleaned}`;
}
