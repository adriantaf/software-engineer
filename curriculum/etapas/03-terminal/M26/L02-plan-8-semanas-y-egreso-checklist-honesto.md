---
id: L02
materia: M26
orden: 2
titulo: Plan 8 semanas y egreso-checklist honesto
horas: 5
semana: 1
lectura: egreso.md rúbrica
evidencia: projects/m26-capstone/plan-8-semanas.md
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


      - Sprint semanal

      - Demo interna

      - Riesgos


      **Objetivo de esta lección:** Publicar plan de 8 semanas con hitos
      semanales y checklist de egreso honesto (gaps visibles).


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
      git commit -m "docs(m26): l02 plan-8-semanas-y-egreso-checklist-honest"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Esqueleto de 8 sprints
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l02 plan-8-semanas-y-egreso-checklist-honest"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Plan 8 semanas y egreso-checklist honesto», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Plan 8 semanas y
          egreso-checklist hones…
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
        texto: >-
          Publicar plan de 8 semanas con hitos semanales y checklist de egreso
          honesto (gaps visibles).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Checklist de egreso honesto
    xp: 10
    cuerpo: >-
      Crea/actualiza `projects/m26-capstone/egreso-checklist.md` copiando ítems
      de [egreso](../../../egreso.md). Columnas: ítem | estado
      (hecho/parcial/no) | evidencia (path/URL) | gap. Marca en rojo lo que aún
      es “no” — sin autoengaño.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/plan-8-semanas.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Plan 8 semanas y egreso-checklist honesto

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/plan-8-semanas.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Publicar plan de 8 semanas con hitos semanales y checklist de egreso honesto (gaps visibles).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Sprint semanal
- Demo interna
- Riesgos

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _egreso.md rúbrica_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Esqueleto de 8 sprints (30–40 min)

En `projects/m26-capstone/plan-8-semanas.md` tabla:

| Semana | Entregable | Demo | Riesgo |
|--------|------------|------|--------|

Una fila por semana 1–8. Fechas reales.

### 3. Checklist de egreso honesto (90–110 min)

Crea/actualiza `projects/m26-capstone/egreso-checklist.md` copiando ítems de [egreso](../../../egreso.md).

Columnas: ítem | estado (hecho/parcial/no) | evidencia (path/URL) | gap.

Marca en rojo lo que aún es “no” — sin autoengaño.

### 4. Bitácora semana 1 (20–30 min)

`bitacora/semana-01.md`: horas plan vs real; 1 dependencia bloqueante.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l02 plan-8-semanas-y-egreso-checklist-honest"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | egreso.md rúbrica | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/plan-8-semanas.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L03 — Modelo tenant_id y resolución de tenant](L03-modelo-tenant-id-y-resolucion-de-tenant.md)
