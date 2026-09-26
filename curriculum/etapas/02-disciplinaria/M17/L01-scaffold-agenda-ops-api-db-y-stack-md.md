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

Sin stack fijo, M17 se convierte en un tour de frameworks. Hoy clavas el monolito modular del piloto.

## Objetivo

Dejar `projects/m17-agenda-ops/` con TypeScript strict, Postgres conectado y `stack.md` inmutable (salvo ADR).

## Por qué empieza así

Cada lección siguiente asume `GET /health` 200 y un esquema alineado a M09 (clientes, servicios, citas).

## Pasos (hazlos en orden)

### 1. Revisa producto y diseño previo (30–40 min)

```bash
cat curriculum/producto-saas.md | head -80
ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null | head
```

Anota en un scratch: endpoints Must del piloto (auth, citas, clientes, servicios, admin).

### 2. Scaffold de carpetas (20 min)

```bash
mkdir -p projects/m17-agenda-ops/{docs,src,tests,scripts,apps}
cp projects/m17-agenda-ops/README.md /tmp/m17-readme.bak 2>/dev/null || true
```

Inicializa el repo app (npm/pnpm) **dentro** de `projects/m17-agenda-ops/` o documenta monorepo. TypeScript `strict: true`.

### 3. Documenta stack.md (40–50 min)

Crea `projects/m17-agenda-ops/stack.md` con: runtime, framework HTTP, ORM/query builder, front, test runner, por qué **no** cambiarás a mitad de materia.

### 4. Conecta Postgres y health (60–80 min)

Reusa Compose M09 o añade el tuyo. Variables en `.env.example` (sin secretos). Implementa `GET /health` que confirme proceso + (ideal) ping DB.

```bash
curl -sS http://localhost:3000/health
```

### 5. Commit

`docs(m17): l01 scaffold stack health postgres`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas.md + m13-diseno + M09 esquema | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Repo scaffold (artefacto: `projects/m17-agenda-ops/stack.md`).
2. stack.md (artefacto: `projects/m17-agenda-ops/stack.md`).
3. DB conecta local (artefacto: `projects/m17-agenda-ops/stack.md`).
4. Health check (artefacto: `projects/m17-agenda-ops/stack.md`).
5. Commit `docs(m17): L01 scaffold-agenda-ops-api-db-y-stack`.

## Errores comunes

- Stack sin documentar.
- Secrets en repo.

## Siguiente

[L02 — Registro con hash de contraseña](L02-registro-con-hash-de-contrasena.md)
