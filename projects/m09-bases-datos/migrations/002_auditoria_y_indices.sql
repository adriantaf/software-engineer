-- M09 · migración 002 — auditoría + índice de reporte (L15–L18)
-- Aplica solo después de 001_init.sql.

BEGIN;

CREATE TABLE IF NOT EXISTS cita_auditoria (
  id            bigserial PRIMARY KEY,
  cita_id       uuid NOT NULL REFERENCES citas (id),
  accion        text NOT NULL,
  detalle       jsonb NOT NULL DEFAULT '{}',
  creado_en     timestamptz NOT NULL DEFAULT now()
);

-- Ejemplo de índice compuesto para reporte “citas por día y estado”
CREATE INDEX IF NOT EXISTS idx_citas_tenant_estado_inicia
  ON citas (tenant_id, estado, inicia_en);

COMMIT;
