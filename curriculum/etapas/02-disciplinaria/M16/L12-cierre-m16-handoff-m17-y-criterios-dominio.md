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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras IHC dejando al yo-de-M17 una lista accionable, no un PDF de
      adorno.


      **Objetivo de esta lección:** Handoff + autoevaluación de criterios de
      dominio.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: handoff-m17.md
    xp: 10
    cuerpo: Tickets UX → pantallas/endpoints M13.
  - id: s3
    tipo: ejemplo
    titulo: Criterios de dominio
    xp: 10
    cuerpo: >-
      Informe con prioridades; hallazgo alto abordado; guion reutilizable;
      mensajes sin filtrar datos ajenos.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M16 — handoff M17 y criterios dominio», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M16 — handoff
          M17 y criterios do…
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
    pregunta: ¿Es recomendable en esta lección? “Handoff sin rutas a prototipo/informe."
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
        texto: Handoff + autoevaluación de criterios de dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M16
    xp: 25
    enunciado: >-
      Cierra **Interacción humano-computadora** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Heurísticas de Nielsen aplicadas a tu UI'
      - 'P2: Test de usabilidad con 5 personas'
      - 'P3: Iteración de UI basada en hallazgos'
      - 'Proyecto: Informe de usabilidad del piloto Vitrina'
      - README índice + handoff-m17.md + autoevaluación
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: README M16 índice P1–P3 + informe.
      - id: r3
        criterio: '`handoff-m17.md` con cambios UX a implementar en el front real.'
      - id: r4
        criterio: 'Commit `docs(m16): cierre handoff M17 y dominio`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - README M16 índice P1–P3 + informe.
      - '`handoff-m17.md` con cambios UX a implementar en el front real.'
      - 'Commit `docs(m16): cierre handoff M17 y dominio`.'
    siguiente: Materia M16 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
