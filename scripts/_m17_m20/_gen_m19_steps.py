"""Generated step labs for M19 polish."""
STEPS: dict[int, list[tuple[str, str]]] = {}
STEPS[1] = [
    ('Carpetas de evidencia (15 min)', r"""
```bash
mkdir -p projects/m19-ops/{scripts,logs,docs}
ls projects/m19-ops
```
"""),
    ('Inventario de secretos sin valores (80–100 min)', r"""
```bash
cat > projects/m19-ops/secrets-inventory.md << 'EOF'
# Inventario de secretos (SIN valores)
| Variable | Staging | Prod | Quién inyecta | Rotación |
|----------|---------|------|---------------|----------|
| DATABASE_URL | sí | sí | PaaS/VPS secrets | 90d |
| SESSION_SECRET | sí | sí | secrets manager | 90d |
EOF
```

Cruza con M17:

```bash
cat projects/m17-agenda-ops/.env.example
```
"""),
    ('ambientes.md staging vs prod (30–40 min)', r"""
```bash
cat > projects/m19-ops/ambientes.md << 'EOF'
# Ambientes
| Env | URL API | URL Front | Notas |
|-----|---------|-----------|-------|
| local | http://localhost:3000 | http://localhost:5173 | |
| staging | https://… | https://… | |
| prod | TBD | TBD | |
EOF
git add projects/m19-ops
git commit -m "docs(m19): L01 inventario secretos ambientes"
```
"""),
]
STEPS[2] = [
    ('Dockerfile multi-stage (90–110 min)', r"""
En el repo de la API (`projects/m17-agenda-ops/` o ruta documentada):

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup -S app && adduser -S app -G app
COPY --from=build /app /app
USER app
EXPOSE 3000
HEALTHCHECK CMD wget -qO- http://127.0.0.1:3000/health || exit 1
CMD ["node", "dist/index.js"]
```
"""),
    ('.dockerignore + build (40–50 min)', r"""
```bash
printf '%s\n' .env node_modules .git '*.md' tests keystores >> .dockerignore
docker build -t agenda-ops-api:dev .
```

Documenta en `projects/m19-ops/docker.md`.
"""),
    ('Commit (15 min)', r"""
```bash
git add Dockerfile .dockerignore projects/m19-ops/docker.md
git commit -m "feat(m19): L02 dockerfile multi-stage"
```
"""),
]
STEPS[3] = [
    ('compose prod-like (80–100 min)', r"""
```yaml
# compose.yml (ejemplo)
services:
  db:
    image: postgres:16-alpine
    volumes: ["pgdata:/var/lib/postgresql/data"]
    env_file: [.env]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER"]
  api:
    build: .
    depends_on:
      db: { condition: service_healthy }
    env_file: [.env]
    ports: ["3000:3000"]
volumes:
  pgdata:
```
"""),
    ('Up + health (50–60 min)', r"""
```bash
docker compose up -d --build
curl -sS http://localhost:3000/health
docker compose ps
```

Pega comandos en `projects/m19-ops/docker.md`.
"""),
    ('Commit (15 min)', r"""
```bash
git add compose.yml projects/m19-ops/docker.md
git commit -m "feat(m19): L03 compose prod-like"
```
"""),
]
STEPS[4] = [
    ('Cierra docker.md P1 (60–80 min)', r"""
```bash
cat >> projects/m19-ops/docker.md << 'EOF'
## Comandos
- build: `docker build -t agenda-ops-api:dev .`
- up: `docker compose up -d`
- down: `docker compose down`
- logs: `docker compose logs -f api`
EOF
```
"""),
    ('Verifica end-to-end local (40 min)', r"""
```bash
docker compose down && docker compose up -d --build
curl -sS http://localhost:3000/health
# login smoke local (cookie) — anota OK en docker.md
git add projects/m19-ops/docker.md
git commit -m "docs(m19): L04 docker.md P1 completo"
```
"""),
]
STEPS[5] = [
    ('ADR PaaS vs VPS (70–90 min)', r"""
```bash
cat > projects/m19-ops/adr-hosting.md << 'EOF'
# ADR hosting
## Contexto
Agenda Ops necesita HTTPS + Postgres managed o self-host.
## Opciones
A) PaaS  B) VPS
## Decisión
…
## Consecuencias
costo, SSH, backups, tiempo-a-staging
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/adr-hosting.md
git commit -m "docs(m19): L05 adr hosting paas vs vps"
```
"""),
]
STEPS[6] = [
    ('Deploy staging HTTPS (90–120 min)', r"""
Sigue el ADR. Inyecta secrets en el panel.

```bash
curl -sSI https://TU-STAGING.example/health | head -15
```
"""),
    ('deploy-log.md (30–40 min)', r"""
```bash
cat > projects/m19-ops/deploy-log.md << 'EOF'
# Deploy log
| Fecha | Env | Versión/commit | URL | Resultado |
|-------|-----|----------------|-----|-----------|
| YYYY-MM-DD | staging | abc123 | https://… | OK health |
EOF
git add projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L06 deploy staging https"
```
"""),
]
STEPS[7] = [
    ('Smoke staging (60–80 min)', r"""
```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
curl -sS -b /tmp/st.ck -X POST "$BASE/citas" -H 'content-type: application/json' -d '{...}'
```

**No** pegues el password en el markdown.
"""),
    ('Documenta smoke-staging.md (30 min)', r"""
```bash
cat > projects/m19-ops/smoke-staging.md << 'EOF'
# Smoke staging
Fecha: …  Health: OK  Login: OK  Cita: OK
EOF
git add projects/m19-ops/smoke-staging.md
git commit -m "docs(m19): L07 smoke staging login cita"
```
"""),
]
STEPS[8] = [
    ('Dominios (50–60 min)', r"""
```bash
cat > projects/m19-ops/dominios.md << 'EOF'
# Dominios
| Uso | FQDN | DNS | TLS |
|-----|------|-----|-----|
| API staging | api-staging.… | CNAME → PaaS | managed |
EOF
```
"""),
    ('Actualiza deploy-log semana 2 (30 min)', r"""
```bash
echo "| $(date -I) | staging | … | https://… | DNS OK |" >> projects/m19-ops/deploy-log.md
git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L08 dominios deploy-log semana2"
```
"""),
]
STEPS[9] = [
    ('Checklist promoción a prod (60–80 min)', r"""
```bash
cat >> projects/m19-ops/ambientes.md << 'EOF'
## Promoción staging → prod
1. Migraciones aplicadas
2. Secrets distintos a staging
3. Smoke health+login
4. Rollback plan listo
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/ambientes.md
git commit -m "docs(m19): L09 promover config a produccion"
```
"""),
]
STEPS[10] = [
    ('Rollback + versión (60–80 min)', r"""
```bash
mkdir -p projects/m19-ops
cat > projects/m19-ops/runbook.md << 'EOF'
# Runbook (borrador)
## Versión desplegada
Cómo ver commit/tag en runtime (header, /health.version, o CLI PaaS).
## Rollback
1. Redeploy imagen/tag anterior
2. Verificar /health
3. Anotar en deploy-log.md
## Logs
comando CLI o URL del provider
EOF
```

```bash
# ejemplo
# fly releases / render releases / docker compose images
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L10 logs rollback version"
```
"""),
]
STEPS[11] = [
    ('Monitoreo mínimo (60–80 min)', r"""
```bash
cat > projects/m19-ops/monitoring.md << 'EOF'
# Monitoreo
- Check: GET /health cada 5 min (UptimeRobot/Cron/… )
- Alerta: email/Telegram si 2 fallos
- Manual: revisar logs tras deploy
EOF
```

```bash
curl -sS https://TU-STAGING.example/health
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/monitoring.md
git commit -m "docs(m19): L11 monitoreo alertas manuales"
```
"""),
]
STEPS[12] = [
    ('Revisión host (70–90 min)', r"""
```bash
# Si VPS (ejemplos — adapta; no abras 0.0.0.0:5432 al mundo):
# sudo ufw status
# ss -tulpn | head
cat > projects/m19-ops/security-host.md << 'EOF'
# Host security
| Control | Estado | Notas |
|---------|--------|-------|
| SSH keys only | | |
| Firewall | | DB no pública |
| Updates | | |
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/security-host.md
git commit -m "docs(m19): L12 seguridad puertos ssh firewall"
```
"""),
]
STEPS[13] = [
    ('Script backup Postgres (80–100 min)', r"""
```bash
cat > projects/m19-ops/scripts/pg_dump_daily.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
: "${DATABASE_URL:?}"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
OUT="backups/agenda-${STAMP}.sql.gz"
mkdir -p backups
pg_dump "$DATABASE_URL" | gzip > "$OUT"
echo "wrote $OUT"
EOF
chmod +x projects/m19-ops/scripts/pg_dump_daily.sh
```
"""),
    ('Documenta backup.md (40 min)', r"""
```bash
cat > projects/m19-ops/backup.md << 'EOF'
# Backup
- Comando: `scripts/pg_dump_daily.sh`
- Destino: object storage / volumen cifrado
- Retención: 7–30 días
- Cron: …
EOF
# añade backups/ a .gitignore
git add projects/m19-ops/scripts/pg_dump_daily.sh projects/m19-ops/backup.md
git commit -m "feat(m19): L13 backup automatico postgresql"
```
"""),
]
STEPS[14] = [
    ('Restore aislado (80–100 min)', r"""
```bash
# entorno scratch — NO prod
createdb agenda_restore_test || true
gunzip -c backups/agenda-XXXX.sql.gz | psql "postgresql://…/agenda_restore_test"
psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM citas;'
```
"""),
    ('restore-test.md (30–40 min)', r"""
```bash
cat > projects/m19-ops/restore-test.md << 'EOF'
# Restore test
Fecha: YYYY-MM-DD
Dump usado: agenda-….sql.gz
Destino: DB aislada …
Resultado: OK — count citas = N
EOF
git add projects/m19-ops/restore-test.md
git commit -m "docs(m19): L14 prueba restore aislado"
```
"""),
]
STEPS[15] = [
    ('Runbook completo (70–90 min)', r"""
Completa `projects/m19-ops/runbook.md`: deploy, rollback, logs, backup, restore, contactos, URLs (sin secretos).

```bash
wc -l projects/m19-ops/runbook.md
rg -n "Rollback|Backup|Health|Secrets" projects/m19-ops/runbook.md
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L15 runbook produccion completo"
```
"""),
]
STEPS[16] = [
    ('Checklist pre-demo M22 (50–60 min)', r"""
```bash
cat > projects/m19-ops/cierre-m19.md << 'EOF'
# Cierre M19
- [ ] docker.md P1
- [ ] deploy-log HTTPS P2
- [ ] restore-test.md P3
- [ ] runbook.md
Handoff: URL staging para M20/M22
EOF
ls projects/m19-ops
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m19-ops
git commit -m "docs(m19): L16 cierre checklist pre-demo"
```
"""),
]
