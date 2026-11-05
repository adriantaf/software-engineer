---
id: L04
materia: M24
orden: 4
titulo: Cierre research semana 1 y backlog M21
horas: 5
semana: 1
lectura: Repaso research + issues Vitrina
evidencia: projects/m24-emergentes/research/README.md + enlace issue M21
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El spike debe resolver duda del producto, no curiosidad técnica aislada.


      Conceptos que debes poder explicar al cerrar:


      - Definition of spike

      - Non-goals

      - Evidencia en git


      **Objetivo de esta lección:** Cerrar P1 research: índice de notas y al
      menos un issue o comentario en backlog relacionado (spike futuro o
      descarte).


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
      git commit -m "docs(m24): l04 cierre-research-semana-1-y-backlog-m21"
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
      git commit -m "docs(m24): l04 cierre-research-semana-1-y-backlog-m21"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre research semana 1 y backlog M21», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre research semana
          1 y backlog M21
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
          Cerrar P1 research: índice de notas y al menos un issue o comentario
          en backlog relacionado (spike futuro o descarte).
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
      En el repo del producto o `projects/m21-proyectos/`, abre issue “M24
      spike: …” o comenta en roadmap.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m24-emergentes/research/README.md +
        enlace issue M21`.
      - README research.
      - Enlace a issue/comentario backlog.
      - Bitácora semana 1 cerrada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre research semana 1 y backlog M21

**~5 h · Semana 1**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/research/README.md + enlace issue M21`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Cerrar P1 research: índice de notas y al menos un issue o comentario en backlog relacionado (spike futuro o descarte).

## Por qué empieza así

El spike debe resolver duda del producto, no curiosidad técnica aislada.

Conceptos que debes poder explicar al cerrar:

- Definition of spike
- Non-goals
- Evidencia en git

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Repaso research + issues Vitrina_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/research`.

`projects/m24-emergentes/research/README.md` enlaza los tres candidatos y resume en 10 líneas cuál parece más prometedor **sin** decidir aún.

### 3. Laboratorio principal (90–120 min)

En el repo del producto o `projects/m21-proyectos/`, abre issue “M24 spike: …” o comenta en roadmap.

### 4. Endurece el entregable (40–60 min)

Cierra `bitacora/semana-01.md` con horas reales vs plan.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l04 cierre-research-semana-1-y-backlog-m21"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Repaso research + issues Vitrina | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/research/README.md + enlace issue M21`.
2. README research.
3. Enlace a issue/comentario backlog.
4. Bitácora semana 1 cerrada.
5. Commit `docs(m24): l04 …` en el historial.

## Errores comunes

- Marcar P1 sin tres archivos.
- Prometer feature en M26 sin go/no-go.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Matriz de adopción y pesos](L05-matriz-de-adopcion-y-pesos.md)
