/** Strategy de precios — completa en L01. */
export type CalculoPrecio = { calcular(base: number): number };

export const tarifaBase: CalculoPrecio = {
  calcular: (base) => base,
};

export const tarifaPromoDiez: CalculoPrecio = {
  calcular: (base) => Math.round(base * 0.9 * 100) / 100,
};

export function totalServicio(base: number, estrategia: CalculoPrecio): number {
  return estrategia.calcular(base);
}
