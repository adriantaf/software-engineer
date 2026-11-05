---
id: L24
materia: M23
orden: 24
titulo: 'Cierre M23 — P1–P3, dominio y handoff M26'
horas: 5
semana: 6
lectura: Repaso ficha M23
evidencia: projects/m23-ia/cierre-m23.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras hilo IA/datos antes de emergentes (M24) y capstone (M26).


      Conceptos que debes poder explicar al cerrar:


      - Checklist.

      - Cross-tenant demo.

      - Dominio.

      - Handoff.


      **Objetivo de esta lección:** Auditar pipeline, eval LLM, RAG aislado,
      FAQ; commit cierre; README L01–L24.


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
      git commit -m "docs(m23): l24 cierre-m23-p1-p3-dominio-y-handoff-m26"
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
      git commit -m "docs(m23): l24 cierre-m23-p1-p3-dominio-y-handoff-m26"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M23 — P1–P3, dominio y handoff M26», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M23 — P1–P3,
          dominio y handoff M…
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
          Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre; README
          L01–L24.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M23
    xp: 25
    enunciado: >-
      Cierra **Ciencia de datos e IA aplicada** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Pipeline de métricas del SaaS (por tenant)'
      - 'P2: Integración LLM con prompts evaluados'
      - 'P3: RAG por tenant (sin mezclar datos ni PII innecesaria)'
      - 'Proyecto: Asistente FAQ scoped por tenant (Vitrina)'
      - projects/m23-ia/cierre-m23.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: 'Existe el entregable: `projects/m23-ia/cierre-m23.md`.'
      - id: r3
        criterio: cierre-m23.md.
      - id: r4
        criterio: Commit cierre.
      - id: r5
        criterio: README índice.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/cierre-m23.md`.'
      - cierre-m23.md.
      - Commit cierre.
      - README índice.
    siguiente: Materia M23 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M23 — P1–P3, dominio y handoff M26

**~5 h · Semana 6**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/cierre-m23.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre; README L01–L24.

## Por qué empieza así

Cierras hilo IA/datos antes de emergentes (M24) y capstone (M26).

Conceptos que debes poder explicar al cerrar:

- Checklist.
- Cross-tenant demo.
- Dominio.
- Handoff.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Repaso ficha M23_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia`.

`projects/m23-ia/cierre-m23.md` responde criterios dominio. Verifica política LLM respetada en scripts.

### 3. Laboratorio principal (90–120 min)

Commit `docs(m23): cierre materia`. Actualiza `projects/m23-ia/README.md` índice lecciones.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l24 cierre-m23-p1-p3-dominio-y-handoff-m26"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Repaso ficha M23 | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/cierre-m23.md`.
2. cierre-m23.md.
3. Commit cierre.
4. README índice.
5. P1–P3 verificados.

## Errores comunes

- Marcar UI sin test cross-tenant.
- PII en logs eval.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
