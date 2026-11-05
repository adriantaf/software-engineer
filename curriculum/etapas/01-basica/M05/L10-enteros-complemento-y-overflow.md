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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Explicar complemento a dos a alto nivel; detectar overflow
      en modelos finitos; relacionar con `Number.MAX_SAFE_INTEGER` en
      JavaScript/TS.


      - **Magnitud y signo** vs **complemento a dos**.

      - **Overflow** aritmético vs **wrap-around** en lenguajes de alto nivel.

      - **Int32** en WASM/Node buffers vs `number` IEEE-754.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```ts
      const casi = Number.MAX_SAFE_INTEGER;
      console.log(casi + 1 === casi + 2);

      function sumaInt32(a: number, b: number): number {
        return (a + b) | 0; // truco educativo; documenta límites
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Enteros, complemento a dos y overflow" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/enteros-overflow.ts + enteros-notas.md
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
      ¿Es buena práctica en esta lección? “Creer que TS previene overflow
      numérico en runtime."
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
          Explicar complemento a dos a alto nivel; detectar overflow en modelos
          finitos; relacionar con `Number.MAX_SAFE_INTEGER` en JavaScript/TS.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ejemplos TS
    xp: 10
    cuerpo: |-
      `enteros-overflow.ts`:

      ```ts
      const casi = Number.MAX_SAFE_INTEGER;
      console.log(casi + 1 === casi + 2);

      function sumaInt32(a: number, b: number): number {
        return (a + b) | 0; // truco educativo; documenta límites
      }
      ```

      Documenta cuándo `| 0` ayuda y cuándo engaña.
  - id: s7
    tipo: explicacion
    titulo: 3. Ejercicios
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
