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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Capa de regresión sobre la API pública de
      `projects/m14-patrones`.


      Los patrones van a mover archivos. Los tests deben anclar el
      *comportamiento* exportado.
  - id: s2
    tipo: ejemplo
    titulo: 1. Define superficie pública
    xp: 10
    cuerpo: '`src/index.ts` reexporta lo estable.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests de regresión en API pública del módulo" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: tests de regresión sobre exports públicos + nota
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
    pregunta: ¿Es buena práctica en esta lección? “Tests acoplados a nombres privados."
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
        texto: Capa de regresión sobre la API pública de `projects/m14-patrones`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tests de contrato
    xp: 10
    cuerpo: 'Casos: precio promo, notifier channel, agendar ok/conflicto.'
  - id: s7
    tipo: explicacion
    titulo: 3. Nota + commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
