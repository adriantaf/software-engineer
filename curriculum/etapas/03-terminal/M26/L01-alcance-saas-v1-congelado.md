---
id: L01
materia: M26
orden: 1
titulo: Alcance SaaS v1 congelado
horas: 5
semana: 1
lectura: producto-saas.md completo + egreso.md
evidencia: projects/m26-capstone/alcance.md
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


      - MVP vs v1.1

      - In/out scope

      - Congelar


      **Objetivo de esta lección:** Congelar por escrito el alcance SaaS v1 de
      Vitrina (in/out) alineado a producto-saas y rúbrica de egreso.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m26-capstone/{memoria,demos,bitacora}
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Crea estructura capstone
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m26-capstone/{memoria,demos,bitacora}

      ```


      Copia mentalmente [producto-saas](../../../producto-saas.md) y
      [egreso](../../../egreso.md) al lado.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Alcance SaaS v1 congelado», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Alcance SaaS v1
          congelado
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

      `mkdir -p projects/m26-capstone/{memoria,demos,bitacora}`
    comandoEsperado:
      - 'mkdir -p projects/m26-capstone/{memoria,demos,bitacora}'
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m26-capstone/{memoria,demos,bitacora}'
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
          Congelar por escrito el alcance SaaS v1 de Vitrina (in/out) alineado a
          producto-saas y rúbrica de egreso.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Congela alcance.md
    xp: 10
    cuerpo: >-
      `alcance.md` con secciones: **In scope v1**, **Out of scope**,
      **Dependencias** (M17/M19/M22/M25), **Criterios de egreso que toca**. ≥8
      bullets in, ≥5 out. Nada de “tal vez WhatsApp” sin decidir.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/alcance.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Alcance SaaS v1 congelado

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/alcance.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Congelar por escrito el alcance SaaS v1 de Vitrina (in/out) alineado a producto-saas y rúbrica de egreso.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- MVP vs v1.1
- In/out scope
- Congelar

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _producto-saas.md completo + egreso.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Crea estructura capstone (20–30 min)

```bash
mkdir -p projects/m26-capstone/{memoria,demos,bitacora}
```

Copia mentalmente [producto-saas](../../../producto-saas.md) y [egreso](../../../egreso.md) al lado.

### 3. Congela alcance.md (100–130 min)

`alcance.md` con secciones: **In scope v1**, **Out of scope**, **Dependencias** (M17/M19/M22/M25), **Criterios de egreso que toca**.

≥8 bullets in, ≥5 out. Nada de “tal vez WhatsApp” sin decidir.

### 4. Bitácora semana 1 (20–30 min)

`bitacora/semana-01.md`: horas plan vs real; 1 riesgo que ya ves.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l01 alcance-saas-v1-congelado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | producto-saas.md completo + egreso.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/alcance.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L02 — Plan 8 semanas y egreso-checklist honesto](L02-plan-8-semanas-y-egreso-checklist-honesto.md)
