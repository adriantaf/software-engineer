-- M09 · migración 001 — esquema base Vitrina (single-tenant por ahora)
-- Completa / ajusta en L02–L07. No uses passwords aquí.
-- Pensado para PostgreSQL 16+.

BEGIN;

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Columna tenant_id prepara M17; en M09 puedes fijar un UUID demo.
-- CREATE TABLE IF NOT EXISTS tenants (...);  -- opcional más adelante

CREATE TABLE IF NOT EXISTS menu_categories (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  nombre        text NOT NULL,
  orden         integer NOT NULL DEFAULT 0,
  activo        boolean NOT NULL DEFAULT true,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS menu_items (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  category_id   uuid NOT NULL REFERENCES menu_categories (id),
  nombre        text NOT NULL,
  descripcion   text,
  precio_centavos integer NOT NULL CHECK (precio_centavos >= 0),
  disponible    boolean NOT NULL DEFAULT true,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS customers (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  nombre        text NOT NULL,
  telefono      text, -- WhatsApp
  notas         text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS orders (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  customer_id   uuid REFERENCES customers (id),
  canal         text NOT NULL DEFAULT 'whatsapp'
                CHECK (canal IN ('whatsapp', 'online')),
  pago          text NOT NULL DEFAULT 'al_recoger'
                CHECK (pago IN ('al_recoger', 'online')),
  estado        text NOT NULL DEFAULT 'recibido'
                CHECK (estado IN ('recibido', 'preparando', 'listo', 'entregado', 'cancelado')),
  total_centavos integer NOT NULL DEFAULT 0 CHECK (total_centavos >= 0),
  notas         text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS order_items (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  order_id      uuid NOT NULL REFERENCES orders (id) ON DELETE CASCADE,
  menu_item_id  uuid NOT NULL REFERENCES menu_items (id),
  cantidad      integer NOT NULL CHECK (cantidad > 0),
  precio_unit_centavos integer NOT NULL CHECK (precio_unit_centavos >= 0),
  nombre_snapshot text NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_menu_items_category ON menu_items (category_id);
CREATE INDEX IF NOT EXISTS idx_orders_tenant_created ON orders (tenant_id, created_at);
CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items (order_id);

COMMIT;
