---
id: L01
materia: M09
orden: 1
titulo: PostgreSQL local y carpeta de evidencia
horas: 5.0
semana: 1
lectura: "Elmasri: intro SGBD + tutorial PostgreSQL (Getting Started)"
evidencia: projects/m09-bases-datos/ con Docker o PG nativo + SELECT version()
---

# L01 — PostgreSQL local y carpeta de evidencia

**~5.0 h · Semana 1**

Sin una BD real, Elmasri se queda en teoría. Hoy levantas PostgreSQL y dejas evidencia en git.

## Objetivo

Dejar `projects/m09-bases-datos/` usable: Compose (o nativo), conexión documentada y un `SELECT version()` ejecutado.

## Por qué empieza así

M09 diseña el esquema de **Agenda Ops**. Cada lección siguiente asume que puedes pegarle SQL a una instancia local.

## Pasos (hazlos en orden)

### 1. Revisa el scaffold (20 min)

Desde la raíz del repo:

```bash
ls projects/m09-bases-datos
cat projects/m09-bases-datos/README.md
```

Ya hay `docker-compose.yml`, `.env.example`, `migrations/` y plantillas. No borres la estructura; amplíala.

### 2. Variables locales (15 min)

```bash
cd projects/m09-bases-datos
cp .env.example .env
# Edita POSTGRES_PASSWORD (y opcionalmente APP_DB_PASSWORD)
```

Confirma que `.env` está en `.gitignore`.

### 3. Levanta PostgreSQL (45–60 min)

**Opción A — Docker:**

```bash
docker compose up -d
docker compose ps
```

**Opción B — Nativo:** crea usuario/DB con los mismos nombres del `.env` y anota el comando de instalación en el README.

### 4. Conecta y prueba (30–40 min)

```bash
set -a && source .env && set +a
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -c 'SELECT version();'
```

Si no tienes `psql` en el host:

```bash
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c 'SELECT version();'
```

Pega la versión (una línea) en una sección `## Conexión local` del README — **sin** password.

### 5. Aplica la migración 001 (45–60 min)

```bash
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -f migrations/001_init.sql
psql "..." -c '\dt'
```

Debes ver `clientes`, `servicios`, `citas`.

### 6. Commit (15 min)

```bash
git add projects/m09-bases-datos
git status   # .env NO debe aparecer
git commit -m "docs(m09): arrancar postgres local y migración 001"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Intro SGBD + [tutorial PG — Getting Started](https://www.postgresql.org/docs/current/tutorial-start.html) | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m09-bases-datos/` con `.env` local (no commiteado) y `docker compose` **o** PG nativo documentado.
2. Corres `SELECT version();` y anotas el resultado en el README (sin password).
3. Commit que mencione el arranque (ej. `docs(m09): arrancar postgres local`).

## Errores comunes

- Subir `.env` con passwords.
- Usar el usuario `postgres` superuser como “la app” desde el día 1.
- Documentar “ya tengo Docker” sin un `SELECT` ejecutado.

## Siguiente

[L02 — Entidades Cliente, Servicio, Cita](L02-entidades-cliente-servicio-cita.md)
