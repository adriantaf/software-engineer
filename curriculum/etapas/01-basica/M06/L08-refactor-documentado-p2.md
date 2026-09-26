---
id: L08
materia: M06
orden: 8
titulo: Refactor documentado (P2)
horas: 5
semana: 2
lectura: "Repaso CC 1–3, 6, 10 + diff git"
evidencia: "refactor-p2.md con antes/después + diff; commit refactor(m06): P2 codigo limpio"
---

# L08 — Refactor documentado (P2)

**~5 h · Semana 2**

La práctica **P2** exige evidencia: no solo código bonito, sino **historia** del cambio.

## Objetivo

Entregar documento `refactor-p2.md` con objetivos, diff representativo y métricas cualitativas (líneas, complejidad, nombres).

## Pasos

### 1. Baseline (30 min)

```bash
git log --oneline -5
git diff pre-refactor-semana1..HEAD --stat
```

Si no tienes tag, compara commit de L04 vs actual.

### 2. Redactar `refactor-p2.md` (90 min)

Secciones:

- Motivación (CC + SOLID).
- Capturas o bloques `diff` de 2–3 archivos clave.
- Tabla: olor → técnica → resultado.
- Checklist CC aplicado.

### 3. Pulido final (120 min)

Última pasada nombres/funciones. Elimina dead code.

### 4. Tests y cobertura manual (45 min)

Lista casos de prueba; no hace falta cobertura 100 %.

### 5. Commit evidencia (15 min)

```bash
git add refactor-p2.md
git commit -m "docs(m06): evidencia refactor P2 codigo limpio"
```

Marca **P2** en la ficha cuando exista diff + narrativa.

## Hecho cuando

1. `refactor-p2.md` completo con diff real.
2. Código actual refleja nombres y funciones pequeñas.
3. Tests verdes.

## Errores comunes

- Diff ilegible (pegar 2000 líneas sin contexto).
- Refactor sin tests.

## Siguiente

[L09 — Union types y modelado de estados](L09-union-types-y-estados.md)
