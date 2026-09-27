---
id: L03
materia: M11
orden: 3
titulo: Señales SIGTERM y apagado graceful
horas: 5.0
semana: 1
lectura: Silberschatz — señales + Node process signals
evidencia: labs/sigterm-node.md + app/graceful-server.js
---

# L03 — Señales SIGTERM y apagado graceful

**~5.0 h · Semana 1**

En deploy (M19) el orquestador envía SIGTERM. Si lo ignoras, cortas pedidos a medias.

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | SIGTERM vs SIGKILL; graceful shutdown de servidor HTTP | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `app/graceful-server.js` maneja SIGTERM, deja de aceptar conexiones y cierra con timeout.
2. `labs/sigterm-node.md` documenta prueba con `kill -TERM` vs `kill -KILL`.
3. Commit `feat(m11): l03 graceful sigterm`.

## Errores comunes

- Ignorar SIGTERM y solo morir con SIGKILL en deploy.
- No poner timeout de cierre (conexiones eternas).
- Confundir Ctrl+C (SIGINT) con lo que envía Kubernetes/Docker.

## Siguiente

[L04 — Cierre semana 1 — práctica P1](L04-cierre-semana-1-practica-p1.md)
