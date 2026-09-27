-- L09 — INNER JOIN y LEFT JOIN (Agenda Ops)
-- Completa y ejecuta contra tu BD local.

-- 1) Citas con nombre de cliente y servicio (solo las que tienen ambos)
SELECT
  c.id AS cita_id,
  cl.nombre AS cliente,
  s.nombre AS servicio,
  c.inicia_en,
  c.estado
FROM citas c
INNER JOIN clientes cl ON cl.id = c.cliente_id
INNER JOIN servicios s ON s.id = c.servicio_id
ORDER BY c.inicia_en
LIMIT 20;

-- 2) Clientes sin ninguna cita (LEFT JOIN + IS NULL)
SELECT cl.id, cl.nombre, cl.telefono
FROM clientes cl
LEFT JOIN citas c ON c.cliente_id = cl.id
WHERE c.id IS NULL
ORDER BY cl.nombre;

-- Salida ejemplo (pega la tuya tras ejecutar):
-- /* ... */
