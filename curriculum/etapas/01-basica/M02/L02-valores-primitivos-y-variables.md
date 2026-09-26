---
id: L02
materia: M02
orden: 2
titulo: Valores, primitivos y variables
horas: 2.5
semana: 1
lectura: "EJ cap. 2 (estructura del programa) + TS Handbook Basic Types"
evidencia: "src/tipos-basicos.ts con ejemplos + 3 katas fáciles en src/katas/"
---

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
