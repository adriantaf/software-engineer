---
id: L03
materia: M11
orden: 3
titulo: Señales SIGTERM y apagado graceful
horas: 5
semana: 1
lectura: Silberschatz — señales + Node process signals
evidencia: labs/sigterm-node.md + app/graceful-server.js
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Un servidor HTTP Node que apaga en orden al recibir SIGTERM.


      En deploy (M19) el orquestador envía SIGTERM. Si lo ignoras, cortas
      pedidos a medias.
  - id: s2
    tipo: ejemplo
    titulo: 1. Código
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Señales SIGTERM y apagado graceful" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: labs/sigterm-node.md + app/graceful-server.js
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Ignorar SIGTERM y solo morir con
      SIGKILL en deploy."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Un servidor HTTP Node que apaga en orden al recibir SIGTERM.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prueba
    xp: 10
    cuerpo: >-
      ```bash

      node projects/m11-so/app/graceful-server.js &

      PID=$!

      curl -s http://127.0.0.1:3099/

      kill -TERM $PID

      wait $PID

      ```


      Repite idea con `kill -KILL` y documenta la diferencia en
      `labs/sigterm-node.md`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so/app projects/m11-so/labs/sigterm-node.md
      git commit -m "feat(m11): l03 graceful sigterm"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `app/graceful-server.js` maneja SIGTERM, deja de aceptar conexiones y
        cierra con timeout.
      - >-
        `labs/sigterm-node.md` documenta prueba con `kill -TERM` vs `kill
        -KILL`.
      - 'Commit `feat(m11): l03 graceful sigterm`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
