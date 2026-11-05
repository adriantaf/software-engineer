---
id: L27
materia: M26
orden: 27
titulo: Registro comercial M22 y trials
horas: 5
semana: 7
lectura: m22-bektor
evidencia: projects/m26-capstone/comercial.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Registro comercial M22 (demos/trials) enlazado al capstone.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Pipeline trials

      - Demos
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l27 registro-comercial-m22-y-trials"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Registro comercial M22 y trials" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/comercial.md
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
        texto: Registro comercial M22 (demos/trials) enlazado al capstone.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario comercial
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/comercial.md` enlaza `projects/m22-bektor/`
      (demos, trials, pricing).
  - id: s7
    tipo: explicacion
    titulo: 3. Estado honesto del pipeline
    xp: 10
    cuerpo: |-
      Tabla: lead/demo/trial | fecha | resultado | siguiente paso.

      Números reales aunque sean cero — declara cero.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/comercial.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L27 — Registro comercial M22 y trials

**~5 h · Semana 7**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/comercial.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Registro comercial M22 (demos/trials) enlazado al capstone.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Pipeline trials
- Demos

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _m22-bektor_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Inventario comercial (25–35 min)

En `projects/m26-capstone/comercial.md` enlaza `projects/m22-bektor/` (demos, trials, pricing).

### 3. Estado honesto del pipeline (90–110 min)

Tabla: lead/demo/trial | fecha | resultado | siguiente paso.

Números reales aunque sean cero — declara cero.

### 4. Puente a producto (25–35 min)

Qué métrica del SaaS alimenta el discurso comercial. Bitácora semana-07.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l27 registro-comercial-m22-y-trials"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | m22-bektor | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/comercial.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L28 — Métricas y post-mortem técnico v1](L28-metricas-y-post-mortem-tecnico-v1.md)
