---
id: L07
materia: M03
orden: 7
titulo: Leyes de conjuntos y pruebas
horas: 2.5
semana: 2
lectura: 'Rosen Cap. 2.2 — leyes (De Morgan conjuntista, distributiva)'
evidencia: 'demos.md +2 demos (De Morgan conjuntos, A∩(B∪C)) + verificación con sets.ts'
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Demostrar dos identidades conjuntistas; verificarlas en un
      universo finito con tu código.


      Las leyes conjuntistas son el análogo de las leyes lógicas (elementos ↔
      predicado `x ∈ …`).
  - id: s2
    tipo: ejemplo
    titulo: 1. Demostración por elementos
    xp: 10
    cuerpo: |-
      En `demos.md`, **Demo 4** y **Demo 5**:

      - Método estándar: “Sea x ∈ U. Entonces x ∈ LHS iff … iff x ∈ RHS.”
      - Una prueba completa por ley.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Leyes de conjuntos y pruebas" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          demos.md +2 demos (De Morgan conjuntos, A∩(B∪C)) + verificación con
          sets.ts
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Demostrar solo con un ejemplo
      numérico (no es prueba general)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Demostrar dos identidades conjuntistas; verificarlas en un universo
          finito con tu código.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Verificación computacional
    xp: 10
    cuerpo: >-
      Test en `sets.test.ts` que, para `U` aleatorio pequeño (o fijo `{1..8}`) y
      `A,B,C` aleatorios, compare:


      - `complemento(union(A,B), U)` vs `interseccion(complemento(A,U),
      complemento(B,U))`

      - etc.


      Usa `iguales` o convierte a arrays ordenados para comparar.
  - id: s7
    tipo: explicacion
    titulo: 3. Rosen
    xp: 10
    cuerpo: >-
      Un ejercicio del libro que pida reescribir una expresión conjuntista;
      solución en `conjuntos.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Dos demostraciones por elementos en `demos.md`.
      - Tests de identidad pasan en un `U` finito.
      - Explicas en una frase el puente ∧/∩ y ∨/∪ en pruebas por elementos.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
