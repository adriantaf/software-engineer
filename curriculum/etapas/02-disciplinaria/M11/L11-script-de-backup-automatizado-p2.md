---
id: L11
materia: M11
orden: 11
titulo: Script de backup automatizado (P2)
horas: 5
semana: 3
lectura: Silberschatz I/O + bash strict
evidencia: projects/m11-so/scripts/backup.sh
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Versionar `scripts/backup.sh` listo para cron/CI con
      secretos por entorno.


      P2 empieza: un backup que otro humano puede correr.
  - id: s2
    tipo: ejemplo
    titulo: 1. Esqueleto
    xp: 10
    cuerpo: |-
      ```bash
      #!/usr/bin/env bash
      set -euo pipefail
      BACKUP_DIR="${BACKUP_DIR:-./backups}"
      RETENTION_DAYS="${RETENTION_DAYS:-7}"
      mkdir -p "$BACKUP_DIR"
      DATE=$(date +%F-%H%M)
      OUT="$BACKUP_DIR/db-$DATE.sql"
      # Usa DATABASE_URL o PG* ; falla si falta
      : "${DATABASE_URL:?DATABASE_URL is required}"
      pg_dump "$DATABASE_URL" > "$OUT"
      gzip -f "$OUT"
      find "$BACKUP_DIR" -name 'db-*.sql.gz' -mtime +"$RETENTION_DAYS" -delete
      echo "wrote ${OUT}.gz"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Script de backup automatizado (P2)" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m11-so/scripts/backup.sh
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

      `mkdir -p "$BACKUP_DIR"`
    comandoEsperado:
      - mkdir -p "$BACKUP_DIR"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p "$BACKUP_DIR"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Versionar `scripts/backup.sh` listo para cron/CI con secretos por
          entorno.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Modo demo sin Postgres
    xp: 10
    cuerpo: >-
      Si aún no tienes DB: añade rama `BACKUP_DEMO=1` que archiva un
      `fixtures/demo.sql` — documenta ambas rutas en el README de scripts.
  - id: s7
    tipo: explicacion
    titulo: 3. Nota
    xp: 10
    cuerpo: 'Cómo invocar desde cron: `DATABASE_URL=… BACKUP_DIR=… /path/backup.sh`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `scripts/backup.sh` con `set -euo pipefail`, usa env vars (sin passwords
        hardcode).
      - Dry-run o corrida contra archivo/fixture documentada en labs.
      - 'Commit `feat(m11): l11 backup.sh`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Script de backup automatizado (P2)

**~5.0 h · Semana 3**

P2 empieza: un backup que otro humano puede correr.

## Objetivo

Versionar `scripts/backup.sh` listo para cron/CI con secretos por entorno.

## Pasos

### 1. Esqueleto (75 min)

`projects/m11-so/scripts/backup.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
BACKUP_DIR="${BACKUP_DIR:-./backups}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"
mkdir -p "$BACKUP_DIR"
DATE=$(date +%F-%H%M)
OUT="$BACKUP_DIR/db-$DATE.sql"
# Usa DATABASE_URL o PG* ; falla si falta
: "${DATABASE_URL:?DATABASE_URL is required}"
pg_dump "$DATABASE_URL" > "$OUT"
gzip -f "$OUT"
find "$BACKUP_DIR" -name 'db-*.sql.gz' -mtime +"$RETENTION_DAYS" -delete
echo "wrote ${OUT}.gz"
```

```bash
chmod +x projects/m11-so/scripts/backup.sh
```

### 2. Modo demo sin Postgres (40 min)

Si aún no tienes DB: añade rama `BACKUP_DEMO=1` que archiva un `fixtures/demo.sql` — documenta ambas rutas en el README de scripts.

### 3. Nota (30 min)

Cómo invocar desde cron: `DATABASE_URL=… BACKUP_DIR=… /path/backup.sh`.

### 4. Commit (15 min)

```bash
git add projects/m11-so/scripts
git commit -m "feat(m11): l11 backup.sh"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Bash set -euo pipefail; pg_dump vía env; retención | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `scripts/backup.sh` con `set -euo pipefail`, usa env vars (sin passwords hardcode).
2. Dry-run o corrida contra archivo/fixture documentada en labs.
3. Commit `feat(m11): l11 backup.sh`.

## Errores comunes

- Password en el script.
- Backup que “funciona” sin fecha en el nombre.
- No fallar si `pg_dump` no existe (ocultar errores).

## Siguiente

[L12 — Rotación de logs y restore de prueba](L12-rotacion-de-logs-y-restore-de-prueba.md)
