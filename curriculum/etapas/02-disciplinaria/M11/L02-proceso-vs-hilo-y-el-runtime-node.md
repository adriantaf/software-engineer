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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Tu API será un proceso Node. Hoy separas proceso, hilo y event loop con
      evidencia.


      **Objetivo de esta lección:** Explicar proceso vs hilo aplicado al runtime
      que usarás en M17.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Conceptos
    xp: 10
    cuerpo: |-
      ```bash
      node -e 'setInterval(() => {}, 1000)' &
      PID=$!
      ps -p $PID -o pid,nlwp,cmd
      # nlwp ≈ número de hilos ligeros reportados
      kill $PID
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Observa Node
    xp: 10
    cuerpo: >-
      ```bash

      node -e 'setInterval(() => {}, 1000)' &

      PID=$!

      ps -p $PID -o pid,nlwp,cmd

      # nlwp ≈ número de hilos ligeros reportados

      kill $PID

      ```


      Anota qué ves y qué significa para “Node es single-threaded” (JS en un
      hilo; pool de libuv aparte).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Proceso vs hilo y el runtime Node», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Proceso vs hilo y el
          runtime Node
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `node -e 'setInterval(() => {}, 1000)' &`
    comandoEsperado:
      - 'node -e ''setInterval(() => {}, 1000)'' &'
      - git add projects/m11-so/labs/semana-01-procesos.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: node -e ''setInterval(() => {}, 1000)'' &'
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
        texto: Explicar proceso vs hilo aplicado al runtime que usarás en M17.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Vitrina
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
