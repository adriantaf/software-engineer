---
id: L18
materia: M10
orden: 18
titulo: Cliente y servidor TCP mínimo (P2)
horas: 5
semana: 5
lectura: "Node net module docs + Tanenbaum transporte"
evidencia: "projects/m10-redes/tcp-echo/ con código y diagrama"
---

# L18 — Cliente y servidor TCP mínimo (P2)

**~5 h · Semana 5**

## Objetivo

Implementar echo TCP en Node/TypeScript y dibujar bytes desde cliente hasta socket servidor.

## Por qué importa

HTTP vive sobre TCP; ver sockets quita miedo a timeouts y backpressure.

## Conceptos

- Socket.
- listen/connect.
- Buffer y encoding.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m10-redes/tcp-echo/` con servidor y cliente mínimos (`net.createServer`, `net.connect`). Añade `diagrama-request.md` comparando capas con HTTP.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l18 cliente-y-servidor-tcp-minimo-p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Node.js | net module | Tanenbaum TCP |

## Hecho cuando

1. Echo funciona en local.
2. Diagrama capas guardado.
3. Commit código + doc.

## Errores comunes

- Dejar servidor escuchando en 0.0.0.0 sin nota.
- No cerrar sockets en error.

## Siguiente

[L19 — Documento de amenazas de red del producto](L19-documento-de-amenazas-de-red-del-producto.md)
