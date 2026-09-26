---
id: L11
materia: M03
orden: 11
titulo: Órdenes parciales y totales
horas: 2.5
semana: 3
lectura: "Rosen Cap. 9.6 — orden parcial, orden total, diagrama de Hasse (intro)"
evidencia: "apuntes/ordenes.md + matrizRelacion() + test divisibilidad en {2,4,6,12}"
---

# L11 — Órdenes parciales y totales

**~2.5 h · Semana 3**

No todo es equivalencia: el orden importa para colas de prioridad, dependencias y DAGs.

## Objetivo

Definir orden parcial (reflexivo, antisimétrico, transitivo) y orden total; construir matriz de relación; ejemplo de divisibilidad.

## Pasos

### 1. Apuntes (40 min)

`projects/m03-discretas/apuntes/ordenes.md`:

- Orden parcial `(A, ≤)`.
- Orden total: además, ∀a,b ∈ A, a ≤ b ∨ b ≤ a.
- Ejemplo: divisibilidad en divisores de 12 vs inclusión de subconjuntos de `{a,b}`.

### 2. Diagrama (30 min)

Dibuja diagrama de Hasse (a mano, foto o ASCII) para divisores de 12 con `|`.

### 3. Matriz de relación (P2 parcial) (60 min)

En `src/relations.ts`:

```ts
export function matrizRelacion<A>(
  r: Relacion<A>,
  elementos: A[],
): number[][] {
  const n = elementos.length;
  const idx = new Map(elementos.map((e, i) => [e, i]));
  const m = Array.from({ length: n }, () => Array(n).fill(0));
  for (const [a, b] of r) {
    const i = idx.get(a)!;
    const j = idx.get(b)!;
    m[i][j] = 1;
  }
  return m;
}
```

Test: relación “divide” en `{2,4,6,12}`; verifica antisimétrica y transitiva con tus predicados de L09.

### 4. Comparación (20 min)

¿Es `≤` en ℝ un orden total? ¿Y divisibilidad en ℤ⁺? Respuesta corta en `ordenes.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 9.6 |

## Hecho cuando

1. `ordenes.md` con definiciones y Hasse de divisores de 12.
2. `matrizRelacion` con test coherente con la relación elegida.
3. Distingues parcial vs total con un ejemplo de cada uno en el mismo conjunto finito.

## Errores comunes

- Llamar “orden” a una relación no transitiva.
- Hasse con todas las aristas redundantes (incluir reflexivos).
- Matriz sin orden fijo de elementos (documenta el orden de filas/columnas).

## Siguiente

[L12 — Inducción matemática](L12-induccion-matematica.md)
