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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      A07 empieza en la tabla `users`: un leak de DB no debe regalar
      contraseñas.


      **Objetivo de esta lección:** Password nunca en MD5/SHA solo; bcrypt (cost
      ≥12) o argon2id. Nota en `projects/m18-appsec/docs/auth-hashing.md` +
      test.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría de hashes débiles
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'md5|sha1|sha256\(|createHash\(|crypto\.hash' -g '!node_modules' |
      rg -i 'pass|pwd|hash' || true

      rg -n 'bcrypt|argon2' -g '!node_modules' | head -20

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Confirmación o fix
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


      Si falta: lib madura + cost documentado. Ejemplo bcrypt:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Hashing de contraseñas con bcrypt o argon2», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Hashing de contraseñas
          con bcrypt o arg…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o argon2id. Nota en
          `projects/m18-appsec/docs/auth-hashing.md` + test.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Test round-trip
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
