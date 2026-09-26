---
id: L14
materia: M03
orden: 14
titulo: Permutaciones y combinaciones
horas: 3
semana: 4
lectura: "Rosen Cap. 6.3–6.4 — permutaciones, combinaciones, notación C(n,k) y P(n,k)"
evidencia: "conteo.md + src/counting.ts (nCk, nPk) + tests factorial pequeño"
---

# L14 — Permutaciones y combinaciones

**~3 h · Semana 4**

Orden importa (permutación) o no (combinación). Debes elegir la fórmula según el **problema**, no según la que recuerdes primero.

## Objetivo

Derivar y usar `P(n,k)` y `C(n,k)`; resolver problemas de selección con y sin repetición (alcance del capítulo); implementar funciones con validación.

## Pasos

### 1. Fórmulas y significado (40 min)

En `conteo.md`:

- `P(n,k) = n!/(n−k)!` — k-permutaciones de n.
- `C(n,k) = n!/(k!(n−k)!)` — subconjuntos de tamaño k.
- Ejemplo narrativo: comité vs podio.

### 2. Problemas (70 min)

**3** problemas:

1. Ordenar 5 libros en un estante de 5 (permutación).
2. Elegir 3 personas de 10 sin orden (combinación).
3. Un problema “trampa” donde el orden sí importa aunque parezca comité — justifica.

### 3. Implementación (60 min)

```ts
export function factorial(n: number): number {
  if (n < 0) throw new Error("n negativo");
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
}

export function nPk(n: number, k: number): number {
  if (k < 0 || k > n) return 0;
  return factorial(n) / factorial(n - k);
}

export function nCk(n: number, k: number): number {
  if (k < 0 || k > n) return 0;
  return factorial(n) / (factorial(k) * factorial(n - k));
}
```

Tests: casos borde `k=0`, `k=n`, `k>n`. Para n grande, comenta overflow (BigInt opcional).

### 4. Rosen (20 min)

Un ejercicio de 6.3 o 6.4 en `conteo.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.3–6.4 |

## Hecho cuando

1. Tres problemas con identificación explícita P vs C.
2. `nPk` y `nCk` con tests borde.
3. Explicas en una frase por qué `C(n,k) = C(n, n−k)`.

## Errores comunes

- Usar `C` cuando el orden importa (ranking).
- No devolver 0 cuando `k > n`.
- Factoriales enormes sin advertir overflow en JS.

## Siguiente

[L15 — Principio de inclusión-exclusión](L15-inclusion-exclusion.md)
