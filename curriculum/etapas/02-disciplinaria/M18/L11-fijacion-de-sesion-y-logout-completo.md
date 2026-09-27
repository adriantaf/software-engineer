---
id: L11
materia: M18
orden: 11
titulo: Fijación de sesión y logout completo
horas: 5.0
semana: 3
lectura: Session fixation + logout best practices
evidencia: projects/m18-appsec/docs/session-lifecycle.md
---

# L11 — Fijación de sesión y logout completo

**~5.0 h · Semana 3**

Robar sesión fija es clásico en apps que reutilizan el mismo session id.

## Objetivo

Ciclo de vida en `projects/m18-appsec/docs/session-lifecycle.md`: rotate post-login + destroy server-side en logout.

## Pasos

### 1. Traza el ciclo en código (40–50 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'regenerate|session\.id|destroy|logout|revoke' -g '!node_modules' | head -30
cat > projects/m18-appsec/docs/session-lifecycle.md <<'EOF'
# Session lifecycle
1. Pre-login id: …
2. Post-login (¿rota?): …
3. Logout server-side: …
4. Request posterior con cookie vieja: esperado 401
EOF
```
### 2. Pruebas login/logout (50–60 min)

```bash
# Dos logins: ¿cambia el valor de Set-Cookie?
curl -sI -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i set-cookie
# Logout + reuse (debe fallar)
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout
curl -b /tmp/m18-cj -s -o /dev/null -w "%{http_code}\n" localhost:3000/api/pedidos
```

Si JWT stateless: documenta deny-list o TTL corto en el mismo archivo.
### 3. Commit (10–15 min)

```bash
git add projects/m18-appsec/docs/session-lifecycle.md
git commit -m "fix(m18): l11 session lifecycle"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session fixation + logout best practices | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc ciclo de vida (artefacto: `projects/m18-appsec/docs/session-lifecycle.md`).
2. Pruebas login/logout documentadas (artefacto: `projects/m18-appsec/docs/session-lifecycle.md`).
3. Commit `docs(m18): L11 fijacion-de-sesion-y-logout-completo`.

## Errores comunes

- Logout solo borra cookie cliente.
- Session id pre-login reutilizado.

## Siguiente

[L12 — Checklist cookies y CSRF en staging](L12-checklist-cookies-y-csrf-en-staging.md)
