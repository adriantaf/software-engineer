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

Tu aplicación no flota en el vacío: corre sobre un kernel, con procesos, memoria, archivos y permisos. Un contenedor mal configurado o un backup que nunca probaste restaurar se convierten en incidentes reales cuando llega el piloto de [Agenda Ops](../../producto-saas.md) (M17). Esta materia enlaza con el [hilo de seguridad](../../hilos/seguridad.md): least privilege en el host y en la imagen.

**En resumen:** administras procesos, permisos y un contenedor sin abusar de root ni meter secretos en la imagen.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Explicar proceso vs hilo y qué implica el scheduling a nivel de operación (no teoría de exámenes).
2. Leer uso de memoria de un proceso Node y reconocer síntomas de OOM.
3. Aplicar permisos de archivos y usuarios/grupos con criterio (evitar `chmod 777`).
4. Escribir scripts bash con `set -euo pipefail` para backup y rotación de logs.
5. Empaquetar un servicio Node en Docker con volumen persistente y usuario no-root cuando sea posible.
6. Documentar un playbook local reproducible para levantar API + base de datos.

## Cómo estudiar esta materia

- Cada concepto del libro → **un comando o experimento** el mismo día en `projects/m11-so/`.
- Piensa siempre en el stack que usarás en M17: Postgres en contenedor o local, API Node, variables en `.env` fuera de la imagen.
- No memorices tablas del kernel: documenta **qué observaste** (`ps`, `top`, `df`, logs).
- Lee [Cómo estudiar](../../como-estudiar.md) si aún no tienes la rutina de 20 h/semana.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Procesos/permisos | 6–8 | Labs Linux + bitácora |
| Scripts ops | 6–8 | Backup / rotación logs |
| Docker | 4–6 | Imagen Node + volumen; user no-root |
| Retro | 1 | Un permiso o señal que te salvó de un error |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea la carpeta de evidencia:
   ```bash
   mkdir -p projects/m11-so/labs
   ```
2. Ejecuta y anota en `projects/m11-so/labs/dia1-comandos.md` (mínimo 10 líneas con salida resumida):
   ```bash
   ps aux | head
   top -b -n 1 | head -20    # o htop si lo tienes
   id
   umask
   ls -la /tmp | head
   ```
3. Crea un usuario o grupo de **práctica** (o usa un directorio propio) y un archivo con permisos `600`; prueba leerlo con otro usuario si puedes.
4. Escribe en la misma nota **por qué `chmod 777` es casi siempre un error** en un servidor o volumen de datos.
5. Haz un commit atómico, por ejemplo: `docs(m11): bitácora día 1 procesos y permisos`.

## Ejemplo — backup simple con rotación

```bash
#!/usr/bin/env bash
set -euo pipefail
BACKUP_DIR="${BACKUP_DIR:-./backups}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"
mkdir -p "$BACKUP_DIR"
DATE=$(date +%F)
# Ajusta el comando a tu motor (pg_dump, mysqldump, etc.)
pg_dump "$DATABASE_URL" > "$BACKUP_DIR/db-$DATE.sql"
find "$BACKUP_DIR" -name 'db-*.sql' -mtime +"$RETENTION_DAYS" -delete
```

Regla: el script debe poder ejecutarse en cron o en un job de CI **sin** secretos hardcodeados (usa variables de entorno).

## Ejemplo — Dockerfile con usuario no-root (idea)

