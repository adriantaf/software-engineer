import { describe, expect, it } from "vitest";
import { rangesOverlap } from "../../src/domain/cita-ranges";

describe("rangesOverlap", () => {
  const t = (h: number, m = 0) => new Date(2026, 0, 1, h, m);

  it("detecta solape parcial", () => {
    expect(rangesOverlap(t(10), t(11), t(10, 30), t(11, 30))).toBe(true);
  });

  it("permite adyacentes sin solape", () => {
    expect(rangesOverlap(t(10), t(11), t(11), t(12))).toBe(false);
  });

  it("detecta contención total", () => {
    expect(rangesOverlap(t(10), t(12), t(10, 30), t(11))).toBe(true);
  });
});
