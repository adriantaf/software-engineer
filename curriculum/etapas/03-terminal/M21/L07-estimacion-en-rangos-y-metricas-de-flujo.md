---
id: L07
materia: M21
orden: 7
titulo: Estimación en rangos y métricas de flujo
horas: 5
semana: 2
lectura: Notas lean/kanban — throughput y carry-over
evidencia: projects/m21-proyectos/metricas-flujo.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar estimaciones en tres rangos y calcular throughput
      simple (issues cerrados/semana) y carry-over.


      Sin métricas de flujo repites el mismo error de estimación en M22 (demos)
      y M26 (capstone).


      Conceptos que debes poder explicar al cerrar:


      - Optimista/realista/pesimista.

      - Throughput.

      - Lead time (idea).

      - Carry-over.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l07 estimaci-n-en-rangos-y-m-tricas-de-flujo"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Estimación en rangos y métricas de flujo" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/metricas-flujo.md
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
          Documentar estimaciones en tres rangos y calcular throughput simple
          (issues cerrados/semana) y carry-over.
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
      Confirma rutas bajo `projects/m21-proyectos`.


      Crea `projects/m21-proyectos/metricas-flujo.md` con definiciones y
      **números reales** del sprint 1.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: 'Tabla: issue, estimación (3 columnas), horas reales si las tienes, estado.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/metricas-flujo.md`.'
      - metricas-flujo.md con números.
      - Rangos en ≥3 issues.
      - Acción para sprint 2.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Estimación en rangos y métricas de flujo

**~5 h · Semana 2**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/metricas-flujo.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Documentar estimaciones en tres rangos y calcular throughput simple (issues cerrados/semana) y carry-over.

## Por qué empieza así

Sin métricas de flujo repites el mismo error de estimación en M22 (demos) y M26 (capstone).

Conceptos que debes poder explicar al cerrar:

- Optimista/realista/pesimista.
- Throughput.
- Lead time (idea).
- Carry-over.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Notas lean/kanban — throughput y carry-over_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Crea `projects/m21-proyectos/metricas-flujo.md` con definiciones y **números reales** del sprint 1.

### 3. Laboratorio principal (90–120 min)

Tabla: issue, estimación (3 columnas), horas reales si las tienes, estado.

### 4. Endurece el entregable (40–60 min)

Calcula: issues cerrados esta semana / issues arrastrados. Una frase: qué cambiarás en sprint 2.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l07 estimaci-n-en-rangos-y-m-tricas-de-flujo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Notas lean/kanban — throughput y carry-over | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/metricas-flujo.md`.
2. metricas-flujo.md con números.
3. Rangos en ≥3 issues.
4. Acción para sprint 2.
5. Commit `docs(m21): l07 …` en el historial.

## Errores comunes

- Solo horas planeadas sin real.
- Vanity ‘100% productividad’.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Sprint 2 documentado y avance P2](L08-sprint-2-documentado-y-avance-p2.md)
