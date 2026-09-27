-- L17 — transacción: cita + auditoría (ajusta UUIDs a tus seeds)

BEGIN;

WITH nueva AS (
  INSERT INTO citas (cliente_id, servicio_id, inicia_en, termina_en, estado)
  VALUES (
    '11111111-1111-4111-8111-111111111111',
    'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',
    now() + interval '5 days',
    now() + interval '5 days 30 minutes',
    'programada'
  )
  RETURNING id
)
INSERT INTO cita_auditoria (cita_id, accion, detalle)
SELECT id, 'crear', jsonb_build_object('via', 'm09-l17')
FROM nueva;

COMMIT;

-- Para probar ROLLBACK: envuelve un INSERT con cliente_id inválido en BEGIN/ROLLBACK.
