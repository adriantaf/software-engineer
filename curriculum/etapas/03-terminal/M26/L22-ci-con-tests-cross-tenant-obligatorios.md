---
id: L22
materia: M26
orden: 22
titulo: CI con tests cross-tenant obligatorios
horas: 5
semana: 6
lectura: pipeline
evidencia: projects/m26-capstone/ci-cross-tenant.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** CI con tests cross-tenant obligatorios (falla el build si A
      lee B).


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Bloqueo merge
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      gh run list --limit 5   # si usas GitHub Actions
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "CI con tests cross-tenant obligatorios" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/ci-cross-tenant.md
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
        texto: CI con tests cross-tenant obligatorios (falla el build si A lee B).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Localiza el job CI
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/ci-cross-tenant.md`: path del workflow + nombre
      del job que corre tests de aislamiento.
  - id: s7
    tipo: ejemplo
    titulo: 3. Haz el test obligatorio
    xp: 10
    cuerpo: |-
      ```bash
      gh run list --limit 5   # si usas GitHub Actions
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/ci-cross-tenant.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L22 — CI con tests cross-tenant obligatorios

**~5 h · Semana 6**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/ci-cross-tenant.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

CI con tests cross-tenant obligatorios (falla el build si A lee B).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Bloqueo merge

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _pipeline_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Localiza el job CI (25–35 min)

En `projects/m26-capstone/ci-cross-tenant.md`: path del workflow + nombre del job que corre tests de aislamiento.

### 3. Haz el test obligatorio (100–120 min)

PR de prueba: rompe a propósito el assert o salta el test — el CI debe fallar. Luego restaura.

Documenta: required check en branch protection (o issue si no tienes permisos).

```bash
gh run list --limit 5   # si usas GitHub Actions
```

### 4. Política escrita (20–30 min)

“Merge bloqueado si cross-tenant rojo”. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l22 ci-con-tests-cross-tenant-obligatorios"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | pipeline | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/ci-cross-tenant.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L23 — Backups prod y runbook ops](L23-backups-prod-y-runbook-ops.md)
