---
id: L05
materia: M18
orden: 5
titulo: Inventario de autenticación actual
horas: 5.0
semana: 2
lectura: OWASP A07 + Authentication Cheat Sheet
evidencia: projects/m18-appsec/docs/auth-inventario.md
---

# L05 — Inventario de autenticación actual

**~5.0 h · Semana 2**

Antes de endurecer, documentas qué hay en M17. Fotografía del estado auth.

## Objetivo

`projects/m18-appsec/docs/auth-inventario.md`: mecanismo, almacenamiento token/sesión, endpoints públicos vs autenticados.

## Pasos

### 1. Inspección en el repo producto (40–50 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'bcrypt|argon2|passport|jsonwebtoken|express-session|setCookie|Set-Cookie|sign\(|verify\(' \
  -g '!node_modules' -g '!dist' | head -40
```
### 2. Inventario happy path + edges (70–90 min)

Describe paso a paso registro/login/logout y 2 edge cases (password malo, usuario inexistente). Sin passwords ni tokens reales.

```bash
mkdir -p projects/m18-appsec/docs
cat > projects/m18-appsec/docs/auth-inventario.md <<'EOF'
# Inventario de autenticación — Vitrina

## Endpoints
| Método | Ruta | Público | Notas |
|--------|------|---------|-------|
| POST | /auth/login | sí | |
| POST | /auth/logout | auth | |
| POST | /auth/register | ? | |

## Transporte / almacenamiento
- Cookie: nombre=… · HttpOnly=… · Secure=… · SameSite=…
- o `Authorization: Bearer …` (dónde se guarda en el cliente)

## Edge cases
1. Password malo → status/mensaje
2. Usuario inexistente → ¿mismo mensaje genérico?

## Riesgos preliminares
- localStorage vs cookie
- rotación de sesión
- logout incompleto
EOF
```
### 3. Verifica mensajes uniformes (20–30 min)

```bash
# Dos intentos; compara cuerpo (sin pegar tokens)
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"noexiste@test.local","password":"x"}' | head -c 200
echo
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"wrong"}' | head -c 200
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/docs/auth-inventario.md
git commit -m "docs(m18): l05 inventario autenticacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A07 + Authentication Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Inventario con endpoints reales (artefacto: `projects/m18-appsec/docs/auth-inventario.md`).
2. Público vs autenticado claro (artefacto: `projects/m18-appsec/docs/auth-inventario.md`).
3. Commit `docs(m18): L05 inventario-de-autenticacion-actual`.

## Errores comunes

- Inventario teórico sin abrir el código.
- Loguear tokens en dev.

## Siguiente

[L06 — Hashing de contraseñas con bcrypt o argon2](L06-hashing-de-contrasenas-con-bcrypt-o-argon2.md)
