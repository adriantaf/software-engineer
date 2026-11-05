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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - pg_dump

      - cron

      - cifrado opcional


      **Objetivo de esta lección:** Automatizar pg_dump o backup gestionado;
      retención y ubicación segura.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Script backup Postgres
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta backup.md
    xp: 10
    cuerpo: >-
      ```bash

      cat > projects/m19-ops/backup.md << 'EOF'

      # Backup

      - Comando: `scripts/pg_dump_daily.sh`

      - Destino: object storage / volumen cifrado

      - Retención: 7–30 días

      - Cron: …

      EOF

      # añade backups/ a .gitignore

      git add projects/m19-ops/scripts/pg_dump_daily.sh
      projects/m19-ops/backup.md

      git commit -m "feat(m19): L13 backup automatico postgresql"

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Backup automático PostgreSQL», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Backup automático
          PostgreSQL
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

      `mkdir -p backups`
    comandoEsperado:
      - mkdir -p backups
      - echo "wrote $OUT"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p backups'
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
        texto: Automatizar pg_dump o backup gestionado; retención y ubicación segura.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `echo "wrote $OUT"`
    comandoEsperado:
      - echo "wrote $OUT"
    explicacionError: 'Esperado: echo "wrote $OUT"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/scripts/pg_dump_daily.sh` +
        `projects/m19-ops/backup.md`.
      - 'Commit `docs(m19): L13 backup-automatico-postgresql`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
