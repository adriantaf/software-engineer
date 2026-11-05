---
id: L12
materia: M21
orden: 12
titulo: 'Cierre M21 — P1–P3, dominio y handoff comercial'
horas: 5
semana: 3
lectura: Repaso ficha M21 criterios de dominio
evidencia: projects/m21-proyectos/cierre-m21.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Auditar evidencias P1–P3, tablero, cuatro sprints y redactar
      handoff a M22 (trials) y M23 (métricas).


      Cierras la materia de gestión antes de vender (M22) y medir con IA (M23).


      Conceptos que debes poder explicar al cerrar:


      - Checklist evidencia.

      - Pitch interno 5 min roadmap.

      - Handoff.

      - Riesgo residual.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l12 cierre-m21-p1-p3-dominio-y-handoff-comer"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M21 — P1–P3, dominio y handoff comercial" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/cierre-m21.md
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
          Auditar evidencias P1–P3, tablero, cuatro sprints y redactar handoff a
          M22 (trials) y M23 (métricas).
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


      Crea `projects/m21-proyectos/cierre-m21.md`: checklist P1–P3 + proyecto
      tablero; responde criterios dominio de la ficha.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Graba guion (texto) de **5 min** explicando roadmap a persona no técnica.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/cierre-m21.md`.'
      - cierre-m21.md completo.
      - README índice.
      - Commit cierre.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Cierre M21 — P1–P3, dominio y handoff comercial

**~5 h · Semana 3**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/cierre-m21.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Auditar evidencias P1–P3, tablero, cuatro sprints y redactar handoff a M22 (trials) y M23 (métricas).

## Por qué empieza así

Cierras la materia de gestión antes de vender (M22) y medir con IA (M23).

Conceptos que debes poder explicar al cerrar:

- Checklist evidencia.
- Pitch interno 5 min roadmap.
- Handoff.
- Riesgo residual.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Repaso ficha M21 criterios de dominio_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Crea `projects/m21-proyectos/cierre-m21.md`: checklist P1–P3 + proyecto tablero; responde criterios dominio de la ficha.

### 3. Laboratorio principal (90–120 min)

Graba guion (texto) de **5 min** explicando roadmap a persona no técnica.

### 4. Endurece el entregable (40–60 min)

Commit `docs(m21): cierre materia`. Actualiza `projects/m21-proyectos/README.md` con índice L01–L12.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l12 cierre-m21-p1-p3-dominio-y-handoff-comer"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Repaso ficha M21 criterios de dominio | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/cierre-m21.md`.
2. cierre-m21.md completo.
3. README índice.
4. Commit cierre.
5. Handoff M22/M23.

## Errores comunes

- Marcar UI sin archivos.
- Roadmap desalineado del board.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
