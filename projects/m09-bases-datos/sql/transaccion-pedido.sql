-- L17 — transacción: pedido + líneas (ajusta UUIDs a tus seeds)

BEGIN;

WITH nuevo AS (
  INSERT INTO orders (customer_id, canal, pago, estado, total_centavos)
  VALUES (
    '11111111-1111-4111-8111-111111111111',
    'whatsapp',
    'al_recoger',
    'recibido',
    8500
  )
  RETURNING id
)
INSERT INTO order_items (order_id, menu_item_id, cantidad, precio_unit_centavos, nombre_snapshot)
SELECT id,
       'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',
       2,
       4250,
       'Matcha latte'
FROM nuevo;

COMMIT;

-- Para probar ROLLBACK: envuelve un INSERT con menu_item_id inválido en BEGIN/ROLLBACK.
