---
id: L12
materia: M16
orden: 12
titulo: Cierre M16 — handoff M17 y criterios dominio
horas: 5
semana: 3
lectura: Handoff UX→implementación M17; criterios dominio
evidencia: README índice + handoff-m17.md + autoevaluación
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Handoff + autoevaluación de criterios de dominio.


      Cierras IHC dejando al yo-de-M17 una lista accionable, no un PDF de
      adorno.
  - id: s2
    tipo: ejemplo
    titulo: 1. handoff-m17.md
    xp: 10
    cuerpo: Tickets UX → pantallas/endpoints M13.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M16 — handoff M17 y criterios dominio" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: README índice + handoff-m17.md + autoevaluación
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
      ¿Es buena práctica en esta lección? “Handoff sin rutas a
      prototipo/informe."
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
        texto: Handoff + autoevaluación de criterios de dominio.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Criterios de dominio
    xp: 10
    cuerpo: >-
      Informe con prioridades; hallazgo alto abordado; guion reutilizable;
      mensajes sin filtrar datos ajenos.
  - id: s7
    tipo: explicacion
    titulo: 4. Commit
    xp: 10
    cuerpo: '`docs(m16): cierre handoff M17 y dominio`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - README M16 índice P1–P3 + informe.
      - '`handoff-m17.md` con cambios UX a implementar en el front real.'
      - 'Commit `docs(m16): cierre handoff M17 y dominio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Cierre M16 — handoff M17 y criterios dominio

**~5.0 h · Semana 3**

Cierras IHC dejando al yo-de-M17 una lista accionable, no un PDF de adorno.

## Objetivo

Handoff + autoevaluación de criterios de dominio.

## Pasos (hazlos en orden)

### 1. handoff-m17.md (50–60 min)

Tickets UX → pantallas/endpoints M13.

### 2. README final (40 min)

### 3. Criterios de dominio (40 min)

Informe con prioridades; hallazgo alto abordado; guion reutilizable; mensajes sin filtrar datos ajenos.

### 4. Commit

`docs(m16): cierre handoff M17 y dominio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Handoff a M17 y criterios de dominio de la ficha | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. README M16 índice P1–P3 + informe.
2. `handoff-m17.md` con cambios UX a implementar en el front real.
3. Commit `docs(m16): cierre handoff M17 y dominio`.

## Errores comunes

- Handoff sin rutas a prototipo/informe.
- Criterios de dominio todos ✓ sin evidencia.
- Guion no reutilizable.

## Siguiente

Materia siguiente: [M17 — Aplicaciones web](../M17-aplicaciones-web.md).
