-- L11 — subconsultas: clientes frecuentes e ítems nunca pedidos

-- 1) Clientes con ≥2 pedidos entregados
SELECT cu.id, cu.nombre, cu.telefono
FROM customers cu
WHERE (
  SELECT count(*) FROM orders o
  WHERE o.customer_id = cu.id AND o.estado = 'entregado'
) >= 2
ORDER BY cu.nombre;

-- 2) Ítems de menú que nunca aparecen en order_items
SELECT s.id, s.nombre
FROM menu_items s
WHERE NOT EXISTS (
  SELECT 1 FROM order_items oi WHERE oi.menu_item_id = s.id
)
ORDER BY s.nombre;

-- Salida ejemplo:
-- /* ... */
