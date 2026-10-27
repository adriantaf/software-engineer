---
id: L03
materia: M17
orden: 3
titulo: Login, sesión y GET /me protegido
horas: 5.0
semana: 1
lectura: MDN cookies + ADR sesión M13
evidencia: POST /auth/login + GET /me
---

# L03 — Login, sesión y GET /me protegido

**~5.0 h · Semana 1**

El panel Vitrina necesita identidad servidor-confiable.

## Objetivo

Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin credencial.

## Conceptos clave

- sesión
- 401
- HttpOnly

## Pasos (hazlos en orden)

### 1. Decide sesión vs JWT-cookie (20–30 min)

```bash
mkdir -p projects/m17-vitrina/docs
cat > projects/m17-vitrina/docs/auth.md << 'EOF'
# Auth Vitrina
- Mecanismo: cookie HttpOnly (preferido) / JWT-en-cookie
- Secure / SameSite: ...
- Riesgos XSS/CSRF y mitigación
EOF
```

### 2. Implementa login + GET /me (80–100 min)

Login verifica hash; setea cookie. `GET /me` → id, email, rol (sin hash).

```bash
curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"Secreto123!"}'
curl -sS -b /tmp/ao.ck http://localhost:3000/me
curl -sS -o /tmp/me.out -w "%{http_code}" http://localhost:3000/me
# sin cookie → 401
```

### 3. Tests 401/200 + commit (40–50 min)

```bash
npm test -- auth
git add projects/m17-vitrina/docs/auth.md projects/m17-vitrina
git commit -m "feat(m17): L03 login sesion y me"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN cookies + ADR sesión M13 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/auth.md` documenta cookie HttpOnly o JWT-cookie.
2. `POST /auth/login` + `GET /me` 200 con sesión; sin cookie → 401.
3. Tests cubren login→me y 401 (artefacto: `POST /auth/login`).
4. Commit `docs(m17): L03 login-sesion-y-get-me-protegido`.

## Errores comunes

- JWT en localStorage sin justificar XSS.
- `GET /me` sin auth devuelve 200.
- Devolver row completo con hash.

## Siguiente

[L04 — Cierre semana 1 — suite auth P1](L04-cierre-semana-1-suite-auth-p1.md)
