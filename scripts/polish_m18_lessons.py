#!/usr/bin/env python3
"""Polish all 32 M18 AppSec lessons to M09 depth.

- Rewrites BODIES in scripts/_m17_m20/m18_lessons.py with timed steps + ``` fences
- Unifies auth evidence to projects/m18-appsec/docs/auth-inventario.md
- Regenerates curriculum/etapas/02-disciplinaria/M18/L*.md via rewrite_m18
- Seeds projects/m18-appsec/ scaffold templates

Run from repo root:
  python3 scripts/polish_m18_lessons.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

P = "projects/m18-appsec"
APP = "projects/m17-agenda-ops"  # repo producto; ajustar si vive fuera


def body(lid: str, titulo: str, semana: int, porque: str, objetivo: str, pasos: str) -> str:
    return f"""# {lid} — {titulo}

**~5.0 h · Semana {semana}**

{porque}

## Objetivo

{objetivo}

## Pasos

{pasos.strip()}
""".strip()


def bash(code: str) -> str:
    return f"```bash\n{code.strip()}\n```"


def ts(code: str) -> str:
    return f"```ts\n{code.strip()}\n```"


def sql(code: str) -> str:
    return f"```sql\n{code.strip()}\n```"


def md(code: str) -> str:
    return f"```markdown\n{code.strip()}\n```"


def yml(code: str) -> str:
    return f"```yaml\n{code.strip()}\n```"


def step(n: int, title: str, content: str) -> str:
    return f"### {n}. {title}\n\n{content.strip()}\n"


# ---------------------------------------------------------------------------
# Full BODIES (M09 depth): timed steps + exact paths + code fences
# ---------------------------------------------------------------------------

BODIES: dict[int, str] = {}

BODIES[1] = body(
    "L01",
    "Activos, actores y datos sensibles en Agenda Ops",
    1,
    "Sin lista de activos, el threat model es decoración. Hoy arrancas P1 y el hilo OWASP.",
    f"Completar tablas Actores y ≥5 Activos en `{P}/threat-model-v0.md` (PII, credenciales, citas, tokens, Postgres).",
    step(1, "Carpeta de evidencia (15 min)", f"""
Crea la estructura si aún no existe:

{bash(f'''mkdir -p {P}/{{docs,pocs,fixes,tests,ci,findings}}
ls {P}''')}
""")
    + step(2, "Actores y activos (80–100 min)", f"""
Abre `{P}/threat-model-v0.md`. Completa **Actores** (dueño, staff, cliente final, atacante anónimo) y **Activos** (≥5) con confidencialidad. Diagrama: navegador → API → Postgres.

{md('''## Actores
| Actor | Objetivos | Capacidades |
|-------|-----------|-------------|
| Dueño (owner) | Gestionar negocio | CRUD total |
| Staff | Operar citas | CRUD limitado |
| Cliente final | Pedir cita | Solo sus datos |
| Atacante anónimo | Robar PII / sesión | Sin credenciales |

## Activos (≥5)
| Activo | Confidencialidad | Dónde vive |
|--------|------------------|------------|
| Teléfono cliente | Alta | `clientes.telefono` |
| Hash password | Crítica | `users.password_hash` |
| Notas de cita | Alta | `citas.notas` |
| Cookie de sesión | Crítica | `Set-Cookie` |
| Postgres | Crítica | volumen / hosting |''')}
""")
    + step(3, "Superficie JSON + anti-secretos (30–40 min)", f"""
Marca qué campos salen en `GET /api/citas`. Ejecuta el barrido y anota rutas (sin pegar secretos):

{bash('''git ls-files | rg -i 'env|secret|credential|\\.pem' || true''')}
""")
    + step(4, "Commit (10–15 min)", f"""
{bash(f'''git add {P}/threat-model-v0.md
git status   # sin .env
git commit -m "docs(m18): l01 activos actores agenda ops"''')}
"""),
)

BODIES[2] = body(
    "L02",
    "Trust boundaries y flujos de confianza",
    1,
    "M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.",
    f"Documentar ≥4 límites y 3 flujos (login, crear cita, deep-link WA) en `{P}/trust-boundaries-appsec.md`.",
    step(1, "Ancla M13 (20–30 min)", f"""
{bash(f'''ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13; parte de cero)"
touch {P}/trust-boundaries-appsec.md''')}
""")
    + step(2, "Tabla de límites (70–90 min)", f"""
Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo 4.

{md('''| Origen | Destino | Protocolo | Auth | Datos |
|--------|---------|-----------|------|-------|
| Browser | API | HTTPS | cookie/JWT | PII citas |
| API | Postgres | TCP | user app | SQL |
| API | SMTP futuro | TLS | API key | recordatorios |
| Operador | Hosting | SSH/HTTPS | MFA | logs, .env |''')}
""")
    + step(3, "Flujos + abuso (40–50 min)", f"""
Para login, crear cita y deep-link WA: datos en tránsito, auth requerida, fallo si se omite authz. Una pregunta de abuso por límite.

{bash(f'''printf "\\n## Flujos\\n- login:\\n- crear cita:\\n- deep-link WA:\\n\\n## Abuso por límite\\n" >> {P}/trust-boundaries-appsec.md''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/trust-boundaries-appsec.md
git commit -m "docs(m18): l02 trust boundaries"''')}
"""),
)

BODIES[3] = body(
    "L03",
    "STRIDE aplicado al CRM de citas",
    1,
    "La matriz obliga a nombrar amenazas antes de buscar exploits al azar.",
    f"Matriz STRIDE ≥4×6 en `{P}/stride-matrix.md` (login, citas, admin) con ≥3 amenazas priorizadas.",
    step(1, "Plantilla STRIDE (25–35 min)", f"""
{bash(f'''cat > {P}/stride-matrix.md <<'EOF'
# Matriz STRIDE — Agenda Ops

| Componente | S | T | R | I | D | E |
|------------|---|---|---|---|---|---|
| Login | | | | | | |
| Lista citas | | | | | | |
| Detalle cita | | | | | | |
| Admin usuarios | | | | | | |
EOF''')}
""")
    + step(2, "Relleno del dominio (90–110 min)", f"""
Frases concretas (no “hackeo”). Ejemplo Login/Spoofing: “fuerza bruta o credenciales robadas”. Incluye IDOR en detalle cita e XSS en notas.

{md('''| Componente | S | T | I |
|------------|---|---|---|
| Login | Fuerza bruta | Tamper cookie | Leak en error |
| Detalle cita | — | PUT sin authz | IDOR lee notas |''')}
""")
    + step(3, "Prioriza 3 celdas (30 min)", f"""
Marca las 3 amenazas de las semanas 2–5. Enlaza `threat-model-v0.md`.

{bash(f'''printf "\\n## Prioridades (rojas)\\n1. ...\\n2. ...\\n3. ...\\n" >> {P}/stride-matrix.md''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/stride-matrix.md
git commit -m "docs(m18): l03 stride crm citas"''')}
"""),
)

BODIES[4] = body(
    "L04",
    "Threat model v0 y lectura OWASP Top 10",
    1,
    "Cierras la semana 1 con backlog de riesgo alineado a la industria.",
    f"Mapa Top 10 en `{P}/owasp-top10-map.md` + `threat-model-v0.md` con riesgo residual semana 1.",
    step(1, "Lectura Top 10 (40–50 min)", f"""
