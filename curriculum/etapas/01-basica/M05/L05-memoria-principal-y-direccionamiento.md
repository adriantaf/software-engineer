---
id: L05
materia: M05
orden: 5
titulo: Memoria principal y direccionamiento
horas: 5
semana: 2
lectura: "Stallings — memoria interna, organización, direccionamiento (cap. memoria según ed.)"
evidencia: "projects/m05-como-corre/memoria-direccionamiento.md"
---

# L05 — Memoria principal y direccionamiento

**~5 h · Semana 2**

La RAM es un arreglo de bytes direccionables. Esa idea explica punteros, segmentación y por qué “out of memory” no es lo mismo que “disco lleno”.

## Objetivo

Explicar direccionamiento, palabra, endianness a alto nivel, y cómo el SO asigna espacio de direcciones a un proceso.

## Conceptos

- **Byte addressable** vs acceso por palabra.
- **Espacio de direcciones** (32 vs 64 bits) a nivel intuitivo.
- **Paginación** (idea: bloques fijos, tablas del SO) sin implementar hardware.
- **Stack vs heap** en el mapa de un proceso (vista de programador).

## Pasos

### 1. Lectura (75–90 min)

Stallings: memoria interna y organización. Anota definición de **MAR**, **MDR** (o equivalentes) y cómo se forma una dirección.

### 2. `memoria-direccionamiento.md` (90 min)

Tabla: concepto → definición → ejemplo en Node/TS (ej.: `Buffer`, `ArrayBuffer`, referencias a objetos en heap).

### 3. Experimento Node (60 min)

```js
// projects/m05-como-corre/mem-size.mjs
const arr = new Array(1_000_000).fill(0);
console.log("array creado");
```

Observa memoria con `free -h` antes/después (orden de magnitud). Documenta: ¿crece RSS? ¿por qué no es exacto?

### 4. Preguntas (30 min)

- ¿Qué significa que dos procesos tengan “el mismo” puntero virtual distinto?
- ¿Por qué un array en TS no es lo mismo que un bloque contiguo expuesto al programador?

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Memoria interna, direccionamiento |
| Opcional | MDN `ArrayBuffer` (15 min) |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Existe `memoria-direccionamiento.md` con tabla y notas del experimento.
2. Explicas paginación como idea (sin confundir con swap).
3. Distinguiste stack y heap con un ejemplo de variables locales vs objetos.

## Errores comunes

- Decir “1 GB de RAM = 1e9 bytes” sin mencionar binario vs decimal.
- Confundir dirección virtual con dirección física.

## Siguiente

[L06 — Jerarquía de memoria y caché](L06-jerarquia-memoria-y-cache.md)
