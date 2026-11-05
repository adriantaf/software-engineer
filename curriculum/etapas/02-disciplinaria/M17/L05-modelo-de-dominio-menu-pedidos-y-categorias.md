---
id: L05
materia: M17
orden: 5
titulo: 'Modelo de dominio menú, pedidos y categorías'
horas: 5
semana: 2
lectura: m13 diagrama clases + srs-v1 + er-vitrina
evidencia: migraciones / entidades menú-pedidos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - entidad / migración / dominio

      - snapshot de precio en líneas de pedido


      **Objetivo de esta lección:** Alinear tablas y entidades con M09/M13:
      `menu_categories`, `menu_items`, `orders`, `order_items`, `customers`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Cruza M13 + M09
    xp: 10
    cuerpo: >-
      ```bash

      ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations

      rg -n "menu_|order|customer" projects/m09-bases-datos/migrations
      projects/m13-diseno 2>/dev/null | head

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Migraciones dominio
    xp: 10
    cuerpo: >-
      ```bash

      npm run migrate

      # o psql "$DATABASE_URL" -c '\dt'

      ```


      Asegura tablas del esquema Vitrina (ver
      `projects/m09-bases-datos/migrations/001_init.sql`) aplicadas en el
      piloto. Evidencia: listado de tablas en nota breve en `docs/` (sin datos
      reales).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Modelo de dominio menú, pedidos y categorías», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Modelo de dominio menú,
          pedidos y categ…
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

      `ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations`
    comandoEsperado:
      - ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations
      - npm run migrate
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls projects/m13-diseno/diagramas
      projects/m09-bases-datos/migrations
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
          Alinear tablas y entidades con M09/M13: `menu_categories`,
          `menu_items`, `orders`, `order_items`, `customers`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Reglas en domain/
    xp: 10
    cuerpo: >-
      ```ts

      // src/domain/order-rules.ts — puro, sin ORM

      export function assertLineas(n: number) {
        if (n < 1) throw new Error("pedido_sin_lineas");
      }

      export function totalCentavos(lineas: { cantidad: number; precioUnit:
      number }[]) {
        return lineas.reduce((s, l) => s + l.cantidad * l.precioUnit, 0);
      }

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Migraciones aplicadas: `menu_categories`, `menu_items`, `orders`,
        `order_items` visibles.
      - Reglas puras en `projects/m17-vitrina/src/domain/` (o equivalente).
      - 'Commit `feat(m17): L05 modelo dominio menu pedidos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Modelo de dominio menú, pedidos y categorías

**~5.0 h · Semana 2**

CRUD sin modelo coherente genera IDOR y datos huérfanos. En Vitrina el núcleo es el **menú**; el pedido referencia ítems con snapshot de precio.

## Objetivo

Alinear tablas y entidades con M09/M13: `menu_categories`, `menu_items`, `orders`, `order_items`, `customers`.

## Conceptos clave

- entidad / migración / dominio
- snapshot de precio en líneas de pedido

## Pasos (hazlos en orden)

### 1. Cruza M13 + M09 (25–35 min)

```bash
ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations
rg -n "menu_|order|customer" projects/m09-bases-datos/migrations projects/m13-diseno 2>/dev/null | head
```

### 2. Migraciones dominio (70–90 min)

Asegura tablas del esquema Vitrina (ver `projects/m09-bases-datos/migrations/001_init.sql`) aplicadas en el piloto.

```bash
npm run migrate
# o psql "$DATABASE_URL" -c '\dt'
```

Evidencia: listado de tablas en nota breve en `docs/` (sin datos reales).

### 3. Reglas en domain/ (50–60 min)

```ts
// src/domain/order-rules.ts — puro, sin ORM
export function assertLineas(n: number) {
  if (n < 1) throw new Error("pedido_sin_lineas");
}
export function totalCentavos(lineas: { cantidad: number; precioUnit: number }[]) {
  return lineas.reduce((s, l) => s + l.cantidad * l.precioUnit, 0);
}
```

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L05 modelo dominio menu pedidos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN + M09 ER | er-vitrina + diagrama clases M13 | [producto-saas](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Migraciones aplicadas: `menu_categories`, `menu_items`, `orders`, `order_items` visibles.
2. Reglas puras en `projects/m17-vitrina/src/domain/` (o equivalente).
3. Commit `feat(m17): L05 modelo dominio menu pedidos`.

## Errores comunes

- Modelar horarios de cita en lugar de menú + pedido.
- Totales solo en el front sin recalcular en servidor.

## Siguiente

[L06 — API pedidos — crear y listar con reglas](L06-api-pedidos-crear-y-listar-con-reglas.md)
