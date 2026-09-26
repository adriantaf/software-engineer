---
id: L05
materia: M03
orden: 5
titulo: Conjuntos — notación y membresía
horas: 2.5
semana: 2
lectura: "Rosen Cap. 2.1 — conjuntos, notación, ⊆, ∈, cardinalidad, ℕ/ℤ/ℝ"
evidencia: "apuntes/conjuntos.md + definición formal de subconjunto en demos o apuntes"
---

# L05 — Conjuntos: notación y membresía

**~2.5 h · Semana 2**

Semana 2: el lenguaje de conjuntos es el de tipos, tablas y consultas. Empiezas con notación rigurosa.

## Objetivo

Usar ∈, ⊆, ⊂, ∅, cardinalidad; describir conjuntos por extensión e intención; distinguir subconjunto propio de igualdad.

## Pasos

### 1. Apuntes base (50–60 min)

`projects/m03-discretas/apuntes/conjuntos.md`:

- Definiciones: conjunto, elemento, cardinalidad `|A|`.
- Notación `{1,2,3}`, `{x ∈ D | P(x)}`.
- `A ⊆ B` vs `A ⊂ B` (propio): da un ejemplo de cada relación entre dos conjuntos concretos.
- Conjuntos estándar: ℕ, ℤ, ℚ, ℝ (qué incluye ℕ en tu libro: ¿0 o no? — **fíjalo** y sé consistente).

### 2. Igualdad de conjuntos (30 min)

Principio de extensionalidad: `A = B` iff ∀x (x ∈ A ↔ x ∈ B). Demuestra en una línea que `{1,2,3} = {3,1,2}` usando el principio.

### 3. Ejercicios Rosen (40 min)

Resuelve **3** ejercicios del cap. 2.1 (descripción de conjuntos, ⊆, cardinalidad) en el apunte (enunciado + solución).

### 4. Puente TS (20 min)

Documenta en el apunte: en TypeScript, `Set<T>` modela conjunto **finito** de valores hashables; `∈` es `.has(x)`. Limitaciones: no hay ℝ como conjunto enumerable.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.1 |
| Ficha M03 | Semana 2 en tabla de lecciones |

## Hecho cuando

1. `conjuntos.md` existe con definiciones, ejemplo ⊆/⊂ y 3 ejercicios resueltos.
2. Declaras explícitamente si ℕ incluye 0 en todo el módulo.
3. Puedes escribir `{n ∈ ℤ | n² < 10}` por extensión.

## Errores comunes

- Usar ∈ entre conjuntos (confundir con ⊆).
- Orden en extensión importa (no importa).
- Mezclar “conjunto de pares ordenados” con “conjunto de primeras componentes” sin decirlo.

## Siguiente

[L06 — Operaciones conjuntistas en TypeScript](L06-operaciones-conjuntistas-en-typescript.md)
