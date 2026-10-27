/** M04 L01 — simulación moneda (completa en la lección). */
export function flip(n: number, p = 0.5): number {
  let heads = 0;
  for (let i = 0; i < n; i++) if (Math.random() < p) heads++;
  return heads / n;
}
if (import.meta.main) {
  console.log(flip(10_000));
}
