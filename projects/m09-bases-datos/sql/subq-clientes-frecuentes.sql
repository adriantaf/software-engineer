-- L11 — HAVING + subconsulta / NOT EXISTS
-- Pregunta: ¿quiénes son clientes frecuentes (≥2 completadas)?

SELECT cl.nombre, count(*) AS completadas
FROM citas c
JOIN clientes cl ON cl.id = c.cliente_id
WHERE c.estado = 'completada'
GROUP BY cl.id, cl.nombre
HAVING count(*) >= 2
ORDER BY completadas DESC;

-- Servicios nunca agendados
SELECT s.id, s.nombre
FROM servicios s
WHERE NOT EXISTS (
  SELECT 1 FROM citas c WHERE c.servicio_id = s.id
)
ORDER BY s.nombre;

-- Salida ejemplo:
-- /* ... */
