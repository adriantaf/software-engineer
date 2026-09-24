# Hilo transversal — Seguridad

La seguridad no es “la materia M18”. Es un hábito en **toda** la academia. Labs ofensivos: **solo tus sistemas**.

## Por etapa

### Básica
| Materia | Práctica mínima de seguridad |
|---------|------------------------------|
| M01 | No subir secretos; `.gitignore` de `.env` |
| M02 | Validar inputs; no loguear contraseñas |
| M03–M05 | — (fundamento; conciencia de límites/representación) |
| M06 | Errores sin filtrar stack traces sensibles al usuario |

### Disciplinaria
| Materia | Práctica mínima |
|---------|-----------------|
| M07–M08 | No “optimizar” validaciones fuera |
| M09 | Least privilege DB; queries parametrizadas desde el día 1 |
| M10 | TLS, superficie de ataque, cookies seguras (concepto) |
| M11 | Permisos Linux, secretos en env, no root innecesario |
| M12 | Requisitos no funcionales de seguridad en el SRS |
| M13–M14 | Trust boundaries en el diseño |
| M15 | Tests de regresión de auth/autorización |
| M16 | No filtrar datos ajenos en UI “por error de UX” |
| M17 | Auth real desde MVP; roles; HTTPS; preparar `tenant_id` ([SaaS](../producto-saas.md)) |
| M18 | AppSec profundo (threat model + OWASP + CI) |
| M19 | Secrets en hosting, backups, staging/prod SaaS |
| M20 | Storage seguro de tokens; certificate pinning intro (opcional) |

### Terminal
| Materia | Práctica mínima |
|---------|-----------------|
| M21 | Riesgos de seguridad en el backlog |
| M22 | No prometer “banco-grade” sin evidencia; vender suscripción con honestidad |
| M23 | IA **por tenant**; no mezclar corpus/PII entre negocios |
| M24 | Evaluar riesgo de deps/experimentos |
| M25 | Security review + **IDOR cross-tenant** + tabletop + hardening |
| M26 | Egreso SaaS con evidencia de aislamiento vigente |

## Reglas de oro

1. **Parametriza** consultas. Nunca concatenes SQL con input de usuario.
2. **Autoriza** en servidor (anti-IDOR) — en SaaS: siempre filtra por **`tenant_id`**.
3. **Hashea** contraseñas con libs maduras.
4. **Secrets** fuera del repo (incl. Stripe).
5. Si no puedes atacar tu app de forma ética controlada, aún no la entiendes.
6. **Aislamiento multi-tenant** es requisito de egreso, no un “nice to have”.

## Siguiente lectura

- [Producto SaaS](../producto-saas.md)
- [M10 Redes](../etapas/02-disciplinaria/M10-redes.md)
- [M18 AppSec](../etapas/02-disciplinaria/M18-seguridad.md)
- [M25 Ciberseguridad aplicada](../etapas/03-terminal/M25-ciberseguridad-aplicada.md)
