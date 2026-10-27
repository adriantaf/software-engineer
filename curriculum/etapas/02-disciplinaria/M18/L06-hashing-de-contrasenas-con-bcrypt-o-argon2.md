---
id: L06
materia: M18
orden: 6
titulo: Hashing de contraseñas con bcrypt o argon2
horas: 5.0
semana: 2
lectura: Password Storage Cheat Sheet
evidencia: commit en repo producto + nota en projects/m18-appsec/docs/auth-hashing.md
---

# L06 — Hashing de contraseñas con bcrypt o argon2

**~5.0 h · Semana 2**

A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.

## Objetivo

Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o argon2id. Nota en `projects/m18-appsec/docs/auth-hashing.md` + test.

## Pasos

### 1. Auditoría de hashes débiles (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'md5|sha1|sha256\(|createHash\(|crypto\.hash' -g '!node_modules' | rg -i 'pass|pwd|hash' || true
rg -n 'bcrypt|argon2' -g '!node_modules' | head -20
```
### 2. Confirmación o fix (70–90 min)

Si falta: lib madura + cost documentado. Ejemplo bcrypt:

```ts
import bcrypt from "bcrypt";

const ROUNDS = 12; // documenta en docs/auth-hashing.md

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, ROUNDS);
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

```bash
cat > projects/m18-appsec/docs/auth-hashing.md <<'EOF'
# Password hashing
- Algoritmo: bcrypt | argon2id
- Parámetros: cost/rounds = …
- Migación usuarios prueba: sí/no
- Commit fix (si hubo): …
EOF
```
### 3. Test round-trip (30–40 min)

```bash
npm test -- --testPathPattern=auth 2>/dev/null || npm test -- auth
# o: node -e "..." con compare true/false
```

```ts
// tests/security/password-hash.test.ts (ejemplo)
expect(await verifyPassword("secret", await hashPassword("secret"))).toBe(true);
expect(await hashPassword("secret")).not.toEqual("secret");
```
### 4. Commit (10 min)

```bash
git add -A
git commit -m "fix(m18): l06 password hashing"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Password Storage Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Hashing correcto en código o ADR si ya estaba (artefacto: `commit en repo producto`).
2. Test o script que verifica compare (artefacto: `commit en repo producto`).
3. Commit `docs(m18): L06 hashing-de-contrasenas-con-bcrypt-o-argon2`.

## Errores comunes

- MD5/SHA1 para passwords.
- Cost 4 ‘para ir rápido’.

## Siguiente

[L07 — Sesiones server-side vs JWT en Vitrina](L07-sesiones-server-side-vs-jwt-en-vitrina.md)
