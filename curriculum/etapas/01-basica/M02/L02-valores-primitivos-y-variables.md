---
id: L02
materia: M02
orden: 2
titulo: 'Valores, primitivos y variables'
horas: 2.5
semana: 1
lectura: EJ cap. 2 (estructura del programa) + TS Handbook Basic Types
evidencia: src/tipos-basicos.ts con ejemplos + 3 katas fáciles en src/katas/
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los bugs de “¿qué tipo es esto?” aparecen en APIs, JSON y CLI. Nombrar
      tipos desde el día 1 te ahorra `any` disfrazado.


      **Objetivo de esta lección:** Escribir un módulo de referencia con tipos
      primitivos, inferencia cuando aporta claridad, y resolver 3 katas cortas
      en TypeScript strict.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Módulo de referencia
    xp: 10
    cuerpo: >-
      ```ts

      export const PI_APROX: number = 3.14159;

      export let contadorSesion = 0;


      export function esMayorDeEdad(edad: number): boolean {
        return edad >= 18;
      }


      export function formatearEtiqueta(nombre: string, activo: boolean): string
      {
        return activo ? `${nombre} ✓` : nombre;
      }


      export let ultimoError: string | null = null;

      ```


      Crea `src/tipos-basicos.ts`: Demuestra con `src/tipos-basicos-demo.ts` que
      importa y hace `console.log` de dos casos.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Inferencia vs anotación
    xp: 10
    cuerpo: >-
      ```ts

      export const PI_APROX: number = 3.14159;

      export let contadorSesion = 0;


      export function esMayorDeEdad(edad: number): boolean {
        return edad >= 18;
      }


      export function formatearEtiqueta(nombre: string, activo: boolean): string
      {
        return activo ? `${nombre} ✓` : nombre;
      }


      export let ultimoError: string | null = null;

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Valores, primitivos y variables», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`src/tipos-basicos.ts` compila y usa `const`/`let` con intención.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Valores, primitivos y
          variables
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
    pregunta: ¿Es recomendable en esta lección? “Usar `var`."
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
          Escribir un módulo de referencia con tipos primitivos, inferencia
          cuando aporta claridad, y resolver 3 katas cortas en TypeScript
          strict.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tres katas
    xp: 10
    cuerpo: >-
      En `src/katas/` tres archivos (EJ cap. 2 o Codewars 8 kyu):
      conversión/redondeo, string no vacío, contar vocales. Cada uno exporta
      funciones tipadas. Lista las 3 en el README.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`src/tipos-basicos.ts` compila y usa `const`/`let` con intención.'
      - Tres katas en `src/katas/`.
      - Explicas en una frase `null` vs `undefined` en TS.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Valores, primitivos y variables

**~2.5 h · Semana 1**

Solidificas el vocabulario: `string`, `number`, `boolean`, `null`, `undefined`, y cuándo usar `const` vs `let`.

## Objetivo

Escribir un módulo de referencia con tipos primitivos, inferencia cuando aporta claridad, y resolver 3 katas cortas en TypeScript strict.

## Por qué importa

Los bugs de “¿qué tipo es esto?” aparecen en APIs, JSON y CLI. Nombrar tipos desde el día 1 te ahorra `any` disfrazado.

## Pasos

### 1. Módulo de referencia (40 min)

Crea `src/tipos-basicos.ts`:

```ts
export const PI_APROX: number = 3.14159;
export let contadorSesion = 0;

export function esMayorDeEdad(edad: number): boolean {
  return edad >= 18;
}

export function formatearEtiqueta(nombre: string, activo: boolean): string {
  return activo ? `${nombre} ✓` : nombre;
}

export let ultimoError: string | null = null;
```

Demuestra con `src/tipos-basicos-demo.ts` que importa y hace `console.log` de dos casos.

### 2. Inferencia vs anotación (25 min)

En `src/inferencia.ts`, tres funciones: inferencia pura, retorno anotado en lógica larga, y un caso donde **debes** anotar (ej. array vacío). Compara con `npx tsc --noEmit`.

### 3. Tres katas (50–60 min)

En `src/katas/` tres archivos (EJ cap. 2 o Codewars 8 kyu): conversión/redondeo, string no vacío, contar vocales. Cada uno exporta funciones tipadas. Lista las 3 en el README.

### 4. Lectura (30 min)

EJ cap. 2 + *Basic Types* del Handbook.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 2 |
| TS Handbook | [Basic Types](https://www.typescriptlang.org/docs/handbook/2/basic-types.html) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `src/tipos-basicos.ts` compila y usa `const`/`let` con intención.
2. Tres katas en `src/katas/`.
3. Explicas en una frase `null` vs `undefined` en TS.

## Errores comunes

- Usar `var`.
- Anotaciones redundantes (`const x: number = 5`).
- Katas copiadas sin reescribir.

## Siguiente

[L03 — Control de flujo](L03-control-de-flujo.md)
