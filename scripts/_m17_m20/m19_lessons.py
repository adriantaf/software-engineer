"""M19 lessons: RAW specs + BODIES (M01/M09 quality)."""
from __future__ import annotations

import json

FILENAMES = {
    1: "L01-inventario-de-secretos-y-ambientes-staging-prod.md",
    2: "L02-dockerfile-multi-stage-para-la-api.md",
    3: "L03-compose-prod-like-api-postgres-volumenes.md",
    4: "L04-stack-local-documentado-y-p1-docker.md",
    5: "L05-adr-hosting-paas-vs-vps.md",
    6: "L06-deploy-staging-con-https.md",
    7: "L07-smoke-test-login-cita-y-health-externo.md",
    8: "L08-dominios-y-deploy-log-semana-2.md",
    9: "L09-promover-configuracion-a-produccion.md",
    10: "L10-logs-rollback-y-version-desplegada.md",
    11: "L11-monitoreo-minimo-y-alertas-manuales.md",
    12: "L12-revision-seguridad-puertos-ssh-y-firewall.md",
    13: "L13-backup-automatico-postgresql.md",
    14: "L14-prueba-de-restore-en-entorno-aislado.md",
    15: "L15-runbook-completo-de-produccion.md",
    16: "L16-cierre-m19-checklist-pre-demo-m22.md",
}

