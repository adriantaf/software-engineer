---
id: M19
titulo: Cómputo en la nube y DevOps
etapa: disciplinaria
orden: 19
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Docker multi-stage + Compose prod-like
  - id: p2
    titulo: Deploy reproducible con secretos en el hosting
  - id: p3
    titulo: Backup automático de BD + restore probado
proyecto:
  id: proj
  titulo: Runbook de producción del CRM
---

# M19 — Nube y DevOps

## Por qué existe
Código sin operación segura no es producto. Secrets, TLS, backups ([hilo](../../hilos/seguridad.md); cierra con M25).

## Día 1 (2–3 h)
1. Lista secretos actuales y dónde viven.
2. Mueve uno que estaba en archivo local al secret store del hosting (o `.env` no commiteado + docs).
3. Healthcheck endpoint `/health`.

## Temario
Docker → deploy → secrets/HTTPS → backups/monitoreo → runbook.

## Recursos
Docs Docker (ES), docs del PaaS/VPS.

## Proyecto útil
URL estable + backups + healthcheck + runbook `projects/m19-ops/`.

## Errores comunes
Secretos en imagen; no probar restore; SSH abierto al mundo sin clave.

## Criterios de dominio
- [ ] Restore de BD probado una vez.
- [ ] Deploy reproducible documentado.
