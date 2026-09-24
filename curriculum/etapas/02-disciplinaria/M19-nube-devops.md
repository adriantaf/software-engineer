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
    titulo: Deploy reproducible con secretos en el hosting (staging/prod)
  - id: p3
    titulo: Backup automático de BD + restore probado
proyecto:
  id: proj
  titulo: Runbook de producción del SaaS Agenda Ops
---

# M19 — Nube y DevOps

## Por qué existe
Un SaaS sin operación segura no es producto. Secrets, TLS, ambientes staging/prod, dominio, backups ([hilo](../../hilos/seguridad.md); [producto-saas](../../producto-saas.md)).

## Día 1 (2–3 h)
1. Lista secretos actuales y dónde viven (incl. futuros de Stripe).
2. Separa config **staging** vs **prod** (aunque staging sea un segundo deploy).
3. Healthcheck `/health`.
4. Anota el dominio que usarás para el SaaS.

## Temario
Docker → deploy → secrets/HTTPS/dominio → backups/monitoreo → runbook SaaS.

## Recursos
Docs Docker (ES), docs del PaaS/VPS, [producto-saas.md](../../producto-saas.md).

## Proyecto útil
URL estable del piloto/SaaS + backups + healthcheck + runbook `projects/m19-ops/`.

## Errores comunes
Secretos en imagen; no probar restore; un solo ambiente “prod” para experimentar; SSH abierto al mundo.

## Criterios de dominio
- [ ] Restore de BD probado una vez.
- [ ] Deploy reproducible documentado (staging y prod diferenciados).
