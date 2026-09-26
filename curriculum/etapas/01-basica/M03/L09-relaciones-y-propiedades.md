---
id: L09
materia: M03
orden: 9
titulo: Relaciones y propiedades
horas: 2.5
semana: 3
lectura: "Rosen Cap. 9.1 — relaciones en conjuntos, propiedades reflexiva, simétrica, antisimétrica, transitiva"
evidencia: "apuntes/relaciones.md + src/relations.ts (predicados de propiedades)"
---

# L09 — Relaciones y propiedades

**~2.5 h · Semana 3**

Las relaciones modelan “conectado”, “≤”, “equivale a”, tablas FK. Empiezas con propiedades sobre un conjunto finito.

## Objetivo

Definir relación binaria `R ⊆ A × A`; verificar reflexiva, simétrica, antisimétrica, transitiva; representar `R` como conjunto de pares.

## Pasos

### 1. Apuntes (40 min)

`projects/m03-discretas/apuntes/relaciones.md`:

- Par ordenado, producto cartesiano (repaso).
- `R` en `A`: notación `aRb` o `(a,b) ∈ R`.
- Definiciones de las cuatro propiedades + **ejemplo** y **contraejemplo** de cada una.

### 2. Matriz de relación (30 min)

Para `A = {1,2,3,4}`, define una relación `R` dada en lista de pares. Dibuja la matriz 0/1 y lee reflexividad/simetría en la matriz.

### 3. Código (60–70 min)

`src/relations.ts`:

```ts
export type Par<A> = [A, A];
export type Relacion<A> = Set<Par<A>>;

export function esReflexiva<A>(r: Relacion<A>, a: Set<A>): boolean { /* ... */ }
export function esSimetrica<A>(r: Relacion<A>): boolean { /* ... */ }
export function esTransitiva<A>(r: Relacion<A>): boolean { /* ... */ }
export function esAntisimetrica<A>(r: Relacion<A>): boolean { /* ... */ }
```

Tests: relación `≤` en `{1,2,3}` codificada como pares; relación “divide a” en `{2,4,6}`; un contraejemplo que falle transitividad.

### 4. Ejercicio Rosen (30 min)

Un ejercicio de clasificar propiedades; solución en `relaciones.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 9.1 (relaciones y propiedades) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Apunte con definiciones y matriz de un ejemplo.
2. Cuatro predicados con tests (incluye al menos un fallo intencional en test de contraejemplo).
3. Sabes dar un contraejemplo mínimo cuando una propiedad falla.

## Errores comunes

- Confundir simétrica con antisimétrica (pueden coexistir solo en casos degenerados — piensa en pares).
- Olvidar pares necesarios para reflexividad en el `Set`.
- Transitividad: no cerrar `R` mentalmente sin listar el par faltante.

## Siguiente

[L10 — Equivalencias y particiones](L10-equivalencias-y-particiones.md)
