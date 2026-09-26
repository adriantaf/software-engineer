---
id: L19
materia: M18
orden: 19
titulo: Rate limiting en login y endpoints sensibles
horas: 5.0
semana: 5
lectura: Brute Force + Rate Limiting Cheat Sheets
evidencia: commit middleware + nota en findings
---

# L19 — Rate limiting en login y endpoints sensibles

**~5.0 h · Semana 5**

Confirma o añade rate limit; mide 429.

## Objetivo

Evidencia 429 en login; hallazgo/fix documentado.

## Pasos (hazlos en orden)

### 1. Prueba carga ligera (50 min)

Script de N logins fallidos.

### 2. Ajuste (60–80 min)

Umbrales; no ban eterno sin doc.

### 3. Commit

`fix(m18): l19 rate limit evidenciado`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Brute Force + Rate Limiting Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Rate limit activo (artefacto: `commit middleware`).
2. Prueba documentada (artefacto: `commit middleware`).
3. Mensaje usuario claro (artefacto: `commit middleware`).
4. Commit `docs(m18): L19 rate-limiting-en-login-y-endpoints-sensibles`.

## Errores comunes

- Rate limit solo en front.
- Bloqueo permanente sin unlock.

## Siguiente

[L20 — Tests automatizados cross-user (P2 avance)](L20-tests-automatizados-cross-user-p2-avance.md)
