---
id: L22
materia: M22
orden: 22
titulo: Síntesis comercial para backlog M21
horas: 5
semana: 6
lectura: Lean — aprendizaje → producto
evidencia: projects/m22-bektor/handoff-producto.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El hilo Ops/SaaS cierra loop gestión ↔ mercado.


      Conceptos que debes poder explicar al cerrar:


      - Backlog.

      - Prioridad.

      - Issue template.

      - Demo feedback.


      **Objetivo de esta lección:** Traducir aprendizajes comerciales en ≥5
      issues priorizados para Vitrina (M21 backlog).


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
      git commit -m "docs(m22): l22 s-ntesis-comercial-para-backlog-m21"
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
      git commit -m "docs(m22): l22 s-ntesis-comercial-para-backlog-m21"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Síntesis comercial para backlog M21», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Síntesis comercial para
          backlog M21
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
          Traducir aprendizajes comerciales en ≥5 issues priorizados para
          Vitrina (M21 backlog).
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
      Crea o enlaza issues reales en repo producto. Notifica en
      `projects/m21-proyectos/board.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/handoff-producto.md`.'
      - ≥5 issues sugeridos.
      - Enlaces GitHub.
      - board.md actualizado.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Síntesis comercial para backlog M21

**~5 h · Semana 6**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/handoff-producto.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Traducir aprendizajes comerciales en ≥5 issues priorizados para Vitrina (M21 backlog).

## Por qué empieza así

El hilo Ops/SaaS cierra loop gestión ↔ mercado.

Conceptos que debes poder explicar al cerrar:

- Backlog.
- Prioridad.
- Issue template.
- Demo feedback.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — aprendizaje → producto_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/handoff-producto.md`: tabla aprendizaje → issue sugerido → prioridad.

### 3. Laboratorio principal (90–120 min)

Crea o enlaza issues reales en repo producto. Notifica en `projects/m21-proyectos/board.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l22 s-ntesis-comercial-para-backlog-m21"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — aprendizaje → producto | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/handoff-producto.md`.
2. ≥5 issues sugeridos.
3. Enlaces GitHub.
4. board.md actualizado.

## Errores comunes

- Lista deseos sin issues.
- Features sin origen demo.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L23 — Pitch final 60s y práctica grabada](L23-pitch-final-60s-y-practica-grabada.md)
