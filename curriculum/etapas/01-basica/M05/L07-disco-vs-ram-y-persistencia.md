---
id: L07
materia: M05
orden: 7
titulo: Disco vs RAM y persistencia
horas: 5
semana: 2
lectura: "Stallings — memoria externa, almacenamiento, SSD/HDD intro"
evidencia: "projects/m05-como-corre/ram-vs-disco.md"
---

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

## Hecho cuando

1. `ram-vs-disco.md` completo con experimento read-twice interpretado.
2. Explicas swap y page cache sin confundirlos.
3. `diagrama.md` actualizado con jerarquía.

## Errores comunes

- “La nube no usa disco”.
- Medir una sola lectura y concluir.

## Siguiente

[L08 — Medición: `free`, `df` y observación del SO](L08-medicion-free-df-y-so.md)
