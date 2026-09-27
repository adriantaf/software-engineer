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

Sin rate limit, A07 y DoS ligero son triviales.

## Objetivo

Límite en login (+1 endpoint costoso); prueba 429 documentada; nota en findings.

## Pasos

### 1. Middleware o proxy (60–80 min)

```ts
import rateLimit from "express-rate-limit";

export const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "too_many_requests" },
});

// app.post("/auth/login", loginLimiter, loginHandler);
```
### 2. Prueba de bloqueo (40–50 min)

```bash
for i in $(seq 1 25); do
  curl -s -o /dev/null -w "$i:%{http_code}\n" -X POST localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@test.local","password":"wrong"}'
done | tail -5
# espera ver 429

printf "\n## Rate limit login\n- window: 15m · max: 20\n- prueba: ver 429 tras N intentos\n- reset dev: reiniciar proceso / redis FLUSH\n" >> projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "fix(m18): l19 rate limit login"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Brute Force + Rate Limiting Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Rate limit activo (artefacto: `commit middleware`).
2. Prueba documentada (artefacto: `commit middleware`).
3. Commit `docs(m18): L19 rate-limiting-en-login-y-endpoints-sensibles`.

## Errores comunes

- Rate limit solo en front.
- Bloqueo permanente sin unlock.

## Siguiente

[L20 — Tests automatizados cross-user (P2 avance)](L20-tests-automatizados-cross-user-p2-avance.md)