RAW = json.loads(r"""
[
  {
    "titulo": "Inventario de secretos y ambientes staging/prod",
    "semana": 1,
    "horas": 5,
    "lectura": "Docker docs — env vars + 12-factor",
    "evidencia": "projects/m19-ops/secrets-inventory.md + ambientes.md",
    "objetivo": "Crear inventario de secretos sin valores y definir URLs/objetivo de staging y prod para Agenda Ops.",
    "porque": "M19 empieza donde M18 dejó: nada de secretos en git antes de empaquetar.",
    "conceptos": [
      "DATABASE_URL",
      "SESSION_SECRET",
      "Stripe test futuro"
    ],
    "pasos_extra": "```bash\nmkdir -p projects/m19-ops\ngit ls-files | rg -i '\\.env|secret|credential' || true\n```\n\nCompleta `secrets-inventory.md` y `ambientes.md` según ficha M19.",
    "lectura_rows": [
      [
        "Plan",
        "producto-saas.md",
        "M18 secrets"
      ]
    ],
    "hecho": [
      "Ambos archivos existen.",
      "Sin valores secretos.",
      "URLs objetivo anotadas."
    ],
    "errores": [
      "Pegar JWT en markdown.",
      "Un solo ambiente ‘prod’."
    ]
  },
  {
    "titulo": "Dockerfile multi-stage para la API",
    "semana": 1,
    "horas": 5,
    "lectura": "Dockerfile best practices (oficial)",
    "evidencia": "Dockerfile en repo + projects/m19-ops/docker.md",
    "objetivo": "Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin devDependencies ni fuentes.",
    "porque": "Imagen pequeña y sin toolchain reduce superficie.",
    "conceptos": [
      "multi-stage",
      "USER node",
      "HEALTHCHECK"
    ],
    "pasos_extra": "Implementa patrón de la ficha M19. Documenta comandos build en `projects/m19-ops/docker.md`.\n\n`.dockerignore`: node_modules, .git, .env.",
    "lectura_rows": [
      [
        "Docker",
        "multi-stage",
        "M11 Docker"
      ]
    ],
    "hecho": [
      "Dockerfile multi-stage.",
      "docker.md con comandos.",
      ".dockerignore."
    ],
    "errores": [
      "COPY .env",
      "root en runtime"
    ]
  },
  {
    "titulo": "Compose prod-like: API + Postgres + volúmenes",
    "semana": 1,
    "horas": 5,
    "lectura": "Compose file reference",
    "evidencia": "compose.yml + projects/m19-ops/docker.md",
    "objetivo": "Orquestar API y PostgreSQL con volúmenes persistentes, red interna y healthchecks.",
    "porque": "P1 M19 es stack local idéntico en espíritu a prod.",
    "conceptos": [
      "depends_on healthy",
      "volumen db-data",
      "puerto 5432 no publicado"
    ],
    "pasos_extra": "`compose.yml`: servicios api, db; env desde `.env.example` sin secretos reales.\n\n`docker compose up --build` documentado con tiempo de arranque y curl `/health`.",
    "lectura_rows": [
      [
        "Docker",
        "Compose",
        "M11 compose"
      ]
    ],
    "hecho": [
      "Compose levanta stack.",
      "Healthcheck OK.",
      "Postgres con volumen."
    ],
    "errores": [
      "5432:5432 público",
      "password en compose commiteado"
    ]
  },
  {
    "titulo": "Stack local documentado y P1 Docker",
    "semana": 1,
    "horas": 5,
    "lectura": "Repaso semana 1",
    "evidencia": "projects/m19-ops/docker.md completo",
    "objetivo": "Consolidar instrucciones un comando, troubleshooting y evidencia de login/cita en contenedores.",
    "porque": "Cierra semana 1 con P1 listo para marcar.",
    "conceptos": [
      "reproducibilidad",
      "logs compose"
    ],
    "pasos_extra": "Añade sección Troubleshooting a docker.md. Captura `docker compose ps` y respuesta `/health`.\n\nSmoke: crear cita desde UI contra stack dockerizado.",
    "lectura_rows": [
      [
        "Ficha",
        "M19 P1",
        "—"
      ]
    ],
    "hecho": [
      "docker.md completo.",
      "Smoke test anotado.",
      "Commit P1."
    ],
    "errores": [
      "Solo README vacío",
      "Imagen sin healthcheck"
    ]
  },
  {
    "titulo": "ADR hosting: PaaS vs VPS",
    "semana": 2,
    "horas": 5,
    "lectura": "Docs Fly/Railway/Render o VPS",
    "evidencia": "projects/m19-ops/adr-hosting.md",
    "objetivo": "Documentar decisión de hosting para Agenda Ops con criterios costo, TLS, Postgres gestionado, DX.",
    "porque": "Evitas re-decidir cada semana.",
    "conceptos": [
      "PaaS",
      "VPS+Docker",
      "egress y region"
    ],
    "pasos_extra": "ADR con alternativas y consecuencias operativas (logs, secrets panel).",
    "lectura_rows": [
      [
        "Ficha",
        "M19 semana 2",
        "—"
      ]
    ],
    "hecho": [
      "ADR firmada.",
      "Proveedor elegido.",
      "Riesgos listados."
    ],
    "errores": [
      "Sin ADR",
      "Elegir solo por tutorial viejo"
    ]
  },
  {
    "titulo": "Deploy staging con HTTPS",
    "semana": 2,
    "horas": 5,
    "lectura": "Proveedor: deploy + TLS",
    "evidencia": "projects/m19-ops/deploy-log.md",
    "objetivo": "Desplegar staging con HTTPS forzado y variables en panel del host.",
    "porque": "Primera URL pública del piloto.",
    "conceptos": [
      "HTTP→HTTPS",
      "env vars",
      "build remoto"
    ],
    "pasos_extra": "Registra URL, fecha, commit SHA en deploy-log. Secretos solo en panel.\n\ncurl -I staging URL.",
    "lectura_rows": [
      [
        "Proveedor",
        "HTTPS docs",
        "M10 TLS"
      ]
    ],
    "hecho": [
      "URL HTTPS viva.",
      "deploy-log entrada.",
      "Sin secretos en repo."
    ],
    "errores": [
      "HTTP plano",
      "TLS solo en front"
    ]
  },
  {
    "titulo": "Smoke test: login, cita y health externo",
    "semana": 2,
    "horas": 5,
    "lectura": "Runbook borrador",
    "evidencia": "projects/m19-ops/smoke-staging.md",
    "objetivo": "Ejecutar checklist smoke desde fuera de tu laptop: login, crear cita, GET /health.",
    "porque": "‘Contenedor verde’ ≠ producto usable.",
    "conceptos": [
      "smoke test",
      "datos prueba"
    ],
    "pasos_extra": "Checklist binario en smoke-staging.md con capturas o salidas curl anonimizadas.",
    "lectura_rows": [
      [
        "Ficha",
        "M19",
        "M17 API"
      ]
    ],
    "hecho": [
      "Smoke completo.",
      "health externo.",
      "Fecha registrada."
    ],
    "errores": [
      "Solo health sin login",
      "Smoke nunca repetido"
    ]
  },
  {
    "titulo": "Dominios y deploy-log semana 2",
    "semana": 2,
    "horas": 5,
    "lectura": "DNS del proveedor",
    "evidencia": "projects/m19-ops/dominios.md",
    "objetivo": "Registrar subdominios staging (y prod planificado); enlazar con deploy-log.",
    "porque": "Trials M22 necesitan URL estable.",
    "conceptos": [
      "CNAME",
      "cert automático"
    ],
    "pasos_extra": "dominios.md con registros y TTL. Verifica cert válido en navegador.",
    "lectura_rows": [
      [
        "M10",
        "DNS",
        "—"
      ]
    ],
    "hecho": [
      "dominios.md",
      "Cert OK",
      "deploy-log actualizado"
    ],
    "errores": [
      "IP directa sin nombre",
      "Cert expirado ignorado"
    ]
  },
  {
    "titulo": "Promover configuración a producción",
    "semana": 3,
    "horas": 5,
    "lectura": "12-factor config",
    "evidencia": "projects/m19-ops/ambientes.md actualizado",
    "objetivo": "Desplegar prod con misma imagen que staging y distintas env vars; documentar diferencias.",
    "porque": "Prod es para design partner, no laboratorio.",
    "conceptos": [
      "promoción imagen",
      "separación datos"
    ],
    "pasos_extra": "Segunda entrada deploy-log prod. Tabla diff staging vs prod en ambientes.md.",
    "lectura_rows": [
      [
        "Ficha",
        "M19 semana 3",
        "—"
      ]
    ],
    "hecho": [
      "Prod URL.",
      "Diff documentado.",
      "Datos separados."
    ],
    "errores": [
      "Migrar en prod primero",
      "Misma DB staging/prod"
    ]
  },
  {
    "titulo": "Logs, rollback y versión desplegada",
    "semana": 3,
    "horas": 5,
    "lectura": "Runbook ops",
    "evidencia": "projects/m19-ops/runbook.md sección rollback",
    "objetivo": "Documentar dónde ver logs, cómo identificar versión y rollback a imagen/tag anterior.",
    "porque": "A las 11 p.m. solo cuenta el runbook.",
    "conceptos": [
      "rollback",
      "tag git",
      "logs PaaS"
    ],
    "pasos_extra": "runbook.md: Rollback en ≤10 pasos numerados. Prueba rollback en staging si es seguro.",
    "lectura_rows": [
      [
        "Proveedor",
        "logs",
        "—"
      ]
    ],
    "hecho": [
      "Rollback documentado.",
      "Versión en runbook.",
      "Prueba o simulacro."
    ],
    "errores": [
      "Rollback ‘redeploy main’ sin tag",
      "Sin logs"
    ]
  },
  {
    "titulo": "Monitoreo mínimo y alertas manuales",
    "semana": 3,
    "horas": 5,
    "lectura": "Uptime básico",
    "evidencia": "projects/m19-ops/monitoring.md",
    "objetivo": "Configurar healthcheck externo o calendario de revisión manual; definir qué hacer si cae.",
    "porque": "No necesitas Datadog para el piloto; sí necesitas saber si está caído.",
    "conceptos": [
      "uptime",
      "on-call manual"
    ],
    "pasos_extra": "monitoring.md: herramienta o ritual calendario + contacto. Enlaza /health prod.",
    "lectura_rows": [
      [
        "Ficha",
        "M19",
        "—"
      ]
    ],
    "hecho": [
      "Monitoreo definido.",
      "Contacto.",
      "health prod"
    ],
    "errores": [
      "Asumir siempre up",
      "Alertas sin acción"
    ]
  },
  {
    "titulo": "Revisión seguridad: puertos, SSH y firewall",
    "semana": 3,
    "horas": 5,
    "lectura": "M18 + M11 seguridad host",
    "evidencia": "projects/m19-ops/security-host.md",
    "objetivo": "Checklist puertos expuestos, SSH (clave, no password), firewall si VPS.",
    "porque": "Deploy sin postura de host revierte M18.",
    "conceptos": [
      "firewall",
      "SSH",
      "least privilege"
    ],
    "pasos_extra": "security-host.md checklist. Si PaaS, documenta qué gestiona el proveedor vs tú.",
    "lectura_rows": [
      [
        "Hilo",
        "seguridad",
        "M18"
      ]
    ],
    "hecho": [
      "Checklist completo.",
      "SSH seguro o N/A PaaS.",
      "Sin Postgres público."
    ],
    "errores": [
      "SSH password root",
      "22 abierto al mundo sin necesidad"
    ]
  },
  {
    "titulo": "Backup automático PostgreSQL",
    "semana": 4,
    "horas": 5,
    "lectura": "pg_dump + proveedor backups",
    "evidencia": "projects/m19-ops/backup.md",
    "objetivo": "Automatizar pg_dump o backup gestionado; retención y ubicación segura.",
    "porque": "P3 sin backup es teatro.",
    "conceptos": [
      "pg_dump",
      "cron",
      "cifrado opcional"
    ],
    "pasos_extra": "backup.md: script o procedimiento, frecuencia, dónde se guarda (sin credenciales).",
    "lectura_rows": [
      [
        "PostgreSQL",
        "backup",
        "Proveedor docs"
      ]
    ],
    "hecho": [
      "Procedimiento escrito.",
      "Job programado o gestionado.",
      "Tamaño estimado."
    ],
    "errores": [
      "Backup manual olvidado",
      "Dump en repo git"
    ]
  },
  {
    "titulo": "Prueba de restore en entorno aislado",
    "semana": 4,
    "horas": 5,
    "lectura": "Restore docs",
    "evidencia": "projects/m19-ops/restore-test.md",
    "objetivo": "Restaurar dump en DB de prueba, verificar citas visibles, registrar tiempo y resultado.",
    "porque": "Un restore nunca probado no cuenta.",
    "conceptos": [
      "restore",
      "RTO idea",
      "vacuum"
    ],
    "pasos_extra": "restore-test.md: fecha, dump usado, duración, éxito/fallo, captura query count citas.",
    "lectura_rows": [
      [
        "Ficha",
        "M19 P3",
        "—"
      ]
    ],
    "hecho": [
      "Restore real documentado.",
      "Verificación datos.",
      "Fecha."
    ],
    "errores": [
      "Solo teoría",
      "Restore sobre prod"
    ]
  },
  {
    "titulo": "Runbook completo de producción",
    "semana": 4,
    "horas": 5,
    "lectura": "SRE runbook lite",
    "evidencia": "projects/m19-ops/runbook.md completo",
    "objetivo": "Unificar deploy, rollback, backup, restore, URLs, secretos (referencias), health.",
    "porque": "Proyecto único M19.",
    "conceptos": [
      "runbook",
      "handoff"
    ],
    "pasos_extra": "runbook.md enlazado desde README m19-ops. Índice al inicio.",
    "lectura_rows": [
      [
        "Ficha",
        "proyecto M19",
        "—"
      ]
    ],
    "hecho": [
      "Runbook navegable.",
      "Enlaces internos.",
      "URLs prod/staging."
    ],
    "errores": [
      "Runbook disperso",
      "Sin restore"
    ]
  },
  {
    "titulo": "Cierre M19 — checklist pre-demo M22",
    "semana": 4,
    "horas": 5,
    "lectura": "Repaso M19",
    "evidencia": "projects/m19-ops/cierre-m19.md",
    "objetivo": "Verificar P1–P3, criterios dominio, prod estable para trials.",
    "porque": "Handoff a M20 (API staging HTTPS) y M22.",
    "conceptos": [
      "checklist",
      "dominio"
    ],
    "pasos_extra": "cierre-m19.md con evidencia por criterio ficha. Actualiza README.",
    "lectura_rows": [
      [
        "Ficha",
        "M19-nube-devops.md",
        "producto"
      ]
    ],
    "hecho": [
      "P1–P3 OK.",
      "cierre escrito.",
      "README índice."
    ],
    "errores": [
      "Prod inestable",
      "Sin restore probado"
    ]
  }
]
""")