Lee OWASP Top 10 (2021) ES. Anota A01, A03, A07 como foco M18.

{bash('''curl -sI https://owasp.org/Top10/es/ | head -5''')}
""")
    + step(2, "Mapa 10 filas (70–90 min)", f"""
{bash(f'''cat > {P}/owasp-top10-map.md <<'EOF'
# OWASP Top 10 → Agenda Ops

| Id | Ejemplo Agenda Ops | Mitigación | Semana |
|----|--------------------|------------|--------|
| A01 | GET /api/citas/:id cross-user | authz owner | 5 |
| A02 | secretos en repo | .env + rotación | 7 |
| A03 | búsqueda concat SQL | params/ORM | 4 |
| A04 | sin rate limit login | 429 | 5 |
| A05 | cookies sin flags | Secure/HttpOnly | 3 |
| A06 | deps vulnerables | npm audit | 7 |
| A07 | hash débil / sesión | bcrypt + rotate | 2 |
| A08 | integridad build | CI firmada (idea) | 8 |
| A09 | logs sin retención | política mínima | 8 |
| A10 | SSRF webhook futuro | allowlist | 6 |
EOF''')}
""")
    + step(3, "Cierra threat-model-v0 (25–35 min)", f"""
Sección **Riesgo residual semana 1** (3 bullets). Confirma P1 tras semana 2 auth.

{bash(f'''printf "\\n## Riesgo residual semana 1\\n- Auth aún no endurecida\\n- Access control por verificar\\n- Deps sin audit\\n" >> {P}/threat-model-v0.md''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/owasp-top10-map.md {P}/threat-model-v0.md
git commit -m "docs(m18): l04 threat model v0 owasp"''')}
"""),
)

BODIES[5] = body(
    "L05",
    "Inventario de autenticación actual",
    2,
    "Antes de endurecer, documentas qué hay en M17. Fotografía del estado auth.",
    f"`{P}/docs/auth-inventario.md`: mecanismo, almacenamiento token/sesión, endpoints públicos vs autenticados.",
    step(1, "Inspección en el repo producto (40–50 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'bcrypt|argon2|passport|jsonwebtoken|express-session|setCookie|Set-Cookie|sign\\(|verify\\(' \\
  -g '!node_modules' -g '!dist' | head -40''')}
""")
    + step(2, "Inventario happy path + edges (70–90 min)", f"""
Describe paso a paso registro/login/logout y 2 edge cases (password malo, usuario inexistente). Sin passwords ni tokens reales.

{bash(f'''mkdir -p {P}/docs
cat > {P}/docs/auth-inventario.md <<'EOF'
# Inventario de autenticación — Agenda Ops

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
EOF''')}
""")
    + step(3, "Verifica mensajes uniformes (20–30 min)", f"""
{bash('''# Dos intentos; compara cuerpo (sin pegar tokens)
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \\
  -d '{"email":"noexiste@test.local","password":"x"}' | head -c 200
echo
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \\
  -d '{"email":"owner@test.local","password":"wrong"}' | head -c 200''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/auth-inventario.md
git commit -m "docs(m18): l05 inventario autenticacion"''')}
"""),
)

BODIES[6] = body(
    "L06",
    "Hashing de contraseñas con bcrypt o argon2",
    2,
    "A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.",
    f"Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o argon2id. Nota en `{P}/docs/auth-hashing.md` + test.",
    step(1, "Auditoría de hashes débiles (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'md5|sha1|sha256\\(|createHash\\(|crypto\\.hash' -g '!node_modules' | rg -i 'pass|pwd|hash' || true
rg -n 'bcrypt|argon2' -g '!node_modules' | head -20''')}
""")
    + step(2, "Confirmación o fix (70–90 min)", f"""
Si falta: lib madura + cost documentado. Ejemplo bcrypt:

{ts('''import bcrypt from "bcrypt";

const ROUNDS = 12; // documenta en docs/auth-hashing.md

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, ROUNDS);
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}''')}

{bash(f'''cat > {P}/docs/auth-hashing.md <<'EOF'
# Password hashing
- Algoritmo: bcrypt | argon2id
- Parámetros: cost/rounds = …
- Migación usuarios prueba: sí/no
- Commit fix (si hubo): …
EOF''')}
""")
    + step(3, "Test round-trip (30–40 min)", f"""
{bash('''npm test -- --testPathPattern=auth 2>/dev/null || npm test -- auth
# o: node -e "..." con compare true/false''')}

