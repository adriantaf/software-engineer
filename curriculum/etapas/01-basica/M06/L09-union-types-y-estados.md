---
id: L09
materia: M06
orden: 9
titulo: Union types y modelado de estados
horas: 5
semana: 3
lectura: TS Handbook — Unions and Intersection Types
evidencia: Tipos de estado discriminated union + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los union types modelan estados mutuamente excluyentes mejor que `boolean`
      sueltos.


      **Objetivo de esta lección:** Modelar estados de préstamo/libro (o tu
      dominio) con **discriminated unions**; eliminar flags inconsistentes
      (`prestado` + `fechaDevolucion` sin sentido).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```ts
      type EstadoLibro =
        | { tipo: "disponible" }
        | { tipo: "prestado"; hasta: Date }
        | { tipo: "reservado"; por: string };
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Diseño
    xp: 10
    cuerpo: |-
      ```ts
      type EstadoLibro =
        | { tipo: "disponible" }
        | { tipo: "prestado"; hasta: Date }
        | { tipo: "reservado"; por: string };
      ```

      Adapta a tu dominio.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Union types y modelado de estados», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Estados inválidos no representables en tipos (en la medida posible).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Union types y modelado
          de estados
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
    pregunta: >-
      ¿Es recomendable en esta lección? “`string` libre donde cabe union
      literal."
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
          Modelar estados de préstamo/libro (o tu dominio) con discriminated
          unions; eliminar flags inconsistentes (`prestado` + `fechaDevolucion`
          sin sentido).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Migración
    xp: 10
    cuerpo: Refactor entidades; actualiza métodos y tests.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Estados inválidos no representables en tipos (en la medida posible).
      - Switch exhaustivo con `assertNever`.
      - Tests actualizados.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Union types y modelado de estados

**~5 h · Semana 3**

Los union types modelan estados mutuamente excluyentes mejor que `boolean` sueltos.

## Objetivo

Modelar estados de préstamo/libro (o tu dominio) con **discriminated unions**; eliminar flags inconsistentes (`prestado` + `fechaDevolucion` sin sentido).

## Pasos

### 1. Lectura (45 min)

Handbook: union types, literal types.

### 2. Diseño (60 min)

```ts
type EstadoLibro =
  | { tipo: "disponible" }
  | { tipo: "prestado"; hasta: Date }
  | { tipo: "reservado"; por: string };
```

Adapta a tu dominio.

### 3. Migración (120 min)

Refactor entidades; actualiza métodos y tests.

### 4. Funciones totales (90 min)

`function puedePrestar(estado: EstadoLibro): boolean` con switch exhaustivo (`never` en default).

### 5. Commit (15 min)

`refactor(m06): union types para estados`

## Hecho cuando

1. Estados inválidos no representables en tipos (en la medida posible).
2. Switch exhaustivo con `assertNever`.
3. Tests actualizados.

## Errores comunes

- `string` libre donde cabe union literal.
- Mezclar null y union sin criterio.

## Siguiente

[L10 — Narrowing y type guards](L10-narrowing-y-type-guards.md)
