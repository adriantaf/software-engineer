-- L10 — agregaciones por ítem de menú
-- Pregunta: ¿qué ítems se piden más y cuánto ingresan (entregados)?

SELECT mi.nombre,
       count(*) AS lineas,
       coalesce(sum(oi.cantidad), 0) AS unidades,
       coalesce(
         sum(oi.cantidad * oi.precio_unit_centavos) FILTER (WHERE o.estado = 'entregado'),
         0
       ) AS ingresos_centavos
FROM order_items oi
JOIN menu_items mi ON mi.id = oi.menu_item_id
JOIN orders o ON o.id = oi.order_id
GROUP BY mi.id, mi.nombre
ORDER BY unidades DESC;

-- Salida ejemplo:
-- /* ... */
