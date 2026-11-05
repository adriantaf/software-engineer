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
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Un solo `await` por paso lógico en `cli.ts`, sin `.then`
      anidados, con `try/catch` en el borde.


      Código que lees en orden de ejecución es código que mantienes. La CLI es
      async de facto por el disco.
  - id: s2
    tipo: ejemplo
    titulo: 1. Refactor cli.ts
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "async/await en la práctica" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: m02-habits src/cli.ts con async main y try/catch
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
      ¿Es buena práctica en esta lección? “`async` en cada función aunque no hay
      await."
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
          Un solo `await` por paso lógico en `cli.ts`, sin `.then` anidados, con
          `try/catch` en el borde.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Paralelo controlado
    xp: 10
    cuerpo: >-
      `src/async/paralelo.ts` — `Promise.all` para leer dos archivos de ejemplo;
      documenta cuándo **no** usar paralelo (misma escritura).
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 11 — resto
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