```dockerfile
FROM node:20-bookworm-slim
WORKDIR /app
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app package*.json ./
RUN npm ci --omit=dev
COPY --chown=app:app . .
USER app
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

Los secretos van en `.env` / secret manager del host, **no** en `docker build`.

## Temario semanal

### Semana 1 — Procesos, hilos y señales (~20 h)

- Estados de proceso; proceso vs hilo en tu runtime (Node event loop + workers opcionales).
- Comandos: `ps`, `top`/`htop`, `kill`, señales `SIGTERM` / `SIGKILL`.
- Experimento: un proceso Node que ignora vs maneja `SIGTERM` (graceful shutdown).
- Bitácora en `projects/m11-so/labs/semana-01-procesos.md`.

### Semana 2 — Memoria y rendimiento a nivel SO (~20 h)

- Memoria virtual y paginación (intuición); por qué aparece OOM.
- Observar RSS/CPU de tu API o de `node` bajo carga ligera.
- Límites: `ulimit` intro; relación con contenedores (cgroups, alto nivel).
- Nota: qué harías si el piloto Agenda Ops se queda sin RAM en un VPS pequeño.

### Semana 3 — Sistema de archivos, I/O y permisos (~20 h)

- Inodos, rutas, enlaces; `df`, `du`, permisos `rwx`, `umask`.
- Usuarios, grupos, `chmod`/`chown`; principio de mínimo privilegio para datos y logs.
- Práctica P2: script de rotación de logs (tamaño o fecha) versionado en el repo.
- Ensayo de restore de un backup (aunque sea a una BD vacía de prueba).

### Semana 4 — Contenedores + playbook local (~20 h)

- Imagen vs contenedor; volúmenes para datos persistentes (Postgres).
- `docker compose` mínimo: API + DB; redes internas; no publicar puertos de DB sin necesidad.
- Práctica P3: Dockerfile Node + volumen; usuario no-root documentado.
- Proyecto: playbook en `projects/m11-so/playbook.md` (levantar, parar, backup, restore).

## Lecturas

Canon: *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES). Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Capítulos (Silberschatz, por tema) | Alternativa / práctica |
|--------|-----------------------------------|-------------------------|
| 1 | **Procesos e hilos** + scheduling (intro) | `ps`, `top`, experimento Node + señales |
| 2 | **Memoria** (paginación, virtual) + por qué OOM | Observa RSS de un proceso Node bajo carga |
| 3 | **Sistema de archivos** + I/O + protección | Labs lectura/escritura + permisos `600`/`750` |
| 4 | **Concurrencia** intro (condiciones de carrera) + síntesis | Enlaza con contenedores y tu playbook M11 |

**Regla:** un experimento de SO por semana documentado en `projects/m11-so/` (comando → qué viste → qué implica para tu stack).

## Prácticas

1. **P1 — Labs:** Notas de procesos, señales y permisos con comandos reproducibles (`projects/m11-so/labs/`).
2. **P2 — Scripts:** Backup automatizado + rotación de logs (o backups) en scripts versionados; al menos **un** restore de prueba documentado.
3. **P3 — Docker:** `Dockerfile` para servicio Node + volumen de datos; contenedor sin root innecesario; `docker-compose.yml` o equivalente documentado.

## Proyecto útil

**Playbook de operación local del stack:** en `projects/m11-so/` deja:

- `playbook.md`: prerequisitos, `docker compose up`, variables de entorno, cómo hacer backup y restore.
- Scripts en `scripts/` o `projects/m11-so/scripts/` referenciados desde el playbook.
- Diagrama simple (texto o Mermaid): host → contenedores → volumen Postgres.

Este playbook es la base ops antes de M19 (staging/prod).

## Errores comunes

- Correr todo como `root` en el host o en el contenedor “porque es más fácil”.
- `chmod 777` en directorios de datos o logs compartidos.
- Backup sin **restore de prueba** (descubres el fallo el día del incidente).
- Secretos en la imagen Docker o en capas cacheadas del build.
- Exponer el puerto de la base de datos al mundo en `docker-compose` “solo en local” y olvidar quitarlo después.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Labs:** `projects/m11-so/labs/` con notas de procesos/señales/permisos (mín. semanas 1 y 3).
- **P2 — Scripts:** Scripts de backup + rotación en el repo; entrada en `projects/m11-so/restore-prueba.md` (fecha y resultado del restore).
- **P3 — Docker:** `projects/m11-so/Dockerfile` (o ruta documentada) + `docker-compose.yml` + nota de usuario no-root.
- **Proyecto — Playbook:** `projects/m11-so/playbook.md` completo y enlazado desde `projects/m11-so/README.md`.

## Criterios de dominio

- [ ] Explicas proceso vs hilo y qué hace una señal `SIGTERM` en tu API.
- [ ] Tienes script de backup y al menos un restore de prueba documentado.
- [ ] Tu contenedor Node no corre como root sin justificación escrita.
- [ ] Otro desarrollador puede levantar el stack local siguiendo solo tu playbook.
