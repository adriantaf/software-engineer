---
id: L02
materia: M03
orden: 2
titulo: 'Implicación, equivalencias y leyes'
horas: 2.5
semana: 1
lectura: 'Rosen Cap. 1.3 — equivalencias, leyes lógicas, formas normales (intro)'
evidencia: apuntes/leyes-logicas.md + evaluar() para fórmulas pequeñas + tests
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dominar ↔ y las leyes clave; verificar equivalencias con
      tablas o álgebra; codificar evaluación de fórmulas con variables
      booleanas.


      `P ↔ Q` es verdadera cuando ambas tienen el **mismo** valor de verdad.
      Muchas “reglas mnemotécnicas” son equivalencias demostrables, no axiomas
      mágicos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Leyes en apuntes
    xp: 10
    cuerpo: |-
      ```ts
      export type Env = Record<string, boolean>;

      export function evaluar(expr: string, env: Env): boolean {
        // Implementa un subconjunto: identificadores, ¬, ∧, ∨, →, paréntesis
        // Sin eval(): parsea tú o usa un árbol simple de 1–2 niveles
        throw new Error("por implementar");
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Implicación, equivalencias y leyes" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: apuntes/leyes-logicas.md + evaluar() para fórmulas pequeñas + tests
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Usar `eval()` de JS con strings
      arbitrarios (riesgo y no demuestra comprensión)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dominar ↔ y las leyes clave; verificar equivalencias con tablas o
          álgebra; codificar evaluación de fórmulas con variables booleanas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tautología y contradicción
    xp: 10
    cuerpo: >-
      Define tautología y contradicción. Ejemplo: `P ∨ ¬P` (tautología).
      Comprueba con tabla.
  - id: s7
    tipo: ejemplo
    titulo: 3. Evaluador en TS
    xp: 10
    cuerpo: |-
      ```ts
      export type Env = Record<string, boolean>;

      export function evaluar(expr: string, env: Env): boolean {
        // Implementa un subconjunto: identificadores, ¬, ∧, ∨, →, paréntesis
        // Sin eval(): parsea tú o usa un árbol simple de 1–2 niveles
        throw new Error("por implementar");
      }
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `leyes-logicas.md` incluye las cuatro leyes con verificación y 2
        ejercicios del libro.
      - >-
        `evaluar` (o funciones auxiliares equivalentes) pasa tests acordados con
        tu diseño.
      - >-
        Explicas la diferencia entre `P → Q` y `P ↔ Q` con un contraejemplo cada
        uno.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


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
