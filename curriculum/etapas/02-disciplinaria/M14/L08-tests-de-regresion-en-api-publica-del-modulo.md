---
id: L08
materia: M14
orden: 8
titulo: Tests de regresión en API pública del módulo
horas: 5
semana: 2
lectura: Tests de contrato/API pública; no internals
evidencia: tests de regresión sobre exports públicos + nota
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los patrones van a mover archivos. Los tests deben anclar el
      *comportamiento* exportado.


      **Objetivo de esta lección:** Capa de regresión sobre la API pública de
      `projects/m14-patrones`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Define superficie pública
    xp: 10
    cuerpo: '`src/index.ts` reexporta lo estable.'
  - id: s3
    tipo: ejemplo
    titulo: Tests de contrato
    xp: 10
    cuerpo: 'Casos: precio promo, notifier channel, agendar ok/conflicto.'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests de regresión en API pública del módulo», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests de regresión en
          API pública del m…
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
    pregunta: ¿Es recomendable en esta lección? “Tests acoplados a nombres privados."
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
        texto: Capa de regresión sobre la API pública de `projects/m14-patrones`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota + commit
    xp: 10
    cuerpo: '`test(m14): regresion api publica modulos`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Suite que ejercita exports públicos (pricing, factory, facade) en verde.'
      - >-
        `docs/regresion-api-publica.md` lista qué es “contrato” vs detalle
        interno.
      - 'Commit `test(m14): regresion api publica modulos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Tests de regresión en API pública del módulo

**~5.0 h · Semana 2**

Los patrones van a mover archivos. Los tests deben anclar el *comportamiento* exportado.

## Objetivo

Capa de regresión sobre la API pública de `projects/m14-patrones`.

## Pasos (hazlos en orden)

### 1. Define superficie pública (30 min)

`src/index.ts` reexporta lo estable.

### 2. Tests de contrato (80–100 min)

Casos: precio promo, notifier channel, agendar ok/conflicto.

### 3. Nota + commit

`test(m14): regresion api publica modulos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Proteger el comportamiento público tras refactors de patrones | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Suite que ejercita exports públicos (pricing, factory, facade) en verde.
2. `docs/regresion-api-publica.md` lista qué es “contrato” vs detalle interno.
3. Commit `test(m14): regresion api publica modulos`.

## Errores comunes

- Tests acoplados a nombres privados.
- Borrar tests “porque cambió el patrón”.
- Cobertura solo de archivos vacíos.

## Siguiente

[L09 — Observer para eventos de dominio](L09-observer-para-eventos-de-dominio.md)
