---
id: L08
materia: M26
orden: 8
titulo: Demo interna semana 2 — dos tenants
horas: 5
semana: 2
lectura: Checklist demo
evidencia: projects/m26-capstone/demos/semana-02.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Demo interna semana 2: dos tenants, guion y resultado en
      `demos/semana-02.md`.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Grabación corta

      - Narrativa
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l08 demo-interna-semana-2-dos-tenants"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Demo interna semana 2 — dos tenants" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/demos/semana-02.md
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
          Demo interna semana 2: dos tenants, guion y resultado en
          `demos/semana-02.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Guion demo semana 2
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/demos/semana-02.md`: guion ≤6 min — login A,
      dato, login B, contraste.
  - id: s7
    tipo: explicacion
    titulo: 3. Ejecuta y registra
    xp: 10
    cuerpo: >-
      Graba Loom/OBS o escribe narrativa paso a paso con timestamps. URLs
      staging reales.


      Resultado: PASS/FAIL aislamiento + 3 bugs vistos.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/demos/semana-02.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Demo interna semana 2 — dos tenants

**~5 h · Semana 2**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/demos/semana-02.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Demo interna semana 2: dos tenants, guion y resultado en `demos/semana-02.md`.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Grabación corta
- Narrativa

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Checklist demo_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Guion demo semana 2 (25–35 min)

En `projects/m26-capstone/demos/semana-02.md`: guion ≤6 min — login A, dato, login B, contraste.

### 3. Ejecuta y registra (100–120 min)

Graba Loom/OBS o escribe narrativa paso a paso con timestamps. URLs staging reales.

Resultado: PASS/FAIL aislamiento + 3 bugs vistos.

### 4. Acciones post-demo (20–30 min)

Issues creados. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l08 demo-interna-semana-2-dos-tenants"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Checklist demo | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/demos/semana-02.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L09 — Pedidos CRUD multi-tenant](L09-pedidos-crud-multi-tenant.md)
