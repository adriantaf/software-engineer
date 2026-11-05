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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La evidencia P3 es binaria: `npm test` verde y conteo ≥10. La CLI
      confiable se sostiene aquí.


      **Objetivo de esta lección:** Cobertura de validación, parse, reportes y
      funciones sobre `Habito[]` — tests rápidos y deterministas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario de funciones puras
    xp: 10
    cuerpo: 'Lista en `TESTING.md` qué funciones merecen test (dominio, no `main`).'
  - id: s3
    tipo: ejemplo
    titulo: Ampliar suite
    xp: 10
    cuerpo: >-
      Apunta a ≥10 tests totales, por ejemplo: - `parseArgv` (3+) -
      `validarNombreHabito` (3+) - `formatearReporte` / `totalMarcados` (4+) Usa
      `describe` por módulo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Suite de tests (P3)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`npm test` → ≥10 tests passing.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Suite de tests (P3)
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
      ¿Es recomendable en esta lección? “Tests que leen `habits.json` real
      (frágiles)."
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
          Cobertura de validación, parse, reportes y funciones sobre `Habito[]`
          — tests rápidos y deterministas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Casos borde
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
