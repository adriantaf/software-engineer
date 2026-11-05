---
id: L02
materia: M15
orden: 2
titulo: Tests unitarios puros de reglas de pedido
horas: 5
semana: 1
lectura: Código limpio cap. pruebas; reglas de solape/estado
evidencia: tests/domain/ reglas de pedido ≥5 tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La base de la pirámide: reglas que el dueño del negocio nota si fallan
      (doble booking).


      **Objetivo de esta lección:** Suite unitaria de dominio de pedidos sin DB
      ni HTTP.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Extrae regla
    xp: 10
    cuerpo: >-
      ```ts

      export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date,
      bEnd: Date): boolean {
        return aStart < bEnd && bStart < aEnd;
      }

      ```


      Ejemplo:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tabla de casos
    xp: 10
    cuerpo: >-
      ```ts

      export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date,
      bEnd: Date): boolean {
        return aStart < bEnd && bStart < aEnd;
      }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests unitarios puros de reglas de pedido», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests unitarios puros
          de reglas de pedi…
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
      ¿Es recomendable en esta lección? “Tests que levantan servidor HTTP para
      una resta de fechas."
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
        texto: Suite unitaria de dominio de pedidos sin DB ni HTTP.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Red→green
    xp: 10
    cuerpo: >-
      Rompe la función, mira fallar, restaura — anota en
      `docs/red-green-pedido.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Funciones de dominio (solape, transición de estado, o validar rango) con
        ≥5 tests.
      - >-
        Al menos un test que falla si rompes la regla a propósito (red→green
        documentado en nota breve).
      - 'Commit `test(m15): reglas de pedido unitarias`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Tests unitarios puros de reglas de pedido

**~5.0 h · Semana 1**

La base de la pirámide: reglas que el dueño del negocio nota si fallan (doble booking).

## Objetivo

Suite unitaria de dominio de pedidos sin DB ni HTTP.

## Pasos (hazlos en orden)

### 1. Extrae regla (40–50 min)

Ejemplo:

```ts
export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date, bEnd: Date): boolean {
  return aStart < bEnd && bStart < aEnd;
}
```

### 2. Tabla de casos (60–70 min)

Adyacentes, contenidos, idénticos, invertidos (`end < start` → throw/invalid).

### 3. Red→green (30 min)

Rompe la función, mira fallar, restaura — anota en `docs/red-green-pedido.md`.

### 4. Commit

`test(m15): reglas de pedido unitarias`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Unit tests puros: sin I/O; reglas de pedido | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Funciones de dominio (solape, transición de estado, o validar rango) con ≥5 tests.
2. Al menos un test que **falla** si rompes la regla a propósito (red→green documentado en nota breve).
3. Commit `test(m15): reglas de pedido unitarias`.

## Errores comunes

- Tests que levantan servidor HTTP para una resta de fechas.
- Asserts débiles (`toBeTruthy` en objetos).
- Reglas duplicadas en test y producción divergentes.

## Siguiente

[L03 — Qué no testear y carpetas de coverage](L03-que-no-testear-y-carpetas-de-coverage.md)
