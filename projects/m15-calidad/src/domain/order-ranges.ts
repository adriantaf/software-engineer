/** Reglas puras de pedido Vitrina (L02). */

export type OrderEstado =
  | 'recibido'
  | 'preparando'
  | 'listo'
  | 'entregado'
  | 'cancelado';

const TRANSITIONS: Record<OrderEstado, OrderEstado[]> = {
  recibido: ['preparando', 'cancelado'],
  preparando: ['listo', 'cancelado'],
  listo: ['entregado', 'cancelado'],
  entregado: [],
  cancelado: [],
};

/** ¿Se puede pasar de `from` a `to`? */
export function canTransition(from: OrderEstado, to: OrderEstado): boolean {
  return TRANSITIONS[from].includes(to);
}

/** Total en centavos: suma de líneas (cantidad × precio unitario). */
export function lineTotalCentavos(cantidad: number, precioUnitCentavos: number): number {
  if (cantidad <= 0 || precioUnitCentavos < 0) return 0;
  return cantidad * precioUnitCentavos;
}
