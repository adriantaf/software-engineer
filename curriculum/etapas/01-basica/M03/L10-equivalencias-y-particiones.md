---
id: L10
materia: M03
orden: 10
titulo: Equivalencias y particiones
horas: 2.5
semana: 3
lectura: "Rosen Cap. 9.5 — relaciones de equivalencia, clases, particiones"
evidencia: "demos.md Demo 7 (equivale a mod n) + clasesDeEquivalencia() en relations.ts"
---

# L10 — Equivalencias y particiones

**~2.5 h · Semana 3**

Una relación de equivalencia **parte** el conjunto en clases disjuntas. Es el modelo de `=` en tipos, congruencias y componentes conexas (más adelante en grafos).

## Objetivo

Probar que `≡ (mod m)` es relación de equivalencia; calcular clases de equivalencia en un conjunto finito.

## Pasos

### 1. Definición (20 min)

En `relaciones.md`: relación de equivalencia = reflexiva + simétrica + transitiva. Teorema: particiona `A` en clases disjuntas cuya unión es `A`.

### 2. Demostración (50–60 min)

**Demo 7** en `demos.md`: en `ℤ` (o en `ℕ` con cuidado), `a ≡ b (mod m)` iff `m | (a−b)` es equivalencia. Prueba las tres propiedades (m fijo ≥ 2).

### 3. Clases en finito (40 min)

En `A = {0,1,…,11}`, `m = 4`: lista clases `[0]`, `[1]`, … sin repetir representantes.

### 4. Implementación (50 min)

```ts
export function clasesDeEquivalencia<A>(
  r: Relacion<A>,
  universo: Set<A>,
): Set<Set<A>> {
  // Encuentra clases por representante: para cada x no visitado, clase = { y | (x,y)∈R }
}
```

Asume `r` ya es equivalencia (documenta). Tests con `mod 3` en `{0,1,2,3,4,5}`.

### 5. Puente conceptual (15 min)

Una frase: cómo esto se parece a “agrupar usuarios con el mismo rol” o “nodos en la misma componente”.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 9.5 |

## Hecho cuando

1. Demo 7 completa en `demos.md`.
2. `clasesDeEquivalencia` pasa test modular pequeño.
3. Dibujas la partición de `{0..11}` mod 4.

## Errores comunes

- Clases que se solapan (error al definir representante).
- Usar `mod` en TS con negativos sin normalizar (documenta convención).
- Confundir clase con conjunto de todos los pares.

## Siguiente

[L11 — Órdenes parciales y totales](L11-ordenes-parciales-y-totales.md)