BODIES: dict[int, str] = {}
BODIES[1] = r"""
# L01 — Inventario de secretos y ambientes staging/prod

**~5.0 h · Semana 1**

Sin mapa de secretos, el Dockerfile los horneará por accidente.

## Objetivo

`ambientes.md` + inventario de secretos **sin valores** (staging vs prod).

## Pasos (hazlos en orden)

### 1. Carpetas (15 min)

```bash
mkdir -p projects/m19-ops/{scripts,logs}
```

### 2. Inventario (80–100 min)

Tabla: nombre var, quién la inyecta, rotación. Separar staging/prod URLs.

### 3. Cruza con M17 `.env.example` (30 min)

### 4. Commit

`docs(m19): l01 inventario secretos ambientes`
"""

BODIES[2] = r"""
# L02 — Dockerfile multi-stage para la API

**~5.0 h · Semana 1**

Imagen final sin devDependencies ni `.env`.

## Objetivo

Dockerfile multi-stage + `.dockerignore`; build local exitoso.

## Pasos (hazlos en orden)

### 1. Escribe Dockerfile (90–110 min)

Stages build/runtime. USER no-root. HEALTHCHECK a `/health`.

### 2. dockerignore (20 min)

`.env`, `node_modules`, tests pesados, keystores.

### 3. Build (40 min)

```bash
docker build -t agenda-ops-api:dev .
```

### 4. Commit

`feat(m19): l02 dockerfile multi-stage`
"""

