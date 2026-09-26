-- L10 — agregaciones por servicio
-- Pregunta: ¿qué servicios se agendan más y cuánto ingresan (completadas)?

SELECT s.nombre,
       count(*) AS total_citas,
       count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
       coalesce(
         sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'),
         0
       ) AS ingresos_centavos
FROM citas c
JOIN servicios s ON s.id = c.servicio_id
GROUP BY s.id, s.nombre
ORDER BY total_citas DESC;

-- Salida ejemplo:
-- /* ... */