{ts('''// tests/security/password-hash.test.ts (ejemplo)
expect(await verifyPassword("secret", await hashPassword("secret"))).toBe(true);
expect(await hashPassword("secret")).not.toEqual("secret");''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash('''git add -A
git commit -m "fix(m18): l06 password hashing"''')}
"""),
)

BODIES[7] = body(
    "L07",
    "Sesiones server-side vs JWT en Agenda Ops",
    2,
    "M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.",
    f"ADR en `{P}/docs/adr-sesion-vs-jwt.md`: decisión, alternativas, impacto XSS/CSRF/móvil M20.",
    step(1, "Compara en contexto (40–50 min)", f"""
Tabla pros/contras: panel+API same-site vs SPA cross-origin; revocación; HttpOnly vs `Authorization`.

{bash(f'''mkdir -p {P}/docs
cat > {P}/docs/adr-sesion-vs-jwt.md <<'EOF'
# ADR — Sesión server-side vs JWT

## Contexto
Agenda Ops: panel web + API; móvil M20 futuro.

## Opciones
| Opción | Revocación | XSS | CSRF | Móvil |
|--------|------------|-----|------|-------|
| Sesión + cookie HttpOnly | inmediata (DB) | mejor | riesgo CSRF | cookie jar |
| JWT en memoria / header | short TTL / deny-list | si en storage, peor | menos CSRF | natural |
| Híbrido | … | … | … | … |

## Decisión
…

## Consecuencias / mitigaciones obligatorias
- HttpOnly / TTL / revoke / SameSite …
EOF''')}
""")
    + step(2, "Prueba logout/reuse (40–50 min)", f"""
Login → copiar cookie/token → logout → reutilizar (debe fallar). Anota en la ADR.

{bash('''# Ejemplo cookie de sesión (ajusta nombre/URL)
curl -c /tmp/m18-cj -s -X POST localhost:3000/auth/login \\
  -H 'content-type: application/json' \\
  -d '{"email":"owner@test.local","password":"***"}' -o /dev/null -w "%{http_code}\\n"
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout -w "%{http_code}\\n"
curl -b /tmp/m18-cj -s localhost:3000/api/citas -w "\\n%{http_code}\\n" | tail -3''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/adr-sesion-vs-jwt.md
git commit -m "docs(m18): l07 adr sesion jwt"''')}
"""),
)

BODIES[8] = body(
    "L08",
    "Threat model v1 post-autenticación (P1)",
    2,
    "P1 exige v1 revisado tras entender login; hoy entregas el hito.",
    f"`{P}/threat-model-v1.md` con controles auth, tabla amenaza→control y residual.",
    step(1, "Diff v0→v1 (30–40 min)", f"""
{bash(f'''cp {P}/threat-model-v0.md {P}/threat-model-v1.md
printf "\\n## Controles auth (post L05–L07)\\n| Amenaza | Control | Estado | Commit/issue |\\n|---------|---------|--------|--------------|\\n| Hash débil | bcrypt/argon2 | OK/TODO | |\\n| Sesión robable | HttpOnly plan | | |\\n| Sin revoke | ADR decisión | | |\\n" >> {P}/threat-model-v1.md''')}
""")
    + step(2, "Redacción P1 (80–100 min)", f"""
Enlaza `{P}/docs/auth-inventario.md` y ADR. Supuestos de staging. Tabla amenaza|control|estado legible sin abrir el código.

{bash(f'''printf "\\n## Enlaces\\n- auth: docs/auth-inventario.md\\n- ADR: docs/adr-sesion-vs-jwt.md\\n\\n## Residual auth\\n- ...\\n" >> {P}/threat-model-v1.md''')}
""")
    + step(3, "README P1 (15 min)", f"""
En `{P}/README.md` marca P1 entregado con fecha y ruta a `threat-model-v1.md`.

{bash(f'''rg -n "P1|threat-model-v1" {P}/README.md || printf "\\n- **P1:** threat-model-v1.md $(date -I)\\n" >> {P}/README.md''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/threat-model-v1.md {P}/README.md
git commit -m "docs(m18): l08 threat model v1 p1"''')}
"""),
)

BODIES[9] = body(
    "L09",
    "Cookies Secure, HttpOnly y SameSite",
    3,
    "Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.",
    f"Tabla real de cookies en `{P}/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si faltan.",
    step(1, "Inspección Set-Cookie (30–40 min)", f"""
{bash('''curl -sI -X POST localhost:3000/auth/login \\
  -H 'content-type: application/json' \\
  -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/''')}
""")
    + step(2, "Documenta + harden (70–90 min)", f"""
{bash(f'''cat > {P}/pocs/cookies.md <<'EOF'
# Cookies lab
| Nombre | HttpOnly | Secure | SameSite | Path | Max-Age |
|--------|----------|--------|----------|------|---------|
| sid? | | | | | |

## Antes / después
- Antes: …
- Después: …
## ¿JS puede leer la cookie de sesión?
document.cookie → …
EOF''')}

Ejemplo Express / cookie-session:

{ts('''res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax", // o "strict" si no hay cross-site legítimo
  path: "/",
});''')}
""")
    + step(3, "Prueba HttpOnly (20 min)", f"""
En DevTools Console (sesión logueada): `document.cookie` no debe mostrar la cookie de sesión. Captura redactada en `pocs/cookies.md`.
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/pocs/cookies.md
git commit -m "fix(m18): l09 cookie flags"''')}
"""),
)

BODIES[10] = body(
    "L10",
    "CSRF en formularios y mutaciones state-changing",
    3,
    "Un atacante no necesita XSS si tu sesión acepta POST cross-site.",
    f"Lista rutas mutables + protección en `{P}/pocs/csrf-notes.md`; ≥1 ruta crítica con token/SameSite; curl sin token → 403.",
    step(1, "Inventario mutaciones (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\\.(post|put|patch|delete)\\(" -g '*.ts' -g '!node_modules' | head -40
cat > {P}/pocs/csrf-notes.md <<'EOF'
# CSRF notes
| Ruta | Método | Protección | Estado |
|------|--------|------------|--------|
| /api/citas | POST | | |
| /api/citas/:id | PUT/DELETE | | |
| /auth/logout | POST | | |
EOF''')}
""")
    + step(2, "Protege la ruta crítica (70–90 min)", f"""
Token sincronizado, double-submit o SameSite estricto + método seguro. Ejemplo chequeo:

{ts('''// middleware mínimo (ilustrativo)
export function requireCsrf(req, res, next) {
  const token = req.headers["x-csrf-token"] || req.body?._csrf;
  if (!token || token !== req.session?.csrfToken) {
    return res.status(403).json({ error: "csrf" });
  }
  next();
}''')}
""")
    + step(3, "curl sin token (20–30 min)", f"""
{bash('''# Con cookie de sesión válida pero sin CSRF → 403
curl -s -o /dev/null -w "%{http_code}\\n" -X POST localhost:3000/api/citas \\
  -H 'content-type: application/json' -b /tmp/m18-cj \\
  -d '{"clienteId":"…","inicio":"2026-01-01T10:00:00Z"}'
# esperado: 403''')}
""")
    + step(4, "Commit (10 min)", f"""
{bash(f'''git add {P}/pocs/csrf-notes.md
git commit -m "fix(m18): l10 csrf mutaciones"''')}
"""),
)

BODIES[11] = body(
    "L11",
    "Fijación de sesión y logout completo",
    3,
    "Robar sesión fija es clásico en apps que reutilizan el mismo session id.",
    f"Ciclo de vida en `{P}/docs/session-lifecycle.md`: rotate post-login + destroy server-side en logout.",
    step(1, "Traza el ciclo en código (40–50 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'regenerate|session\\.id|destroy|logout|revoke' -g '!node_modules' | head -30
cat > {P}/docs/session-lifecycle.md <<'EOF'
# Session lifecycle
1. Pre-login id: …
2. Post-login (¿rota?): …
3. Logout server-side: …
4. Request posterior con cookie vieja: esperado 401
EOF''')}
""")
    + step(2, "Pruebas login/logout (50–60 min)", f"""
{bash('''# Dos logins: ¿cambia el valor de Set-Cookie?
curl -sI -X POST localhost:3000/auth/login -H 'content-type: application/json' \\
  -d '{"email":"owner@test.local","password":"***"}' | rg -i set-cookie
# Logout + reuse (debe fallar)
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout
curl -b /tmp/m18-cj -s -o /dev/null -w "%{http_code}\\n" localhost:3000/api/citas''')}

Si JWT stateless: documenta deny-list o TTL corto en el mismo archivo.
""")
    + step(3, "Commit (10–15 min)", f"""
{bash(f'''git add {P}/docs/session-lifecycle.md
git commit -m "fix(m18): l11 session lifecycle"''')}
"""),
)

BODIES[12] = body(
    "L12",
    "Checklist cookies y CSRF en staging",
    3,
    "Operacionalizas controles para M19 deploy y trials M22.",
    f"Checklist ≥10 ítems en `{P}/docs/checklist-cookies-csrf.md` ejecutado contra staging (fecha + URL).",
    step(1, "Escribe el checklist (40–50 min)", f"""
{bash(f'''cat > {P}/docs/checklist-cookies-csrf.md <<'EOF'
# Checklist cookies / CSRF — staging

Fecha: ____ · URL: ____

| # | Ítem | Sí/No | Nota |
|---|------|-------|------|
| 1 | Cookie sesión HttpOnly | | |
| 2 | Secure en HTTPS | | |
| 3 | SameSite Lax/Strict | | |
| 4 | Session id rota post-login | | |
| 5 | Logout invalida server-side | | |
| 6 | POST citas exige CSRF/equiv | | |
| 7 | GET no muta estado | | |
| 8 | Mensajes login genéricos | | |
| 9 | HTTPS redirect (si aplica) | | |
| 10 | Sin cookie sesión en document.cookie | | |

## Residual CSRF
- …

## Commits semana 3
- …
EOF''')}
""")
    + step(2, "Ejecuta en staging/local (60–80 min)", f"""
Marca Sí/No con evidencia (curl headers, captura redactada). Corrige ≥1 ítem No si aparece.

{bash('''curl -sI https://<tu-staging>/ | rg -i 'strict-transport|set-cookie' || true''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/checklist-cookies-csrf.md
git commit -m "docs(m18): l12 checklist cookies csrf"''')}
"""),
)

BODIES[13] = body(
    "L13",
    "SQLi: reproducir en tu propia API",
    4,
    "Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.",
    f"PoC o “no reproducible con ORM” en `{P}/findings/001-sqli.md` (sin PII real).",
    step(1, "Caza concatenación SQL (50–60 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\\$\\{{|query\\(|\\.query\\(|execute\\(|raw\\(|sql`" -g '!node_modules' | head -50
rg -n "SELECT.*\\+|WHERE.*\\+" -g '*.ts' -g '*.js' | head -20 || true''')}
""")
    + step(2, "PoC controlada (60–80 min)", f"""
