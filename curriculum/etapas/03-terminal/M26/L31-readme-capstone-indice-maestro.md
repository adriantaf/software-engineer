---
id: L31
materia: M26
orden: 31
titulo: README capstone índice maestro
horas: 5
semana: 8
lectura: README proyecto
evidencia: projects/m26-capstone/README.md
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


      - Prod URL

      - Repos


      **Objetivo de esta lección:** README capstone como índice maestro de toda
      la evidencia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l31 readme-capstone-ndice-maestro"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Estructura del README
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l31 readme-capstone-ndice-maestro"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «README capstone índice maestro», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de README capstone índice
          maestro
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/'
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
        texto: README capstone como índice maestro de toda la evidencia.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Índice maestro clickeable
    xp: 10
    cuerpo: >-
      Links relativos a **todos** los artefactos clave (alcance, demos, billing,
      security-review, egreso-checklist). Un evaluador entra solo por este
      archivo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/README.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L31 — README capstone índice maestro

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/README.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

README capstone como índice maestro de toda la evidencia.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Prod URL
- Repos

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _README proyecto_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Estructura del README (25–35 min)

En `projects/m26-capstone/README.md`: Prod URL | Staging | Demo video | Memoria | Seguridad | Comercial | Cómo correr tests.

### 3. Índice maestro clickeable (90–110 min)

Links relativos a **todos** los artefactos clave (alcance, demos, billing, security-review, egreso-checklist).

Un evaluador entra solo por este archivo.

### 4. Smoke del índice (25–35 min)

Abre 5 links al azar; arregla rotos. Bitácora semana-08.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l31 readme-capstone-ndice-maestro"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | README proyecto | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/README.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L32 — Cierre integrador y handoff v1.1](L32-cierre-integrador-y-handoff-v1-1.md)
