#!/usr/bin/env bash
set -euo pipefail
BACKUP_DIR="${BACKUP_DIR:-./backups}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"
mkdir -p "$BACKUP_DIR"
DATE=$(date +%F-%H%M)

if [[ "${BACKUP_DEMO:-}" == "1" ]]; then
  OUT="$BACKUP_DIR/demo-$DATE.txt"
  echo "demo backup $(date -Iseconds)" >"$OUT"
  gzip -f "$OUT"
  echo "wrote ${OUT}.gz (demo mode)"
  exit 0
fi

: "${DATABASE_URL:?DATABASE_URL is required (or set BACKUP_DEMO=1)}"
OUT="$BACKUP_DIR/db-$DATE.sql"
pg_dump "$DATABASE_URL" >"$OUT"
gzip -f "$OUT"
find "$BACKUP_DIR" -name 'db-*.sql.gz' -mtime +"$RETENTION_DAYS" -delete
echo "wrote ${OUT}.gz"
