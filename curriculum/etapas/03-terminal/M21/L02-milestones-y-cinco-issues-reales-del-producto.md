---
id: L02
materia: M21
orden: 2
titulo: Milestones y cinco issues reales del producto
horas: 5
semana: 1
lectura: Scrum Guide — artefactos y compromiso del backlog
evidencia: projects/m21-proyectos/board.md borrador
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El tablero ficticio no prepara trials (M22) ni FAQ (M23); hoy enlazas
      gestión al código que ya desplegaste.


      Conceptos que debes poder explicar al cerrar:


      - Milestone.

      - Issue vs épica.

      - Etiquetas feature/security/ops.

      - Prioridad vs urgencia.


      **Objetivo de esta lección:** Crear milestones de cuatro semanas de M21 y
      mover cinco issues **reales** del repo Vitrina al backlog priorizado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l02 milestones-y-cinco-issues-reales-del-pro"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l02 milestones-y-cinco-issues-reales-del-pro"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Milestones y cinco issues reales del producto», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Milestones y cinco
          issues reales del pr…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
        texto: >-
          Crear milestones de cuatro semanas de M21 y mover cinco issues reales
          del repo Vitrina al backlog priorizado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: >-
      Mueve **5 issues** del repo producto al backlog ordenado. **Al menos uno**
      debe ser seguridad o `tenant_id` (cross-tenant, secretos, backup).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/board.md borrador`.'
      - 5 issues enlazados.
      - ≥1 issue security/tenant.
      - board.md con URL.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Milestones y cinco issues reales del producto

**~5 h · Semana 1**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/board.md borrador`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Crear milestones de cuatro semanas de M21 y mover cinco issues **reales** del repo Vitrina al backlog priorizado.

## Por qué empieza así

El tablero ficticio no prepara trials (M22) ni FAQ (M23); hoy enlazas gestión al código que ya desplegaste.

Conceptos que debes poder explicar al cerrar:

- Milestone.
- Issue vs épica.
- Etiquetas feature/security/ops.
- Prioridad vs urgencia.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — artefactos y compromiso del backlog_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

En GitHub Projects (o Linear): milestones `M21-S1` … `M21-S4` con fechas orientativas.

### 3. Laboratorio principal (90–120 min)

Mueve **5 issues** del repo producto al backlog ordenado. **Al menos uno** debe ser seguridad o `tenant_id` (cross-tenant, secretos, backup).

### 4. Endurece el entregable (40–60 min)

Escribe `projects/m21-proyectos/board.md` con URL del board + fecha de captura. Lista los 5 issues con enlace `#`.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l02 milestones-y-cinco-issues-reales-del-pro"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — artefactos y compromiso del backlog | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/board.md borrador`.
2. 5 issues enlazados.
3. ≥1 issue security/tenant.
4. board.md con URL.
5. Commit `docs(m21): l02 …` en el historial.

## Errores comunes

- Issues de tutorial sin repo producto.
- Milestone sin fechas.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Roadmap trimestral alineado a producto-saas](L03-roadmap-trimestral-alineado-a-producto-saas.md)
