---
id: L08
materia: M02
orden: 8
titulo: Union types y narrowing
horas: 2.5
semana: 2
lectura: TS Handbook Narrowing + repaso EJ caps. 4–5
evidencia: 'src/tipos/resultado.ts con Result<T,E> + parse seguro'
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La CLI recibirá strings sucios. Narrowing es cómo conviertes “string
      cualquiera” en datos válidos o error legible.


      **Objetivo de esta lección:** Parsear entrada de usuario o JSON parcial
      con ramas que TypeScript entiende después de cada guardia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tipo Result
    xp: 10
    cuerpo: |-
      ```ts
      export type Result<T, E = string> =
        | { ok: true; value: T }
        | { ok: false; error: E };

      export function ok<T>(value: T): Result<T, never> {
        return { ok: true, value };
      }

      export function err<E>(error: E): Result<never, E> {
        return { ok: false, error };
      }
      ```

      `src/tipos/resultado.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Parse de entero positivo
    xp: 10
    cuerpo: >-
      ```ts

      import { err, ok, type Result } from "./resultado.js";


      export function parseEnteroPositivo(raw: string): Result<number, string> {
        const t = raw.trim();
        if (!/^\d+$/.test(t)) return err("no es un entero positivo");
        const n = Number(t);
        if (n === 0) return err("debe ser mayor que cero");
        return ok(n);
      }

      ```


      `src/tipos/parse.ts`: Usa `if (!result.ok) { ... }` y observa cómo TS
      acota `value`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Union types y narrowing», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `Result` y `parseEnteroPositivo` compilan; ramas `ok`/`err` usadas
          correctamente.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Union types y narrowing
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
      ¿Es recomendable en esta lección? “Union sin campo discriminante y lógica
      frágil."
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
          Parsear entrada de usuario o JSON parcial con ramas que TypeScript
          entiende después de cada guardia.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Handbook Narrowing
    xp: 10
    cuerpo: >-
      Lee *Narrowing* y replica **2 ejemplos** del handbook en
      `src/tipos/ejemplos-narrowing.ts`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `Result` y `parseEnteroPositivo` compilan; ramas `ok`/`err` usadas
        correctamente.
      - Bitácora semana 2 M02 con horas y bloqueos.
      - ≥15 katas o plan explícito para llegar a 20.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Union types y narrowing

**~2.5 h · Semana 2**

Cierras la semana 2 con uniones discriminadas, `typeof`/`in` y un patrón `Result` para errores sin excepciones everywhere.

## Objetivo

Parsear entrada de usuario o JSON parcial con ramas que TypeScript entiende después de cada guardia.

## Por qué importa

La CLI recibirá strings sucios. Narrowing es cómo conviertes “string cualquiera” en datos válidos o error legible.

## Pasos

### 1. Tipo Result (45 min)

`src/tipos/resultado.ts`:

```ts
export type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export function ok<T>(value: T): Result<T, never> {
  return { ok: true, value };
}

export function err<E>(error: E): Result<never, E> {
  return { ok: false, error };
}
```

### 2. Parse de entero positivo (40 min)

`src/tipos/parse.ts`:

```ts
import { err, ok, type Result } from "./resultado.js";

export function parseEnteroPositivo(raw: string): Result<number, string> {
  const t = raw.trim();
  if (!/^\d+$/.test(t)) return err("no es un entero positivo");
  const n = Number(t);
  if (n === 0) return err("debe ser mayor que cero");
  return ok(n);
}
```

Usa `if (!result.ok) { ... }` y observa cómo TS acota `value`.

### 3. Handbook Narrowing (40 min)

Lee *Narrowing* y replica **2 ejemplos** del handbook en `src/tipos/ejemplos-narrowing.ts`.

### 4. Katas + P1 progreso (25 min)

Llega a **≥15 katas** o deja lista en README cuántas faltan para 20 (P1).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| TS Handbook | [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) |
| *Eloquent JavaScript* | Repaso caps. 4–5 (ejercicio pendiente) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `Result` y `parseEnteroPositivo` compilan; ramas `ok`/`err` usadas correctamente.
2. Bitácora semana 2 M02 con horas y bloqueos.
3. ≥15 katas o plan explícito para llegar a 20.

## Errores comunes

- Union sin campo discriminante y lógica frágil.
- Cast con `as` para callar al compilador en vez de narrow.
- Ignorar el branch `ok: false`.

## Siguiente

[L09 — Módulos ES en Node](L09-modulos-es-en-node.md)
