#!/usr/bin/env python3
"""Rewrite M11 lessons to M01/M09 quality (concrete timed steps, no boilerplate)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M11"
BIBLIO = "../../../bibliografia.md#m11-sistemas-operativos"
SILBER = "*Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES)"
NODE_PROCESS = "https://nodejs.org/api/process.html"
DOCKER_DOCS = "https://docs.docker.com/get-started/"


def fm(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, str) and (":" in v or v.startswith("*") or '"' in v or "'" in v):
            safe = v.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def lectura_block(que, enlace_titulo="Node.js process", enlace=NODE_PROCESS):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {SILBER} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11]({BIBLIO}) |
"""


def render(lesson: dict) -> str:
    pub = {
        "id": lesson["id"],
        "materia": "M11",
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
    }
    enlace = lesson.get("_enlace", {})
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(lesson.get("_lectura_corta", lesson["lectura"]), **enlace)}

## Hecho cuando

Marca la lección **solo si**:

{lesson["_hecho"].strip()}

## Errores comunes

{lesson["_errores"].strip()}

## Siguiente

{lesson["siguiente"]}
"""


FILENAMES = {
    1: "L01-procesos-permisos-y-bitacora-dia-1.md",
    2: "L02-proceso-vs-hilo-y-el-runtime-node.md",
    3: "L03-senales-sigterm-y-apagado-graceful.md",
    4: "L04-cierre-semana-1-practica-p1.md",
    5: "L05-memoria-virtual-y-paginacion-intuicion.md",
    6: "L06-observar-rss-y-cpu-de-node.md",
    7: "L07-oom-ulimit-y-sintomas.md",
    8: "L08-cgroups-y-memoria-en-contenedores.md",
    9: "L09-sistema-de-archivos-inodos-y-espacio.md",
    10: "L10-permisos-usuarios-y-minimo-privilegio.md",
    11: "L11-script-de-backup-automatizado-p2.md",
    12: "L12-rotacion-de-logs-y-restore-de-prueba.md",
    13: "L13-imagenes-contenedores-y-volumenes.md",
    14: "L14-dockerfile-node-sin-root-p3.md",
    15: "L15-docker-compose-api-y-base-de-datos.md",
    16: "L16-playbook-local-y-cierre-m11.md",
}

LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Procesos, permisos y bitácora día 1",
        horas=5.0,
        semana=1,
        lectura="Silberschatz — procesos (intro) + permisos básicos",
        evidencia="projects/m11-so/labs/dia1-comandos.md",
        _lectura_corta="PID/PPID, usuario efectivo, permisos rwx, umask",
        _enlace={"enlace_titulo": "man ps (conceptos)", "enlace": "https://man7.org/linux/man-pages/man1/ps.1.html"},
        _hecho="""1. `labs/dia1-comandos.md` con salidas anotadas de `ps`, `id`, `umask` y un archivo `chmod 600`.
2. Párrafo: por qué `chmod 777` es inaceptable para datos de clientes Agenda Ops.
3. Commit `docs(m11): l01 procesos y permisos dia1`.""",
        _errores="""- Pegar `ps aux` completo sin marcar tu shell/node.
- Correr labs como root “porque sí”.
- Dejar el archivo de prueba world-readable.""",
        siguiente="[L02 — Proceso vs hilo y el runtime Node](L02-proceso-vs-hilo-y-el-runtime-node.md)",
        body=r"""
# L01 — Procesos, permisos y bitácora día 1

**~5.0 h · Semana 1**

Agenda Ops correrá en un VPS o contenedor. Hoy lees procesos e identidad como lo harás en un incidente.

## Objetivo

Levantar `projects/m11-so/` y documentar procesos, `id`/`umask` y permisos mínimos.

## Pasos (hazlos en orden)

### 1. Scaffold (15 min)

```bash
mkdir -p projects/m11-so/{labs,scripts,app,samples}
cat projects/m11-so/README.md
```

### 2. Procesos (45 min)

```bash
ps aux | head -20
ps -o pid,ppid,user,stat,cmd --forest | head -40
```

