---
id: L07
materia: M18
orden: 7
titulo: Sesiones server-side vs JWT en Agenda Ops
horas: 5.0
semana: 2
lectura: Session Management + JWT Cheat Sheets
evidencia: projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)
---

# L07 — Sesiones server-side vs JWT en Agenda Ops

**~5.0 h · Semana 2**

M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.

## Objetivo

ADR en `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: decisión, alternativas, impacto XSS/CSRF/móvil M20.

## Pasos

### 1. Compara en contexto (40–50 min)

Tabla pros/contras: panel+API same-site vs SPA cross-origin; revocación; HttpOnly vs `Authorization`.

```bash
mkdir -p projects/m18-appsec/docs
cat > projects/m18-appsec/docs/adr-sesion-vs-jwt.md <<'EOF'
# ADR — Sesión server-side vs JWT

## Contexto
Agenda Ops: panel web + API; móvil M20 futuro.

## Opciones
| Opción | Revocación | XSS | CSRF | Móvil |
|--------|------------|-----|------|-------|
| Sesión + cookie HttpOnly | inmediata (DB) | mejor | riesgo CSRF | cookie jar |
| JWT en memoria / header | short TTL / deny-list | si en storage, peor | menos CSRF | natural |
| Híbrido | … | … | … | … |

## Decisión
…

## Consecuencias / mitigaciones obligatorias
- HttpOnly / TTL / revoke / SameSite …
EOF
```
### 2. Prueba logout/reuse (40–50 min)

Login → copiar cookie/token → logout → reutilizar (debe fallar). Anota en la ADR.

```bash
# Ejemplo cookie de sesión (ajusta nombre/URL)
curl -c /tmp/m18-cj -s -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' -o /dev/null -w "%{http_code}\n"
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout -w "%{http_code}\n"
curl -b /tmp/m18-cj -s localhost:3000/api/citas -w "\n%{http_code}\n" | tail -3
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/adr-sesion-vs-jwt.md
git commit -m "docs(m18): l07 adr sesion jwt"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session Management + JWT Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR con alternativas (artefacto: `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
2. Prueba logout/reuse documentada (artefacto: `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
3. Commit `docs(m18): L07 sesiones-server-side-vs-jwt-en-agenda-ops`.

## Errores comunes

- JWT en localStorage sin plan anti-XSS.
- Sin estrategia de revocación.

## Siguiente

[L08 — Threat model v1 post-autenticación (P1)](L08-threat-model-v1-post-autenticacion-p1.md)
