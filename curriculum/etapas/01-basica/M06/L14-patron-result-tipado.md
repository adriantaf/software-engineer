---
id: L14
materia: M06
orden: 14
titulo: Patrón Result tipado
horas: 5
semana: 4
lectura: Notas M06 + ejemplo Result en ficha; artículos sobre Result/Either
evidencia: API principal devuelve Result; helpers map/flatMap opcionales
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      `Result<T, E>` hace explícito el fracaso sin depender solo de excepciones.


      **Objetivo de esta lección:** Implementar `Result` genérico y migrar
      operaciones core (`prestar`, `agregar`) a retorno `Result`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tipo base
    xp: 10
    cuerpo: |-
      ```ts
      export type Ok<T> = { ok: true; value: T };
      export type Err<E> = { ok: false; error: E };
      export type Result<T, E = string> = Ok<T> | Err<E>;
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Helpers
    xp: 10
    cuerpo: |-
      ```ts
      export type Ok<T> = { ok: true; value: T };
      export type Err<E> = { ok: false; error: E };
      export type Result<T, E = string> = Ok<T> | Err<E>;
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Patrón Result tipado», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Operaciones principales exportan Result.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Patrón Result tipado
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
    pregunta: '¿Es recomendable en esta lección? “Result con `error: any`."'
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
          Implementar `Result` genérico y migrar operaciones core (`prestar`,
          `agregar`) a retorno `Result`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Migración API
    xp: 10
    cuerpo: 'Elige: excepciones solo en frontera CLI; dominio usa Result.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Operaciones principales exportan Result.
      - Callers manejan `ok` con narrowing.
      - Tests cubren ambos caminos.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Patrón Result tipado

**~5 h · Semana 4**

`Result<T, E>` hace explícito el fracaso sin depender solo de excepciones.

## Objetivo

Implementar `Result` genérico y migrar operaciones core (`prestar`, `agregar`) a retorno `Result`.

## Pasos

### 1. Tipo base (60 min)

```ts
export type Ok<T> = { ok: true; value: T };
export type Err<E> = { ok: false; error: E };
export type Result<T, E = string> = Ok<T> | Err<E>;
```

### 2. Helpers (60 min)

`ok()`, `err()`, `map`, `flatMap` (opcional pero recomendado).

### 3. Migración API (120 min)

Elige: excepciones solo en frontera CLI; dominio usa Result.

### 4. Tests (60 min)

Casos ok y err tipados (`E` union de códigos literales).

### 5. Documentación (30 min)

En README interno, cuándo usar Result vs throw.

## Hecho cuando

1. Operaciones principales exportan Result.
2. Callers manejan `ok` con narrowing.
3. Tests cubren ambos caminos.

## Errores comunes

- Result con `error: any`.
- Mezclar throw y Result sin regla.

## Siguiente

[L15 — Tests de borde: null, vacío, duplicados (P3)](L15-tests-de-borde-p3.md)
