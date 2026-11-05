---
id: L18
materia: M10
orden: 18
titulo: Cliente y servidor TCP mínimo (P2)
horas: 5
semana: 5
lectura: Node net module + Tanenbaum transporte
evidencia: projects/m10-redes/tcp-echo/ con código y diagrama
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar echo TCP mínimo y un diagrama de una request
      real del producto.


      Bajas una capa: bytes sobre TCP sin HTTP. P2 exige código que corre.
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold
    xp: 10
    cuerpo: |-
      ```js
      import net from "node:net";
      const port = Number(process.env.PORT || 9000);
      const server = net.createServer((socket) => {
        socket.on("data", (buf) => {
          socket.write(buf);
        });
      });
      server.listen(port, "127.0.0.1", () => {
        console.log(`echo on 127.0.0.1:${port}`);
      });
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cliente y servidor TCP mínimo (P2)" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m10-redes/tcp-echo/ con código y diagrama
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `mkdir -p projects/m10-redes/tcp-echo`
    comandoEsperado:
      - mkdir -p projects/m10-redes/tcp-echo
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m10-redes/tcp-echo'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar echo TCP mínimo y un diagrama de una request real del
          producto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Servidor
    xp: 10
    cuerpo: |-
      `server.js`:

      ```js
      import net from "node:net";
      const port = Number(process.env.PORT || 9000);
      const server = net.createServer((socket) => {
        socket.on("data", (buf) => {
          socket.write(buf);
        });
      });
      server.listen(port, "127.0.0.1", () => {
        console.log(`echo on 127.0.0.1:${port}`);
      });
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Cliente
    xp: 10
    cuerpo: |-
      ```bash
      node server.js &
      node client.js
      kill %1
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`tcp-echo/server.js` + `client.js` (o TS) funcionan en localhost.'
      - '`diagrama-request.md` compara echo TCP vs request HTTP/TLS.'
      - 'Commit `feat(m10): l18 tcp echo p2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L18 — Cliente y servidor TCP mínimo (P2)

**~5.0 h · Semana 5**

Bajas una capa: bytes sobre TCP sin HTTP. P2 exige código que corre.

## Objetivo

Implementar echo TCP mínimo y un diagrama de una request real del producto.

## Pasos

### 1. Scaffold (20 min)

```bash
mkdir -p projects/m10-redes/tcp-echo
cd projects/m10-redes/tcp-echo
```

### 2. Servidor (60 min)

`server.js`:

```js
import net from "node:net";
const port = Number(process.env.PORT || 9000);
const server = net.createServer((socket) => {
  socket.on("data", (buf) => {
    socket.write(buf);
  });
});
server.listen(port, "127.0.0.1", () => {
  console.log(`echo on 127.0.0.1:${port}`);
});
```

### 3. Cliente (45 min)

`client.js` conecta, envía una línea, imprime eco, cierra. Prueba:

```bash
node server.js &
node client.js
kill %1
```

### 4. Diagrama (45 min)

`diagrama-request.md`: eco TCP (L18) vs `GET /api/pedidos` (DNS→TCP→TLS→HTTP). Relaciona puertos.

### 5. Commit (15 min)

```bash
git add projects/m10-redes/tcp-echo
git commit -m "feat(m10): l18 tcp echo p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Sockets TCP en Node: listen, connect, stream de bytes | [Node.js net](https://nodejs.org/api/net.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `tcp-echo/server.js` + `client.js` (o TS) funcionan en localhost.
2. `diagrama-request.md` compara echo TCP vs request HTTP/TLS.
3. Commit `feat(m10): l18 tcp echo p2`.

## Errores comunes

- Servidor que no hace `.end()` / deja sockets colgados.
- Confundir “eco TCP” con HTTP.
- Bind en `0.0.0.0` expuesto sin firewall en una red no confiable.

## Siguiente

[L19 — Documento de amenazas de red del producto](L19-documento-de-amenazas-de-red-del-producto.md)
