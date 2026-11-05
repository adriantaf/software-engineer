---
id: L09
materia: M26
orden: 9
titulo: Pedidos CRUD multi-tenant
horas: 5
semana: 3
lectura: Paridad M17 sin hardcode piloto
evidencia: projects/m26-capstone/memoria/pedidos-crud.md
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


      - Regresión

      - `tenant_id` en queries

      - Snapshot de precio por línea


      **Objetivo de esta lección:** CRUD de pedidos multi-tenant con tests de
      aislamiento en el camino crítico (menú → pedido → estados).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      # create en A

      curl -s -X POST "$API/orders" -H "Authorization: Bearer $TOKEN_A" \
        -H "Content-Type: application/json" \
        -d '{"canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"…","cantidad":2}]}'

      # A intenta leer pedido de B → 403/404

      curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A"
      "$API/orders/$ORDER_B"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Matriz CRUD pedidos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l09 pedidos-crud-multi-tenant"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pedidos CRUD multi-tenant», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pedidos CRUD
          multi-tenant
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

      `curl -s -X POST "$API/orders" -H "Authorization: Bearer $TOKEN_A" \`
    comandoEsperado:
      - 'curl -s -X POST "$API/orders" -H "Authorization: Bearer $TOKEN_A" \'
      - >-
        curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A"
        "$API/orders/$ORDER_B"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -X POST "$API/orders" -H "Authorization: Bearer
      $TOKEN_A" \
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
          CRUD de pedidos multi-tenant con tests de aislamiento en el camino
          crítico (menú → pedido → estados).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Implementa/verifica flujos + aislamiento
    xp: 10
    cuerpo: >-
      Ejecuta create + cambio de estado en A y B. Ningún hardcode de un solo
      design partner. Pega status codes en la memoria.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Create/list/estado de pedidos funciona en ≥2 tenants.
      - A no lee pedidos de B (evidencia HTTP + test).
      - Memoria `pedidos-crud.md` en git.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Pedidos CRUD multi-tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/pedidos-crud.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

CRUD de pedidos multi-tenant con tests de aislamiento en el camino crítico (menú → pedido → estados).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Regresión
- `tenant_id` en queries
- Snapshot de precio por línea

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Paridad M17 sin hardcode piloto_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Matriz CRUD pedidos (25–35 min)

En `projects/m26-capstone/memoria/pedidos-crud.md` tabla create/read/update estado × status esperado por tenant.

### 3. Implementa/verifica flujos + aislamiento (100–130 min)

Ejecuta create + cambio de estado en A y B. Ningún hardcode de un solo design partner.

```bash
# create en A
curl -s -X POST "$API/orders" -H "Authorization: Bearer $TOKEN_A" \
  -H "Content-Type: application/json" \
  -d '{"canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"…","cantidad":2}]}'

# A intenta leer pedido de B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" "$API/orders/$ORDER_B"
```

Pega status codes en la memoria.

### 4. Test mínimo (30–40 min)

Añade o enlaza test de regresión cross-tenant. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l09 pedidos-crud-multi-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Paridad M17 sin hardcode piloto | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Create/list/estado de pedidos funciona en ≥2 tenants.
2. A no lee pedidos de B (evidencia HTTP + test).
3. Memoria `pedidos-crud.md` en git.

## Errores comunes

- Reusar IDs de menú del tenant A en el tenant B.
- Confiar en el precio enviado por el cliente.

## Siguiente

[L10 — Menú por tenant](L10-menu-por-tenant.md)
