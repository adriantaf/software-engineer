---
id: L10
materia: M05
orden: 10
titulo: 'Enteros, complemento a dos y overflow'
horas: 5
semana: 3
lectura: 'Stallings — enteros con signo, complemento a dos, overflow aritmético'
evidencia: projects/m05-como-corre/enteros-overflow.ts + enteros-notas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - **Magnitud y signo** vs **complemento a dos**.

      - **Overflow** aritmético vs **wrap-around** en lenguajes de alto nivel.

      - **Int32** en WASM/Node buffers vs `number` IEEE-754.


      **Objetivo de esta lección:** Explicar complemento a dos a alto nivel;
      detectar overflow en modelos finitos; relacionar con
      `Number.MAX_SAFE_INTEGER` en JavaScript/TS.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```ts
      const casi = Number.MAX_SAFE_INTEGER;
      console.log(casi + 1 === casi + 2);

      function sumaInt32(a: number, b: number): number {
        return (a + b) | 0; // truco educativo; documenta límites
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Ejemplos TS
    xp: 10
    cuerpo: |-
      ```ts
      const casi = Number.MAX_SAFE_INTEGER;
      console.log(casi + 1 === casi + 2);

      function sumaInt32(a: number, b: number): number {
        return (a + b) | 0; // truco educativo; documenta límites
      }
      ```

      `enteros-overflow.ts`: Documenta cuándo `| 0` ayuda y cuándo engaña.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Enteros, complemento a dos y overflow», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`enteros-notas.md` con traza 4-bit y ejercicios resueltos.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Enteros, complemento a
          dos y overflow
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Creer que TS previene overflow numérico
      en runtime."
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
          Explicar complemento a dos a alto nivel; detectar overflow en modelos
          finitos; relacionar con `Number.MAX_SAFE_INTEGER` en JavaScript/TS.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Ejercicios
    xp: 10
    cuerpo: >-
      Al menos 5 preguntas tipo examen (respuestas al final del archivo de
      notas): overflow sí/no, rango de n bits.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`enteros-notas.md` con traza 4-bit y ejercicios resueltos.'
      - '`enteros-overflow.ts` ejecutado y comentado.'
      - >-
        Explicas por qué JS no tiene enteros de 64 bits expuestos como tipo
        primitivo.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Enteros, complemento a dos y overflow

**~5 h · Semana 3**

Los enteros tienen ancho fijo en hardware. El complemento a dos explica suma con signo; el overflow explica bugs silenciosos.

## Objetivo

Explicar complemento a dos a alto nivel; detectar overflow en modelos finitos; relacionar con `Number.MAX_SAFE_INTEGER` en JavaScript/TS.

## Conceptos

- **Magnitud y signo** vs **complemento a dos**.
- **Overflow** aritmético vs **wrap-around** en lenguajes de alto nivel.
- **Int32** en WASM/Node buffers vs `number` IEEE-754.

## Pasos

### 1. Lectura (75 min)

Stallings: representación de enteros con signo. Traza suma 5 + (-3) en 4 bits (toy example) en `enteros-notas.md`.

### 2. Ejemplos TS (90 min)

`enteros-overflow.ts`:

```ts
const casi = Number.MAX_SAFE_INTEGER;
console.log(casi + 1 === casi + 2);

function sumaInt32(a: number, b: number): number {
  return (a + b) | 0; // truco educativo; documenta límites
}
```

Documenta cuándo `| 0` ayuda y cuándo engaña.

### 3. Ejercicios (60 min)

Al menos 5 preguntas tipo examen (respuestas al final del archivo de notas): overflow sí/no, rango de n bits.

### 4. Enlace a P2 (15 min)

Lista qué archivos forman la evidencia **P2** hasta ahora (L09–L10).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Enteros, complemento a dos |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. `enteros-notas.md` con traza 4-bit y ejercicios resueltos.
2. `enteros-overflow.ts` ejecutado y comentado.
3. Explicas por qué JS no tiene enteros de 64 bits expuestos como tipo primitivo.

## Errores comunes

- Creer que TS previene overflow numérico en runtime.
- Ignorar `MAX_SAFE_INTEGER` en IDs y contadores.

## Siguiente

[L11 — Punto flotante y precisión (P2–P3)](L11-punto-flotante-y-benchmark-io.md)
