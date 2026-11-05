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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `projects/m15-calidad/checklist-review.md` usable.

      P3 empieza aquí: lo que mirarás en cada PR del piloto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Borrador por secciones
    xp: 10
    cuerpo: >-
      Estilo · Tests · Authz · Validación · Migraciones · Secrets ·
      Observabilidad mínima.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Checklist de code review" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: checklist-review.md (P3)
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
    pregunta: ¿Es buena práctica en esta lección? “Lista de 80 ítems inusable."
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
        texto: '`projects/m15-calidad/checklist-review.md` usable.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m15): checklist de code review`'
  - id: s7
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
