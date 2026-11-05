---
id: L30
materia: M26
orden: 30
titulo: Checklist egreso con evidencia enlazada
horas: 5
semana: 8
lectura: egreso.md
evidencia: projects/m26-capstone/egreso-checklist.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Hashes commit

      - URLs


      **Objetivo de esta lección:** Checklist de egreso con cada ítem enlazado a
      evidencia en git/URL.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git log --oneline -20 -- projects/m26-capstone projects/m25-ciber
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Congela checklist final
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l30 checklist-egreso-con-evidencia-enlazada"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Checklist egreso con evidencia enlazada», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Checklist egreso con
          evidencia enlazada
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

      `git log --oneline -20 -- projects/m26-capstone projects/m25-ciber`
    comandoEsperado:
      - git log --oneline -20 -- projects/m26-capstone projects/m25-ciber
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git log --oneline -20 -- projects/m26-capstone
      projects/m25-ciber
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
        texto: Checklist de egreso con cada ítem enlazado a evidencia en git/URL.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Enlaza evidencias
    xp: 10
    cuerpo: >-
      Cada “hecho” lleva path git, URL, o commit hash. Nada de “está en mi
      laptop”. Pega hashes relevantes junto a ítems difíciles.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/egreso-checklist.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L30 — Checklist egreso con evidencia enlazada

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/egreso-checklist.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Checklist de egreso con cada ítem enlazado a evidencia en git/URL.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Hashes commit
- URLs

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _egreso.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Congela checklist final (30–40 min)

En `projects/m26-capstone/egreso-checklist.md`: cada ítem de [egreso](../../../egreso.md) con estado final.

### 3. Enlaza evidencias (100–120 min)

Cada “hecho” lleva path git, URL, o commit hash. Nada de “está en mi laptop”.

```bash
git log --oneline -20 -- projects/m26-capstone projects/m25-ciber
```

Pega hashes relevantes junto a ítems difíciles.

### 4. Ítems parciales (25–35 min)

Los parciales explican gap + plan. Bitácora semana-08.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l30 checklist-egreso-con-evidencia-enlazada"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | egreso.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/egreso-checklist.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L31 — README capstone índice maestro](L31-readme-capstone-indice-maestro.md)
