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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La CLI validará comandos e índices aquí. TS avisa cuando una rama no
      devuelve valor.


      **Objetivo de esta lección:** Implementar un clasificador con `if`/`else`,
      `switch` y bucles, sin `return` olvidados.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Clasificador de notas
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


      `src/flujo/clasificador.ts`: Añade `etiquetaCorta(nivel: Nivel): string`
      con `switch`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Bucles y acumuladores
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Control de flujo», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: >-
          `clasificador.ts` y `suma-rango.ts` compilan; caso `max <= 0`
          cubierto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Control de flujo
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “`return` faltante en una rama."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Implementar un clasificador con `if`/`else`, `switch` y bucles, sin
          `return` olvidados.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Dos katas con bucles
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
