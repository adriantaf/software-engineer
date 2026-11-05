---
id: L13
materia: M02
orden: 13
titulo: Promises y el modelo mental async
horas: 2.5
semana: 4
lectura: EJ cap. 11 (asíncrono) — callbacks y Promises
evidencia: src/async/delay.ts + demo secuencia con .then
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Escribir utilidades con Promises y explicar sync vs async en
      tus propias palabras (bitácora).


      Fetch, fs y la CLI concurrente comparten el mismo modelo. Sin esto,
      `await` es superstición.
  - id: s2
    tipo: ejemplo
    titulo: 1. Delay y secuencia
    xp: 10
    cuerpo: |-
      ```ts
      export function delay(ms: number): Promise<void> {
        return new Promise((resolve) => setTimeout(resolve, ms));
      }

      export function pasos(): Promise<string[]> {
        const log: string[] = [];
        return delay(10)
          .then(() => {
            log.push("uno");
            return delay(10);
          })
          .then(() => {
            log.push("dos");
            return log;
          });
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Promises y el modelo mental async" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/async/delay.ts + demo secuencia con .then
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
      ¿Es buena práctica en esta lección? “Olvidar `return` dentro de `.then`
      (cadena rota)."
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
          Escribir utilidades con Promises y explicar sync vs async en tus
          propias palabras (bitácora).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Promisificar lectura
    xp: 10
    cuerpo: >-
      Refactoriza una función sync pequeña a `Promise` manualmente (ej. validar
      archivo existe) antes de usar solo `fs/promises`.
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 11 — primera mitad
    xp: 10
    cuerpo: Lee hasta Promises; **1 ejercicio** del capítulo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`delay` y `pasos` funcionan; entiendes el orden de impresión.'
      - Nota sync vs async escrita.
      - Sin mezclar callbacks y Promises en el mismo flujo sin razón.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Promises y el modelo mental async

**~2.5 h · Semana 4**

Entiendes la cola de microtareas, encadenas `.then`/`.catch` y por qué `loadEstado` ya era async sin magia.

## Objetivo

Escribir utilidades con Promises y explicar sync vs async en tus propias palabras (bitácora).

## Por qué importa

Fetch, fs y la CLI concurrente comparten el mismo modelo. Sin esto, `await` es superstición.

## Pasos

### 1. Delay y secuencia (45 min)

`src/async/delay.ts`:

```ts
export function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export function pasos(): Promise<string[]> {
  const log: string[] = [];
  return delay(10)
    .then(() => {
      log.push("uno");
      return delay(10);
    })
    .then(() => {
      log.push("dos");
      return log;
    });
}
```

Demo con `pasos().then(console.log)`.

### 2. Promisificar lectura (40 min)

Refactoriza una función sync pequeña a `Promise` manualmente (ej. validar archivo existe) antes de usar solo `fs/promises`.

### 3. EJ cap. 11 — primera mitad (50 min)

Lee hasta Promises; **1 ejercicio** del capítulo.

### 4. Nota conceptual (15 min)

En bitácora: 5 líneas sync vs async con ejemplo de tu CLI.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 11 (inicio) |
| MDN | [Promise](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `delay` y `pasos` funcionan; entiendes el orden de impresión.
2. Nota sync vs async escrita.
3. Sin mezclar callbacks y Promises en el mismo flujo sin razón.

## Errores comunes

- Olvidar `return` dentro de `.then` (cadena rota).
- `new Promise` sin `reject` en errores reales.
- Bloquear el hilo con trabajo pesado sync “porque async”.

## Siguiente

[L14 — async/await en la práctica](L14-async-await-en-la-practica.md)
