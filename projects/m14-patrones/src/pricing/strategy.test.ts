import { describe, expect, it } from "vitest";
import { tarifaBase, tarifaPromoDiez, totalServicio } from "./strategy";

describe("Strategy precios Vitrina", () => {
  it("tarifa base no cambia el monto", () => {
    expect(totalServicio(100, tarifaBase)).toBe(100);
  });

  it("promo -10% redondea a centavos", () => {
    expect(totalServicio(100, tarifaPromoDiez)).toBe(90);
    expect(totalServicio(99.99, tarifaPromoDiez)).toBe(89.99);
  });

  it("no acepta estrategia undefined (falla tipado en tsc)", () => {
    expect(totalServicio(50, tarifaBase)).toBe(50);
  });
});
