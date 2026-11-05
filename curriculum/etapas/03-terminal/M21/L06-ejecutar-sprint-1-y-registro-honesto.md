---
id: L06
materia: M21
orden: 6
titulo: Ejecutar sprint 1 y registro honesto
horas: 5
semana: 2
lectura: Scrum Guide — Daily Scrum (adaptado a bitácora)
evidencia: projects/m21-proyectos/sprints/sprint-01.md tabla hecho
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Trabajar el sprint 1 sobre Vitrina y registrar **hecho
      real** vs planeado sin borrar desviaciones.


      La retrospectiva útil exige datos honestos; inflar ‘hecho’ destruye P2.


      Conceptos que debes poder explicar al cerrar:


      - Daily de 3 líneas.

      - Bloqueo documentado.

      - Carry-over explícito.

      - Demo a ti mismo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l06 ejecutar-sprint-1-y-registro-honesto"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Ejecutar sprint 1 y registro honesto" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/sprints/sprint-01.md tabla hecho
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Trabajar el sprint 1 sobre Vitrina y registrar **hecho real** vs
          planeado sin borrar desviaciones.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m21-proyectos/sprints`.


      Durante el sprint, añade notas diarias de 3 líneas en `sprint-01.md`
      (ayer/hoy/bloqueo).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Al cerrar parcialmente la semana, llena la tabla **Planeado | Hecho |
      Aprendizaje** aunque falte trabajo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m21-proyectos/sprints/sprint-01.md tabla
        hecho`.
      - Tabla parcialmente llena.
      - ≥3 notas diarias.
      - Desviación explicada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Ejecutar sprint 1 y registro honesto

**~5 h · Semana 2**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/sprints/sprint-01.md tabla hecho`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Trabajar el sprint 1 sobre Vitrina y registrar **hecho real** vs planeado sin borrar desviaciones.

## Por qué empieza así

La retrospectiva útil exige datos honestos; inflar ‘hecho’ destruye P2.

Conceptos que debes poder explicar al cerrar:

- Daily de 3 líneas.
- Bloqueo documentado.
- Carry-over explícito.
- Demo a ti mismo.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — Daily Scrum (adaptado a bitácora)_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos/sprints`.

Durante el sprint, añade notas diarias de 3 líneas en `sprint-01.md` (ayer/hoy/bloqueo).

### 3. Laboratorio principal (90–120 min)

Al cerrar parcialmente la semana, llena la tabla **Planeado | Hecho | Aprendizaje** aunque falte trabajo.

### 4. Endurece el entregable (40–60 min)

Si subestimaste migración o deploy, escribe **horas reales** aproximadas.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l06 ejecutar-sprint-1-y-registro-honesto"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — Daily Scrum (adaptado a bitácora) | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/sprints/sprint-01.md tabla hecho`.
2. Tabla parcialmente llena.
3. ≥3 notas diarias.
4. Desviación explicada.
5. Commit `docs(m21): l06 …` en el historial.

## Errores comunes

- Borrar filas ‘no hecho’.
- Cerrar issues sin DoD.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Estimación en rangos y métricas de flujo](L07-estimacion-en-rangos-y-metricas-de-flujo.md)
