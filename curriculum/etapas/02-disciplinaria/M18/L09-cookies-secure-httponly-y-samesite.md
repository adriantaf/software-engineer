---
id: L09
materia: M18
orden: 9
titulo: Cookies Secure, HttpOnly y SameSite
horas: 5.0
semana: 3
lectura: OWASP Session Management + cookie flags
evidencia: projects/m18-appsec/pocs/cookies.md
---

# L09 — Cookies Secure, HttpOnly y SameSite

**~5.0 h · Semana 3**

Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.

## Objetivo

Tabla real de cookies en `projects/m18-appsec/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si faltan.

## Pasos

### 1. Inspección Set-Cookie (30–40 min)

```bash
curl -sI -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
```
### 2. Documenta + harden (70–90 min)

```bash
cat > projects/m18-appsec/pocs/cookies.md <<'EOF'
# Cookies lab
| Nombre | HttpOnly | Secure | SameSite | Path | Max-Age |
|--------|----------|--------|----------|------|---------|
| sid? | | | | | |

## Antes / después
- Antes: …
- Después: …
## ¿JS puede leer la cookie de sesión?
document.cookie → …
EOF
```

Ejemplo Express / cookie-session:

```ts
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax", // o "strict" si no hay cross-site legítimo
  path: "/",
});
```
### 3. Prueba HttpOnly (20 min)

En DevTools Console (sesión logueada): `document.cookie` no debe mostrar la cookie de sesión. Captura redactada en `pocs/cookies.md`.
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/cookies.md
git commit -m "fix(m18): l09 cookie flags"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Session Management + cookie flags | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla de cookies real (artefacto: `projects/m18-appsec/pocs/cookies.md`).
2. Parche o justificación documentada (artefacto: `projects/m18-appsec/pocs/cookies.md`).
3. Commit `docs(m18): L09 cookies-secure-httponly-y-samesite`.

## Errores comunes

- SameSite=None sin Secure.
- Cookie de sesión accesible desde JS.

## Siguiente

[L10 — CSRF en formularios y mutaciones state-changing](L10-csrf-en-formularios-y-mutaciones-state-changing.md)
