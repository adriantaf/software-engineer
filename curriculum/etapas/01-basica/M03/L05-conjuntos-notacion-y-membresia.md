---
id: L05
materia: M03
orden: 5
titulo: Conjuntos — notación y membresía
horas: 2.5
semana: 2
lectura: 'Rosen Cap. 2.1 — conjuntos, notación, ⊆, ∈, cardinalidad, ℕ/ℤ/ℝ'
evidencia: apuntes/conjuntos.md + definición formal de subconjunto en demos o apuntes
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Semana 2: el lenguaje de conjuntos es el de tipos, tablas y consultas.
      Empiezas con notación rigurosa.


      **Objetivo de esta lección:** Usar ∈, ⊆, ⊂, ∅, cardinalidad; describir
      conjuntos por extensión e intención; distinguir subconjunto propio de
      igualdad.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Apuntes base
    xp: 10
    cuerpo: >-
      `projects/m03-discretas/apuntes/conjuntos.md`: - Definiciones: conjunto,
      elemento, cardinalidad `|A|`. - Notación `{1,2,3}`, `{x ∈ D | P(x)}`. - `A
      ⊆ B` vs `A ⊂ B` (propio): da un ejemplo de cada relación entre dos
      conjuntos concretos. - Conjuntos estándar: ℕ, ℤ, ℚ, ℝ (qué incluye ℕ en tu
      libro: ¿0 o no? — **fíjalo** y sé consistente).
  - id: s3
    tipo: ejemplo
    titulo: Igualdad de conjuntos
    xp: 10
    cuerpo: >-
      Principio de extensionalidad: `A = B` iff ∀x (x ∈ A ↔ x ∈ B). Demuestra en
      una línea que `{1,2,3} = {3,1,2}` usando el principio.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Conjuntos — notación y membresía», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `conjuntos.md` existe con definiciones, ejemplo ⊆/⊂ y 3 ejercicios
          resueltos.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Conjuntos — notación y
          membresía
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Usar ∈ entre conjuntos (confundir con
      ⊆)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Usar ∈, ⊆, ⊂, ∅, cardinalidad; describir conjuntos por extensión e
          intención; distinguir subconjunto propio de igualdad.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Ejercicios Rosen
    xp: 10
    cuerpo: >-
      Resuelve **3** ejercicios del cap. 2.1 (descripción de conjuntos, ⊆,
      cardinalidad) en el apunte (enunciado + solución).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `conjuntos.md` existe con definiciones, ejemplo ⊆/⊂ y 3 ejercicios
        resueltos.
      - Declaras explícitamente si ℕ incluye 0 en todo el módulo.
      - 'Puedes escribir `{n ∈ ℤ | n² < 10}` por extensión.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


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