BODIES[3] = r"""
# L03 — Compose prod-like: API + Postgres + volúmenes

**~5.0 h · Semana 1**

Compose que imita prod: red interna, volumen datos, env file.

## Objetivo

`compose.yml` (o `compose.prod.yml`) API+Postgres; `docker compose up` documentado.

## Pasos (hazlos en orden)

### 1. Compose (80–100 min)

Depends_on healthy; puerto solo lo necesario; secrets via env_file no bakeado.

### 2. Prueba (50–60 min)

Up → health → login smoke local.

### 3. Commit

`feat(m19): l03 compose prod-like`
"""

BODIES[4] = r"""
# L04 — Stack local documentado y P1 Docker

**~5.0 h · Semana 1**

P1: imágenes + instrucciones en `docker.md`.

## Objetivo

`projects/m19-ops/docker.md` con build/up/down y enlace al Dockerfile del producto.

## Pasos (hazlos en orden)

### 1. Documenta (60–70 min)

Comandos copy-paste. Troubleshooting puerto ocupado.

### 2. Evidencia P1 (40 min)

`docker images` / `compose ps` anotados sin secretos.

### 3. README (20 min)

### 4. Commit

`docs(m19): l04 p1 docker documentado`
"""

BODIES[5] = r"""
# L05 — ADR hosting: PaaS vs VPS

**~5.0 h · Semana 2**

Elige con criterios: costo, TLS, backups, tiempo.

## Objetivo

`adr-hosting.md` con decisión y consecuencias para Agenda Ops.

## Pasos (hazlos en orden)

### 1. Compara (60 min)

PaaS vs VPS tabla.

### 2. ADR (70–90 min)

Decisión alineada a tu staging M17 si ya existe.

### 3. Commit

`docs(m19): l05 adr hosting`
"""

