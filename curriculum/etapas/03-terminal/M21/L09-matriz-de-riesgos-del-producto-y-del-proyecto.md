---
id: L09
materia: M21
orden: 9
titulo: Matriz de riesgos del producto y del proyecto
horas: 5
semana: 3
lectura: Gestión de riesgos (notas propias) + Scrum impediments
evidencia: projects/m21-proyectos/riesgos.md borrador
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 y criterios de dominio exigen riesgos accionables, no lista genérica de
      ‘bugs’.


      Conceptos que debes poder explicar al cerrar:


      - Probabilidad × impacto.

      - Riesgo vs issue.

      - Mitigación verificable.

      - Dueño = tú o mentor.


      **Objetivo de esta lección:** Identificar ≥5 riesgos con probabilidad,
      impacto, mitigación, dueño y fecha de revisión.


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
      git commit -m "docs(m21): l09 matriz-de-riesgos-del-producto-y-del-pro"
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
      git commit -m "docs(m21): l09 matriz-de-riesgos-del-producto-y-del-pro"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Matriz de riesgos del producto y del proyecto», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Matriz de riesgos del
          producto y del pr…
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
          Identificar ≥5 riesgos con probabilidad, impacto, mitigación, dueño y
          fecha de revisión.
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
      Incluye riesgos de **producto** (un solo design partner, scope creep) y
      **técnicos** (dependencia PaaS).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/riesgos.md borrador`.'
      - ≥5 riesgos.
      - Mitigación concreta cada uno.
      - Fechas revisión.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Matriz de riesgos del producto y del proyecto

**~5 h · Semana 3**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/riesgos.md borrador`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Identificar ≥5 riesgos con probabilidad, impacto, mitigación, dueño y fecha de revisión.

## Por qué empieza así

P3 y criterios de dominio exigen riesgos accionables, no lista genérica de ‘bugs’.

Conceptos que debes poder explicar al cerrar:

- Probabilidad × impacto.
- Riesgo vs issue.
- Mitigación verificable.
- Dueño = tú o mentor.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Gestión de riesgos (notas propias) + Scrum impediments_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Crea `projects/m21-proyectos/riesgos.md` con tabla (≥5 filas): descripción, P, I, mitigación, dueño, revisión.

### 3. Laboratorio principal (90–120 min)

Incluye riesgos de **producto** (un solo design partner, scope creep) y **técnicos** (dependencia PaaS).

### 4. Endurece el entregable (40–60 min)

Enlaza issues de mitigación cuando existan.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l09 matriz-de-riesgos-del-producto-y-del-pro"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Gestión de riesgos (notas propias) + Scrum impediments | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/riesgos.md borrador`.
2. ≥5 riesgos.
3. Mitigación concreta cada uno.
4. Fechas revisión.
5. Commit `docs(m21): l09 …` en el historial.

## Errores comunes

- Riesgos ‘hackeo’ sin vector.
- Sin dueño.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Riesgos de seguridad, privacidad y multi-tenant](L10-riesgos-de-seguridad-privacidad-y-multi-tenant.md)
