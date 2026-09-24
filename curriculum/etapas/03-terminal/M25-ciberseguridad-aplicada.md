---
id: M25
titulo: Ciberseguridad aplicada
etapa: terminal
orden: 25
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Inventario de activos y superficie (prod/staging)
  - id: p2
    titulo: Security review manual + issues priorizados
  - id: p3
    titulo: Tabletop de incidente (.env filtrado) documentado
proyecto:
  id: proj
  titulo: Reporte tipo security review + hardening de producción
---

# M25 — Ciberseguridad aplicada

## Por qué existe

**Capa C** de la pista de seguridad. M18 te enseñó AppSec en desarrollo; aquí operas como ingeniero responsable del **producto en el mundo real**: superficie, review, hardening de deploy, respuesta básica e incidentes.

## Análogos
UABC: Seguridad / gestión. Tec: Ciberseguridad (cierre aplicado).

## Objetivos

1. Inventariar activos y superficie de un sistema desplegado.
2. Hacer un security review estructurado (no “sentir que está bien”).
3. Hardening de producción enlazado a M19 (HTTPS, backups, least privilege).
4. Ejecutar un tabletop de incidente y documentar runbook.
5. Intro a privacidad/datos personales a nivel ingeniería (contexto MX).

## Cómo estudiar esta materia

- Trabaja **sobre tu producto** (CRM/Agenda), no sobre demos ajenos.
- Prioriza hallazgos por impacto × probabilidad (no por “se ve cool”).
- Toda prueba ofensiva: solo tus ambientes.

## Día 1 (2–3 h)

1. Lista URLs, paneles admin, webhooks, DB, storage, CI secrets.
2. Exporta (redactado) `projects/m25-ciber/inventario.md`.
3. Corre healthchecks y anota versiones de dependencias críticas.
4. Relee tu informe M18: ¿qué quedó pendiente en prod?
5. Define “severidad”: crítica / alta / media / baja con ejemplos tuyos.

## Ejemplo — checklist rápido de review

```text
[ ] Auth en todos los endpoints sensibles
[ ] Autorización por dueño/rol (anti-IDOR)
[ ] Rate limit en login
[ ] Headers de seguridad en prod
[ ] Backups restaurables (probado)
[ ] Logs sin contraseñas/tokens
[ ] Dependencias con CVEs críticos conocidas
```

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Inventario, superficie, clasificación de datos |
| 2 | Review manual auth/roles + tooling básico |
| 3 | Hardening deploy (TLS, firewall, secrets en hosting) |
| 4 | Logging, abuso, alertas mínimas |
| 5 | Privacidad / retención de datos (intro ingeniería) |
| 6 | Tabletop incidente + reporte final |

## Recursos (ES)

- OWASP Testing Guide (selectos) + tu checklist.
- Docs de tu proveedor cloud (secretos, firewall).
- [Hilo de seguridad](../../hilos/seguridad.md).

## Prácticas

1. **P1:** Inventario completo (con dueño de cada secreto).
2. **P2:** ≥8 issues en el tracker del producto, 5 cerrados con evidencia.
3. **P3:** Tabletop escrito: detección → contención → rotación → postmortem.

## Proyecto útil

`projects/m25-ciber/security-review.md` estilo profesional + enlaces a PRs. Este documento alimenta el egreso y el M26.

## Errores comunes

- Escanear internet al azar “para practicar”.
- Reportar 50 hallazgos cosméticos y cero IDOR reales.
- No probar restore de backups (“ya hay backup” ≠ funciona).

## Criterios de dominio

- [ ] Puedes guiar un tabletop de 30 min sin leer un tutorial.
- [ ] Prod tiene TLS + secretos fuera del repo + backup restaurado al menos 1 vez.
- [ ] El security review es accionable (prioridad + dueño + deadline).
