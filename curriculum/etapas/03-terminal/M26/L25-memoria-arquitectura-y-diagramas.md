---
id: L25
materia: M26
orden: 25
titulo: Memoria — arquitectura y diagramas
horas: 5
semana: 7
lectura: plantilla memoria
evidencia: projects/m26-capstone/memoria/arquitectura.md
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


      - C4 ligero

      - Deploy


      **Objetivo de esta lección:** Memoria: arquitectura y diagramas
      (C4/ligero) del SaaS real.


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
      git commit -m "docs(m26): l25 memoria-arquitectura-y-diagramas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Bosqueja C4 ligero
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l25 memoria-arquitectura-y-diagramas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Memoria — arquitectura y diagramas», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Memoria — arquitectura
          y diagramas
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
        texto: 'Memoria: arquitectura y diagramas (C4/ligero) del SaaS real.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Diagrama deploy real
    xp: 10
    cuerpo: >-
      Mermaid o imagen en repo: regiones, servicios, secretos (nombres). URLs
      prod/staging. Sección **Decisiones**: 5 ADRs cortas (tenancy, auth,
      billing, logs, mobile).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/memoria/arquitectura.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L25 — Memoria — arquitectura y diagramas

**~5 h · Semana 7**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/arquitectura.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Memoria: arquitectura y diagramas (C4/ligero) del SaaS real.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- C4 ligero
- Deploy

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _plantilla memoria_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Bosqueja C4 ligero (30–40 min)

En `projects/m26-capstone/memoria/arquitectura.md`: contexto (actores) + contenedores (web, API, DB, Stripe, CI).

### 3. Diagrama deploy real (90–110 min)

Mermaid o imagen en repo: regiones, servicios, secretos (nombres). URLs prod/staging.

Sección **Decisiones**: 5 ADRs cortas (tenancy, auth, billing, logs, mobile).

### 4. Revisión de frescura (25–35 min)

Fecha del diagrama = esta semana. Bitácora semana-07.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l25 memoria-arquitectura-y-diagramas"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | plantilla memoria | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/arquitectura.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L26 — Memoria — tenancy, billing, seguridad](L26-memoria-tenancy-billing-seguridad.md)
