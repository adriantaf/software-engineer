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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Contrastar memoria principal y almacenamiento secundario;
      explicar filesystem, bloques y por qué `readFile` puede costar más que
      millones de sumas en CPU.


      - **Volatilidad** y **persistencia**.

      - **Bloque** de disco vs **página** de memoria.

      - **Buffering** y **page cache** del SO (lectura repetida más rápida).

      - SSD vs HDD: latencia y throughput cualitativo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Disco vs RAM y persistencia" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/ram-vs-disco.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? ““La nube no usa disco”."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Contrastar memoria principal y almacenamiento secundario; explicar
          filesystem, bloques y por qué `readFile` puede costar más que millones
          d…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `ram-vs-disco.md`
    xp: 10
    cuerpo: >-
      Secciones:


      - Comparación RAM vs disco (velocidad, tamaño, costo, volatilidad).

      - Qué ocurre cuando guardas un archivo desde Node (`writeFileSync`
      conceptual).

      - **Swap**: qué es y por qué puede hacer todo lento (párrafo).
  - id: s7
    tipo: ejemplo
    titulo: 3. Experimento
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
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`ram-vs-disco.md` completo con experimento read-twice interpretado.'
      - Explicas swap y page cache sin confundirlos.
      - '`diagrama.md` actualizado con jerarquía.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
