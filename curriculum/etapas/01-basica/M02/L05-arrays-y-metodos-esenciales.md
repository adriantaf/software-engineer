---
id: L05
materia: M02
orden: 5
titulo: Arrays y métodos esenciales
horas: 2.5
semana: 2
lectura: "EJ cap. 4 (objetos y arrays) — primera mitad"
evidencia: "src/arrays/ con push/map inmutable + 3 katas sobre arrays"
---

# L05 — Arrays y métodos esenciales

**~2.5 h · Semana 2**

Arrays tipados, inmutabilidad práctica y métodos que usarás cada día: `map`, `filter`, `slice`, `includes`.

## Objetivo

Modelar listas de datos sin mutar por accidente y resolver 3 katas centradas en arrays.

## Por qué importa

Tu CLI guardará listas de hábitos y tareas. Casi todo pasa por copiar → transformar → persistir.

## Pasos

### 1. Arrays readonly en espíritu (40 min)

`src/arrays/lista.ts`:

```ts
export type Tarea = { id: string; titulo: string; hecha: boolean };

export function marcarHecha(tareas: Tarea[], id: string): Tarea[] {
  return tareas.map((t) => (t.id === id ? { ...t, hecha: true } : t));
}

export function pendientes(tareas: Tarea[]): Tarea[] {
  return tareas.filter((t) => !t.hecha);
}
```

### 2. Métodos de consulta (30 min)

`src/arrays/estadisticas.ts`: `suma`, `promedio`, `maximo` sobre `number[]` con validación de array vacío (`null` o throw — elige y documenta).

### 3. Tres katas arrays (55 min)

Ej.: rotar array, eliminar duplicados, intersección de dos listas pequeñas.

### 4. Lectura (25 min)

EJ cap. 4 hasta objetos/arrays básicos.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 4 (inicio) |
| TS Handbook | [Everyday Types — Arrays](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays) |

## Hecho cuando

1. `marcarHecha` no muta el array original (prueba con `const antes = [...]` y compara).
2. Tres katas nuevas en `src/katas/`.
3. ≥10 katas totales en el repo o documentas cuántas faltan para P1.

## Errores comunes

- Mutar con `.sort()` sin copiar antes.
- `array[i]` sin comprobar límites en funciones públicas.
- Tipar arrays como `any[]`.

## Siguiente

[L06 — Objetos, interfaces y tipos](L06-objetos-interfaces-y-tipos.md)
