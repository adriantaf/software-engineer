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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 empieza: un backup que otro humano puede correr.


      **Objetivo de esta lección:** Versionar `scripts/backup.sh` listo para
      cron/CI con secretos por entorno.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Esqueleto
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

      `projects/m11-so/scripts/backup.sh`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Modo demo sin Postgres
    xp: 10
    cuerpo: |-
      ```bash
      chmod +x projects/m11-so/scripts/backup.sh
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Script de backup automatizado (P2)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Script de backup
          automatizado (P2)
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

      `mkdir -p "$BACKUP_DIR"`
    comandoEsperado:
      - mkdir -p "$BACKUP_DIR"
      - find "$BACKUP_DIR" -name 'db-*.sql.gz' -mtime +"$RETENTION_DAYS" -delete
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p "$BACKUP_DIR"'
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
          Versionar `scripts/backup.sh` listo para cron/CI con secretos por
          entorno.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
