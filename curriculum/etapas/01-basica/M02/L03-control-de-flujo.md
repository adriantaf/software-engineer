---
id: L03
materia: M02
orden: 3
titulo: Control de flujo
horas: 3
semana: 1
lectura: EJ cap. 2 — bucles y condicionales
evidencia: src/flujo/clasificador.ts + 2 katas con bucles
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar un clasificador con `if`/`else`, `switch` y
      bucles, sin `return` olvidados.


      La CLI validará comandos e índices aquí. TS avisa cuando una rama no
      devuelve valor.
  - id: s2
    tipo: ejemplo
    titulo: 1. Clasificador de notas
    xp: 10
    cuerpo: >-
      ```ts

      export type Nivel = "insuficiente" | "aprobado" | "notable" |
      "sobresaliente";


      export function nivelDesdePuntos(puntos: number, max: number): Nivel {
        if (max <= 0) {
          throw new Error("max debe ser positivo");
        }
        const ratio = puntos / max;
        if (ratio < 0.5) return "insuficiente";
        if (ratio < 0.7) return "aprobado";
        if (ratio < 0.9) return "notable";
        return "sobresaliente";
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Control de flujo" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/flujo/clasificador.ts + 2 katas con bucles
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
    pregunta: ¿Es buena práctica en esta lección? “`return` faltante en una rama."
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
          Implementar un clasificador con `if`/`else`, `switch` y bucles, sin
          `return` olvidados.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Bucles y acumuladores
    xp: 10
    cuerpo: >-
      `src/flujo/suma-rango.ts` con `sumaHasta(n)` y `primerDivisor(n): number |
      null`.
  - id: s7
    tipo: explicacion
    titulo: 3. Dos katas con bucles
    xp: 10
    cuerpo: FizzBuzz tipado y búsqueda lineal sin `.find` todavía.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`clasificador.ts` y `suma-rango.ts` compilan; caso `max <= 0` cubierto.'
      - Dos katas nuevas con bucles.
      - '`npx tsc --noEmit` limpio en `src/`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Control de flujo

**~3 h · Semana 1**

Condicionales y bucles con tipos claros: ramas que TypeScript puede seguir y funciones que retornan en todos los caminos.

## Objetivo

Implementar un clasificador con `if`/`else`, `switch` y bucles, sin `return` olvidados.

## Por qué importa

La CLI validará comandos e índices aquí. TS avisa cuando una rama no devuelve valor.

## Pasos

### 1. Clasificador de notas (45 min)

`src/flujo/clasificador.ts`:

```ts
export type Nivel = "insuficiente" | "aprobado" | "notable" | "sobresaliente";

export function nivelDesdePuntos(puntos: number, max: number): Nivel {
  if (max <= 0) {
    throw new Error("max debe ser positivo");
  }
  const ratio = puntos / max;
  if (ratio < 0.5) return "insuficiente";
  if (ratio < 0.7) return "aprobado";
  if (ratio < 0.9) return "notable";
  return "sobresaliente";
}
```

Añade `etiquetaCorta(nivel: Nivel): string` con `switch`.

### 2. Bucles y acumuladores (40 min)

`src/flujo/suma-rango.ts` con `sumaHasta(n)` y `primerDivisor(n): number | null`.

### 3. Dos katas con bucles (50 min)

FizzBuzz tipado y búsqueda lineal sin `.find` todavía.

### 4. Lectura EJ (35 min)

Cap. 2 + **1 ejercicio** en TS.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 2 (control de flujo) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `clasificador.ts` y `suma-rango.ts` compilan; caso `max <= 0` cubierto.
2. Dos katas nuevas con bucles.
3. `npx tsc --noEmit` limpio en `src/`.

## Errores comunes

- `return` faltante en una rama.
- `switch` sin salida clara por rama.
- Bucles infinitos.

## Siguiente

[L04 — Funciones tipadas](L04-funciones-tipadas.md)
