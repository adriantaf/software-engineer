---
id: L07
materia: M17
orden: 7
titulo: CRUD menú y categorías
horas: 5.0
semana: 2
lectura: SRS RF menú
evidencia: /menu/categories /menu/items
---

# L07 — CRUD menú y categorías

**~5.0 h · Semana 2**

El menú es el producto principal de Vitrina. Sin categorías e ítems no hay perfil público útil.

## Objetivo

CRUD completo de categorías e ítems de menú con autorización owner/staff.

## Conceptos clave

- CRUD
- disponibilidad
- precio_centavos

## Pasos (hazlos en orden)

### 1. CRUD categorías (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \
  -H 'content-type: application/json' \
  -d '{"nombre":"Bebidas","orden":1}'
curl -sS -b /tmp/ao.ck http://localhost:3000/menu/categories
```

### 2. CRUD ítems (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/items \
  -H 'content-type: application/json' \
  -d '{"categoryId":"...","nombre":"Matcha latte","precioCentavos":6500,"disponible":true}'
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/menu/items/ID \
  -H 'content-type: application/json' \
  -d '{"disponible":false}'
```

### 3. Commit (20 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L07 crud menu categorias items"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas | MVP menú | [producto-saas](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. CRUD categorías e ítems con auth; ítem puede marcarse no disponible.
2. Precios en centavos (enteros).
3. Commit `feat(m17): L07 crud menu categorias items`.

## Errores comunes

- Precio en float.
- Borrar categoría con ítems sin regla clara (restringe o cascada documentada).

## Siguiente

[L08 — Seeds demo y datos design partner](L08-seeds-demo-y-datos-design-partner.md)
