---
id: L13
materia: M19
orden: 13
titulo: Backup automático PostgreSQL
horas: 5
semana: 4
lectura: pg_dump + proveedor backups
evidencia: projects/m19-ops/backup.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Automatizar pg_dump o backup gestionado; retención y
      ubicación segura.


      - pg_dump

      - cron

      - cifrado opcional
  - id: s2
    tipo: ejemplo
    titulo: 1. Script backup Postgres
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Backup automático PostgreSQL" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/backup.md
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

      `mkdir -p backups`
    comandoEsperado:
      - mkdir -p backups
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p backups'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Automatizar pg_dump o backup gestionado; retención y ubicación segura.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta backup.md
    xp: 10
    cuerpo: >-
      ```bash

      cat > projects/m19-ops/backup.md << 'EOF'

      Backup

      - Comando: `scripts/pg_dump_daily.sh`

      - Destino: object storage / volumen cifrado

      - Retención: 7–30 días

      - Cron: …

      EOF

      añade backups/ a .gitignore

      git add projects/m19-ops/scripts/pg_dump_daily.sh
      projects/m19-ops/backup.md

      git commit -m "feat(m19): L13 backup automatico postgresql"

      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/scripts/pg_dump_daily.sh` +
        `projects/m19-ops/backup.md`.
      - 'Commit `docs(m19): L13 backup-automatico-postgresql`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Backup automático PostgreSQL

**~5.0 h · Semana 4**

P3 sin backup es teatro.

## Objetivo

Automatizar pg_dump o backup gestionado; retención y ubicación segura.

## Conceptos clave

- pg_dump
- cron
- cifrado opcional

## Pasos (hazlos en orden)

### 1. Script backup Postgres (80–100 min)

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

### 2. Documenta backup.md (40 min)

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | pg_dump + proveedor backups | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/scripts/pg_dump_daily.sh` + `projects/m19-ops/backup.md`.
2. Commit `docs(m19): L13 backup-automatico-postgresql`.

## Errores comunes

- Dumps con PII en el repo git.
- Backup sin retención ni destino.

## Siguiente

[L14 — Prueba de restore en entorno aislado](L14-prueba-de-restore-en-entorno-aislado.md)
