---
id: L03
materia: M05
orden: 3
titulo: Buses, E/S y periféricos
horas: 5
semana: 1
lectura: "Stallings — buses, E/S programada/interrupciones/DMA (intro según ed.)"
evidencia: "projects/m05-como-corre/es-y-buses.md + salida de lsblk o equivalente"
---

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
