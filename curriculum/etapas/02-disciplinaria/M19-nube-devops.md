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

**En cristiano:** el piloto sobrevive fuera de tu laptop: Docker, secretos, HTTPS, backup con restore probado.

## Día 1 (2–3 h)
1. Lista secretos actuales y dónde viven (incl. futuros de Stripe).
2. Separa config **staging** vs **prod** (aunque staging sea un segundo deploy).
3. Healthcheck `/health`.
4. Anota el dominio que usarás para el SaaS.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Docker | 6–8 | Multi-stage |
| Deploy | 6–8 | Staging/prod + secrets |
| Backup | 4–6 | Restore real una vez |
| Retro | 1 | Runbook actualizado |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Temario
Docker → deploy → secrets/HTTPS/dominio → backups/monitoreo → runbook SaaS.

## Lecturas

Canon: documentación Docker + docs del PaaS. Ver [bibliografía](../../bibliografia.md) y [producto-saas](../../producto-saas.md).

| Semana | Lectura | Alternativa |
|--------|---------|-------------|
| 1 | Docker **Get started** + Dockerfile best practices (oficial) | — |
| 2 | Docs deploy del PaaS/VPS elegido (HTTPS, dominio) | — |
| 3 | Secrets del proveedor + variables de entorno (nunca en imagen) | Runbook borrador |
| 4 | Backups/restore + healthchecks + [producto-saas](../../producto-saas.md) ops | Prueba de restore real |

**Regla:** un restore de BD probado vale más que tres tutoriales.

## Proyecto útil
URL estable del piloto/SaaS + backups + healthcheck + runbook `projects/m19-ops/`.

## Errores comunes
Secretos en imagen; no probar restore; un solo ambiente “prod” para experimentar; SSH abierto al mundo.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Imágenes:** Dockerfile multi-stage + Compose.
- **P2 — Deploy:** URL estable; secretos fuera de la imagen.
- **P3 — Restore:** Prueba de restore documentada.
- **Proyecto — Runbook:** `projects/m19-ops/` del SaaS.

## Criterios de dominio
- [ ] Restore de BD probado una vez.
- [ ] Deploy reproducible documentado (staging y prod diferenciados).
