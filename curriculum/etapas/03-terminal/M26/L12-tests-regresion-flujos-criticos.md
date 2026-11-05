---
id: L12
materia: M26
orden: 12
titulo: Tests regresión flujos críticos
horas: 5
semana: 3
lectura: CI verde
evidencia: projects/m26-capstone/tests-regresion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Suite de regresión de flujos críticos en CI (o pipeline
      documentado).


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Smoke E2E opcional

      - API tests
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      pnpm test   # o el comando real
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests regresión flujos críticos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/tests-regresion.md
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

      `pnpm test   # o el comando real`
    comandoEsperado:
      - 'pnpm test   # o el comando real'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: pnpm test   # o el comando real'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Suite de regresión de flujos críticos en CI (o pipeline documentado).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Elige suite mínima
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/tests-regresion.md`: lista tests (auth, pedidos
      CRUD, cross-tenant). Comando exacto.
  - id: s7
    tipo: ejemplo
    titulo: 3. Corre en CI o documenta pipeline
    xp: 10
    cuerpo: |-
      ```bash
      pnpm test   # o el comando real
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/tests-regresion.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Tests regresión flujos críticos

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/tests-regresion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Suite de regresión de flujos críticos en CI (o pipeline documentado).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Smoke E2E opcional
- API tests

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _CI verde_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Elige suite mínima (25–35 min)

En `projects/m26-capstone/tests-regresion.md`: lista tests (auth, pedidos CRUD, cross-tenant). Comando exacto.

### 3. Corre en CI o documenta pipeline (100–120 min)

```bash
pnpm test   # o el comando real
```

Pega resumen (passed/failed). Si CI: enlace a workflow verde. Si no: YAML propuesto + issue.

### 4. Política de merge (25–35 min)

Escribe: “no merge a main sin X verde”. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l12 tests-regresi-n-flujos-cr-ticos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | CI verde | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/tests-regresion.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L13 — Notificaciones o WhatsApp si en alcance](L13-notificaciones-o-whatsapp-si-en-alcance.md)
