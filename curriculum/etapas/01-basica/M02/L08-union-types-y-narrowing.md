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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Parsear entrada de usuario o JSON parcial con ramas que
      TypeScript entiende después de cada guardia.


      La CLI recibirá strings sucios. Narrowing es cómo conviertes “string
      cualquiera” en datos válidos o error legible.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tipo Result
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Union types y narrowing" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: 'src/tipos/resultado.ts con Result<T,E> + parse seguro'
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
      ¿Es buena práctica en esta lección? “Union sin campo discriminante y
      lógica frágil."
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
          Parsear entrada de usuario o JSON parcial con ramas que TypeScript
          entiende después de cada guardia.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Parse de entero positivo
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: explicacion
    titulo: 3. Handbook Narrowing
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
