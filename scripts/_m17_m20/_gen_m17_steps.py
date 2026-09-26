"""Generated step labs for M17 polish — do not edit by hand lightly."""
STEPS: dict[int, list[tuple[str, str]]] = {}
STEPS[1] = [
    ('Revisa producto y diseño previo (30–40 min)', r"""
```bash
cd /workspace   # o raíz del monorepo academia
head -n 80 curriculum/producto-saas.md
ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null | head
```

Anota 5 endpoints Must del piloto: register, login, me, citas, clientes/servicios.
"""),
    ('Scaffold de carpetas y toolchain (40–50 min)', r"""
```bash
mkdir -p projects/m17-agenda-ops/{docs,src,tests,scripts,apps}
cd projects/m17-agenda-ops
# Si aún no hay package.json:
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

Confirma `strict: true` en `tsconfig.json`. Runtime Node LTS + framework HTTP alineado a M13 ADR 001.
"""),
    ('Documenta stack.md inmutable (30–40 min)', r"""
Completa `projects/m17-agenda-ops/stack.md` (ya hay plantilla). Ejemplo mínimo:

```md
| Capa | Elección | Notas |
|------|----------|-------|
| Runtime | Node 22 LTS | |
| API | Fastify / Express / Nest | TypeScript strict |
| ORM | drizzle / prisma / knex | esquema M09 |
| Front | React / Next | |
| Tests | Vitest | |
| Auth | Cookie HttpOnly | docs/auth.md |
```

Cambio de stack = ADR en `docs/`.
"""),
    ('Postgres + GET /health (60–80 min)', r"""
```bash
cp projects/m17-agenda-ops/.env.example projects/m17-agenda-ops/.env
# Edita DATABASE_URL / POSTGRES_* — .env NO va a git
# Reusa Compose M09 o el tuyo; luego arranca la API
curl -sS http://localhost:3000/health
# Esperado JSON tipo {"ok":true,"db":"up"}
```

Si falla DB, anota el error en README **sin** password.
"""),
    ('Commit (10–15 min)', r"""
```bash
git add projects/m17-agenda-ops
git status   # .env NO debe aparecer
git commit -m "docs(m17): L01 scaffold stack health postgres"
```
"""),
]
STEPS[2] = [
    ('Lectura OWASP Password Storage (25–35 min)', r"""
Abre la Cheat Sheet (enlace en la tabla). Anota en `docs/auth.md`: algoritmo (bcrypt/argon2), cost factor, y “nunca MD5/SHA solo”.
"""),
    ('Migración usuarios (30–40 min)', r"""
```sql
-- migrations/00x_usuarios.sql (adapta a tu ORM)
CREATE TABLE usuarios (
  id UUID PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  rol TEXT NOT NULL CHECK (rol IN ('owner','staff')),
  negocio_id UUID NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

```bash
# aplica con tu runner, ej.:
npm run migrate
# o: psql "$DATABASE_URL" -f migrations/00x_usuarios.sql
```
"""),
    ('POST /auth/register (70–90 min)', r"""
Valida body (Zod/valibot): email, password ≥8. Hash con bcrypt/argon2. Respuesta **201** sin el hash.

```bash
curl -sS -X POST http://localhost:3000/auth/register \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"Secreto123!"}'
# 201 + id/email/rol — nunca password_hash
curl -sS -X POST http://localhost:3000/auth/register \
  -H 'content-type: application/json' \
  -d '{"email":"malo","password":"x"}'
# 400
```
"""),
    ('Tests + commit (40–50 min)', r"""
```bash
npm test -- auth
git add projects/m17-agenda-ops
git commit -m "feat(m17): L02 register con hash"
```

Casos mínimos: 201 feliz; 400 email inválido; hash ≠ plaintext en DB.
"""),
]
STEPS[3] = [
    ('Decide sesión vs JWT-cookie (20–30 min)', r"""
```bash
mkdir -p projects/m17-agenda-ops/docs
cat > projects/m17-agenda-ops/docs/auth.md << 'EOF'
# Auth Agenda Ops
- Mecanismo: cookie HttpOnly (preferido) / JWT-en-cookie
- Secure / SameSite: ...
- Riesgos XSS/CSRF y mitigación
EOF
```
"""),
    ('Implementa login + GET /me (80–100 min)', r"""
Login verifica hash; setea cookie. `GET /me` → id, email, rol (sin hash).

```bash
curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"Secreto123!"}'
curl -sS -b /tmp/ao.ck http://localhost:3000/me
curl -sS -o /tmp/me.out -w "%{http_code}" http://localhost:3000/me
# sin cookie → 401
```
"""),
    ('Tests 401/200 + commit (40–50 min)', r"""
```bash
npm test -- auth
git add projects/m17-agenda-ops/docs/auth.md projects/m17-agenda-ops
git commit -m "feat(m17): L03 login sesion y me"
```
"""),
]
STEPS[4] = [
    ('Consolida suite auth (80–100 min)', r"""
En `projects/m17-agenda-ops/tests/auth.test.ts` (o equivalente) cubre: register, login, me, logout, 401, password malo. Mínimo **6** tests.

```ts
// esqueleto
it("login → me 200", async () => { /* ... */ });
it("me sin cookie → 401", async () => { /* ... */ });
it("logout invalida sesión", async () => { /* ... */ });
```
"""),
    ('Documenta comando en README (20–30 min)', r"""
```bash
npm test
# anota en README la línea exacta que deja P1 verde
```

Marca P1 parcial en el checklist del README de `projects/m17-agenda-ops/`.
"""),
    ('Commit cierre semana 1 (15 min)', r"""
```bash
git add projects/m17-agenda-ops
git commit -m "test(m17): L04 suite auth P1 semana 1"
```
"""),
]
STEPS[5] = [
    ('Cruza M13 + M09 (25–35 min)', r"""
```bash
ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations
rg -n "cita|cliente|servicio" projects/m13-diseno projects/m12-srs 2>/dev/null | head
```
"""),
    ('Migraciones dominio (70–90 min)', r"""
Asegura tablas `clientes`, `servicios`, `citas` con FKs (negocio/usuario según diseño).

```bash
npm run migrate
# o psql "$DATABASE_URL" -c '\dt'
```

Evidencia: listado de tablas en nota breve en `docs/` o salida en README (sin datos reales).
"""),
    ('Reglas en domain/ (50–60 min)', r"""
```ts
// src/domain/cita-rules.ts — puro, sin ORM
export function assertHorario(inicio: Date, fin: Date) {
  if (!(fin > inicio)) throw new Error("fin_debe_ser_despues_de_inicio");
}
```

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L05 modelo dominio citas clientes servicios"
```
"""),
]
STEPS[6] = [
    ('POST /citas autenticado (70–90 min)', r"""
```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/citas \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T15:00:00Z","fin":"2026-10-01T15:30:00Z"}'
# 201
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/citas \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T16:00:00Z","fin":"2026-10-01T15:00:00Z"}'
# 400 horario
```
"""),
    ('GET /citas + reglas (50–60 min)', r"""
Listar con filtro fecha; 401 sin auth; 409 si documentas solapamiento.

```bash
curl -sS -b /tmp/ao.ck "http://localhost:3000/citas?desde=2026-10-01&hasta=2026-10-02"
curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/citas
# 401
```
"""),
    ('Tests + commit (40 min)', r"""
```bash
npm test -- citas
git add projects/m17-agenda-ops
git commit -m "feat(m17): L06 api citas crear y listar"
```
"""),
]
STEPS[7] = [
    ('CRUD clientes (50–60 min)', r"""
```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/clientes \
  -H 'content-type: application/json' \
  -d '{"nombre":"Ana Demo","telefono":"+525500000000"}'
curl -sS -b /tmp/ao.ck http://localhost:3000/clientes
```
"""),
    ('CRUD servicios (50–60 min)', r"""
```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/servicios \
  -H 'content-type: application/json' \
  -d '{"nombre":"Corte","duracionMin":30,"precioCentavos":25000}'
curl -sS -b /tmp/ao.ck http://localhost:3000/servicios
```

PATCH/DELETE según matriz (staff no borra si owner-only).
"""),
    ('Tests + commit (40 min)', r"""
```bash
npm test -- clientes servicios
git add projects/m17-agenda-ops
git commit -m "feat(m17): L07 crud clientes y servicios"
```
"""),
]
STEPS[8] = [
    ('Script seed reproducible (70–90 min)', r"""
```ts
// projects/m17-agenda-ops/scripts/seed.ts
// owner demo + 2 staff + 5 clientes + 3 servicios + citas fake
// SOLO datos sintéticos — sin PII real del design partner
```

```bash
npx tsx scripts/seed.ts
# o: npm run seed
```
"""),
    ('Documenta en README (20 min)', r"""
```bash
rg -n "seed" projects/m17-agenda-ops/README.md || echo "añade sección Seed"
```

Incluye emails demo y password **solo** en `.env.example` como placeholders, no secretos de staging.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/scripts/seed.ts projects/m17-agenda-ops/README.md
git commit -m "feat(m17): L08 seeds demo design partner"
```
"""),
]
STEPS[9] = [
    ('Redacta matriz owner/staff (60–80 min)', r"""
```bash
mkdir -p projects/m17-agenda-ops/docs
```

Crea `projects/m17-agenda-ops/docs/permisos.md`:

```md
| Acción | owner | staff |
|--------|-------|-------|
| CRUD citas propias negocio | sí | sí |
| Borrar servicio | sí | no |
| Invitar staff | sí | no |
| Ver panel /admin | sí | no |
```
"""),
    ('Cruza con rutas API (40 min)', r"""
```bash
rg -n "router\\.(get|post|patch|delete)|app\\.(get|post)" projects/m17-agenda-ops/src | head -40
```

Marca en la matriz qué ruta aplica cada fila.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/permisos.md
git commit -m "docs(m17): L09 matriz permisos owner staff"
```
"""),
]
STEPS[10] = [
    ('Middleware authorize (80–100 min)', r"""
```ts
// src/middleware/authorize.ts
export function authorize(...roles: Array<"owner"|"staff">) {
  return (req, res, next) => {
    const u = req.user; // inyectado por auth
    if (!u || !roles.includes(u.rol)) return res.status(403).json({ error: "forbidden" });
    next();
  };
}
```
"""),
    ('Aplica a rutas sensibles (40 min)', r"""
Ej.: `DELETE /servicios/:id` y `/admin/*` → `authorize("owner")`.

```bash
# staff cookie → 403 en acción owner
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" \
  -X DELETE http://localhost:3000/servicios/<id>
# 403
```
"""),
    ('Tests IDOR/403 + commit (40–50 min)', r"""
```bash
npm test -- authz
git add projects/m17-agenda-ops
git commit -m "feat(m17): L10 middleware autorizacion"
```
"""),
]
STEPS[11] = [
    ('Ruta /admin mínima (70–90 min)', r"""
UI o API: listar staff, invitar/desactivar. Solo owner.

```bash
curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" http://localhost:3000/admin/staff
# 403
```
"""),
    ('Evidencia + commit (40 min)', r"""
Anota URL/ruta en `docs/permisos.md` o captura redactada en `docs/`.

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L11 panel admin staff"
```
"""),
]
STEPS[12] = [
    ('Guion demo roles (50–60 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/demo-roles.md << 'EOF'
# Demo roles
1. Login owner → /admin OK
2. Login staff → /admin 403 / UI oculta
3. Ambos crean cita
EOF
```
"""),
    ('Ejecuta y anota (40–50 min)', r"""
```bash
npm run seed
# recorre el guion con dos sesiones/cookies
```
"""),
    ('Kickoff P3 WhatsApp (30 min) + commit', r"""
Crea borrador `docs/integracion-whatsapp.md` (enlace wa.me, sin API Business obligatoria).

```bash
git add projects/m17-agenda-ops/docs
git commit -m "docs(m17): L12 demo roles inicio whatsapp"
```
"""),
]
STEPS[13] = [
    ('Scaffold front (60–80 min)', r"""
```bash
mkdir -p projects/m17-agenda-ops/apps/web
# Vite/Next según stack.md — TypeScript
cd projects/m17-agenda-ops/apps/web && npm create vite@latest . -- --template react-ts
```

Documenta el comando real en `stack.md`.
"""),
    ('Rutas protegidas (60–80 min)', r"""
```ts
// ProtectedRoute: si !session → redirect /login
```

```bash
# sin cookie, /citas en browser → login
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/apps projects/m17-agenda-ops/stack.md
git commit -m "feat(m17): L13 scaffold front rutas protegidas"
```
"""),
]
STEPS[14] = [
    ('Página login (60–80 min)', r"""
Form email/password → `POST /auth/login` (credentials include). Maneja error 401 visible.
"""),
    ('Logout limpia sesión (40–50 min)', r"""
```bash
# DevTools → Application → Cookies: tras logout la cookie de sesión desaparece
```

Botón logout → `POST /auth/logout` + redirect `/login`.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/apps
git commit -m "feat(m17): L14 login logout UI"
```
"""),
]
STEPS[15] = [
    ('Estados de lista (70–90 min)', r"""
Loading skeleton/spinner; error con reintento; vacío con CTA “Crear cita”.
"""),
    ('Documenta ui-estados.md (30–40 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/ui-estados.md << 'EOF'
# UI estados (P2)
| Vista | loading | error | vacío |
|-------|---------|-------|-------|
| /citas | … | … | … |
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/ui-estados.md projects/m17-agenda-ops/apps
git commit -m "feat(m17): L15 listas loading error vacio"
```
"""),
]
STEPS[16] = [
    ('Forms accesibles (80–100 min)', r"""
Labels asociados, `aria-invalid`, mensajes de error ligados al campo. Crear cita + cliente.
"""),
    ('Verifica teclado (30 min)', r"""
```bash
# Tab order completo; Enter envía; error anunciado
# Anota checklist en docs/ui-estados.md
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L16 formularios citas clientes a11y"
```
"""),
]
STEPS[17] = [
    ('Diseña mensaje wa.me (50–60 min)', r"""
```bash
# plantilla (sin PII real en git):
# https://wa.me/52XXXXXXXXXX?text=Hola%20...%20cita%20...
```

Documenta en `projects/m17-agenda-ops/docs/integracion-whatsapp.md` campos: nombre, fecha, deep link ficha.
"""),
    ('Helper URL encoder (40–50 min)', r"""
```ts
export function whatsappReminderUrl(phoneE164: string, text: string) {
  const n = phoneE164.replace(/\\D/g, "");
  return `https://wa.me/${n}?text=${encodeURIComponent(text)}`;
}
```

```bash
npm test -- whatsapp
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops
git commit -m "docs(m17): L17 deep links whatsapp mensaje"
```
"""),
]
STEPS[18] = [
    ('Botón en ficha cita (70–90 min)', r"""
Acción “Enviar recordatorio” abre `wa.me` (window.open). No requiere WhatsApp Business API.
"""),
    ('Evidencia (30 min)', r"""
```bash
# captura redactada o nota en integracion-whatsapp.md con URL de ejemplo sin teléfono real
echo "ej: https://wa.me/525500000000?text=..." >> projects/m17-agenda-ops/docs/integracion-whatsapp.md
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L18 boton recordatorio whatsapp"
```
"""),
]
STEPS[19] = [
    ('Estados de cita (60–80 min)', r"""
```sql
-- enum o check: pendiente | confirmada | cancelada | atendida
ALTER TABLE citas ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
```

API PATCH `/citas/:id/estado` con authz.
"""),
    ('UI + tests (50–60 min)', r"""
```bash
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/citas/<id>/estado \
  -H 'content-type: application/json' \
  -d '{"estado":"confirmada"}'
npm test -- citas
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L19 confirmacion estados cita"
```
"""),
]
STEPS[20] = [
    ('Cierra doc P3 (50–60 min)', r"""
Completa `projects/m17-agenda-ops/docs/integracion-whatsapp.md`: flujo, límites (manual), riesgos PII en URL, captura demo.
"""),
    ('Checklist README (30 min)', r"""
```bash
rg -n "P3|WhatsApp" projects/m17-agenda-ops/README.md
```

Marca P3 si el botón + doc existen.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/integracion-whatsapp.md projects/m17-agenda-ops/README.md
git commit -m "docs(m17): L20 cierre P3 whatsapp"
```
"""),
]
STEPS[21] = [
    ('Inventaria vars (40–50 min)', r"""
```bash
cat projects/m17-agenda-ops/.env.example
rg -n "process\\.env|env\\." projects/m17-agenda-ops/src | head -40
```

Cada var en `.env.example` con comentario; **sin** valores secretos.
"""),
    ('Separa secrets de config (40 min)', r"""
```bash
# ejemplo .env.example
cat >> projects/m17-agenda-ops/.env.example << 'EOF'
# DATABASE_URL=postgresql://app:changeme@localhost:5432/agenda_ops
# SESSION_SECRET=change-me-min-32-chars
# CORS_ORIGIN=http://localhost:5173
EOF
```

Confirma `.env` en `.gitignore`.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/.env.example
git status | grep -i '\\.env$' && echo 'FAIL: .env tracked' || true
git commit -m "docs(m17): L21 env example secrets"
```
"""),
]
STEPS[22] = [
    ('Elige PaaS y despliega (90–120 min)', r"""
Fly/Render/Railway/etc. Build desde Dockerfile o buildpack. Secrets en el panel, no en git.

```bash
# ejemplo genérico — sustituye por CLI real
# fly launch / render blueprint / railway up
curl -sS https://TU-STAGING.example/health
```
"""),
    ('Documenta URL (30 min)', r"""
```bash
mkdir -p projects/m17-agenda-ops/docs
echo "Staging: https://TU-STAGING.example" > projects/m17-agenda-ops/docs/deploy.md
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/deploy.md
git commit -m "docs(m17): L22 deploy staging paas"
```
"""),
]
STEPS[23] = [
    ('Fuerza HTTPS (40–50 min)', r"""
```bash
curl -sSI https://TU-STAGING.example/health | head -20
# sin -k; certificado válido
curl -sS -o /dev/null -w "%{http_code}\n" http://TU-STAGING.example/health
# redirect 301/308 a https o rechazo
```
"""),
    ('Health externo (40 min)', r"""
```bash
curl -sS https://TU-STAGING.example/health
# pega JSON (sin secrets) en docs/deploy.md
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/deploy.md
git commit -m "docs(m17): L23 https y health checks"
```
"""),
]
STEPS[24] = [
    ('Smoke script (60–80 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/smoke-test.md << 'EOF'
# Smoke post-deploy
1. GET /health → 200
2. POST /auth/login (user demo staging)
3. POST /citas → 201
4. GET /citas → incluye la cita
Fecha: YYYY-MM-DD  Resultado: OK/FAIL
EOF
```

```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"FROM_SECRET_MANAGER"}'
```
"""),
    ('Registra resultado + commit (30 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/smoke-test.md
git commit -m "docs(m17): L24 smoke test post-deploy"
```
"""),
]
STEPS[25] = [
    ('Mapa OWASP Top 10 (80–100 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/owasp-mapa.md << 'EOF'
# OWASP Top 10 → Agenda Ops
| Riesgo | ¿Aplica? | Control en piloto | Gap |
|--------|----------|-------------------|-----|
| A01 Broken Access Control | sí | authorize()+tests 403 | |
| A02 Cryptographic Failures | sí | bcrypt + HTTPS | |
EOF
```

Cubre al menos A01–A05 con evidencia (ruta de test o doc).
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/owasp-mapa.md
git commit -m "docs(m17): L25 mapa owasp top10"
```
"""),
]
STEPS[26] = [
    ('Headers seguridad (60–80 min)', r"""
```ts
// helmet() o equivalentes: CSP básica, nosniff, frameguard
```

```bash
curl -sSI https://TU-STAGING.example/health | rg -i 'content-security|x-frame|x-content-type|strict-transport'
```
"""),
    ('CORS prod (40 min)', r"""
Allowlist `CORS_ORIGIN` de staging/prod — no `*`. Documenta en `docs/deploy.md`.

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L26 headers seguridad cors"
```
"""),
]
STEPS[27] = [
    ('Rate limit login (70–90 min)', r"""
```ts
// p.ej. 5 intentos / 15 min por IP+email en POST /auth/login → 429
```

```bash
for i in $(seq 1 8); do
  curl -sS -o /dev/null -w "%{http_code}\\n" -X POST http://localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@demo.local","password":"wrong"}'
done
# últimos → 429
```
"""),
    ('Tests + commit (40 min)', r"""
```bash
npm test -- rate-limit
git add projects/m17-agenda-ops
git commit -m "feat(m17): L27 rate limit login"
```
"""),
]
STEPS[28] = [
    ('CI o script reproducible (70–90 min)', r"""
```yaml
# .github/workflows/m17-auth.yml (si usas GH Actions)
name: m17-auth
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test -- auth
```

Alternativa local documentada:

```bash
# scripts/ci-auth.sh
set -euo pipefail
npm ci
npm test -- auth
```
"""),
    ('Evidencia + commit (30 min)', r"""
```bash
bash scripts/ci-auth.sh   # o mira el run verde en Actions
git add .github/workflows projects/m17-agenda-ops/scripts 2>/dev/null || true
git add projects/m17-agenda-ops
git commit -m "ci(m17): L28 tests auth reproducibles"
```
"""),
]
STEPS[29] = [
    ('ADR tenant_id (70–90 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/adr-tenant-id.md << 'EOF'
# ADR: tenant_id / multi-negocio
## Contexto
Piloto single-tenant hoy; camino a SaaS.
## Decisión
Columna/negocio_id nullable ahora; queries siempre filtradas cuando presente.
## Consecuencias
...
EOF
```
"""),
    ('Marca código futuro (30 min)', r"""
```ts
// TODO(tenant): filtrar por negocio_id en listados
```

```bash
git add projects/m17-agenda-ops/docs/adr-tenant-id.md
git commit -m "docs(m17): L29 adr tenant_id multi-negocio"
```
"""),
]
STEPS[30] = [
    ('Checklist SaaS (70–90 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/checklist-saas.md << 'EOF'
# Camino a SaaS
- [ ] Aislamiento tenant en queries
- [ ] Billing (out of scope piloto)
- [ ] Backups (→ M19)
- [ ] Observabilidad
- [ ] Onboarding self-serve
EOF
```

Marca hecho/gap con enlace a evidencia.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m17-agenda-ops/docs/checklist-saas.md
git commit -m "docs(m17): L30 checklist camino saas"
```
"""),
]
STEPS[31] = [
    ('Guion demo grabable (50–60 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/demo-script.md << 'EOF'
# Demo design partner (≤8 min)
1. Login owner
2. Crear cita
3. Recordatorio WhatsApp
4. Rol staff 403 admin
EOF
```
"""),
    ('Ensayo + nota (40–50 min)', r"""
Cronometra. Anota URL staging y usuario demo (password en gestor, no en git).

```bash
git add projects/m17-agenda-ops/docs/demo-script.md
git commit -m "docs(m17): L31 demo script design partner"
```
"""),
]
STEPS[32] = [
    ('Índice de evidencias (50–60 min)', r"""
```bash
cat > projects/m17-agenda-ops/docs/nota-cierre-m17.md << 'EOF'
# Cierre M17
## Artefactos
- stack.md, docs/auth.md, permisos.md, ui-estados.md
- integracion-whatsapp.md, deploy.md, smoke-test.md
- owasp-mapa.md, adr-tenant-id.md, checklist-saas.md
## Handoff M19
Dockerfile pendiente / Compose / secrets → projects/m19-ops/
EOF
ls projects/m17-agenda-ops/docs
```
"""),
    ('README proyecto + commit (40 min)', r"""
Actualiza checklist P1–P3 del README. Enlace a M19.

```bash
git add projects/m17-agenda-ops
git commit -m "docs(m17): L32 cierre evidencias handoff m19"
```
"""),
]
