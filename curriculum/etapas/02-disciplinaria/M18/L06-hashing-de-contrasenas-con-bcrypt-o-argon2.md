---
id: L06
materia: M18
orden: 6
titulo: Hashing de contraseñas con bcrypt o argon2
horas: 5.0
semana: 2
lectura: Password Storage Cheat Sheet
evidencia: commit en repo producto + nota en projects/m18-appsec/auth-hashing.md
---

# L06 — Hashing de contraseñas con bcrypt o argon2

**~5.0 h · Semana 2**

Verifica cost factor y ausencia de hashes débiles.

## Objetivo

PoC o test: password nunca en MD5/SHA solo; bcrypt/argon2 con cost documentado; fix si hace falta.

## Pasos (hazlos en orden)

### 1. Auditoría (40 min)

Busca `md5|sha1|sha256\\(password` en el repo app.

### 2. Fix/confirmación (70–90 min)

Cost ≥12 bcrypt o argon2id razonable. Test verify round-trip.

### 3. Evidencia (20 min)

Entrada hallazgo o “N/A — ya conforme” con commit hash.

### 4. Commit

`fix(m18): l06 password hashing`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Password Storage Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Hashing correcto en código o ADR si ya estaba (artefacto: `commit en repo producto`).
2. Test o script que verifica compare (artefacto: `commit en repo producto`).
3. Doc de parámetros (artefacto: `commit en repo producto`).
4. Commit `docs(m18): L06 hashing-de-contrasenas-con-bcrypt-o-argon2`.

## Errores comunes

- MD5/SHA1 para passwords.
- Cost 4 ‘para ir rápido’.

## Siguiente

[L07 — Sesiones server-side vs JWT en Agenda Ops](L07-sesiones-server-side-vs-jwt-en-agenda-ops.md)
