---
id: L08
materia: M21
orden: 8
titulo: Sprint 2 documentado y avance P2
horas: 5
semana: 2
lectura: Scrum Guide — Sprint Review y Retrospective
evidencia: projects/m21-proyectos/sprints/sprint-02.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Planificar y registrar sprint 2; retrospectiva del sprint 1
      con mantener/cambiar/probar.


      P2 pide **4 sprints**; hoy dejas dos registros distintos y accionables.


      Conceptos que debes poder explicar al cerrar:


      - Retro formato 3 preguntas.

      - Review con demo URL.

      - Aprendizaje ≠ excusa.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l08 sprint-2-documentado-y-avance-p2"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sprint 2 documentado y avance P2" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/sprints/sprint-02.md
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
          Planificar y registrar sprint 2; retrospectiva del sprint 1 con
          mantener/cambiar/probar.
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
    cuerpo: |-
      Confirma rutas bajo `projects/m21-proyectos/sprints`.

      Cierra sprint 1: sección **Retrospectiva** (mantener / cambiar / probar).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Abre `projects/m21-proyectos/sprints/sprint-02.md` con nueva meta. Al
      final de la lección, sprint 2 debe tener plan **y** al menos una fila de
      progreso en la tabla.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/sprints/sprint-02.md`.'
      - sprint-01 retro completa.
      - sprint-02.md creado.
      - DoD usada en cierre.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Sprint 2 documentado y avance P2

**~5 h · Semana 2**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/sprints/sprint-02.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Planificar y registrar sprint 2; retrospectiva del sprint 1 con mantener/cambiar/probar.

## Por qué empieza así

P2 pide **4 sprints**; hoy dejas dos registros distintos y accionables.

Conceptos que debes poder explicar al cerrar:

- Retro formato 3 preguntas.
- Review con demo URL.
- Aprendizaje ≠ excusa.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — Sprint Review y Retrospective_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos/sprints`.

Cierra sprint 1: sección **Retrospectiva** (mantener / cambiar / probar).

### 3. Laboratorio principal (90–120 min)

Abre `projects/m21-proyectos/sprints/sprint-02.md` con nueva meta. Al final de la lección, sprint 2 debe tener plan **y** al menos una fila de progreso en la tabla.

### 4. Endurece el entregable (40–60 min)

Verifica DoD en ≥1 issue cerrado esta semana.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l08 sprint-2-documentado-y-avance-p2"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — Sprint Review y Retrospective | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/sprints/sprint-02.md`.
2. sprint-01 retro completa.
3. sprint-02.md creado.
4. DoD usada en cierre.
5. Commit `docs(m21): l08 …` en el historial.

## Errores comunes

- Retro vacía.
- Sprint 2 copia-pega de sprint 1.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — Matriz de riesgos del producto y del proyecto](L09-matriz-de-riesgos-del-producto-y-del-proyecto.md)