BODIES[6] = r"""
# L06 — Deploy staging con HTTPS

**~5.0 h · Semana 2**

Staging HTTPS estable usando la decisión del ADR.

## Objetivo

URL HTTPS en `deploy-log.md`; secretos solo en el hosting.

## Pasos (hazlos en orden)

### 1. Deploy (100–130 min)

Build, migraciones, env. Reusa o mejora M17 staging.

### 2. Verifica TLS (30 min)

### 3. Commit

`docs(m19): l06 deploy staging https`
"""

BODIES[7] = r"""
# L07 — Smoke test: login, cita y health externo

**~5.0 h · Semana 2**

Health solo no basta: login + crear cita.

## Objetivo

Corrida fechada en `deploy-log.md` o `smoke-staging.md`.

## Pasos (hazlos en orden)

### 1. Script/checklist (50 min)

### 2. Ejecuta contra staging (70–90 min)

Registra pass/fail.

### 3. Commit

`docs(m19): l07 smoke staging`
"""

BODIES[8] = r"""
# L08 — Dominios y deploy-log semana 2

**~5.0 h · Semana 2**

Dominio/DNS y bitácora de deploys.

## Objetivo

`deploy-log.md` con fechas, versiones, dominio; cierre semana 2.

## Pasos (hazlos en orden)

### 1. DNS/docs (50–60 min)

### 2. Log histórico (50 min)

Al menos 2 entradas (aunque una sea re-deploy).

### 3. Commit

`docs(m19): l08 dominios deploy-log`
"""

