-- M09 · migración 003 — least privilege (L19)
-- Sustituye la contraseña con APP_DB_PASSWORD de tu .env local antes de aplicar.
-- Nunca commits passwords reales.

BEGIN;

DO $$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'agenda_app') THEN
    CREATE ROLE agenda_app LOGIN PASSWORD 'cambia_esto_app';
  END IF;
END
$$;

GRANT CONNECT ON DATABASE agenda_ops TO agenda_app;
GRANT USAGE ON SCHEMA public TO agenda_app;

GRANT SELECT, INSERT, UPDATE ON TABLE clientes, servicios, citas, cita_auditoria TO agenda_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO agenda_app;

-- Sin DROP, sin CREATE TABLE, sin superuser.
-- Opcional endurecer: REVOKE CREATE ON SCHEMA public FROM PUBLIC;

COMMIT;
