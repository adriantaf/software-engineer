---
id: L11
materia: M05
orden: 11
titulo: Punto flotante y precisión (P2–P3)
horas: 5
semana: 3
lectura: Stallings — IEEE 754 intro + repaso localidad (L06)
evidencia: projects/m05-como-corre/float-notas.md + benchmark-loop-vs-io.mjs (P3)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      IEEE 754 explica `0.1 + 0.2 !== 0.3`. Hoy cierras **P2** y ejecutas
      **P3**: CPU-bound vs I/O-bound.


      **Objetivo de esta lección:** Describir flotantes de simple precisión a
      alto nivel; demostrar errores de redondeo; medir y comparar un bucle CPU
      vs lectura de archivo (≥3 repeticiones).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```js
      import { readFileSync } from "node:fs";

      console.time("cpu-loop");
      let s = 0;
      for (let i = 0; i < 50_000_000; i++) s += i;
      console.timeEnd("cpu-loop");

      console.time("io-read");
      readFileSync("package.json");
      console.timeEnd("io-read");
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`float-notas.md`'
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m05-como-corre/
      git commit -m "docs(m05): representación numérica y benchmark loop vs IO"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Punto flotante y precisión (P2–P3)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'P2: conversiones + enteros + flotantes documentados y en git.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Punto flotante y
          precisión (P2–P3)
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
    pregunta: ¿Es recomendable en esta lección? “Una sola corrida del benchmark."
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
        texto: >-
          Describir flotantes de simple precisión a alto nivel; demostrar
          errores de redondeo; medir y comparar un bucle CPU vs lectura de
          archivo (≥3 repeticiones).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Benchmark P3
    xp: 10
    cuerpo: >-
      Crea `benchmark-loop-vs-io.mjs`: - Repite el script **≥3 veces**; registra
      tiempos en `benchmark-resultados.md`. - Explica diferencia usando
      jerarquía de memoria, caché y E/S (L06–L07). - Ajusta tamaño del loop o
      archivo si tu máquina es muy lenta/rápida; documenta parámetros.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'P2: conversiones + enteros + flotantes documentados y en git.'
      - >-
        P3: benchmark ≥3 repeticiones + explicación causal (no solo “I/O es
        lento”).
      - Entiendes cuándo usar comparación epsilon.
      - Marca P2 y P3 en la ficha cuando la evidencia exista.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Punto flotante y precisión (P2–P3)

**~5 h · Semana 3**

IEEE 754 explica `0.1 + 0.2 !== 0.3`. Hoy cierras **P2** y ejecutas **P3**: CPU-bound vs I/O-bound.

## Objetivo

Describir flotantes de simple precisión a alto nivel; demostrar errores de redondeo; medir y comparar un bucle CPU vs lectura de archivo (≥3 repeticiones).

## Pasos

### 1. Lectura (60 min)

Stallings: representación en punto flotante (signo, exponente, mantisa). Sin memorizar todos los casos especiales; sí **NaN** e **inf** existen.

### 2. `float-notas.md` (60 min)

- Por qué `0.1 + 0.2` falla la igualdad estricta.
- Qué es epsilon comparativo (`Number.EPSILON`) en una frase.
- Completa evidencia **P2**: enlaza L09–L10–L11.

### 3. Benchmark P3 (120 min)

Crea `benchmark-loop-vs-io.mjs`:

```js
import { readFileSync } from "node:fs";

console.time("cpu-loop");
let s = 0;
for (let i = 0; i < 50_000_000; i++) s += i;
console.timeEnd("cpu-loop");

console.time("io-read");
readFileSync("package.json");
console.timeEnd("io-read");
```

- Repite el script **≥3 veces**; registra tiempos en `benchmark-resultados.md`.
- Explica diferencia usando jerarquía de memoria, caché y E/S (L06–L07).
- Ajusta tamaño del loop o archivo si tu máquina es muy lenta/rápida; documenta parámetros.

### 4. Commit P2/P3 parcial (15 min)

```bash
git add projects/m05-como-corre/
git commit -m "docs(m05): representación numérica y benchmark loop vs IO"
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Punto flotante |
| Tus L06–L07 | Caché y disco |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. P2: conversiones + enteros + flotantes documentados y en git.
2. P3: benchmark ≥3 repeticiones + explicación causal (no solo “I/O es lento”).
3. Entiendes cuándo usar comparación epsilon.

Marca **P2** y **P3** en la ficha cuando la evidencia exista.

## Errores comunes

- Una sola corrida del benchmark.
- Explicar con “Node es lento” sin hardware/SO.

## Siguiente

[L12 — Documental “cómo corre `node`” y cierre](L12-documental-como-corre-node-y-cierre.md)