En `labs/dia1-comandos.md`: define PID, PPID, STAT común (R/S/Z a alto nivel).

### 3. Identidad y umask (40 min)

```bash
id
umask
echo "dato-piloto" > "/tmp/m11-test-$USER.txt"
chmod 600 "/tmp/m11-test-$USER.txt"
ls -la "/tmp/m11-test-$USER.txt"
```

Explica owner/group/other.

### 4. Anti-patrón (30 min)

Escribe por qué `chmod 777` en un directorio de backups/logs rompe confidencialidad de clientes.

### 5. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): l01 procesos y permisos dia1"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Proceso vs hilo y el runtime Node",
        horas=5.0,
        semana=1,
        lectura="Silberschatz — hilos + Node event loop",
        evidencia="labs/semana-01-procesos.md sección hilos",
        _lectura_corta="Proceso vs hilo; event loop de Node; workers opcionales",
        _enlace={
            "enlace_titulo": "Node.js — The Node Event Loop",
            "enlace": "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/",
        },
        _hecho="""1. Sección en `labs/semana-01-procesos.md`: proceso vs hilo + cómo encaja el event loop.
2. Experimento: un `node` idle y `ps`/`top` anotando un solo proceso (salvo workers).
3. Commit `docs(m11): l02 proceso vs hilo node`.""",
        _errores="""- Decir “Node es single-thread” sin matizar libuv/threadpool.
- Confundir concurrency con paralelismo CPU.
- Abrir 10 terminales sin documentar qué PID es cuál.""",
        siguiente="[L03 — Señales SIGTERM y apagado graceful](L03-senales-sigterm-y-apagado-graceful.md)",
        body=r"""
# L02 — Proceso vs hilo y el runtime Node

**~5.0 h · Semana 1**

Tu API será un proceso Node. Hoy separas proceso, hilo y event loop con evidencia.

## Objetivo

Explicar proceso vs hilo aplicado al runtime que usarás en M17.

## Pasos

### 1. Conceptos (45 min)

En `labs/semana-01-procesos.md`: espacio de direcciones, hilos compartiendo memoria, costo de context switch (intuición).

### 2. Observa Node (45 min)

```bash
node -e 'setInterval(() => {}, 1000)' &
PID=$!
ps -p $PID -o pid,nlwp,cmd
# nlwp ≈ número de hilos ligeros reportados
kill $PID
```

Anota qué ves y qué significa para “Node es single-threaded” (JS en un hilo; pool de libuv aparte).

### 3. Agenda Ops (30 min)

¿Dónde pondrías CPU-bound (reporte pesado)? ¿Worker thread, job queue, o otro servicio? 6–8 líneas.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-01-procesos.md
git commit -m "docs(m11): l02 proceso vs hilo node"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Señales SIGTERM y apagado graceful",
        horas=5.0,
        semana=1,
        lectura="Silberschatz — señales + Node process signals",
        evidencia="labs/sigterm-node.md + app/graceful-server.js",
        _lectura_corta="SIGTERM vs SIGKILL; graceful shutdown de servidor HTTP",
        _hecho="""1. `app/graceful-server.js` maneja SIGTERM, deja de aceptar conexiones y cierra con timeout.
2. `labs/sigterm-node.md` documenta prueba con `kill -TERM` vs `kill -KILL`.
3. Commit `feat(m11): l03 graceful sigterm`.""",
        _errores="""- Ignorar SIGTERM y solo morir con SIGKILL en deploy.
- No poner timeout de cierre (conexiones eternas).
- Confundir Ctrl+C (SIGINT) con lo que envía Kubernetes/Docker.""",
        siguiente="[L04 — Cierre semana 1 — práctica P1](L04-cierre-semana-1-practica-p1.md)",
        body=r"""
# L03 — Señales SIGTERM y apagado graceful

**~5.0 h · Semana 1**

En deploy (M19) el orquestador envía SIGTERM. Si lo ignoras, cortas citas a medias.

## Objetivo

Un servidor HTTP Node que apaga en orden al recibir SIGTERM.

## Pasos