Cuenta de prueba. Payload en búsqueda clientes/citas. **No** `DROP` en staging compartido.

{bash(f'''mkdir -p {P}/findings {P}/pocs
cat > {P}/findings/001-sqli.md <<'EOF'
# Finding 001 — SQLi
- Endpoint:
- Payload (ejemplo): `' OR '1'='1`
- Respuesta / impacto:
- ¿ORM parametrizado? evidencia:
- PII: ninguna en este reporte
EOF
# Ejemplo de prueba (ajusta query param)
curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" | head -c 400''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings/001-sqli.md
git commit -m "docs(m18): l13 poc sqli"''')}
"""),
)

BODIES[14] = body(
    "L14",
    "Mitigar SQLi: queries parametrizadas y permisos DB",
    4,
    "Hallazgo sin fix no cuenta para P2.",
    "Fix parametrizado + test de regresión; `001-sqli.md` → Cerrado con commit hash.",
    step(1, "Parametriza la query (60–80 min)", f"""
{ts('''// MAL
// db.query(`SELECT * FROM clientes WHERE nombre LIKE '%${q}%'`)

// BIEN (pg)
await db.query(
  "SELECT id, nombre, telefono FROM clientes WHERE nombre ILIKE $1 LIMIT 50",
  [`%${q}%`],
);''')}

{sql('''-- Usuario app sin DDL (idea)
-- CREATE ROLE agenda_app LOGIN PASSWORD '...';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO agenda_app;
-- (sin CREATE/DROP)''')}
""")
    + step(2, "Test de regresión (40–50 min)", f"""
{ts('''// tests/security/sqli-search.test.ts
it("rejects or safely handles SQLi-like search", async () => {
  const res = await api.get("/api/clientes", { q: "' OR '1'='1" });
  expect(res.status).not.toBe(500);
  expect(String(res.body)).not.toMatch(/syntax error|pg_|\bSQL\b/i);
});''')}

{bash('''npm test -- --testPathPattern=sqli || npm test -- security''')}
""")
    + step(3, "Cierra finding (20 min)", f"""
{bash(f'''printf "\\n## Estado: Cerrado\\n- Commit fix: \\n- Test: \\n" >> {P}/findings/001-sqli.md
git add -A && git commit -m "fix(m18): l14 sqli parametrized"''')}
"""),
)

BODIES[15] = body(
    "L15",
    "XSS reflejado en campos de cliente o búsqueda",
    4,
    "XSS roba sesiones si las cookies son legibles por JS.",
    f"PoC reflejado en `{P}/findings/002-xss-reflected.md` (solo tu cuenta de prueba; sin exfiltración externa).",
    step(1, "Localiza render de input (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'dangerouslySetInnerHTML|innerHTML|\\$\\{{.*q|searchParams|mensaje' -g '!node_modules' | head -30''')}
""")
    + step(2, "PoC local (60–80 min)", f"""
Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`. Solo impacto local.

{bash(f'''cat > {P}/findings/002-xss-reflected.md <<'EOF'
# Finding 002 — XSS reflejado
- Pantalla / query:
- Payload:
- ¿Ejecutó en el navegador? sí/no
- Contexto (HTML text / attr / JS):
EOF
# Ejemplo
curl -sG "localhost:3000/clientes" --data-urlencode "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings/002-xss-reflected.md
git commit -m "docs(m18): l15 poc xss reflected"''')}
"""),
)

BODIES[16] = body(
    "L16",
    "XSS almacenado y escape en plantillas/API",
    4,
    "El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.",
    f"Fix escape/sanitización; actualizar finding; filas SQLi+XSS en `{P}/findings-table.md`.",
    step(1, "Stored en notas de cita (50–60 min)", f"""
{bash('''# Crea cita con payload en notas (cuenta prueba)
curl -s -X POST localhost:3000/api/citas -H 'content-type: application/json' -b /tmp/m18-cj \\
  -d '{"clienteId":"…","inicio":"2026-01-02T10:00:00Z","notas":"<img src=x onerror=alert(1)>"}'
# Lista y verifica escape en HTML''')}
""")
    + step(2, "Fix + test (60–80 min)", f"""
Usa textContent / escape del framework; evita `dangerouslySetInnerHTML` con input usuario.

{ts('''// API: devolver texto; el front escapa al render
// Test:
it("escapes stored XSS in notas", async () => {
  const payload = "<script>alert(1)</script>";
  await createCita({ notas: payload });
  const html = await renderListaCitas();
  expect(html).not.toContain("<script>");
  expect(html).toContain("&lt;script&gt;") // o equivalente escapado
});''')}
""")
    + step(3, "Tabla P2 (20–30 min)", f"""
{bash(f'''cat > {P}/findings-table.md <<'EOF'
# Findings P2
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | | |
| 002 | A03/XSS | findings/002-xss-reflected.md | | |
EOF
git add -A && git commit -m "fix(m18): l16 xss stored escape"''')}
"""),
)

BODIES[17] = body(
    "L17",
    "IDOR en citas y recursos por ID",
    5,
    "Ocultar botones no basta: autorización server-side.",
    f"PoC cross-user en `{P}/findings/003-idor.md` con dos cuentas de prueba.",
    step(1, "Dos usuarios de prueba (20–30 min)", f"""
{bash('''# Login A y B; guarda cookies separadas
curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \\
  -d '{"email":"a@test.local","password":"***"}' -o /dev/null
curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \\
  -d '{"email":"b@test.local","password":"***"}' -o /dev/null''')}
""")
    + step(2, "PoC IDOR (60–80 min)", f"""
A crea cita → B intenta `GET/PUT /api/citas/:id`.

{bash(f'''CITA_ID=…  # id creado por A
curl -s -o /dev/null -w "%{{http_code}}\\n" -b /tmp/m18-b localhost:3000/api/citas/$CITA_ID
# esperado tras fix: 403 o 404 (no 200 con datos de A)

cat > {P}/findings/003-idor.md <<'EOF'
# Finding 003 — IDOR
- Ruta: GET/PUT /api/citas/:id
- Pasos:
- Impacto:
- Estado:
EOF''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings/003-idor.md
git commit -m "docs(m18): l17 poc idor"''')}
"""),
)

