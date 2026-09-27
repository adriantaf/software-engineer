---
id: L02
materia: M11
orden: 2
titulo: Proceso vs hilo y el runtime Node
horas: 5.0
semana: 1
lectura: Silberschatz — hilos + Node event loop
evidencia: labs/semana-01-procesos.md sección hilos
---

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Proceso vs hilo; event loop de Node; workers opcionales | [Node.js — The Node Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. Sección en `labs/semana-01-procesos.md`: proceso vs hilo + cómo encaja el event loop.
2. Experimento: un `node` idle y `ps`/`top` anotando un solo proceso (salvo workers).
3. Commit `docs(m11): l02 proceso vs hilo node`.

## Errores comunes

- Decir “Node es single-thread” sin matizar libuv/threadpool.
- Confundir concurrency con paralelismo CPU.
- Abrir 10 terminales sin documentar qué PID es cuál.

## Siguiente

[L03 — Señales SIGTERM y apagado graceful](L03-senales-sigterm-y-apagado-graceful.md)
