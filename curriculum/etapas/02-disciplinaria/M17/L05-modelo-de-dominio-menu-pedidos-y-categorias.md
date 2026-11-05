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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Alinear tablas y entidades con M09/M13: `menu_categories`,
      `menu_items`, `orders`, `order_items`, `customers`.


      - entidad / migración / dominio

      - snapshot de precio en líneas de pedido
  - id: s2
    tipo: ejemplo
    titulo: 1. Cruza M13 + M09
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Modelo de dominio menú, pedidos y categorías" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: migraciones / entidades menú-pedidos
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

      `ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations`
    comandoEsperado:
      - ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: ls projects/m13-diseno/diagramas
      projects/m09-bases-datos/migrations
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Alinear tablas y entidades con M09/M13: `menu_categories`,
          `menu_items`, `orders`, `order_items`, `customers`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Migraciones dominio
    xp: 10
    cuerpo: >-
      Asegura tablas del esquema Vitrina (ver
      `projects/m09-bases-datos/migrations/001_init.sql`) aplicadas en el
      piloto.


      ```bash

      npm run migrate

      o psql "$DATABASE_URL" -c '\dt'

      ```


      Evidencia: listado de tablas en nota breve en `docs/` (sin datos reales).
  - id: s7
    tipo: ejemplo
    titulo: 3. Reglas en domain/
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
