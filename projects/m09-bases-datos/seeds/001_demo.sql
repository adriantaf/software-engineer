-- Seeds demo (L20). Datos ficticios — no uses teléfonos reales de clientes.
-- Ejecuta después de migrations/001_init.sql (y 002 si ya la tienes).

BEGIN;

INSERT INTO clientes (id, nombre, telefono, email) VALUES
  ('11111111-1111-4111-8111-111111111111', 'Ana Ruiz', '+526461110001', 'ana@example.com'),
  ('22222222-2222-4222-8222-222222222222', 'Luis Mora', '+526461110002', 'luis@example.com'),
  ('33333333-3333-4333-8333-333333333333', 'Diana Sol', '+526461110003', NULL)
ON CONFLICT (id) DO NOTHING;

INSERT INTO servicios (id, nombre, duracion_min, precio_centavos) VALUES
  ('aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa', 'Corte clásico', 30, 15000),
  ('bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb', 'Corte + barba', 45, 22000),
  ('cccccccc-cccc-4ccc-8ccc-cccccccccccc', 'Tinte', 90, 45000)
ON CONFLICT (id) DO NOTHING;

INSERT INTO citas (cliente_id, servicio_id, inicia_en, termina_en, estado) VALUES
  ('11111111-1111-4111-8111-111111111111', 'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',
   now() + interval '1 day', now() + interval '1 day 30 minutes', 'programada'),
  ('11111111-1111-4111-8111-111111111111', 'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb',
   now() - interval '3 days', now() - interval '3 days' + interval '45 minutes', 'completada'),
  ('22222222-2222-4222-8222-222222222222', 'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',
   now() - interval '1 day', now() - interval '1 day' + interval '30 minutes', 'no_show'),
  ('22222222-2222-4222-8222-222222222222', 'cccccccc-cccc-4ccc-8ccc-cccccccccccc',
   now() + interval '2 days', now() + interval '2 days 90 minutes', 'confirmada')
;

COMMIT;
