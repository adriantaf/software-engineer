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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Publicar plan de 8 semanas con hitos semanales y checklist
      de egreso honesto (gaps visibles).


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Sprint semanal

      - Demo interna

      - Riesgos
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l02 plan-8-semanas-y-egreso-checklist-honest"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Plan 8 semanas y egreso-checklist honesto" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/plan-8-semanas.md
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Publicar plan de 8 semanas con hitos semanales y checklist de egreso
          honesto (gaps visibles).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Esqueleto de 8 sprints
    xp: 10
    cuerpo: |-
      En `projects/m26-capstone/plan-8-semanas.md` tabla:

      | Semana | Entregable | Demo | Riesgo |
      |--------|------------|------|--------|

      Una fila por semana 1–8. Fechas reales.
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist de egreso honesto
    xp: 10
    cuerpo: >-
      Crea/actualiza `projects/m26-capstone/egreso-checklist.md` copiando ítems
      de [egreso](../../../egreso.md).


      Columnas: ítem | estado (hecho/parcial/no) | evidencia (path/URL) | gap.


      Marca en rojo lo que aún es “no” — sin autoengaño.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/plan-8-semanas.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
