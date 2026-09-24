---
id: M11
titulo: Sistemas operativos
etapa: disciplinaria
orden: 11
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Procesos, señales y permisos en Linux
  - id: p2
    titulo: Scripts de administración (backup, rotación logs)
  - id: p3
    titulo: Dockerizar un servicio Node + volumen (sin root innecesario)
proyecto:
  id: proj
  titulo: Playbook de operación local del stack
---

# M11 — Sistemas operativos

## Por qué existe
Tu app corre sobre un SO. Permisos, procesos y contenedores mal puestos = incidentes. Enlace con [hilo seguridad](../../hilos/seguridad.md).

## Análogos
UABC: Administración de SO. Tec: Sistemas operativos.

## Objetivos
Procesos, memoria a alto nivel, FS, permisos, Docker intro seguro.

## Día 1 (2–3 h)
1. `ps`, `top`/`htop`, `chmod`, `chown` — bitácora de 10 comandos.
2. Crea un usuario/grupo de práctica y un archivo con permisos 600.
3. Explica por qué `chmod 777` es casi siempre un error.

## Ejemplo — backup simple
```bash
#!/usr/bin/env bash
set -euo pipefail
DATE=$(date +%F)
pg_dump "$DATABASE_URL" > "backups/db-$DATE.sql"
```

## Temario
Procesos/hilos → memoria/FS → permisos/usuarios → Docker + proyecto playbook.

## Libros (ES)
Silberschatz ed. ES — capítulos selectos.

## Proyecto útil
Scripts + Compose mínimo documentado (DB + API), usuario no-root en contenedor si es posible.

## Errores comunes
Correr todo como root; no probar restore; secretos en imagen Docker.

## Criterios de dominio
- [ ] Explicas proceso vs hilo.
- [ ] Tienes script de backup y al menos un restore de prueba.
