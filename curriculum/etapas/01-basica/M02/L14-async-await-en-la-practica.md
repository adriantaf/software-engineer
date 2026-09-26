---
id: L14
materia: M02
orden: 14
titulo: async/await en la práctica
horas: 3
semana: 4
lectura: "EJ cap. 11 (async) + refactor CLI a async main"
evidencia: "m02-habits src/cli.ts con async main y try/catch"
---

# L14 — async/await en la práctica

**~3 h · Semana 4**

Reescribes el entry de la CLI con `async function main()` y manejo de errores async legible.

## Objetivo

Un solo `await` por paso lógico en `cli.ts`, sin `.then` anidados, con `try/catch` en el borde.

## Por qué importa

Código que lees en orden de ejecución es código que mantienes. La CLI es async de facto por el disco.

## Pasos

### 1. Refactor cli.ts (55 min)

```ts
async function main(): Promise<void> {
  const comando = parseArgv(process.argv);
  try {
    const estado = await loadEstado();
    // switch comando → mutar estado en memoria
    await saveEstado(estado);
  } catch (e) {
    console.error("Error:", e instanceof Error ? e.message : e);
    process.exitCode = 1;
  }
}

main();
```

Extrae handlers `ejecutarAdd`, `ejecutarList` async si hace falta.

### 2. Paralelo controlado (40 min)

`src/async/paralelo.ts` — `Promise.all` para leer dos archivos de ejemplo; documenta cuándo **no** usar paralelo (misma escritura).

### 3. EJ cap. 11 — resto (45 min)

Termina el capítulo; ejercicio async en TS.

### 4. Prueba manual CLI (30 min)

Tres comandos seguidos verificando que el JSON persiste.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 11 |

## Hecho cuando

1. CLI usa `async/await` en el entry.
2. Errores de I/O muestran mensaje y exit code.
3. Ejercicio cap. 11 commiteado.

## Errores comunes

- `async` en cada función aunque no hay await.
- `await` dentro de `forEach` (no espera).
- Tragar errores en `catch` vacío.

## Siguiente

[L15 — fetch y APIs JSON](L15-fetch-y-apis-json.md)
