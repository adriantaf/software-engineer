---
id: L13
materia: M02
orden: 13
titulo: Promises y el modelo mental async
horas: 2.5
semana: 4
lectura: "EJ cap. 11 (asíncrono) — callbacks y Promises"
evidencia: "src/async/delay.ts + demo secuencia con .then"
---

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
