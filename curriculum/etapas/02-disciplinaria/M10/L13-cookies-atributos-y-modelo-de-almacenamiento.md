---
id: L13
materia: M10
orden: 13
titulo: "Cookies: atributos y modelo de almacenamiento"
horas: 5.0
semana: 4
lectura: MDN Cookies (ES)
evidencia: labs/cookies.md
---

# L13 — Cookies: atributos y modelo de almacenamiento

**~5.0 h · Semana 4**

La sesión del dueño del salón vivirá en cookies o en headers. Hoy eliges atributos a conciencia.

## Objetivo

Documentar el modelo de cookie de sesión para Agenda Ops.

## Pasos

### 1. Lectura MDN (50 min)

Subraya Secure, HttpOnly, SameSite=Lax/Strict/None, Domain, Path, Max-Age vs Expires.

### 2. Lab observación (40 min)

```bash
curl -sI https://example.com | grep -i set-cookie || true
```

Si no hay cookies, inventa un ejemplo realista en la bitácora y analiza cada flag.

### 3. Decisión producto (60 min)

En `labs/cookies.md`:

```text
Set-Cookie: session=…; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=…
```

Justifica cada flag para owner/staff. Contrasta con token en `Authorization` header.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cookies.md
git commit -m "docs(m10): l13 cookies"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Set-Cookie; Secure, HttpOnly, SameSite, Path, Domain, Max-Age | [MDN · HTTP cookies](https://developer.mozilla.org/es/docs/Web/HTTP/Cookies) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cookies.md` tabla de atributos con decisión recomendada para sesión Agenda Ops.
2. Ejemplo `Set-Cookie` redactado (valores ficticios).
3. Commit `docs(m10): l13 cookies`.

## Errores comunes

- Cookie de sesión sin `Secure`/`HttpOnly` en prod.
- `SameSite=None` sin entender CSRF.
- Guardar access tokens de larga vida en `localStorage` “porque es más fácil”.

## Siguiente

[L14 — Sesiones, tokens y estado en APIs](L14-sesiones-tokens-y-estado-en-apis.md)
