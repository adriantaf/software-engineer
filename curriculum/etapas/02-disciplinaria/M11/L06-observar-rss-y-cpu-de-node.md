---
id: L06
materia: M11
orden: 6
titulo: Observar RSS y CPU de Node
horas: 5.0
semana: 2
lectura: man ps, top/htop
evidencia: labs/rss-node.md
---

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | RSS/VSZ; %CPU; process.memoryUsage() en Node | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/rss-node.md` con mediciones de un proceso Node (ps + memoryUsage).
2. Script o one-liner que imprime heap/rss.
3. Commit `docs(m11): l06 rss cpu node`.

## Errores comunes

- Mirar solo VSZ y asustarse.
- Medir una vez sin carga ni idle.
- No anotar unidades (kB vs MB).

## Siguiente

[L07 — OOM, ulimit y síntomas](L07-oom-ulimit-y-sintomas.md)
