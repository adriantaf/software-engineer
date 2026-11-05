---
id: L21
materia: M26
orden: 21
titulo: Re-ejecutar review M25 y cerrar gaps
horas: 5
semana: 6
lectura: security-review.md
evidencia: projects/m26-capstone/seguridad-m25.md
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


      - Cross-tenant CI

      - Headers


      **Objetivo de esta lección:** Re-ejecutar security review M25 y cerrar
      gaps bloqueantes.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      pnpm test -- aislamiento   # adapta
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Relee security-review M25
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l21 re-ejecutar-review-m25-y-cerrar-gaps"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Re-ejecutar review M25 y cerrar gaps», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Re-ejecutar review M25
          y cerrar gaps
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

      `pnpm test -- aislamiento   # adapta`
    comandoEsperado:
      - 'pnpm test -- aislamiento   # adapta'
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: pnpm test -- aislamiento   # adapta'
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
        texto: Re-ejecutar security review M25 y cerrar gaps bloqueantes.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cierra gaps bloqueantes
    xp: 10
    cuerpo: >-
      Lista P0/P1. Cada uno: issue, fix o waiver firmado con riesgo residual.
      Re-corre test cross-tenant:
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/seguridad-m25.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L21 — Re-ejecutar review M25 y cerrar gaps

**~5 h · Semana 6**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/seguridad-m25.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Re-ejecutar security review M25 y cerrar gaps bloqueantes.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Cross-tenant CI
- Headers

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _security-review.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Relee security-review M25 (30–40 min)

En `projects/m26-capstone/seguridad-m25.md` índice de hallazgos abiertos vs cerrados desde `projects/m25-ciber/security-review.md`.

### 3. Cierra gaps bloqueantes (100–120 min)

Lista P0/P1. Cada uno: issue, fix o waiver firmado con riesgo residual.

Re-corre test cross-tenant:

```bash
pnpm test -- aislamiento   # adapta
```

### 4. Handoff a demo pública (25–35 min)

Qué debe estar verde antes del video. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l21 re-ejecutar-review-m25-y-cerrar-gaps"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | security-review.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/seguridad-m25.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L22 — CI con tests cross-tenant obligatorios](L22-ci-con-tests-cross-tenant-obligatorios.md)
