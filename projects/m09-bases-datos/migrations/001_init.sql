-- M09 · migración 001 — esquema base Agenda Ops (single-tenant por ahora)
-- Completa / ajusta en L02–L07. No uses passwords aquí.
-- Pensado para PostgreSQL 16+.

BEGIN;

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Columna tenant_id prepara M17; en M09 puedes fijar un UUID demo.
-- CREATE TABLE IF NOT EXISTS tenants (...);  -- opcional más adelante

CREATE TABLE IF NOT EXISTS clientes (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  nombre        text NOT NULL,
  telefono      text,
  email         text,
  notas         text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS servicios (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  nombre        text NOT NULL,
  duracion_min  integer NOT NULL CHECK (duracion_min > 0),
  precio_centavos integer NOT NULL CHECK (precio_centavos >= 0),
  activo        boolean NOT NULL DEFAULT true,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS citas (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     uuid NOT NULL DEFAULT '00000000-0000-4000-8000-000000000001',
  cliente_id    uuid NOT NULL REFERENCES clientes (id),
  servicio_id   uuid NOT NULL REFERENCES servicios (id),
  inicia_en     timestamptz NOT NULL,
  termina_en    timestamptz NOT NULL,
  estado        text NOT NULL DEFAULT 'programada'
                CHECK (estado IN ('programada', 'confirmada', 'completada', 'cancelada', 'no_show')),
  notas         text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now(),
  CHECK (termina_en > inicia_en)
);

CREATE INDEX IF NOT EXISTS idx_citas_cliente ON citas (cliente_id);
CREATE INDEX IF NOT EXISTS idx_citas_inicia_en ON citas (inicia_en);
CREATE INDEX IF NOT EXISTS idx_citas_tenant_inicia ON citas (tenant_id, inicia_en);

COMMIT;
