---
id: L14
materia: M02
orden: 14
titulo: async/await en la práctica
horas: 3
semana: 4
lectura: EJ cap. 11 (async) + refactor CLI a async main
evidencia: m02-habits src/cli.ts con async main y try/catch
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Código que lees en orden de ejecución es código que mantienes. La CLI es
      async de facto por el disco.


      **Objetivo de esta lección:** Un solo `await` por paso lógico en `cli.ts`,
      sin `.then` anidados, con `try/catch` en el borde.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Refactor cli.ts
    xp: 10
    cuerpo: |-
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Paralelo controlado
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «async/await en la práctica», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: CLI usa `async/await` en el entry.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de async/await en la
          práctica
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
      ¿Es recomendable en esta lección? “`async` en cada función aunque no hay
      await."
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
          Un solo `await` por paso lógico en `cli.ts`, sin `.then` anidados, con
          `try/catch` en el borde.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: EJ cap. 11 — resto
    xp: 10
    cuerpo: Termina el capítulo; ejercicio async en TS.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - CLI usa `async/await` en el entry.
      - Errores de I/O muestran mensaje y exit code.
      - Ejercicio cap. 11 commiteado.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
