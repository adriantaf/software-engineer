---
id: L02
materia: M03
orden: 2
titulo: Implicación, equivalencias y leyes
horas: 2.5
semana: 1
lectura: "Rosen Cap. 1.3 — equivalencias, leyes lógicas, formas normales (intro)"
evidencia: "apuntes/leyes-logicas.md + evaluar() para fórmulas pequeñas + tests"
---

# L02 — Implicación, equivalencias y leyes

**~2.5 h · Semana 1**

Pasas de tablas sueltas a **equivalencias** que usarás en demostraciones: contrapositiva, De Morgan, distributividad.

## Objetivo

Dominar ↔ y las leyes clave; verificar equivalencias con tablas o álgebra; codificar evaluación de fórmulas con variables booleanas.

## Idea clave

`P ↔ Q` es verdadera cuando ambas tienen el **mismo** valor de verdad. Muchas “reglas mnemotécnicas” son equivalencias demostrables, no axiomas mágicos.

## Pasos

### 1. Leyes en apuntes (40–50 min)

En `projects/m03-discretas/apuntes/leyes-logicas.md` documenta con **tabla o cálculo**:

| Ley | Fórmula |
|-----|---------|
| Doble negación | ¬¬P ↔ P |
| De Morgan | ¬(P ∧ Q) ↔ (¬P ∨ ¬Q) |
| Contrapositiva | (P → Q) ↔ (¬Q → ¬P) |
| Implicación como ∨ | (P → Q) ↔ (¬P ∨ Q) |

Para cada una: tabla de 4 filas **o** cadena de reescrituras justificada.

### 2. Tautología y contradicción (20 min)

Define tautología y contradicción. Ejemplo: `P ∨ ¬P` (tautología). Comprueba con tabla.

### 3. Evaluador en TS (50–60 min)

Extiende `src/logic.ts`:

```ts
export type Env = Record<string, boolean>;

export function evaluar(expr: string, env: Env): boolean {
  // Implementa un subconjunto: identificadores, ¬, ∧, ∨, →, paréntesis
  // Sin eval(): parsea tú o usa un árbol simple de 1–2 niveles
  throw new Error("por implementar");
}
```

**Alcance mínimo:** fórmulas como `(P -> Q) && !R` con `env = { P: true, Q: false, R: true }`. Si ya dominas parsing, generaliza; si no, empieza con 2–3 patrones fijos y documenta la limitación en el apunte.

Tests: al menos 3 fórmulas distintas, incluyendo una equivalencia de De Morgan.

### 4. Ejercicio Rosen (20 min)

Del cap. 1 (sección de equivalencias): resuelve **2** ejercicios de “mostrar equivalencia” en `leyes-logicas.md` (enunciado + tu solución).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 1.3 (equivalencias, leyes) |
| Apuntes | `logica-proposicional.md` (repaso si hace falta) |

## Hecho cuando

1. `leyes-logicas.md` incluye las cuatro leyes con verificación y 2 ejercicios del libro.
2. `evaluar` (o funciones auxiliares equivalentes) pasa tests acordados con tu diseño.
3. Explicas la diferencia entre `P → Q` y `P ↔ Q` con un contraejemplo cada uno.

## Errores comunes

- Usar `eval()` de JS con strings arbitrarios (riesgo y no demuestra comprensión).
- Afirmar equivalencia sin tabla ni reescritura.
- Confundir contrapositiva con conversa (`Q → P`).

## Siguiente

[L03 — Predicados y cuantificadores](L03-predicados-y-cuantificadores.md)
