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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Modelar estados de préstamo/libro (o tu dominio) con
      **discriminated unions**; eliminar flags inconsistentes (`prestado` +
      `fechaDevolucion` sin sentido).


      Los union types modelan estados mutuamente excluyentes mejor que `boolean`
      sueltos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```ts
      type EstadoLibro =
        | { tipo: "disponible" }
        | { tipo: "prestado"; hasta: Date }
        | { tipo: "reservado"; por: string };
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Union types y modelado de estados" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Tipos de estado discriminated union + tests
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
      ¿Es buena práctica en esta lección? “`string` libre donde cabe union
      literal."
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
          Modelar estados de préstamo/libro (o tu dominio) con **discriminated
          unions**; eliminar flags inconsistentes (`prestado` +
          `fechaDevolucion…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Diseño
    xp: 10
    cuerpo: |-
      ```ts
      type EstadoLibro =
        | { tipo: "disponible" }
        | { tipo: "prestado"; hasta: Date }
        | { tipo: "reservado"; por: string };
      ```

      Adapta a tu dominio.
  - id: s7
    tipo: explicacion
    titulo: 3. Migración
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
