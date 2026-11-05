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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `Result` genérico y migrar operaciones core
      (`prestar`, `agregar`) a retorno `Result`.


      `Result<T, E>` hace explícito el fracaso sin depender solo de excepciones.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tipo base
    xp: 10
    cuerpo: |-
      ```ts
      export type Ok<T> = { ok: true; value: T };
      export type Err<E> = { ok: false; error: E };
      export type Result<T, E = string> = Ok<T> | Err<E>;
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Patrón Result tipado" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: API principal devuelve Result; helpers map/flatMap opcionales
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
    pregunta: '¿Es buena práctica en esta lección? “Result con `error: any`."'
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
          Implementar `Result` genérico y migrar operaciones core (`prestar`,
          `agregar`) a retorno `Result`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Helpers
    xp: 10
    cuerpo: '`ok()`, `err()`, `map`, `flatMap` (opcional pero recomendado).'
  - id: s7
    tipo: explicacion
    titulo: 3. Migración API
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
