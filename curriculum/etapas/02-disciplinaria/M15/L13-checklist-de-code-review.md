---
id: L13
materia: M15
orden: 13
titulo: Checklist de code review
horas: 5
semana: 4
lectura: 'Checklist review: calidad + seguridad'
evidencia: checklist-review.md (P3)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 empieza aquí: lo que mirarás en cada PR del piloto.


      **Objetivo de esta lección:** `projects/m15-calidad/checklist-review.md`
      usable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Borrador por secciones
    xp: 10
    cuerpo: >-
      Estilo · Tests · Authz · Validación · Migraciones · Secrets ·
      Observabilidad mínima.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m15): checklist de code review`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Checklist de code review», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Checklist de code
          review
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
    pregunta: ¿Es recomendable en esta lección? “Lista de 80 ítems inusable."
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
        texto: '`projects/m15-calidad/checklist-review.md` usable.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Cero ítems de seguridad."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `checklist-review.md` con ítems de estilo, tests, seguridad
        (auth/IDOR/validación), secrets.
      - 'Ítems accionables (sí/no), no vagos.'
      - 'Commit `docs(m15): checklist de code review`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Checklist de code review

**~5.0 h · Semana 4**

P3 empieza aquí: lo que mirarás en cada PR del piloto.

## Objetivo

`projects/m15-calidad/checklist-review.md` usable.

## Pasos (hazlos en orden)

### 1. Borrador por secciones (70–90 min)

Estilo · Tests · Authz · Validación · Migraciones · Secrets · Observabilidad mínima.

### 2. Alinea a M13 boundaries (30 min)

### 3. Commit

`docs(m15): checklist de code review`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Checklist PR: tests, auth, secrets, migraciones | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `checklist-review.md` con ítems de estilo, tests, seguridad (auth/IDOR/validación), secrets.
2. Ítems accionables (sí/no), no vagos.
3. Commit `docs(m15): checklist de code review`.

## Errores comunes

- Lista de 80 ítems inusable.
- Cero ítems de seguridad.
- Copiar checklist enterprise sin adaptar al piloto.

## Siguiente

[L14 — Review simulado en PR o notas](L14-review-simulado-en-pr-o-notas.md)
