---
id: L07
materia: M05
orden: 7
titulo: Disco vs RAM y persistencia
horas: 5
semana: 2
lectura: 'Stallings — memoria externa, almacenamiento, SSD/HDD intro'
evidencia: projects/m05-como-corre/ram-vs-disco.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - **Volatilidad** y **persistencia**.

      - **Bloque** de disco vs **página** de memoria.

      - **Buffering** y **page cache** del SO (lectura repetida más rápida).

      - SSD vs HDD: latencia y throughput cualitativo.


      **Objetivo de esta lección:** Contrastar memoria principal y
      almacenamiento secundario; explicar filesystem, bloques y por qué
      `readFile` puede costar más que millones de sumas en CPU.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```js
      // projects/m05-como-corre/read-twice.mjs
      import { readFileSync } from "node:fs";
      const p = "package.json"; // o un archivo grande que tengas
      console.time("read1");
      readFileSync(p);
      console.timeEnd("read1");
      console.time("read2");
      readFileSync(p);
      console.timeEnd("read2");
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`ram-vs-disco.md`'
    xp: 10
    cuerpo: |-
      ```js
      // projects/m05-como-corre/read-twice.mjs
      import { readFileSync } from "node:fs";
      const p = "package.json"; // o un archivo grande que tengas
      console.time("read1");
      readFileSync(p);
      console.timeEnd("read1");
      console.time("read2");
      readFileSync(p);
      console.timeEnd("read2");
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Disco vs RAM y persistencia», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`ram-vs-disco.md` completo con experimento read-twice interpretado.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Disco vs RAM y
          persistencia
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
    pregunta: ¿Es recomendable en esta lección? ““La nube no usa disco”."
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
          Contrastar memoria principal y almacenamiento secundario; explicar
          filesystem, bloques y por qué `readFile` puede costar más que millones
          de sumas en CPU.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Experimento
    xp: 10
    cuerpo: >-
      Ejecuta desde raíz del repo. ¿Segunda lectura más rápida? Explica con page
      cache.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`ram-vs-disco.md` completo con experimento read-twice interpretado.'
      - Explicas swap y page cache sin confundirlos.
      - '`diagrama.md` actualizado con jerarquía.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Disco vs RAM y persistencia

**~5 h · Semana 2**

RAM es volátil y rápida; el almacenamiento persiste y es más lento. Mezclarlos es el error clásico del principiante.

## Objetivo

Contrastar memoria principal y almacenamiento secundario; explicar filesystem, bloques y por qué `readFile` puede costar más que millones de sumas en CPU.

## Conceptos

- **Volatilidad** y **persistencia**.
- **Bloque** de disco vs **página** de memoria.
- **Buffering** y **page cache** del SO (lectura repetida más rápida).
- SSD vs HDD: latencia y throughput cualitativo.

## Pasos

### 1. Lectura (75 min)

Stallings: memoria externa / almacenamiento. Resume SSD vs HDD en tabla (3 filas).

### 2. `ram-vs-disco.md` (90 min)

Secciones:

- Comparación RAM vs disco (velocidad, tamaño, costo, volatilidad).
- Qué ocurre cuando guardas un archivo desde Node (`writeFileSync` conceptual).
- **Swap**: qué es y por qué puede hacer todo lento (párrafo).

### 3. Experimento (60–75 min)

```js
// projects/m05-como-corre/read-twice.mjs
import { readFileSync } from "node:fs";
const p = "package.json"; // o un archivo grande que tengas
console.time("read1");
readFileSync(p);
console.timeEnd("read1");
console.time("read2");
readFileSync(p);
console.timeEnd("read2");
```

Ejecuta desde raíz del repo. ¿Segunda lectura más rápida? Explica con page cache.

### 4. Actualiza `diagrama.md` (30 min)

Añade subsección “Jerarquía completa” enlazando a L06–L07.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Almacenamiento externo |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. `ram-vs-disco.md` completo con experimento read-twice interpretado.
2. Explicas swap y page cache sin confundirlos.
3. `diagrama.md` actualizado con jerarquía.

## Errores comunes

- “La nube no usa disco”.
- Medir una sola lectura y concluir.

## Siguiente

[L08 — Medición: `free`, `df` y observación del SO](L08-medicion-free-df-y-so.md)
