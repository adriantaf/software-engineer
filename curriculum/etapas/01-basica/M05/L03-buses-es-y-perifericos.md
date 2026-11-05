---
id: L03
materia: M05
orden: 3
titulo: 'Buses, E/S y periféricos'
horas: 5
semana: 1
lectura: 'Stallings — buses, E/S programada/interrupciones/DMA (intro según ed.)'
evidencia: projects/m05-como-corre/es-y-buses.md + salida de lsblk o equivalente
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - **Bus**: ancho de banda y contención (CPU y DMA compiten).

      - **Controlador de dispositivo** + **driver** del SO.

      - **Interrupción**: señal asíncrona que desvía el flujo (handler).

      - **DMA**: transferencia memoria ↔ dispositivo con menos intervención de
      CPU.


      **Objetivo de esta lección:** Explicar bus de direcciones, datos y
      control; distinguir E/S programada, interrupciones y DMA a nivel
      conceptual; mapear periféricos comunes en tu máquina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```js
      import { readFileSync } from "node:fs";

      console.time("sync-read");
      readFileSync(import.meta.filename);
      console.timeEnd("sync-read");
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Archivo `es-y-buses.md`
    xp: 10
    cuerpo: |-
      ```bash
      lsblk          # o diskutil list en macOS
      ls -la /dev/*  # muestra parcial; no ejecutes como root sin saber
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Buses, E/S y periféricos», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Existe `es-y-buses.md` con diagrama, tabla de dispositivos y notas del
          experimento.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Buses, E/S y
          periféricos
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

      `ls -la /dev/*  # muestra parcial; no ejecutes como root sin saber`
    comandoEsperado:
      - 'ls -la /dev/*  # muestra parcial; no ejecutes como root sin saber'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls -la /dev/*  # muestra parcial; no ejecutes como root sin
      saber
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
        texto: >-
          Explicar bus de direcciones, datos y control; distinguir E/S
          programada, interrupciones y DMA a nivel conceptual; mapear
          periféricos comunes en tu máquina.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Observación en terminal
    xp: 10
    cuerpo: >-
      Pega salida **recortada** (sin datos sensibles) en el archivo y explica
      qué bloque representa (disco, partición).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        Existe `es-y-buses.md` con diagrama, tabla de dispositivos y notas del
        experimento.
      - 'Distinguiste E/S programada, interrupción y DMA con un ejemplo cada una.'
      - >-
        Corriste `io-demo.mjs` y documentaste observaciones (aunque sean
        preliminares).
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Buses, E/S y periféricos

**~5 h · Semana 1**

Los datos no teletransportan: viajan por buses. La E/S explica por qué leer un archivo puede dominar un cálculo.

## Objetivo

Explicar bus de direcciones, datos y control; distinguir E/S programada, interrupciones y DMA a nivel conceptual; mapear periféricos comunes en tu máquina.

## Conceptos

- **Bus**: ancho de banda y contención (CPU y DMA compiten).
- **Controlador de dispositivo** + **driver** del SO.
- **Interrupción**: señal asíncrona que desvía el flujo (handler).
- **DMA**: transferencia memoria ↔ dispositivo con menos intervención de CPU.

## Pasos

### 1. Lectura (60–90 min)

Stallings: capítulo de **buses** y **organización de E/S**. Resume en tres párrafos: programada vs interrupción vs DMA (ventaja / costo de cada una).

### 2. Archivo `es-y-buses.md` (90 min)

Crea `projects/m05-como-corre/es-y-buses.md`:

- Diagrama CPU–bus–memoria–controladores (disco, red, USB).
- Tabla: dispositivo → tipo de E/S típico → latencia relativa (orden de magnitud, no cifras memorizadas).
- Párrafo: qué es un **syscall** y cómo conecta tu programa con el driver (conceptual).

### 3. Observación en terminal (45–60 min)

```bash
lsblk          # o diskutil list en macOS
ls -la /dev/*  # muestra parcial; no ejecutes como root sin saber
```

Pega salida **recortada** (sin datos sensibles) en el archivo y explica qué bloque representa (disco, partición).

### 4. Experimento mental + código (60 min)

Escribe `projects/m05-como-corre/io-demo.mjs`:

```js
import { readFileSync } from "node:fs";

console.time("sync-read");
readFileSync(import.meta.filename);
console.timeEnd("sync-read");
```

Ejecuta varias veces. En `es-y-buses.md`, anota: ¿qué E/S ocurre? ¿CPU al 100 %? (observa con `top`/`htop` si puedes). Hipótesis para L11.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Buses + entrada/salida |
| Plan | Man `read(2)` o docs Node `fs` (10 min, conceptual) |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Existe `es-y-buses.md` con diagrama, tabla de dispositivos y notas del experimento.
2. Distinguiste E/S programada, interrupción y DMA con un ejemplo cada una.
3. Corriste `io-demo.mjs` y documentaste observaciones (aunque sean preliminares).

## Errores comunes

- Tratar “bus” como solo USB.
- Ignorar que la red es E/S con latencias muy distintas al disco local.
- Confundir driver de kernel con biblioteca de usuario (`fs`).

## Siguiente

[L04 — Diagrama CPU–RAM–I/O (P1)](L04-diagrama-cpu-ram-io-p1.md)