BODIES[18] = body(
    "L18",
    "Autorización por rol owner vs staff",
    5,
    "Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.",
    f"Matriz rol×recurso×acción en `{P}/docs/rbac-matrix.md` + ≥1 prueba manual de gap.",
    step(1, "Matriz RBAC (50–60 min)", f"""
{bash(f'''cat > {P}/docs/rbac-matrix.md <<'EOF'
# RBAC — Agenda Ops
| Recurso / acción | Owner | Staff | Anónimo |
|------------------|-------|-------|---------|
| Listar citas | ✓ | ✓ (alcance) | ✗ |
| Crear cita | ✓ | ✓ | ✗ |
| Borrar cualquier cita | ✓ | ? | ✗ |
| Configuración negocio | ✓ | ✗ | ✗ |
| Gestionar usuarios | ✓ | ✗ | ✗ |

## Gaps código vs SRS
- …
## Prueba manual
- Actor: staff · Acción: … · Resultado HTTP: …
EOF''')}
""")
    + step(2, "Prueba staff vs owner (50–70 min)", f"""
{bash('''curl -s -o /dev/null -w "%{http_code}\\n" -b /tmp/m18-staff \\
  -X PATCH localhost:3000/api/settings -H 'content-type: application/json' -d '{"tz":"UTC"}'
# esperado: 403''')}

{ts('''// guard ilustrativo
if (req.user.role !== "owner") return res.status(403).json({ error: "forbidden" });''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/rbac-matrix.md
git commit -m "docs(m18): l18 rbac matrix"''')}
"""),
)

BODIES[19] = body(
    "L19",
    "Rate limiting en login y endpoints sensibles",
    5,
    "Sin rate limit, A07 y DoS ligero son triviales.",
    "Límite en login (+1 endpoint costoso); prueba 429 documentada; nota en findings.",
    step(1, "Middleware o proxy (60–80 min)", f"""
{ts('''import rateLimit from "express-rate-limit";

export const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "too_many_requests" },
});

// app.post("/auth/login", loginLimiter, loginHandler);''')}
""")
    + step(2, "Prueba de bloqueo (40–50 min)", f"""
{bash(f'''for i in $(seq 1 25); do
  curl -s -o /dev/null -w "$i:%{{http_code}}\\n" -X POST localhost:3000/auth/login \\
    -H 'content-type: application/json' \\
    -d '{{"email":"owner@test.local","password":"wrong"}}'
done | tail -5
# espera ver 429

printf "\\n## Rate limit login\\n- window: 15m · max: 20\\n- prueba: ver 429 tras N intentos\\n- reset dev: reiniciar proceso / redis FLUSH\\n" >> {P}/findings-table.md''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash('''git add -A && git commit -m "fix(m18): l19 rate limit login"''')}
"""),
)

BODIES[20] = body(
    "L20",
    "Tests automatizados cross-user (P2 avance)",
    5,
    "P2 pide hallazgo→fix→test; hoy consolidas access control.",
    f"≥2 tests authz (cross-user + rol) + `{P}/findings-table.md` con ≥3 filas.",
    step(1, "Fixture dos usuarios (30–40 min)", f"""
{ts('''// tests/security/authz-cross-user.test.ts
async function login(email: string) { /* cookie jar / token */ }

it("B cannot read A's cita", async () => {
  const a = await login("a@test.local");
  const b = await login("b@test.local");
  const cita = await a.post("/api/citas", { /* … */ });
  const res = await b.get(`/api/citas/${cita.id}`);
  expect([403, 404]).toContain(res.status);
});

it("staff cannot patch settings", async () => {
  const staff = await login("staff@test.local");
  const res = await staff.patch("/api/settings", { tz: "UTC" });
  expect(res.status).toBe(403);
});''')}
""")
    + step(2, "Corre tests + actualiza tabla (60–80 min)", f"""
{bash(f'''npm test -- --testPathPattern=authz || npm test -- security
# Actualiza findings-table: 001–003 + rate limit
rg -n '^\\|' {P}/findings-table.md''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash('''git add -A && git commit -m "test(m18): l20 authz cross-user"''')}
"""),
)

BODIES[21] = body(
    "L21",
    "SSRF: superficie en webhooks e integraciones",
    6,
    "Aun sin feature URL, documentar el control evita sorpresas en M26.",
    f"Doc SSRF + allowlist en `{P}/findings/004-ssrf.md`. Sin escanear terceros ni metadata cloud en prod.",
    step(1, "Busca fetch server-side (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'fetch\\(|axios\\.|got\\(|request\\(|http\\.get' -g '!node_modules' | head -40''')}
""")
    + step(2, "Diseño / PoC aislada (70–90 min)", f"""
Si no hay feature: simula diseño. Si hay: prueba URL interna **solo en staging aislado**.

{bash(f'''cat > {P}/findings/004-ssrf.md <<'EOF'
# Finding 004 — SSRF (superficie)
## ¿Hay URL server-side hoy?
- webhook / import / avatar: sí/no · ruta:

## Riesgo ilustrativo
`http://169.254.169.254/` (metadata) — **no probar en cloud compartido**

## Allowlist propuesta
- hosts: `hooks.stripe.com`, …
- schemata: https only
- bloqueo: link-local, RFC1918, localhost

## Estado
- N/A feature | Mitigado | Abierto
EOF''')}

{ts('''function assertSafeUrl(raw: string) {
  const u = new URL(raw);
  if (u.protocol !== "https:") throw new Error("scheme");
  const allow = new Set(["hooks.example.com"]);
  if (!allow.has(u.hostname)) throw new Error("host");
}''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings/004-ssrf.md
git commit -m "docs(m18): l21 ssrf superficie"''')}
"""),
)

BODIES[22] = body(
    "L22",
    "Subida de archivos segura",
    6,
    "Un .php disfrazado de .jpg es folklore porque sigue pasando.",
    f"Checklist o prueba real en `{P}/findings/005-upload.md`: tipo/tamaño, nombre aleatorio, fuera de webroot.",
    step(1, "Superficie upload (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'multer|formidable|multipart|upload|createWriteStream' -g '!node_modules' | head -30''')}
""")
    + step(2, "Checklist / prueba (70–90 min)", f"""
{bash(f'''cat > {P}/findings/005-upload.md <<'EOF'
# Finding 005 — Upload
## ¿Hay upload hoy?
- ruta / campo:

## Controles
| Control | Sí/No |
|---------|-------|
| Allowlist MIME + magic bytes | |
| Tamaño máximo | |
| Nombre aleatorio (uuid) | |
| Fuera de `public/` / webroot | |
| No ejecutable por el server | |

## Prueba (si aplica)
- archivo: `pocs/evil.jpg.html` o similar
- resultado:
EOF''')}

{ts('''// multer sketch
const upload = multer({
  storage: multer.diskStorage({
    destination: "/var/agenda/uploads", // fuera de public
    filename: (_req, _file, cb) => cb(null, `${crypto.randomUUID()}`),
  }),
  limits: { fileSize: 2_000_000 },
  fileFilter: (_req, file, cb) => {
    cb(null, ["image/png", "image/jpeg"].includes(file.mimetype));
  },
});''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings/005-upload.md
git commit -m "docs(m18): l22 upload checklist"''')}
"""),
)

