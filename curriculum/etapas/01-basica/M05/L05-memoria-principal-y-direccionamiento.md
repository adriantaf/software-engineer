---
id: L05
materia: M05
orden: 5
titulo: Memoria principal y direccionamiento
horas: 5
semana: 2
lectura: >-
  Stallings — memoria interna, organización, direccionamiento (cap. memoria
  según ed.)
evidencia: projects/m05-como-corre/memoria-direccionamiento.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Explicar direccionamiento, palabra, endianness a alto nivel,
      y cómo el SO asigna espacio de direcciones a un proceso.


      - **Byte addressable** vs acceso por palabra.

      - **Espacio de direcciones** (32 vs 64 bits) a nivel intuitivo.

      - **Paginación** (idea: bloques fijos, tablas del SO) sin implementar
      hardware.

      - **Stack vs heap** en el mapa de un proceso (vista de programador).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```js
      // projects/m05-como-corre/mem-size.mjs
      const arr = new Array(1_000_000).fill(0);
      console.log("array creado");
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Memoria principal y direccionamiento" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/memoria-direccionamiento.md
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Decir “1 GB de RAM = 1e9 bytes” sin
      mencionar binario vs decimal."
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
          Explicar direccionamiento, palabra, endianness a alto nivel, y cómo el
          SO asigna espacio de direcciones a un proceso.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `memoria-direccionamiento.md`
    xp: 10
    cuerpo: >-
      Tabla: concepto → definición → ejemplo en Node/TS (ej.: `Buffer`,
      `ArrayBuffer`, referencias a objetos en heap).
  - id: s7
    tipo: ejemplo
    titulo: 3. Experimento Node
    xp: 10
    cuerpo: |-
      ```js
      // projects/m05-como-corre/mem-size.mjs
      const arr = new Array(1_000_000).fill(0);
      console.log("array creado");
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Existe `memoria-direccionamiento.md` con tabla y notas del experimento.
      - Explicas paginación como idea (sin confundir con swap).
      - >-
        Distinguiste stack y heap con un ejemplo de variables locales vs
        objetos.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
