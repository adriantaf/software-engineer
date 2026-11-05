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
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Fetch, fs y la CLI concurrente comparten el mismo modelo. Sin esto,
      `await` es superstición.


      **Objetivo de esta lección:** Escribir utilidades con Promises y explicar
      sync vs async en tus propias palabras (bitácora).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Delay y secuencia
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

      `src/async/delay.ts`: Demo con `pasos().then(console.log)`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Promisificar lectura
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Promises y el modelo mental async», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`delay` y `pasos` funcionan; entiendes el orden de impresión.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Promises y el modelo
          mental async
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
      ¿Es recomendable en esta lección? “Olvidar `return` dentro de `.then`
      (cadena rota)."
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
          Escribir utilidades con Promises y explicar sync vs async en tus
          propias palabras (bitácora).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: EJ cap. 11 — primera mitad
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
