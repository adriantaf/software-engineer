---
id: L18
materia: M10
orden: 18
titulo: Cliente y servidor TCP mínimo (P2)
horas: 5.0
semana: 5
lectura: Node net module + Tanenbaum transporte
evidencia: projects/m10-redes/tcp-echo/ con código y diagrama
---

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
