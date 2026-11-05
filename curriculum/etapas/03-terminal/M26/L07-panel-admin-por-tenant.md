---
id: L07
materia: M26
orden: 7
titulo: Panel admin por tenant
horas: 5
semana: 2
lectura: Roles dueño/staff
evidencia: projects/m26-capstone/memoria/panel-admin.md
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


      - RBAC

      - UI scoped


      **Objetivo de esta lección:** Panel admin por tenant con rutas/capturas y
      nota de authz.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq
      'length'

      curl -s -H "Authorization: Bearer $TOKEN_B" "$API/admin/clientes" | jq
      'length'

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario de rutas admin
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l07 panel-admin-por-tenant"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Panel admin por tenant», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Panel admin por tenant
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq
      'length'`
    comandoEsperado:
      - >-
        curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq
        'length'
      - >-
        curl -s -H "Authorization: Bearer $TOKEN_B" "$API/admin/clientes" | jq
        'length'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -H "Authorization: Bearer $TOKEN_A"
      "$API/admin/clientes" | jq 'length'
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
        texto: Panel admin por tenant con rutas/capturas y nota de authz.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Prueba UI scoped
    xp: 10
    cuerpo: >-
      Login A: captura o anota IDs visibles. Login B: confirma que no ves
      recursos de A. Para ≥1 ruta API detrás del panel:
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/memoria/panel-admin.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Panel admin por tenant

**~5 h · Semana 2**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/panel-admin.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Panel admin por tenant con rutas/capturas y nota de authz.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- RBAC
- UI scoped

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Roles dueño/staff_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Inventario de rutas admin (25–35 min)

En `projects/m26-capstone/memoria/panel-admin.md` lista rutas del panel (dashboard, pedidos, clientes, staff, billing).

### 3. Prueba UI scoped (100–120 min)

Login A: captura o anota IDs visibles. Login B: confirma que no ves recursos de A.

Para ≥1 ruta API detrás del panel:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq 'length'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/admin/clientes" | jq 'length'
```

### 4. Nota de authz (25–35 min)

Staff vs owner: qué pantallas cambian. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l07 panel-admin-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Roles dueño/staff | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/panel-admin.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L08 — Demo interna semana 2 — dos tenants](L08-demo-interna-semana-2-dos-tenants.md)
