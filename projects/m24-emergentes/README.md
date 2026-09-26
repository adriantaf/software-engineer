# M24 — Tecnologías emergentes

Research, matriz de adopción y spike go/no-go para Agenda Ops.

## En resumen

Separas hype de utilidad: research, criterios (incluye seguridad) y un spike go/no-go.

## Estructura esperada

```text
projects/m24-emergentes/
  README.md
  candidatos.md
  matriz-adopcion.md
  go-no-go.md
  bitacora/
    semana-01.md … semana-03.md
  research/
    README.md
    candidato-1.md
    candidato-2.md
    candidato-3.md
    comparacion-v0.md
  spike/
    README.md
    hipotesis.md
    plan.md
    threat-sketch.md
    demo-log.md
    resultados.md
    .env.example
```

## Checklist

- **P1 — Notes:** 3 research con fuentes primarias.
- **P2 — Matriz:** costo/riesgo/valor/seguridad/fit.
- **P3 — Spike:** PoC ≤1 semana en `spike/`.
- **Proyecto — Go/no-go:** `go-no-go.md` argumentado.

## Reglas

1. Docs oficiales antes de puntuar la matriz.
2. Spike aislado — no merge a prod sin go.
3. Un “no” bien fundado vale igual que un “go”.

## Enlaces

- Ficha: `curriculum/etapas/03-terminal/M24-tecnologias-emergentes.md`
- Bibliografía: `curriculum/bibliografia.md#m24-tecnologias-emergentes`
