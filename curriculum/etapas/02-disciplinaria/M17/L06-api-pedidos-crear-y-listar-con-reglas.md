---
id: L06
materia: M17
orden: 6
titulo: API pedidos — crear y listar con reglas
horas: 5.0
semana: 2
lectura: REST + validación de líneas/estados
evidencia: POST/GET /orders
---

# L06 — API pedidos — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto Vitrina: crear un pedido con ítems del menú.

## Objetivo

Endpoints crear/listar pedidos con auth, ≥1 línea, precios desde servidor (snapshot), estados válidos.

## Conceptos clave

- REST
- snapshot de precio
- estados: recibido → preparando → listo → entregado

## Pasos (hazlos en orden)

### 1. POST /orders autenticado (70–90 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
  -H 'content-type: application/json' \
  -d '{"customerName":"Ana","customerPhone":"5255...","canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"...","cantidad":2}]}'
# 201
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
  -H 'content-type: application/json' \
  -d '{"items":[]}'
# 400 pedido_sin_lineas
```

El servidor resuelve precio/nombre desde `menu_items` y guarda snapshot en `order_items`.

### 2. GET /orders + reglas (50–60 min)

Listar con filtro estado; 401 sin auth.

```bash
curl -sS -b /tmp/ao.ck "http://localhost:3000/orders?estado=recibido"
curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/orders
# 401
```

### 3. Tests + commit (40 min)

```bash
npm test -- orders
git add projects/m17-vitrina
git commit -m "feat(m17): L06 api orders crear y listar"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | REST + validación | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /orders` y `GET /orders` con auth; 401 sin sesión.
2. Tests 201, 400 sin líneas; total recalculado en servidor.
3. Commit `feat(m17): L06 api orders crear y listar`.

## Errores comunes

- Confiar en el precio que manda el cliente.
- Listar pedidos sin autenticación.

## Siguiente

[L07 — CRUD menú y categorías](L07-crud-menu-y-categorias.md)
