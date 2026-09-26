---
id: L03
materia: M02
orden: 3
titulo: Control de flujo
horas: 3
semana: 1
lectura: "EJ cap. 2 — bucles y condicionales"
evidencia: "src/flujo/clasificador.ts + 2 katas con bucles"
---

# L03 — Control de flujo

**~3 h · Semana 1**

Condicionales y bucles con tipos claros: ramas que TypeScript puede seguir y funciones que retornan en todos los caminos.

## Objetivo

Implementar un clasificador con `if`/`else`, `switch` y bucles, sin `return` olvidados.

## Por qué importa

La CLI validará comandos e índices aquí. TS avisa cuando una rama no devuelve valor.

## Pasos

### 1. Clasificador de notas (45 min)

`src/flujo/clasificador.ts`:

```ts
export type Nivel = "insuficiente" | "aprobado" | "notable" | "sobresaliente";

export function nivelDesdePuntos(puntos: number, max: number): Nivel {
  if (max <= 0) {
    throw new Error("max debe ser positivo");
  }
  const ratio = puntos / max;
  if (ratio < 0.5) return "insuficiente";
  if (ratio < 0.7) return "aprobado";
  if (ratio < 0.9) return "notable";
  return "sobresaliente";
}
```

Añade `etiquetaCorta(nivel: Nivel): string` con `switch`.

### 2. Bucles y acumuladores (40 min)

`src/flujo/suma-rango.ts` con `sumaHasta(n)` y `primerDivisor(n): number | null`.

### 3. Dos katas con bucles (50 min)

FizzBuzz tipado y búsqueda lineal sin `.find` todavía.

### 4. Lectura EJ (35 min)

Cap. 2 + **1 ejercicio** en TS.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 2 (control de flujo) |

## Hecho cuando

1. `clasificador.ts` y `suma-rango.ts` compilan; caso `max <= 0` cubierto.
2. Dos katas nuevas con bucles.
3. `npx tsc --noEmit` limpio en `src/`.

## Errores comunes

- `return` faltante en una rama.
- `switch` sin salida clara por rama.
- Bucles infinitos.

## Siguiente

[L04 — Funciones tipadas](L04-funciones-tipadas.md)
