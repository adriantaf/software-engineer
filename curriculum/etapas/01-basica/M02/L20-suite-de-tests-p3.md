---
id: L20
materia: M02
orden: 20
titulo: Suite de tests (P3)
horas: 3
semana: 5
lectura: Vitest — matchers y casos borde
evidencia: npm test verde con ≥10 tests de dominio (habits + reportes)
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cobertura de validación, parse, reportes y funciones sobre
      `Habito[]` — tests rápidos y deterministas.


      La evidencia P3 es binaria: `npm test` verde y conteo ≥10. La CLI
      confiable se sostiene aquí.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario de funciones puras
    xp: 10
    cuerpo: 'Lista en `TESTING.md` qué funciones merecen test (dominio, no `main`).'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Suite de tests (P3)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: npm test verde con ≥10 tests de dominio (habits + reportes)
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
      ¿Es buena práctica en esta lección? “Tests que leen `habits.json` real
      (frágiles)."
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
          Cobertura de validación, parse, reportes y funciones sobre `Habito[]`
          — tests rápidos y deterministas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ampliar suite
    xp: 10
    cuerpo: |-
      Apunta a ≥10 tests totales, por ejemplo:

      - `parseArgv` (3+)
      - `validarNombreHabito` (3+)
      - `formatearReporte` / `totalMarcados` (4+)

      Usa `describe` por módulo.
  - id: s7
    tipo: explicacion
    titulo: 3. Casos borde
    xp: 10
    cuerpo: >-
      Nombre vacío, JSON de reporte con `items: []`, hábito sin completados en
      stats futuro.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`npm test` → ≥10 tests passing.'
      - '`TESTING.md` o README explica qué cubre cada grupo.'
      - Listo para marcar P3 en la ficha con evidencia.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Suite de tests (P3)

**~3 h · Semana 5**

Completas la **práctica P3**: ≥10 tests de lógica de dominio, sin tocar red ni disco real en la mayoría.

## Objetivo

Cobertura de validación, parse, reportes y funciones sobre `Habito[]` — tests rápidos y deterministas.

## Por qué importa

La evidencia P3 es binaria: `npm test` verde y conteo ≥10. La CLI confiable se sostiene aquí.

## Pasos

### 1. Inventario de funciones puras (20 min)

Lista en `TESTING.md` qué funciones merecen test (dominio, no `main`).

### 2. Ampliar suite (100 min)

Apunta a ≥10 tests totales, por ejemplo:

- `parseArgv` (3+)
- `validarNombreHabito` (3+)
- `formatearReporte` / `totalMarcados` (4+)

Usa `describe` por módulo.

### 3. Casos borde (40 min)

Nombre vacío, JSON de reporte con `items: []`, hábito sin completados en stats futuro.

### 4. CI local (20 min)

Documenta en README: `npm test` antes de cada commit de features.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Vitest | [Matchers](https://vitest.dev/api/expect.html) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `npm test` → ≥10 tests passing.
2. `TESTING.md` o README explica qué cubre cada grupo.
3. Listo para marcar **P3** en la ficha con evidencia.

## Errores comunes

- Tests que leen `habits.json` real (frágiles).
- Un solo test gigante.
- No correr tests tras refactor L18.

## Siguiente

[L21 — CLI: dominio y persistencia](L21-cli-dominio-y-persistencia.md)