### 1. Código (75–90 min)

Crea `projects/m11-so/app/graceful-server.js`:

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("ok\n");
});

const port = Number(process.env.PORT || 3099);
server.listen(port, "127.0.0.1", () => console.log("listen", port));

function shutdown(signal) {
  console.log("got", signal, "closing…");
  server.close(() => {
    console.log("closed");
    process.exit(0);
  });
  setTimeout(() => {
    console.error("force exit");
    process.exit(1);
  }, 10_000).unref();
}

process.on("SIGTERM", () => shutdown("SIGTERM"));
process.on("SIGINT", () => shutdown("SIGINT"));
```

### 2. Prueba (40 min)

```bash
node projects/m11-so/app/graceful-server.js &
PID=$!
curl -s http://127.0.0.1:3099/
kill -TERM $PID
wait $PID
```

Repite idea con `kill -KILL` y documenta la diferencia en `labs/sigterm-node.md`.

### 3. Commit (15 min)

```bash
git add projects/m11-so/app projects/m11-so/labs/sigterm-node.md
git commit -m "feat(m11): l03 graceful sigterm"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Cierre semana 1 — práctica P1",
        horas=5.0,
        semana=1,
        lectura="Repaso Silberschatz procesos",
        evidencia="labs/semana-01-procesos.md consolidado (P1)",
        _lectura_corta="Síntesis procesos/hilos/señales; checklist P1 parcial",
        _hecho="""1. `labs/semana-01-procesos.md` unifica L01–L03 con comandos reproducibles.
2. README marca P1 parcial (procesos/señales).
3. Commit `docs(m11): l04 cierre semana 1 p1`.""",
        _errores="""- Labs sin comandos copiables.
- Código graceful sin nota de prueba.
- Checklist vacía.""",
        siguiente="[L05 — Memoria virtual y paginación (intuición)](L05-memoria-virtual-y-paginacion-intuicion.md)",
        body=r"""
# L04 — Cierre semana 1 — práctica P1

**~5.0 h · Semana 1**

P1 es bitácora de procesos/señales/permisos. Hoy la dejas revisable.

## Objetivo

Consolidar semana 1 y actualizar el README.

## Pasos

### 1. Inventario (25 min)

```bash
find projects/m11-so -type f | sort
```

### 2. Consolida (90–110 min)

`semana-01-procesos.md` con secciones: dia1, proceso vs hilo, SIGTERM (enlace al código). Incluye 3 comandos “runbook” de diagnóstico.

### 3. README (40 min)

Checklist:

- [x] labs dia1
- [x] notas hilos/event loop
- [x] graceful-server + prueba

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): l04 cierre semana 1 p1"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Memoria virtual y paginación (intuición)",
        horas=5.0,
        semana=2,
        lectura="Silberschatz — memoria virtual",
        evidencia="labs/semana-02-memoria.md",
        _lectura_corta="Espacio virtual vs físico; páginas; swap/thrashing intuición",
        _hecho="""1. `labs/semana-02-memoria.md` explica virtual vs RSS vs swap en lenguaje propio.
2. Comandos `free -h` / `/proc/meminfo` (o equivalente) anotados.
3. Commit `docs(m11): l05 memoria virtual`.""",
        _errores="""- Equivaler “memoria virtual” con “archivo swap” solamente.
- Diagramas copiados sin explicación.
- Ignorar qué pasa cuando el VPS de Agenda Ops thrashing-ea.""",
        siguiente="[L06 — Observar RSS y CPU de Node](L06-observar-rss-y-cpu-de-node.md)",
        body=r"""
# L05 — Memoria virtual y paginación (intuición)

**~5.0 h · Semana 2**

OOM y lentitud empiezan cuando no entiendes qué es RSS. Hoy el modelo mental.

## Objetivo

