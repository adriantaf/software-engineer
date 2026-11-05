---
id: L15
materia: M22
orden: 15
titulo: Objeción
horas: 5
semana: 4
lectura: Lean — build-measure-learn en producto
evidencia: projects/m22-bektor/objeciones-sintesis.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Criterio dominio: nombrar objeción #1 y qué cambiaste.


      Conceptos que debes poder explicar al cerrar:


      - Objeción.

      - Backlog producto.

      - Mensaje.

      - Trazabilidad M21.


      **Objetivo de esta lección:** Identificar objeción más frecuente y
      documentar cambio en mensaje **o** issue en backlog Vitrina.


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
      git commit -m "docs(m22): l15 objeci-n-1-y-cambio-de-producto-o-mensaj"
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
      git commit -m "docs(m22): l15 objeci-n-1-y-cambio-de-producto-o-mensaj"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: 'Al terminar «Objeción», ¿qué demuestra que cumpliste el criterio mínimo?'
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Objeción
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
          Identificar objeción más frecuente y documentar cambio en mensaje o
          issue en backlog Vitrina.
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
      Abre issue en repo producto **o** entrada en
      `projects/m21-proyectos/roadmap-trimestre.md` si el fix es producto.
      Enlaza en demo fichas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/objeciones-sintesis.md`.'
      - Top 3 objeciones.
      - Cambio mensaje/producto enlazado.
      - Issue o roadmap.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Objeción #1 y cambio de producto o mensaje

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/objeciones-sintesis.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Identificar objeción más frecuente y documentar cambio en mensaje **o** issue en backlog Vitrina.

## Por qué empieza así

Criterio dominio: nombrar objeción #1 y qué cambiaste.

Conceptos que debes poder explicar al cerrar:

- Objeción.
- Backlog producto.
- Mensaje.
- Trazabilidad M21.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — build-measure-learn en producto_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Crea `projects/m22-bektor/objeciones-sintesis.md` con ranking top 3 objeciones.

### 3. Laboratorio principal (90–120 min)

Abre issue en repo producto **o** entrada en `projects/m21-proyectos/roadmap-trimestre.md` si el fix es producto. Enlaza en demo fichas.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l15 objeci-n-1-y-cambio-de-producto-o-mensaj"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — build-measure-learn en producto | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/objeciones-sintesis.md`.
2. Top 3 objeciones.
3. Cambio mensaje/producto enlazado.
4. Issue o roadmap.
5. Commit `docs(m22): l15 …` en el historial.

## Errores comunes

- Quejarse sin acción.
- Objeción inventada sin demos.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L16 — Refinar pricing tras métricas semana 4](L16-refinar-pricing-tras-metricas-semana-4.md)
