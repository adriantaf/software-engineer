---
id: L07
materia: M03
orden: 7
titulo: Leyes de conjuntos y pruebas
horas: 2.5
semana: 2
lectura: "Rosen Cap. 2.2 — leyes (De Morgan conjuntista, distributiva)"
evidencia: "demos.md +2 demos (De Morgan conjuntos, A∩(B∪C)) + verificación con sets.ts"
---

# L07 — Leyes de conjuntos y pruebas

**~2.5 h · Semana 2**

Las leyes conjuntistas son el análogo de las leyes lógicas (elementos ↔ predicado `x ∈ …`).

## Objetivo

Demostrar dos identidades conjuntistas; verificarlas en un universo finito con tu código.

## Leyes objetivo

1. `(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ` (De Morgan) respecto a `U`.
2. `A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)` (distributiva).

## Pasos

### 1. Demostración por elementos (60–70 min)

En `demos.md`, **Demo 4** y **Demo 5**:

- Método estándar: “Sea x ∈ U. Entonces x ∈ LHS iff … iff x ∈ RHS.”
- Una prueba completa por ley.

### 2. Verificación computacional (40 min)

Test en `sets.test.ts` que, para `U` aleatorio pequeño (o fijo `{1..8}`) y `A,B,C` aleatorios, compare:

- `complemento(union(A,B), U)` vs `interseccion(complemento(A,U), complemento(B,U))`
- etc.

Usa `iguales` o convierte a arrays ordenados para comparar.

### 3. Rosen (30 min)

Un ejercicio del libro que pida reescribir una expresión conjuntista; solución en `conjuntos.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.2 (leyes) |
| Apuntes | `leyes-logicas.md` (paralelo De Morgan) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Dos demostraciones por elementos en `demos.md`.
2. Tests de identidad pasan en un `U` finito.
3. Explicas en una frase el puente ∧/∩ y ∨/∪ en pruebas por elementos.

## Errores comunes

- Demostrar solo con un ejemplo numérico (no es prueba general).
- Olvidar “sea x ∈ U” al usar complemento.
- Tests que solo usan un caso trivial.

## Siguiente

[L08 — Funciones: imagen, inyectividad y biyección](L08-funciones-imagen-e-inyectividad.md)
