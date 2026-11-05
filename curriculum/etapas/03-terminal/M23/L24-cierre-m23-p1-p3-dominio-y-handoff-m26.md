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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre;
      README L01–L24.


      Cierras hilo IA/datos antes de emergentes (M24) y capstone (M26).


      Conceptos que debes poder explicar al cerrar:


      - Checklist.

      - Cross-tenant demo.

      - Dominio.

      - Handoff.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l24 cierre-m23-p1-p3-dominio-y-handoff-m26"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M23 — P1–P3, dominio y handoff M26" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m23-ia/cierre-m23.md
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
          Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre; README
          L01–L24.
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
      Confirma rutas bajo `projects/m23-ia`.


      `projects/m23-ia/cierre-m23.md` responde criterios dominio. Verifica
      política LLM respetada en scripts.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Commit `docs(m23): cierre materia`. Actualiza `projects/m23-ia/README.md`
      índice lecciones.
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