BODIES[23] = body(
    "L23",
    "Deserialización y JSON peligroso",
    6,
    "Node rara vez hace Java deserialization, pero prototype pollution y lógica sí.",
    f"`{P}/docs/json-trust.md`: endpoints + schema; límite de body; ≥1 mejora commitada.",
    step(1, "Inventario JSON bodies (40–50 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "express\\.json|bodyParser|z\\.object|Joi\\.|safeParse" -g '!node_modules' | head -40
cat > {P}/docs/json-trust.md <<'EOF'
# JSON trust
| Endpoint | Schema (zod/joi/…) | Límite body | Notas |
|----------|--------------------|-------------|-------|
| POST /auth/login | | | |
| POST /api/citas | | | |
EOF''')}
""")
    + step(2, "Límite + rechazo campos extra (60–80 min)", f"""
{ts('''app.use(express.json({ limit: "100kb" }));

// zod: strip o strict
const CitaInput = z.object({
  clienteId: z.string().uuid(),
  inicio: z.string().datetime(),
  notas: z.string().max(2000).optional(),
}).strict();''')}

{bash('''# Payload enorme → 413
python3 - <<'PY'
print('{"x":"' + ('a'*200000) + '"}')
PY | curl -s -o /dev/null -w "%{http_code}\\n" -X POST localhost:3000/api/citas \\
  -H 'content-type: application/json' -b /tmp/m18-cj --data-binary @-''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/json-trust.md
git commit -m "fix(m18): l23 json trust limits"''')}
"""),
)

BODIES[24] = body(
    "L24",
    "Consolidar hallazgos semana 6 en P2",
    6,
    "Mitad del módulo: P2 debe ser visible en git (≥5 hallazgos).",
    f"`{P}/findings-table.md` con ≥5 filas PoC→fix→test (o plan fechado); sin secretos.",
    step(1, "Auditoría de la tabla (40–50 min)", f"""
{bash(f'''wc -l {P}/findings/*.md
cat {P}/findings-table.md
# Completa hasta ≥5 filas (001–005 + rate limit / headers si aplica)''')}
""")
    + step(2, "Cierra gaps (80–100 min)", f"""
Cada fila: ID, OWASP, PoC, commit fix, test/link. Issues para abiertos con fecha semana 7–8.

{md('''| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | abc123 | security/sqli |
| 002 | XSS | findings/002-… | | |
| 003 | A01 | findings/003-idor.md | | authz |
| 004 | SSRF | findings/004-ssrf.md | n/a diseño | |
| 005 | Upload | findings/005-upload.md | | |''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/findings-table.md
git commit -m "docs(m18): l24 findings table p2"''')}
"""),
)

BODIES[25] = body(
    "L25",
    "npm audit y cadena de dependencias",
    7,
    "A06: la cadena de deps es superficie. Hoy mides y remedias al menos un high/critical.",
    f"Salida de audit en `{P}/docs/npm-audit.md` (+ mirror `{P}/deps-audit.md` si quieres); ≥1 remediación o justificación.",
    step(1, "Corre audit (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
npm audit --omit=dev 2>/dev/null || npm audit
npm audit --json > /tmp/m18-audit.json || true
mkdir -p {P}/docs
cp /tmp/m18-audit.json {P}/docs/npm-audit.json 2>/dev/null || true''')}
""")
    + step(2, "Documenta + remedia (70–90 min)", f"""
{bash(f'''cat > {P}/docs/npm-audit.md <<'EOF'
# npm audit — Agenda Ops
Fecha:
High/Critical:
Acción (update / ignore justificado):
Commit:
EOF
# Remedia al menos 1
npm audit fix --omit=dev || true
npm ls --depth=0 | head''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/npm-audit.md
git commit -m "docs(m18): l25 npm audit"''')}
"""),
)

BODIES[26] = body(
    "L26",
    "Secretos, .env y rotación",
    7,
    "Secretos en git son incidentes. Inventario (sin valores) + plan de rotación.",
    f"`{P}/docs/rotacion-secretos.md`: inventario, dónde viven, pasos rotar session secret / DB URL.",
    step(1, "Busca secretos en historial (30–40 min)", f"""
{bash('''git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
git ls-files | rg -i '\\.env|credential|secret|\\.pem' || true
# gitleaks / trufflehog si los tienes instalados''')}
""")
    + step(2, "Inventario + rotación (70–90 min)", f"""
{bash(f'''cat > {P}/docs/rotacion-secretos.md <<'EOF'
# Secretos y rotación
| Secreto | Dónde (local/staging) | En git? | Rotar cómo |
|---------|----------------------|---------|------------|
| DATABASE_URL | .env / PaaS | no | … |
| SESSION_SECRET | .env | no | reiniciar sesiones |
| SMTP_KEY | … | | |

## Pasos rotar SESSION_SECRET (staging)
1. Generar nuevo valor
2. Deploy
3. Invalidar sesiones previas
4. Verificar login
EOF''')}

{bash('''# Genera candidato (no lo commits)
openssl rand -hex 32''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/rotacion-secretos.md
git status   # .env no debe aparecer
git commit -m "docs(m18): l26 rotacion secretos"''')}
"""),
)

BODIES[27] = body(
    "L27",
    "Cabeceras de seguridad con Helmet o equivalente",
    7,
    "Headers baratos reducen XSS clickjacking y MIME sniffing.",
    "Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.",
    step(1, "Baseline headers (20–30 min)", f"""
{bash(f'''curl -sI localhost:3000/ | tee {P}/pocs/headers-before.txt | rg -i 'x-|content-security|strict-transport|referrer|permissions'|| true''')}
""")
    + step(2, "Activa Helmet (60–80 min)", f"""
{ts('''import helmet from "helmet";
app.use(helmet({
  contentSecurityPolicy: false, // CSP en L28
  frameguard: { action: "deny" },
  noSniff: true,
  referrerPolicy: { policy: "no-referrer" },
}));''')}

{bash(f'''curl -sI localhost:3000/ | tee {P}/pocs/headers-after.txt
diff -u {P}/pocs/headers-before.txt {P}/pocs/headers-after.txt || true''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/pocs/headers-*.txt
git commit -m "fix(m18): l27 security headers"''')}
"""),
)

BODIES[28] = body(
    "L28",
    "CSP básica sin romper Agenda Ops",
    7,
    "CSP report-only primero: observas violaciones sin romper el panel.",
    f"Política en `{P}/docs/csp.md`; report-only en staging; anota violaciones.",
    step(1, "Inventaria fuentes (30–40 min)", f"""
{bash(f'''cd {APP} 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'cdn\\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g '*.jsx' | head -30
cat > {P}/docs/csp.md <<'EOF'
# CSP — Agenda Ops
## Fuentes externas
- …

## Política propuesta (report-only)
default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none';

## Violaciones observadas
- …
EOF''')}
""")
    + step(2, "Report-Only (60–80 min)", f"""
{ts('''app.use((_req, res, next) => {
  res.setHeader(
    "Content-Security-Policy-Report-Only",
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'",
  );
  next();
});''')}

{bash('''curl -sI localhost:3000/ | rg -i content-security-policy''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/docs/csp.md
git commit -m "docs(m18): l28 csp report-only"''')}
"""),
)

BODIES[29] = body(
    "L29",
    "Pipeline CI: lint, test, audit, anti-secretos",
    8,
    "P3: cada PR corre lint+test+audit (+ grep secretos).",
    f"Workflow documentado en `{P}/ci/ci-appsec.yml` (o enlace) + `{P}/ci/README.md` con run id.",
    step(1, "Scaffold workflow (40–50 min)", f"""
{bash(f'''mkdir -p {P}/ci
cat > {P}/ci/ci-appsec.yml <<'EOF'
# Copiar a .github/workflows/appsec.yml del repo producto
name: appsec
on: [pull_request, push]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: {{ node-version: "20" }}
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm audit --audit-level=high
      - name: anti-secrets
        run: |
          ! git ls-files | rg -i '\\.env$|id_rsa|\\.pem$'
EOF''')}
""")
    + step(2, "Ejecuta en branch de prueba (60–80 min)", f"""
Copia al repo producto, push, pega run id en `{P}/ci/README.md`.

{bash(f'''cat > {P}/ci/README.md <<'EOF'
# CI AppSec
- Workflow: .github/workflows/appsec.yml
- Run id / URL:
- Jobs: lint, test, audit, anti-secrets
EOF''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/ci
git commit -m "ci(m18): l29 pipeline p3"''')}
"""),
)

BODIES[30] = body(
    "L30",
    "Estructura del informe AppSec",
    8,
    "El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos, mitigaciones, residual.",
    f"Borrador `{P}/informe-appsec.md` enlazando PoCs y commits (sin PII de partner).",
    step(1, "Plantilla (25–35 min)", f"""
{bash(f'''cat > {P}/informe-appsec.md <<'EOF'
# Informe AppSec — Agenda Ops

## 1. Ejecutivo
- …

## 2. Alcance y supuestos
- Solo staging/local propio
- Fuera de alcance: …

## 3. Metodología
STRIDE + OWASP Top 10 + PoC en API propia

## 4. Hallazgos
Tabla → ver findings-table.md (severidad, estado)

## 5. Mitigaciones
Commits / PRs: …

## 6. Riesgo residual
Top 3 con dueño/fecha

## 7. Anexos
- threat-model-v1.md
- docs/auth-inventario.md
- ci/
EOF''')}
""")
    + step(2, "Redacción con enlaces (90–110 min)", f"""
Rellena §§1–6 con datos reales de tu P2/P3. Verifica que no hay secretos ni teléfonos reales.

{bash(f'''rg -n 'password|Bearer |postgresql://|@gmail' {P}/informe-appsec.md || echo "sin secretos obvios"''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash(f'''git add {P}/informe-appsec.md
git commit -m "docs(m18): l30 informe appsec"''')}
"""),
)

BODIES[31] = body(
    "L31",
    "Tests de regresión de seguridad (≥3)",
    8,
    "≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u equivalentes).",
    f"Suite documentada en `{P}/docs/security-tests.md`; CI los corre.",
    step(1, "Selecciona 3 (20–30 min)", f"""
{bash(f'''cat > {P}/docs/security-tests.md <<'EOF'
# Security regression tests
| # | Archivo | Protege |
|---|---------|---------|
| 1 | tests/security/authz-cross-user.test.ts | IDOR citas |
| 2 | tests/security/xss-escape.test.ts | stored XSS notas |
| 3 | tests/security/rbac-settings.test.ts | staff≠owner |
EOF''')}
""")
    + step(2, "Implementa / verde (100–120 min)", f"""
Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).

{bash('''npm test -- --testPathPattern=security
# Confirma que el workflow L29 incluye este pattern''')}
""")
    + step(3, "Commit (10 min)", f"""
{bash('''git add -A && git commit -m "test(m18): l31 regresion seguridad"''')}
"""),
)

BODIES[32] = body(
    "L32",
    "Cierre M18 — dominio y riesgo residual",
    8,
    "Riesgo residual explícito > “somos seguros”. Cierra P1–P3 y handoff a M19/M25.",
    f"`{P}/informe-appsec.md` final + README con residual top-3 y criterios de dominio.",
    step(1, "Auditoría de evidencias (40–50 min)", f"""
{bash(f'''ls -la {P} {P}/docs {P}/findings {P}/ci {P}/pocs
test -f {P}/threat-model-v1.md && echo P1=ok
wc -l {P}/findings-table.md
test -f {P}/ci/ci-appsec.yml && echo P3=ok
test -f {P}/docs/auth-inventario.md && echo auth=ok''')}
""")
    + step(2, "Residual + handoff (50–60 min)", f"""
{bash(f'''printf "\\n## Riesgo residual (cierre)\\n| Riesgo | Dueño | Fecha revisión |\\n|--------|-------|----------------|\\n| … | | |\\n\\n## Handoff\\n- M19: secrets en PaaS, HTTPS, backups\\n- M25: retest en trial\\n" >> {P}/informe-appsec.md''')}
""")
    + step(3, "README final (20–30 min)", f"""
Actualiza `{P}/README.md`: P1/P2/P3 ✅, enlace informe, residual.

{bash(f'''git add {P}/README.md {P}/informe-appsec.md
git commit -m "docs(m18): l32 cierre dominio residual"''')}
"""),
)


assert len(BODIES) == 32, len(BODIES)
assert all("```" in BODIES[i] for i in range(1, 33)), "every body needs a fence"


def patch_raw_auth() -> None:
    """Unify auth-inventory → docs/auth-inventario.md in RAW specs."""
    path = ROOT / "scripts/_m17_m20/m18_lessons.py"
    text = path.read_text(encoding="utf-8")
    text2 = text.replace(
        "projects/m18-appsec/auth-inventory.md",
        "projects/m18-appsec/docs/auth-inventario.md",
    )
    # Also align ADR / hashing / other docs mentioned in README under docs/
    replacements = {
        "projects/m18-appsec/auth-hashing.md": "projects/m18-appsec/docs/auth-hashing.md",
        "projects/m18-appsec/adr-sesion-vs-jwt.md": "projects/m18-appsec/docs/adr-sesion-vs-jwt.md",
        "projects/m18-appsec/session-lifecycle.md": "projects/m18-appsec/docs/session-lifecycle.md",
        "projects/m18-appsec/checklist-cookies-csrf.md": "projects/m18-appsec/docs/checklist-cookies-csrf.md",
        "projects/m18-appsec/rbac-matrix.md": "projects/m18-appsec/docs/rbac-matrix.md",
        "projects/m18-appsec/deps-audit.md": "projects/m18-appsec/docs/npm-audit.md",
        "projects/m18-appsec/secrets-rotation.md": "projects/m18-appsec/docs/rotacion-secretos.md",
        "projects/m18-appsec/json-trust.md": "projects/m18-appsec/docs/json-trust.md",
        "projects/m18-appsec/csp.md": "projects/m18-appsec/docs/csp.md",
        "projects/m18-appsec/csrf-notes.md": "projects/m18-appsec/pocs/csrf-notes.md",
        "projects/m18-appsec/cookies-lab.md": "projects/m18-appsec/pocs/cookies.md",
    }
    for a, b in replacements.items():
        text2 = text2.replace(a, b)
    if text2 != text:
        path.write_text(text2, encoding="utf-8")
        print("patched RAW paths in m18_lessons.py")
    else:
        print("RAW paths already patched or patterns missing")


def replace_bodies_in_source() -> None:
    """Replace BODIES dict assignments in m18_lessons.py with polished ones."""
    path = ROOT / "scripts/_m17_m20/m18_lessons.py"
    text = path.read_text(encoding="utf-8")
    marker = "BODIES: dict[int, str] = {}"
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("BODIES marker not found")
    # Keep everything before BODIES; append new BODIES block
    head = text[:idx]
    parts = [head, marker, ""]
    for i in range(1, 33):
        # Use repr of raw string carefully — store as triple-quoted raw
        content = BODIES[i]
        parts.append(f"BODIES[{i}] = r\"\"\"\n{content}\n\"\"\"\n")
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("wrote polished BODIES to m18_lessons.py")


def seed_scaffolds() -> None:
    base = ROOT / P
    (base / "docs").mkdir(parents=True, exist_ok=True)
    (base / "pocs").mkdir(parents=True, exist_ok=True)
    (base / "findings").mkdir(parents=True, exist_ok=True)
    (base / "fixes").mkdir(parents=True, exist_ok=True)
    (base / "tests").mkdir(parents=True, exist_ok=True)
    (base / "ci").mkdir(parents=True, exist_ok=True)

    templates = {
        "docs/auth-inventario.md": """# Inventario de autenticación — Agenda Ops

## Endpoints
| Método | Ruta | Público | Notas |
|--------|------|---------|-------|
| POST | /auth/login | sí | |
| POST | /auth/logout | auth | |

## Transporte / almacenamiento
- Cookie / Bearer: (completa en L05)

## Edge cases
1. Password malo →
2. Usuario inexistente →
""",
        "docs/checklist-cookies-csrf.md": """# Checklist cookies / CSRF — staging

Fecha: · URL:

| # | Ítem | Sí/No | Nota |
|---|------|-------|------|
| 1 | Cookie sesión HttpOnly | | |
| 2 | Secure en HTTPS | | |
| 3 | SameSite Lax/Strict | | |
| 4 | Session id rota post-login | | |
| 5 | Logout invalida server-side | | |
| 6 | POST citas exige CSRF/equiv | | |
| 7 | GET no muta estado | | |
| 8 | Mensajes login genéricos | | |
| 9 | HTTPS redirect (si aplica) | | |
| 10 | Sin cookie sesión en document.cookie | | |
""",
        "docs/rotacion-secretos.md": """# Secretos y rotación

| Secreto | Dónde | En git? | Rotar cómo |
|---------|-------|---------|------------|
| DATABASE_URL | | no | |
| SESSION_SECRET | | no | |
""",
        "docs/npm-audit.md": """# npm audit — Agenda Ops

Fecha:
High/Critical:
Acción:
Commit:
""",
        "docs/auth-hashing.md": """# Password hashing

- Algoritmo:
- Parámetros (cost/rounds):
- Commit:
""",
        "docs/adr-sesion-vs-jwt.md": """# ADR — Sesión server-side vs JWT

## Contexto

## Decisión

## Consecuencias
""",
        "findings-table.md": """# Findings P2

| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | | |
""",
        "ci/README.md": """# CI AppSec

- Workflow: (enlace o `ci-appsec.yml`)
- Run id:
""",
    }
    for rel, content in templates.items():
        path = base / rel
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            print("seeded", path.relative_to(ROOT))

    readme = base / "README.md"
    text = readme.read_text(encoding="utf-8")
    # Ensure Spanish auth-inventario and no English auth-inventory
    if "auth-inventory" in text:
        text = text.replace("auth-inventory.md", "auth-inventario.md")
        readme.write_text(text, encoding="utf-8")
        print("README auth path unified")
    # Expand tree note if deps-audit naming
    if "npm-audit.md" not in text:
        pass
    print("scaffolds ready")


def trim_hecho_to_three() -> None:
    """Keep 2 content checks so builder adds commit → exactly 3 Hecho cuando items.

    Operates on parsed RAW JSON (not regex on the key name) to avoid corrupting items.
    """
    path = ROOT / "scripts/_m17_m20/m18_lessons.py"
    text = path.read_text(encoding="utf-8")
    m = re.search(r"RAW = json.loads\(r\"\"\"\n(.*)\n\"\"\"\)", text, re.S)
    if not m:
        raise SystemExit("RAW block not found")
    import json

    raw = json.loads(m.group(1))
    for spec in raw:
        items = [h for h in spec["hecho"] if "commit" not in h.lower()]
        spec["hecho"] = items[:2] if len(items) >= 2 else spec["hecho"][:2]
    new_json = json.dumps(raw, ensure_ascii=False, indent=2)
    assert '"""' not in new_json
    start, end = m.start(1), m.end(1)
    path.write_text(text[:start] + new_json + text[end:], encoding="utf-8")
    print("trimmed RAW hecho lists to 2 content checks (+ commit)")


def verify() -> dict:
    out = ROOT / "curriculum/etapas/02-disciplinaria/M18"
    files = sorted(out.glob("L*.md"))
    with_fence = [f for f in files if "```" in f.read_text(encoding="utf-8")]
    lee = [f for f in files if "Lee la sección" in f.read_text(encoding="utf-8")]
    auth_inv = []
    auth_en = []
    for f in files:
        t = f.read_text(encoding="utf-8")
        if "auth-inventario" in t:
            auth_inv.append(f.name)
        if "auth-inventory" in t:
            auth_en.append(f.name)
    return {
        "lessons": len(files),
        "with_fence": len(with_fence),
        "lee_la_seccion": len(lee),
        "auth_inventario_files": auth_inv,
        "auth_inventory_english_files": auth_en,
    }


def main() -> None:
    patch_raw_auth()
    replace_bodies_in_source()
    trim_hecho_to_three()
    seed_scaffolds()

    import importlib
    import _m17_m20.m18_lessons as m18

    importlib.reload(m18)
    from _m17_m20.builder import write_module

    write_module(
        materia="M18",
        out_rel="curriculum/etapas/02-disciplinaria/M18",
        filenames=m18.FILENAMES,
        raw_lessons=m18.RAW,
        fuente="OWASP Top 10 + Cheat Sheets",
        biblio="../../../bibliografia.md#m18-seguridad-appsec",
        biblio_label="Bibliografía · M18",
        default_enlace_titulo="OWASP Top 10",
        default_enlace="https://owasp.org/www-project-top-ten/",
        proj="projects/m18-appsec",
        final_siguiente="Materia siguiente / refuerzo: [M19 — Nube/DevOps](../M19-nube-devops.md) y [hilo seguridad](../../../hilos/seguridad.md).",
        body_overrides=m18.BODIES,
    )
    stats = verify()
    print("VERIFY", stats)
    if stats["with_fence"] < 28:
        raise SystemExit(f"fence count too low: {stats['with_fence']}")
    if stats["lee_la_seccion"]:
        raise SystemExit("found Lee la sección")
    if stats["auth_inventory_english_files"]:
        raise SystemExit(
            f"english auth-inventory still present: {stats['auth_inventory_english_files']}"
        )
    print("OK")


if __name__ == "__main__":
    main()