Documentar memoria virtual/paginación a nivel operador.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/semana-02-memoria.md`: página, page fault (suave/duro), por qué un proceso “pide” más de la RAM física.

### 2. Host (40 min)

```bash
free -h
head -20 /proc/meminfo
```

Define MemAvailable vs swap used en tus palabras.

### 3. Producto (30 min)

Escenario: VPS 1 GB con API + Postgres. Qué síntomas verías antes del OOM killer.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-02-memoria.md
git commit -m "docs(m11): l05 memoria virtual"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Observar RSS y CPU de Node",
        horas=5.0,
        semana=2,
        lectura="man ps, top/htop",
        evidencia="labs/rss-node.md",
        _lectura_corta="RSS/VSZ; %CPU; process.memoryUsage() en Node",
        _hecho="""1. `labs/rss-node.md` con mediciones de un proceso Node (ps + memoryUsage).
2. Script o one-liner que imprime heap/rss.
3. Commit `docs(m11): l06 rss cpu node`.""",
        _errores="""- Mirar solo VSZ y asustarse.
- Medir una vez sin carga ni idle.
- No anotar unidades (kB vs MB).""",
        siguiente="[L07 — OOM, ulimit y síntomas](L07-oom-ulimit-y-sintomas.md)",
        body=r"""
# L06 — Observar RSS y CPU de Node

**~5.0 h · Semana 2**

Mides el proceso que importa: tu runtime.

## Objetivo

Capturar RSS/CPU de Node y `process.memoryUsage()`.

## Pasos

### 1. Proceso de muestra (50 min)

```bash
node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5)); console.log(process.memoryUsage());}, 1000)' &
PID=$!
sleep 3
ps -p $PID -o pid,pcpu,rss,vsz,cmd
kill $PID
```

Copia números a `labs/rss-node.md` e interpreta rss vs heapUsed.

### 2. top (30 min)

```bash
# una snapshot:
ps aux --sort=-%mem | head -15
```

Localiza `node` si queda alguno.

### 3. Nota ops (30 min)

Qué alarma pondrías en el piloto (RSS > X MB sostenido).

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/rss-node.md
git commit -m "docs(m11): l06 rss cpu node"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="OOM, ulimit y síntomas",
        horas=5.0,
        semana=2,
        lectura="Silberschatz OOM + ulimit man",
        evidencia="labs/oom-ulimit.md",
        _lectura_corta="OOM killer; ulimit -n/-v; síntomas en logs",
        _hecho="""1. `labs/oom-ulimit.md` con `ulimit -a` anotado y escenarios OOM.
2. Lista de síntomas (exit 137, dmesg OOM, contenedor reiniciando).
3. Commit `docs(m11): l07 oom ulimit`.""",
        _errores="""- Forzar OOM en máquina compartida sin cuidado.
- Ignorar file descriptors (`ulimit -n`) en APIs con muchas conexiones.
- Culpar “Node lento” cuando es thrashing.""",
        siguiente="[L08 — cgroups y memoria en contenedores](L08-cgroups-y-memoria-en-contenedores.md)",
        body=r"""
# L07 — OOM, ulimit y síntomas

**~5.0 h · Semana 2**

Cuando el kernel mata tu API, el síntoma parece “se reinició solo”. Hoy lo reconoces.

## Objetivo

Documentar límites (`ulimit`) y la firma de un OOM.

## Pasos

### 1. ulimit (30 min)

```bash
ulimit -a
ulimit -n
```

Anota open files y qué pasaría si la API abre demasiados sockets.

### 2. Señales OOM (60 min)

En `labs/oom-ulimit.md` documenta (sin tumbar el host):

- exit code 137 (128+9 SIGKILL) en contenedores
- `dmesg | grep -i oom` (si tienes permiso)
- restart loops en compose

### 3. Runbook corto (40 min)

Pasos si Agenda Ops cae por memoria: mirar RSS, logs PG, bajar concurrency, subir RAM o limitar cgroup.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/oom-ulimit.md
git commit -m "docs(m11): l07 oom ulimit"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="cgroups y memoria en contenedores",
        horas=5.0,
        semana=2,
        lectura="Docker docs memory + Silberschatz resumen",
        evidencia="labs/cgroups-nota.md",
        _lectura_corta="cgroups memoria/CPU; docker run -m; por qué el límite no es “RAM del host”",
        _enlace={
            "enlace_titulo": "Docker · Memory constraints",
            "enlace": "https://docs.docker.com/config/containers/resource_constraints/",
        },
        _hecho="""1. `labs/cgroups-nota.md` explica límite `-m`/`mem_limit` y qué ve el proceso.
2. Experimento documentado con `docker run --memory` (o nota si Docker no está disponible + comandos listos).
3. Commit `docs(m11): l08 cgroups memoria`.""",
        _errores="""- Contenedor sin límite en un VPS pequeño compartiendo con Postgres.
- Confundir límite soft/hard.
- Pensar que cgroup “arregla leaks”.""",
        siguiente="[L09 — Sistema de archivos: inodos y espacio](L09-sistema-de-archivos-inodos-y-espacio.md)",
        body=r"""
# L08 — cgroups y memoria en contenedores

**~5.0 h · Semana 2**

Docker no “aisla magia”: usa cgroups. Hoy lo conectas con OOM de contenedor.

## Objetivo

Explicar límites de memoria en contenedores con un experimento o procedimiento escrito.

## Pasos

### 1. Lectura (40 min)

Docker memory constraints + idea de cgroup v1/v2 (alto nivel). Notas en `labs/cgroups-nota.md`.

### 2. Experimento (60–75 min)

Si tienes Docker:

```bash
docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0 || true
```

Documenta el fallo. Si no hay Docker: deja el comando y describe el resultado esperado + plan de verificación en L13.

### 3. Diseño piloto (30 min)

Propón límites tentativos API vs Postgres en un VPS 2 GB.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/cgroups-nota.md
git commit -m "docs(m11): l08 cgroups memoria"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Sistema de archivos: inodos y espacio",
        horas=5.0,
        semana=3,
        lectura="Silberschatz sistema de archivos",
        evidencia="labs/semana-03-fs.md",
        _lectura_corta="Inodos, enlaces, df/du; quedarse sin inodos vs sin bloques",
        _hecho="""1. `labs/semana-03-fs.md` con `df -h`, `df -i`, `du -sh` anotados.
2. Explicas diferencia “disco lleno” vs “sin inodos”.
3. Commit `docs(m11): l09 filesystem inodos`.""",
        _errores="""- Borrar logs a ciegas en prod.
- Llenar disco con dumps de BD sin rotación.
- Ignorar tamaño de `node_modules`/imágenes Docker.""",
        siguiente="[L10 — Permisos, usuarios y mínimo privilegio](L10-permisos-usuarios-y-minimo-privilegio.md)",
        body=r"""
# L09 — Sistema de archivos: inodos y espacio

**~5.0 h · Semana 3**

Backups y logs viven en disco. Hoy mides espacio e inodos.

## Objetivo

Diagnosticar uso de disco como operador del piloto.

## Pasos

### 1. Medición (45 min)

```bash
df -h
df -i
du -sh projects/* 2>/dev/null | sort -h
```

### 2. Conceptos (45 min)

Inodo vs nombre de archivo; hardlink vs symlink (una tabla). Qué pasa con muchas fotos/tmp de citas.

### 3. Política (30 min)

Dónde vivirían backups y logs de Agenda Ops; cuota mínima libre antes de alerta.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-03-fs.md
git commit -m "docs(m11): l09 filesystem inodos"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Permisos, usuarios y mínimo privilegio",
        horas=5.0,
        semana=3,
        lectura="Silberschatz protección",
        evidencia="labs/permisos.md",
        _lectura_corta="chmod/chown, usuarios/grupos, least privilege en datos y logs",
        _hecho="""1. `labs/permisos.md` con árbol de permisos propuesto para `backups/`, `logs/`, `.env`.
2. Demostración local de archivo 600 vs intento de lectura con otro usuario (o explicación equivalente).
3. Commit `docs(m11): l10 permisos least privilege`.""",
        _errores="""- `chmod 777` otra vez.
- Meter el usuario de la app en grupo docker sin necesidad.
- Secretos con ACL abierta en el repo.""",
        siguiente="[L11 — Script de backup automatizado (P2)](L11-script-de-backup-automatizado-p2.md)",
        body=r"""
# L10 — Permisos, usuarios y mínimo privilegio

**~5.0 h · Semana 3**

Least privilege en host es parte del [hilo de seguridad](../../../hilos/seguridad.md).

## Objetivo

Definir permisos para datos sensibles del piloto.

## Pasos

### 1. Lab (50 min)

```bash
mkdir -p projects/m11-so/samples/permisos-demo
echo 'fake-secret' > projects/m11-so/samples/permisos-demo/secret.env
chmod 600 projects/m11-so/samples/permisos-demo/secret.env
ls -la projects/m11-so/samples/permisos-demo
# secret.env es demo: no pongas secretos reales; añade samples/ al criterio de no-commit si hace falta
```

Asegura que `secret.env` **no** se commitea si contiene algo real — usa placeholder y `.gitignore` si es necesario. Mejor: documenta solo `ls -la` y borra el secreto.

### 2. Política (60 min)

En `labs/permisos.md`: owner del proceso API, grupo, modo de `backups/*.sql`, logs, claves TLS.

### 3. Commit (15 min)

```bash
git add projects/m11-so/labs/permisos.md
git commit -m "docs(m11): l10 permisos least privilege"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Script de backup automatizado (P2)",
        horas=5.0,
        semana=3,
        lectura="Silberschatz I/O + bash strict",
        evidencia="projects/m11-so/scripts/backup.sh",
        _lectura_corta="Bash set -euo pipefail; pg_dump vía env; retención",
        _hecho="""1. `scripts/backup.sh` con `set -euo pipefail`, usa env vars (sin passwords hardcode).
2. Dry-run o corrida contra archivo/fixture documentada en labs.
3. Commit `feat(m11): l11 backup.sh`.""",
        _errores="""- Password en el script.
- Backup que “funciona” sin fecha en el nombre.
- No fallar si `pg_dump` no existe (ocultar errores).""",
        siguiente="[L12 — Rotación de logs y restore de prueba](L12-rotacion-de-logs-y-restore-de-prueba.md)",
        body=r"""
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
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Rotación de logs y restore de prueba",
        horas=5.0,
        semana=3,
        lectura="logrotate concept + tu script de backup",
        evidencia="restore-prueba.md + script rotación",
        _lectura_corta="Rotación por tamaño/fecha; restore de backup a destino de prueba",
        _hecho="""1. Script de rotación de logs (o backups) en `scripts/`.
2. `restore-prueba.md` con fecha, comandos y resultado (aunque sea fixture).
3. Commit `feat(m11): l12 rotacion y restore`.""",
        _errores="""- Backup sin restore de prueba.
- Rotar borrando el único backup bueno.
- Restore sobre prod sin decirlo.""",
        siguiente="[L13 — Imágenes, contenedores y volúmenes](L13-imagenes-contenedores-y-volumenes.md)",
        body=r"""
# L12 — Rotación de logs y restore de prueba

**~5.0 h · Semana 3**

Un backup no probado es un cuento. Hoy rotas y restauras.

## Objetivo

Cerrar P2 con rotación + `restore-prueba.md`.

## Pasos

### 1. Rotación (60 min)

`scripts/rotate-logs.sh`: mueve `logs/app.log` a `logs/app-$(date +%F).log` si supera N bytes; comprime; borra >RETENTION.

### 2. Restore de prueba (75–90 min)

```bash
# idea; ajusta a tu motor
# createdb agenda_restore_test
# gunzip -c backups/db-….sql.gz | psql agenda_restore_test
```

Documenta en `restore-prueba.md`: fecha, origen, destino, verificación (`SELECT count(*)` o equivalente en fixture).

### 3. README P2 (20 min)

Marca P2 listo con enlaces a scripts + restore.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "feat(m11): l12 rotacion y restore"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Imágenes, contenedores y volúmenes",
        horas=5.0,
        semana=4,
        lectura="Docker docs get started + Silberschatz síntesis",
        evidencia="labs/docker-intro.md",
        _lectura_corta="Imagen vs contenedor; capas; volúmenes para datos persistentes",
        _enlace={"enlace_titulo": "Docker Get Started", "enlace": DOCKER_DOCS},
        _hecho="""1. `labs/docker-intro.md` con vocabulario y un `docker run`/`volume` documentado.
2. Explicas por qué el FS del contenedor no basta para Postgres.
3. Commit `docs(m11): l13 docker intro`.""",
        _errores="""- Guardar la BD solo en la capa writable del contenedor.
- Confundir bind mount con named volume.
- Correr todo `--privileged`.""",
        siguiente="[L14 — Dockerfile Node sin root (P3)](L14-dockerfile-node-sin-root-p3.md)",
        body=r"""
# L13 — Imágenes, contenedores y volúmenes

**~5.0 h · Semana 4**

Antes del Dockerfile de la API: vocabulario sólido.

## Objetivo

Dejar notas reproducibles de imagen/contenedor/volumen.

## Pasos

### 1. Vocabulario (40 min)

Tabla en `labs/docker-intro.md`: image, container, layer, registry, volume, network.

### 2. Lab (60–75 min)

```bash
docker version
docker run --rm hello-world
docker volume create m11-demo
docker run --rm -v m11-demo:/data alpine sh -c 'echo hola >/data/x; cat /data/x'
```

Si Docker no está: instálalo o documenta el bloqueo y comandos exactos para cuando lo tengas (el playbook L16 lo exigirá).

### 3. Postgres (30 min)

Por qué el volumen sobrevive a `docker rm` y por qué eso importa en Agenda Ops.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/docker-intro.md
git commit -m "docs(m11): l13 docker intro"
```
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="Dockerfile Node sin root (P3)",
        horas=5.0,
        semana=4,
        lectura="Dockerfile reference USER",
        evidencia="projects/m11-so/Dockerfile",
        _lectura_corta="USER no-root; npm ci; no secretos en capas",
        _enlace={
            "enlace_titulo": "Dockerfile reference",
            "enlace": "https://docs.docker.com/reference/dockerfile/",
        },
        _hecho="""1. `Dockerfile` multi-stage o slim con `USER` no-root.
2. App mínima en `app/` que responde HTTP; build documentado.
3. Commit `feat(m11): l14 dockerfile non-root`.""",
        _errores="""- Correr como root sin justificación.
- `COPY .` con `.env` dentro.
- `npm install` en runtime en vez de build.""",
        siguiente="[L15 — docker compose: API y base de datos](L15-docker-compose-api-y-base-de-datos.md)",
        body=r"""
# L14 — Dockerfile Node sin root (P3)

**~5.0 h · Semana 4**

P3: imagen de servicio Node endurecida lo razonable para local/piloto.

## Objetivo

Escribir un `Dockerfile` que no corra como root.

## Pasos

### 1. App mínima (40 min)

Reutiliza o adapta `app/graceful-server.js` como `CMD`. Añade `app/package.json` si hace falta (`"type":"module"`).

### 2. Dockerfile (75 min)

```dockerfile
FROM node:20-bookworm-slim
WORKDIR /app
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app app/package*.json ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY --chown=app:app app/ ./
USER app
EXPOSE 3099
CMD ["node", "graceful-server.js"]
```

Ajusta rutas a tu layout. Documenta build:

```bash
docker build -t m11-api:dev -f projects/m11-so/Dockerfile projects/m11-so
docker run --rm -p 127.0.0.1:3099:3099 m11-api:dev
```

### 3. Verificación user (30 min)

```bash
docker run --rm m11-api:dev id
```

Debe ser `app`, no `root`.

### 4. Commit (15 min)

```bash
git add projects/m11-so/Dockerfile projects/m11-so/app
git commit -m "feat(m11): l14 dockerfile non-root"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="docker compose: API y base de datos",
        horas=5.0,
        semana=4,
        lectura="Compose file reference",
        evidencia="docker-compose.yml documentado",
        _lectura_corta="Servicios api+db; red interna; volúmenes; no exponer 5432 públicamente",
        _enlace={
            "enlace_titulo": "Compose specification",
            "enlace": "https://docs.docker.com/compose/compose-file/",
        },
        _hecho="""1. `docker-compose.yml` con API + Postgres, volumen, red, env desde `.env.example`.
2. Nota: puerto DB solo interno o localhost; API en localhost.
3. Commit `feat(m11): l15 compose api db`.""",
        _errores="""- Publicar `5432:5432` a 0.0.0.0 sin necesidad.
- Passwords en el YAML commiteadas.
- Olvidar healthcheck / depends_on con criterio.""",
        siguiente="[L16 — Playbook local y cierre M11](L16-playbook-local-y-cierre-m11.md)",
        body=r"""
# L15 — docker compose: API y base de datos

**~5.0 h · Semana 4**

El stack local del piloto: API + Postgres como en Agenda Ops.

## Objetivo

Dejar `docker-compose.yml` usable y documentado.

## Pasos

### 1. Compose (90 min)

`projects/m11-so/docker-compose.yml` (ajusta nombres):

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: agenda
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: agenda
    volumes:
      - pgdata:/var/lib/postgresql/data
    # no ports: públicos; la API habla por la red compose
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U agenda"]
      interval: 5s
      timeout: 5s
      retries: 5
  api:
    build: .
    environment:
      PORT: 3099
      DATABASE_URL: postgres://agenda:${POSTGRES_PASSWORD}@db:5432/agenda
    ports:
      - "127.0.0.1:3099:3099"
    depends_on:
      db:
        condition: service_healthy
volumes:
  pgdata:
```

### 2. Env example (30 min)

`.env.example` con `POSTGRES_PASSWORD=change-me`. `.env` en `.gitignore`.

### 3. Up (40 min)

```bash
cd projects/m11-so
cp -n .env.example .env
docker compose up -d --build
curl -s http://127.0.0.1:3099/
docker compose ps
```

### 4. Commit (15 min)

```bash
git add projects/m11-so/docker-compose.yml projects/m11-so/.env.example
git commit -m "feat(m11): l15 compose api db"
```
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Playbook local y cierre M11",
        horas=5.0,
        semana=4,
        lectura="Ficha M11 completa",
        evidencia="playbook.md + cierre P1–P3",
        _lectura_corta="Playbook reproducible: up/down/backup/restore",
        _hecho="""1. `playbook.md` con prerequisitos, up/down, backup, restore, troubleshooting.
2. README enlaza P1 labs, P2 scripts, P3 Docker, playbook.
3. Commit `docs(m11): cierre playbook`.""",
        _errores="""- Playbook que solo funciona en tu cabeza.
- Secretos en el playbook.
- Marcar dominio sin restore documentado.""",
        siguiente="Cierra la [ficha M11](../M11-sistemas-operativos.md). Recomendado: [M27](../M27-sistemas-bajo-nivel.md) o sigue a [M12](../M12-requerimientos.md).",
        body=r"""
# L16 — Playbook local y cierre M11

**~5.0 h · Semana 4**

Otro desarrollador debe levantar el stack solo con tu playbook.

## Objetivo

Publicar `playbook.md` y cerrar evidencias P1–P3.

## Pasos

### 1. Redacta playbook (90–110 min)

`projects/m11-so/playbook.md`:

- Prerequisitos (Docker, puertos)
- `cp .env.example .env` + editar
- `docker compose up -d --build`
- Healthcheck curl
- Backup (`scripts/backup.sh`)
- Restore de prueba (enlace)
- `docker compose down`
- Diagrama Mermaid host → api/db → volume

### 2. Dry-run (50 min)

Sigue el playbook desde cero (borra contenedores) y anota fricciones; corrígelas.

### 3. Checklist dominio (30 min)

Responde en `dominio-oral.md`: SIGTERM, backup+restore, non-root, playbook ajeno.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): cierre playbook"
```
""",
    )
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(LESSONS) == 16, len(LESSONS)
    for lesson in LESSONS:
        path = OUT / FILENAMES[lesson["orden"]]
        text = render(lesson)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
