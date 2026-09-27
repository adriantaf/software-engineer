import { describe, expect, it } from "vitest";
import { canTransition, lineTotalCentavos } from "../../src/domain/order-ranges";

describe("canTransition", () => {
  it("permite recibido → preparando", () => {
    expect(canTransition("recibido", "preparando")).toBe(true);
  });

  it("no permite entregado → recibido", () => {
    expect(canTransition("entregado", "recibido")).toBe(false);
  });

  it("permite listo → entregado", () => {
    expect(canTransition("listo", "entregado")).toBe(true);
  });
});

describe("lineTotalCentavos", () => {
  it("multiplica cantidad por precio", () => {
    expect(lineTotalCentavos(2, 4250)).toBe(8500);
  });

  it("cantidad inválida → 0", () => {
    expect(lineTotalCentavos(0, 4250)).toBe(0);
  });
});
