---
id: L05
materia: M17
orden: 5
titulo: Modelo de dominio menú, pedidos y categorías
horas: 5.0
semana: 2
lectura: m13 diagrama clases + srs-v1 + er-vitrina
evidencia: migraciones / entidades menú-pedidos
---

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
