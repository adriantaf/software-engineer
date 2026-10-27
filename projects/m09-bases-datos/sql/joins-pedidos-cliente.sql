-- L09 — INNER JOIN y LEFT JOIN (Vitrina)
-- Completa y ejecuta contra tu BD local.

-- 1) Pedidos con nombre de cliente e ítems (solo los que tienen cliente)
SELECT
  o.id AS order_id,
  cu.nombre AS cliente,
  o.estado,
  o.canal,
  o.total_centavos,
  o.created_at
FROM orders o
INNER JOIN customers cu ON cu.id = o.customer_id
ORDER BY o.created_at DESC
LIMIT 20;

-- 2) Ítems de menú sin ninguna línea de pedido (LEFT JOIN + IS NULL)
SELECT mi.id, mi.nombre, mi.precio_centavos
FROM menu_items mi
LEFT JOIN order_items oi ON oi.menu_item_id = mi.id
WHERE oi.id IS NULL
ORDER BY mi.nombre;

-- Salida ejemplo (pega la tuya tras ejecutar):
-- /* ... */
