---
id: L06
materia: M03
orden: 6
titulo: Operaciones conjuntistas en TypeScript
horas: 3
semana: 2
lectura: "Rosen Cap. 2.2 — unión, intersección, diferencia, complemento (respecto a U)"
evidencia: "src/sets.ts con ∪, ∩, \\, ⊆, tests Vitest"
---

# L06 — Operaciones conjuntistas en TypeScript

**~3 h · Semana 2**

Implementas las operaciones que Rosen define y las pruebas contra ejemplos finitos.

## Objetivo

Implementar unión, intersección, diferencia, subconjunto y complemento relativo a un universo `U`; cubrir con tests.

## Pasos

### 1. Especificación (20 min)

En `apuntes/conjuntos.md`, añade sección **Operaciones** con definiciones:

- `A ∪ B = {x | x ∈ A ∨ x ∈ B}`
- `A ∩ B = {x | x ∈ A ∧ x ∈ B}`
- `A − B = {x | x ∈ A ∧ x ∉ B}`
- `Ā` respecto a `U`: `U − A`

### 2. Implementación (70–80 min)

`projects/m03-discretas/src/sets.ts`:

```ts
export function union<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a, ...b]);
}

export function interseccion<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a].filter((x) => b.has(x)));
}

export function diferencia<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a].filter((x) => !b.has(x)));
}

export function esSubconjunto<T>(a: Set<T>, b: Set<T>): boolean {
  for (const x of a) if (!b.has(x)) return false;
  return true;
}

export function complemento<T>(a: Set<T>, universo: Set<T>): Set<T> {
  return diferencia(universo, a);
}
```

Añade `iguales(a,b)` por cardinalidad y doble inclusión si quieres rigor extra.

### 3. Tests (40–50 min)

`sets.test.ts`: al menos 2 casos por función, incluyendo conjuntos vacíos y `U` finito pequeño.

```bash
npm test
```

### 4. Ejemplo aplicado (20 min)

Dado `U = {1..10}`, `A = pares`, `B = múltiplos de 3`, calcula a mano `|A ∩ B|` y verifica con tu código (construye los `Set` en un test o script `tsx`).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.2 |

## Hecho cuando

1. `sets.ts` exporta las operaciones listadas y `npm test` pasa.
2. Manejas `∅` sin errores (unión con vacío, complemento de vacío).
3. `esSubconjunto` coincide con definición (∀x ∈ A → x ∈ B).

## Errores comunes

- Complemento sin universo explícito.
- Mutar el `Set` de entrada al calcular unión.
- `filter` sobre `b` en intersección cuando deberías iterar el más pequeño (eficiencia: opcional, pero documenta).

## Siguiente

[L07 — Leyes de conjuntos y pruebas](L07-leyes-de-conjuntos-y-pruebas.md)