BODIES[9] = r"""
# L09 — Promover configuración a producción

**~5.0 h · Semana 3**

Prod ≠ staging con el mismo secret.

## Objetivo

Ambiente prod (o “prod-candidato”) con secretos y URL distintos documentados.

## Pasos (hazlos en orden)

### 1. Checklist promoción (40 min)

### 2. Configura prod (100–120 min)

Migraciones cuidadosas. Smoke mínimo.

### 3. Commit

`docs(m19): l09 promover produccion`
"""

BODIES[10] = r"""
# L10 — Logs, rollback y versión desplegada

**~5.0 h · Semana 3**

Sabes qué versión corre y cómo volver atrás.

## Objetivo

Sección runbook: versión, dónde están logs, procedimiento rollback ensayado en seco.

## Pasos (hazlos en orden)

### 1. Versionado (40 min)

Tag/git sha visible en `/health` o header.

### 2. Rollback dry-run (70–90 min)

Documenta pasos sin necesariamente tumbar prod si riesgoso — al menos staging.

### 3. Commit

`docs(m19): l10 logs rollback version`
"""

BODIES[11] = r"""
# L11 — Monitoreo mínimo y alertas manuales

**~5.0 h · Semana 3**

Uptime mínimo: ping health + alerta humana.

## Objetivo

`docs/monitoreo.md`: qué miras, cada cuánto, a quién avisas.

## Pasos (hazlos en orden)

### 1. Define señales (40 min)

### 2. Configura check (70–90 min)

Cron externo, Better Uptime free, o script. Evidencia.

### 3. Commit

`docs(m19): l11 monitoreo minimo`
"""

BODIES[12] = r"""
# L12 — Revisión seguridad: puertos, SSH y firewall

**~5.0 h · Semana 3**

Si VPS: SSH keys, ufw/security group. Si PaaS: documenta superficie.

## Objetivo

Checklist host harden; sin SSH password abierto al mundo.

## Pasos (hazlos en orden)

### 1. Inventario puertos (40 min)

### 2. Hardening/doc (70–90 min)

`docs/host-security.md`.

### 3. Commit

`docs(m19): l12 host security`
"""

BODIES[13] = r"""
# L13 — Backup automático PostgreSQL

**~5.0 h · Semana 4**

Backup que no corre no existe.

## Objetivo

`backup.md` + script/cron `pg_dump` (o snapshot proveedor) con retención.

## Pasos (hazlos en orden)

### 1. Script dump (80–100 min)

```bash
pg_dump "$DATABASE_URL" -Fc -f backup.dump
```

Almacena fuera del contenedor efímero.

### 2. Automatiza (40 min)

Cron/GitHub scheduled/PaaS job. Documenta.

### 3. Commit

`feat(m19): l13 backup postgres`
"""

BODIES[14] = r"""
# L14 — Prueba de restore en entorno aislado

**~5.0 h · Semana 4**

P3: restore real documentado.

## Objetivo

`restore-test.md` con fecha, tamaño dump, tiempo, resultado.

## Pasos (hazlos en orden)

### 1. Entorno aislado (40 min)

DB temporal/local.

### 2. Restore (80–100 min)

`pg_restore` / pipe. Verifica conteo citas seed.

### 3. Registra (20 min)

### 4. Commit

`docs(m19): l14 restore test p3`
"""

BODIES[15] = r"""
# L15 — Runbook completo de producción

**~5.0 h · Semana 4**

El proyecto M19 es el runbook.

## Objetivo

`runbook.md`: URLs, deploy, rollback, secretos, backup/restore, contacto.

## Pasos (hazlos en orden)

### 1. Integra docs previas (90–110 min)

Enlaces relativos, no copies eternos desactualizados.

### 2. Ensayo lectura (30 min)

Cronometra: ¿otro tú encuentra rollback en <5 min?

### 3. Commit

`docs(m19): l15 runbook produccion`
"""

BODIES[16] = r"""
# L16 — Cierre M19 — checklist pre-demo M22

**~5.0 h · Semana 4**

Antes de vender el piloto, ops debe sobrevivir.

## Objetivo

Checklist P1–P3 + criterios dominio + nota pre-demo comercial.

## Pasos (hazlos en orden)

### 1. Auditoría (50 min)

### 2. Pre-demo M22 (50–60 min)

Qué puede fallar en vivo; smoke del día.

### 3. README final (30 min)

### 4. Commit

`docs(m19): l16 cierre pre-demo`
"""

