---
id: L06
materia: M26
orden: 6
titulo: Seeds y datos demo por tenant
horas: 5
semana: 2
lectura: Datos prueba multi-tenant
evidencia: projects/m26-capstone/demo-tenants.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Seeds/datos demo para ≥2 tenants distintos, listos para
      demos internas.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - No datos compartidos

      - PII ficticia
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo
      pnpm seed:demo   # o npm run db:seed:demo
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Seeds y datos demo por tenant" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/demo-tenants.md
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

      `pnpm seed:demo   # o npm run db:seed:demo`
    comandoEsperado:
      - 'pnpm seed:demo   # o npm run db:seed:demo'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: pnpm seed:demo   # o npm run db:seed:demo'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Seeds/datos demo para ≥2 tenants distintos, listos para demos
          internas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Diseña seeds A/B
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/demo-tenants.md`: negocio A vs B, 3 clientes, 3
      servicios, 5 pedidos cada uno — PII ficticia.
  - id: s7
    tipo: ejemplo
    titulo: 3. Script seed idempotente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo
      pnpm seed:demo   # o npm run db:seed:demo
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/demo-tenants.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Seeds y datos demo por tenant

**~5 h · Semana 2**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/demo-tenants.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Seeds/datos demo para ≥2 tenants distintos, listos para demos internas.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- No datos compartidos
- PII ficticia

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Datos prueba multi-tenant_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Diseña seeds A/B (25–35 min)

En `projects/m26-capstone/demo-tenants.md`: negocio A vs B, 3 clientes, 3 servicios, 5 pedidos cada uno — PII ficticia.

### 3. Script seed idempotente (100–120 min)

Implementa o documenta comando:

```bash
# ejemplo
pnpm seed:demo   # o npm run db:seed:demo
```

Debe poder re-correrse sin duplicar basura. Verifica que pedidos de A no aparecen en queries de B.

### 4. Evidencia de aislamiento en seed (25–35 min)

Tabla counts por tenant. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l06 seeds-y-datos-demo-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Datos prueba multi-tenant | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/demo-tenants.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L07 — Panel admin por tenant](L07-panel-admin-por-tenant.md)
