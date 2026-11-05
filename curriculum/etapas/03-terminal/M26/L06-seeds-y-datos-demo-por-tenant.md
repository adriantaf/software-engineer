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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - No datos compartidos

      - PII ficticia


      **Objetivo de esta lección:** Seeds/datos demo para ≥2 tenants distintos,
      listos para demos internas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo
      pnpm seed:demo   # o npm run db:seed:demo
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Diseña seeds A/B
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l06 seeds-y-datos-demo-por-tenant"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Seeds y datos demo por tenant», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Seeds y datos demo por
          tenant
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

      `pnpm seed:demo   # o npm run db:seed:demo`
    comandoEsperado:
      - 'pnpm seed:demo   # o npm run db:seed:demo'
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: pnpm seed:demo   # o npm run db:seed:demo'
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
          Seeds/datos demo para ≥2 tenants distintos, listos para demos
          internas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Script seed idempotente
    xp: 10
    cuerpo: >-
      Implementa o documenta comando: Debe poder re-correrse sin duplicar
      basura. Verifica que pedidos de A no aparecen en queries de B.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/demo-tenants.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
