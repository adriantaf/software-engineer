---
id: L06
materia: M18
orden: 6
titulo: Hashing de contraseñas con bcrypt o argon2
horas: 5
semana: 2
lectura: Password Storage Cheat Sheet
evidencia: commit en repo producto + nota en projects/m18-appsec/docs/auth-hashing.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o
      argon2id. Nota en `projects/m18-appsec/docs/auth-hashing.md` + test.


      A07 empieza en la tabla `users`: un leak de DB no debe regalar
      contraseñas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría de hashes débiles
    xp: 10
    cuerpo: >-
      ```ts

      import bcrypt from "bcrypt";


      const ROUNDS = 12; // documenta en docs/auth-hashing.md


      export async function hashPassword(plain: string): Promise<string> {
        return bcrypt.hash(plain, ROUNDS);
      }


      export async function verifyPassword(plain: string, hash: string):
      Promise<boolean> {
        return bcrypt.compare(plain, hash);
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Hashing de contraseñas con bcrypt o argon2" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: >-
          commit en repo producto + nota en
          projects/m18-appsec/docs/auth-hashing.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o argon2id. Nota en
          `projects/m18-appsec/docs/auth-hashing.md` + test.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Confirmación o fix
    xp: 10
    cuerpo: >-
      Si falta: lib madura + cost documentado. Ejemplo bcrypt:


      ```ts

      import bcrypt from "bcrypt";


      const ROUNDS = 12; // documenta en docs/auth-hashing.md


      export async function hashPassword(plain: string): Promise<string> {
        return bcrypt.hash(plain, ROUNDS);
      }


      export async function verifyPassword(plain: string, hash: string):
      Promise<boolean> {
        return bcrypt.compare(plain, hash);
      }

      ```


      ```bash

      cat > projects/m18-appsec/docs/auth-hashing.md <<'EOF'

      Password hashing

      - Algoritmo: bcrypt | argon2id

      - Parámetros: cost/rounds = …

      - Migación usuarios prueba: sí/no

      - Commit fix (si hubo): …

      EOF

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Test round-trip
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- --testPathPattern=auth 2>/dev/null || npm test -- auth
      # o: node -e "..." con compare true/false
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Hashing correcto en código o ADR si ya estaba (artefacto: `commit en
        repo producto`).
      - >-
        Test o script que verifica compare (artefacto: `commit en repo
        producto`).
      - 'Commit `docs(m18): L06 hashing-de-contrasenas-con-bcrypt-o-argon2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
