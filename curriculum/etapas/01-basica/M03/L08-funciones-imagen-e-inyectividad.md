---
id: L08
materia: M03
orden: 8
titulo: Funciones — imagen, inyectividad y biyección
horas: 3
semana: 2
lectura: "Rosen Cap. 2.3 — funciones, imagen, inyectiva, sobreyectiva, biyectiva"
evidencia: "apuntes/funciones.md + src/functions.ts (predicados) + 1 demo inyectividad"
---

# L08 — Funciones: imagen, inyectividad y biyección

**~3 h · Semana 2**

Cierras la semana 2 relacionando conjuntos con **funciones** (la base de map/filter y de cardinalidad).

## Objetivo

Definir función como relación funcional; clasificar inyectiva / sobreyectiva / biyectiva; implementar predicados sobre funciones finitas `f: A → B`.

## Pasos

### 1. Apuntes (40–50 min)

`projects/m03-discretas/apuntes/funciones.md`:

- `f: A → B`, dominio, codominio, imagen `f(S)`.
- Definiciones formales de inyectiva, sobreyectiva, biyectiva.
- Ejemplo: `f: ℤ → ℤ`, `f(n)=2n` (inyectiva, no sobreyectiva) — ajusta si usas ℕ.

### 2. Demostración corta (40 min)

**Demo 6** en `demos.md`: prueba de que la composición de dos funciones inyectivas es inyectiva (o ejercicio equivalente del Rosen).

### 3. Implementación finita (60–70 min)

Modela `f` como `Map<A,B>` o `Record` con dominio listado.

`src/functions.ts`:

```ts
export function esInyectiva<A>(f: Map<A, unknown>): boolean {
  const vistos = new Set<unknown>();
  for (const v of f.values()) {
    if (vistos.has(v)) return false;
    vistos.add(v);
  }
  return true;
}

export function esSobreyectiva<A, B>(
  f: Map<A, B>,
  codominio: Set<B>,
): boolean {
  const imagen = new Set(f.values());
  for (const y of codominio) if (!imagen.has(y)) return false;
  return true;
}
```

Importa `esSubconjunto` solo si lo reutilizas; la versión con bucle deja claro el cuantificador ∀y ∈ codominio.

Tests con funciones en dominios de 3–4 elementos.

### 4. Retro semana 2 (15 min)

Nota en `conjuntos.md` o bitácora: qué operación de `sets.ts` usarás en relaciones (semana 3).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.3 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `funciones.md` con definiciones y al menos un ejemplo de cada tipo de función.
2. Predicados inyectiva/sobreyectiva con tests en dominio finito.
3. **Demo 6** en `demos.md` commiteada.

## Errores comunes

- Confundir codominio con imagen.
- Probar inyectividad solo con 2 valores.
- Sobreyectiva: olvidar un elemento del codominio.

## Siguiente

[L09 — Relaciones y propiedades](L09-relaciones-y-propiedades.md)
