---
id: L02
materia: M11
orden: 2
titulo: Proceso vs hilo y el runtime Node
horas: 5
semana: 1
lectura: Silberschatz — hilos + Node event loop
evidencia: labs/semana-01-procesos.md sección hilos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Explicar proceso vs hilo aplicado al runtime que usarás en
      M17.


      Tu API será un proceso Node. Hoy separas proceso, hilo y event loop con
      evidencia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Conceptos
    xp: 10
    cuerpo: |-
      ```bash
      node -e 'setInterval(() => {}, 1000)' &
      PID=$!
      ps -p $PID -o pid,nlwp,cmd
      # nlwp ≈ número de hilos ligeros reportados
      kill $PID
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Proceso vs hilo y el runtime Node" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/semana-01-procesos.md sección hilos
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

      `node -e 'setInterval(() => {}, 1000)' &`
    comandoEsperado:
      - 'node -e ''setInterval(() => {}, 1000)'' &'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: node -e ''setInterval(() => {}, 1000)'' &'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Explicar proceso vs hilo aplicado al runtime que usarás en M17.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Observa Node
    xp: 10
    cuerpo: >-
      ```bash

      node -e 'setInterval(() => {}, 1000)' &

      PID=$!

      ps -p $PID -o pid,nlwp,cmd

      nlwp ≈ número de hilos ligeros reportados

      kill $PID

      ```


      Anota qué ves y qué significa para “Node es single-threaded” (JS en un
      hilo; pool de libuv aparte).
  - id: s7
    tipo: explicacion
    titulo: 3. Vitrina
    xp: 10
    cuerpo: >-
      ¿Dónde pondrías CPU-bound (reporte pesado)? ¿Worker thread, job queue, o
      otro servicio? 6–8 líneas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Sección en `labs/semana-01-procesos.md`: proceso vs hilo + cómo encaja
        el event loop.
      - >-
        Experimento: un `node` idle y `ps`/`top` anotando un solo proceso (salvo
        workers).
      - 'Commit `docs(m11): l02 proceso vs hilo node`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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

### 3. Vitrina (30 min)

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
