# Hilo transversal — Producto (Agenda Ops)

El currículo no son materias sueltas: desde M12 construyes un **SaaS vertical** (citas/ops para negocios de servicio en Ensenada). Spec completa: [producto-saas.md](../producto-saas.md).

## Mapa de artefactos

| Materia | Artefacto que deja | Carpeta sugerida |
|---------|--------------------|------------------|
| [M12](../etapas/02-disciplinaria/M12-requerimientos.md) | SRS + RNF seguridad + MVP freeze | [`projects/m12-srs/`](../../projects/m12-srs/) |
| [M13](../etapas/02-disciplinaria/M13-analisis-y-diseno.md) | Diagramas + ADRs + trust boundaries | [`projects/m13-diseno/`](../../projects/m13-diseno/) |
| [M14](../etapas/02-disciplinaria/M14-patrones.md) | ≥5 patrones justificados en el código | [`projects/m14-patrones/`](../../projects/m14-patrones/) |
| [M15](../etapas/02-disciplinaria/M15-vv-calidad.md) | CI verde + tests de dominio/auth | [`projects/m15-calidad/`](../../projects/m15-calidad/) |
| [M16](../etapas/02-disciplinaria/M16-ihc.md) | Informe usabilidad + iteración UI | [`projects/m16-ihc/`](../../projects/m16-ihc/) |
| [M17](../etapas/02-disciplinaria/M17-aplicaciones-web.md) | **Piloto** web (1 negocio) + ADR `tenant_id` | [`projects/m17-agenda-ops/`](../../projects/m17-agenda-ops/) |
| [M18](../etapas/02-disciplinaria/M18-seguridad.md) | Threat model + hardening + tests | [`projects/m18-appsec/`](../../projects/m18-appsec/) |
| [M19](../etapas/02-disciplinaria/M19-nube-devops.md) | Deploy, secrets, backup/restore | [`projects/m19-ops/`](../../projects/m19-ops/) |
| [M20](../etapas/02-disciplinaria/M20-aplicaciones-moviles.md) | App cliente misma auth | [`projects/m20-movil/`](../../projects/m20-movil/) |
| [M21](../etapas/03-terminal/M21-admin-proyectos.md) | Roadmap + sprints del SaaS | [`projects/m21-proyectos/`](../../projects/m21-proyectos/) |
| [M22](../etapas/03-terminal/M22-emprendimiento.md) | 10 demos/trials + pricing Free/Pro | [`projects/m22-bektor/`](../../projects/m22-bektor/) |
| [M23](../etapas/03-terminal/M23-ia-datos.md) | FAQ/RAG **por tenant** | [`projects/m23-ia/`](../../projects/m23-ia/) |
| [M24](../etapas/03-terminal/M24-tecnologias-emergentes.md) | Spike go/no-go (opcional al core) | [`projects/m24-emergentes/`](../../projects/m24-emergentes/) |
| [M25](../etapas/03-terminal/M25-ciberseguridad-aplicada.md) | Security review cross-tenant | [`projects/m25-ciber/`](../../projects/m25-ciber/) |
| [M26](../etapas/03-terminal/M26-proyecto-integrador.md) | SaaS en prod + Stripe test + egreso | [`projects/m26-capstone/`](../../projects/m26-capstone/) |

## Reglas de oro del hilo

1. Cada materia **deja un artefacto** que la siguiente puede abrir sin adivinar.
2. El piloto (M17) es un negocio; el SaaS (M26) son **≥2 tenants**.
3. Seguridad y `tenant_id` no se “dejan para el final” — ver [hilo seguridad](seguridad.md).
4. Comercial (M22) y técnico (M17–M26) se alimentan: demos reales sobre el producto real.

## Cómo usarlo

1. Antes de M12, lee [producto-saas](../producto-saas.md).
2. En cada materia del mapa, abre la carpeta `projects/mXX-*` y cumple **Evidencia de hecho**.
3. En M26, la rúbrica de [egreso](../egreso.md) exige el hilo completo (no un CRUD suelto).

## Relacionado

- [Producto SaaS (spec)](../producto-saas.md)
- [Hilo seguridad](seguridad.md)
- [Egreso](../egreso.md)
- [Índice de projects/](../../projects/README.md)
