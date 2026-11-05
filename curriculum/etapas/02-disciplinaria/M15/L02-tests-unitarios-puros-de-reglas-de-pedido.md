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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Suite unitaria de dominio de pedidos sin DB ni HTTP.


      La base de la pirámide: reglas que el dueño del negocio nota si fallan
      (doble booking).
  - id: s2
    tipo: ejemplo
    titulo: 1. Extrae regla
    xp: 10
    cuerpo: >-
      ```ts

      export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date,
      bEnd: Date): boolean {
        return aStart < bEnd && bStart < aEnd;
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests unitarios puros de reglas de pedido" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: tests/domain/ reglas de pedido ≥5 tests
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
      ¿Es buena práctica en esta lección? “Tests que levantan servidor HTTP para
      una resta de fechas."
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
        texto: Suite unitaria de dominio de pedidos sin DB ni HTTP.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla de casos
    xp: 10
    cuerpo: >-
      Adyacentes, contenidos, idénticos, invertidos (`end < start` →
      throw/invalid).
  - id: s7
    tipo: explicacion
    titulo: 3. Red→green
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
