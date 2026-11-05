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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      En deploy (M19) el orquestador envía SIGTERM. Si lo ignoras, cortas
      pedidos a medias.


      **Objetivo de esta lección:** Un servidor HTTP Node que apaga en orden al
      recibir SIGTERM.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Código
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

      Crea `projects/m11-so/app/graceful-server.js`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Prueba
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Señales SIGTERM y apagado graceful», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Señales SIGTERM y
          apagado graceful
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Ignorar SIGTERM y solo morir con
      SIGKILL en deploy."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Un servidor HTTP Node que apaga en orden al recibir SIGTERM.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
