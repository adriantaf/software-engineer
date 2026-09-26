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

## Cómo estudiar esta materia (lecciones)

M11 usa lecciones L01–L16 (como M01): terminal, scripts y Docker con evidencia en `projects/m11-so/`.

1. Orden **L01 → L16**; marca solo con “Hecho cuando” cumplido.
2. Cada concepto del libro → **un comando o experimento** el mismo día.
3. Piensa en el stack de **Agenda Ops** (API Node + Postgres en contenedor).
4. Prácticas P1–P3 y playbook se distribuyen en las lecciones indicadas.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Procesos / memoria / FS | 10–12 | 4 lecciones (~5 h c/u) |
| Scripts ops (P2) | 4–6 | Backup, rotación, restore |
| Docker + playbook (P3) | 4–6 | Imagen no-root, compose |
| Retro | 1 | Permiso o señal que evitó un incidente |

Si un día solo tienes 2 h: **una lección práctica**. No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Procesos, hilos y señales (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Procesos, permisos y bitácora día 1](M11/L01-procesos-permisos-y-bitacora-dia-1.md) | 5 |
| L02 | [Proceso vs hilo y el runtime Node](M11/L02-proceso-vs-hilo-y-el-runtime-node.md) | 5 |
| L03 | [Señales SIGTERM y apagado graceful](M11/L03-senales-sigterm-y-apagado-graceful.md) | 5 |
| L04 | [Cierre semana 1 — práctica P1](M11/L04-cierre-semana-1-practica-p1.md) | 5 |

### Semana 2 — Memoria y contenedores (cgroups) (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Memoria virtual y paginación (intuición)](M11/L05-memoria-virtual-y-paginacion-intuicion.md) | 5 |
| L06 | [Observar RSS y CPU de Node](M11/L06-observar-rss-y-cpu-de-node.md) | 5 |
| L07 | [OOM, ulimit y síntomas](M11/L07-oom-ulimit-y-sintomas.md) | 5 |
| L08 | [cgroups y memoria en contenedores](M11/L08-cgroups-y-memoria-en-contenedores.md) | 5 |

### Semana 3 — Archivos, permisos y scripts ops (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Sistema de archivos: inodos y espacio](M11/L09-sistema-de-archivos-inodos-y-espacio.md) | 5 |
| L10 | [Permisos, usuarios y mínimo privilegio](M11/L10-permisos-usuarios-y-minimo-privilegio.md) | 5 |
| L11 | [Script de backup automatizado (P2)](M11/L11-script-de-backup-automatizado-p2.md) | 5 |
| L12 | [Rotación de logs y restore de prueba](M11/L12-rotacion-de-logs-y-restore-de-prueba.md) | 5 |

### Semana 4 — Docker y playbook local (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Imágenes, contenedores y volúmenes](M11/L13-imagenes-contenedores-y-volumenes.md) | 5 |
| L14 | [Dockerfile Node sin root (P3)](M11/L14-dockerfile-node-sin-root-p3.md) | 5 |
| L15 | [docker compose: API y base de datos](M11/L15-docker-compose-api-y-base-de-datos.md) | 5 |
| L16 | [Playbook local y cierre M11](M11/L16-playbook-local-y-cierre-m11.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES). Catálogo: [bibliografía](../../bibliografia.md#m11-sistemas-operativos).

| Semana | Lecciones | Capítulos (por tema) | Alternativa / práctica |
|--------|-----------|----------------------|-------------------------|
| 1 | L01–L04 | **Procesos e hilos** + señales | `ps`, `top`, Node + SIGTERM |
| 2 | L05–L08 | **Memoria** virtual, OOM, cgroups | RSS Node, límites Docker |
| 3 | L09–L12 | **Sistema de archivos** + protección | Permisos, backup P2 |
| 4 | L13–L16 | **Contenedores** + síntesis | Dockerfile, compose, playbook |

**Regla:** un experimento documentado por semana en `projects/m11-so/`.



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

## Siguiente

**[M27 — Sistemas a bajo nivel](M27-sistemas-bajo-nivel.md)** (recomendado antes de seguir a M12 si quieres profundidad de sistemas). Luego M12 requerimientos / hilo Agenda Ops.

## Criterios de dominio

- [ ] Explicas proceso vs hilo y qué hace una señal `SIGTERM` en tu API.
- [ ] Tienes script de backup y al menos un restore de prueba documentado.
- [ ] Tu contenedor Node no corre como root sin justificación escrita.
- [ ] Otro desarrollador puede levantar el stack local siguiendo solo tu playbook.
