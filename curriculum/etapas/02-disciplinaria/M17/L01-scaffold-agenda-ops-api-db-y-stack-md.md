---
id: L01
materia: M17
orden: 1
titulo: Scaffold Agenda Ops — API, DB y stack
horas: 5.0
semana: 1
lectura: producto-saas.md + m13-diseno + M09 esquema
evidencia: projects/m17-agenda-ops/stack.md + scaffold API
---

# L01 — Scaffold Agenda Ops — API, DB y stack

**~5.0 h · Semana 1**

Cambiar stack a mitad de materia sin ADR destruye velocidad.

## Objetivo

Inicializar `projects/m17-agenda-ops/` con TypeScript strict, conexión Postgres y documentar stack fijo.

## Conceptos clave

- scaffold
- Postgres
- monolito modular

## Pasos (hazlos en orden)

### 1. Revisa producto y diseño previo (30–40 min)

```bash
cd /workspace   # o raíz del monorepo academia
head -n 80 curriculum/producto-saas.md
ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null | head
```

Anota 5 endpoints Must del piloto: register, login, me, citas, clientes/servicios.

### 2. Scaffold de carpetas y toolchain (40–50 min)

```bash
mkdir -p projects/m17-agenda-ops/{docs,src,tests,scripts,apps}
cd projects/m17-agenda-ops
# Si aún no hay package.json:
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

Confirma `strict: true` en `tsconfig.json`. Runtime Node LTS + framework HTTP alineado a M13 ADR 001.

### 3. Documenta stack.md inmutable (30–40 min)

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

### 4. Postgres + GET /health (60–80 min)

```bash
cp projects/m17-agenda-ops/.env.example projects/m17-agenda-ops/.env
# Edita DATABASE_URL / POSTGRES_* — .env NO va a git
# Reusa Compose M09 o el tuyo; luego arranca la API
curl -sS http://localhost:3000/health
# Esperado JSON tipo {"ok":true,"db":"up"}
```

Si falla DB, anota el error en README **sin** password.

### 5. Commit (10–15 min)

```bash
git add projects/m17-agenda-ops
git status   # .env NO debe aparecer
git commit -m "docs(m17): L01 scaffold stack health postgres"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas.md + m13-diseno + M09 esquema | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/` con TypeScript strict y carpetas `src/`/`tests/`/`docs/`.
2. `projects/m17-agenda-ops/stack.md` lista runtime, API, ORM, front, tests y auth.
3. `GET /health` responde 200 con DB up (anotado en README sin secrets).
4. Commit `docs(m17): L01 scaffold-agenda-ops-api-db-y-stack`.

## Errores comunes

- Subir `.env` con passwords.
- Cambiar framework sin ADR.
- Health 200 sin ping a DB documentado.

## Siguiente

[L02 — Registro con hash de contraseña](L02-registro-con-hash-de-contrasena.md)
