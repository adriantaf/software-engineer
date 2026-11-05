---
id: L03
materia: M08
orden: 3
titulo: Análisis de bucles y recursión simple
horas: 5
semana: 1
lectura: Sumas de bucles anidados y recurrencias simples
evidencia: 3 snippets analizados en markdown
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Pasas de definiciones a contar operaciones en código que tú escribes.


      **Objetivo de esta lección:** Analizar tres snippets (2 iterativos + 1
      recursivo) en `docs/analisis-bucles.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Snippet A — bucle simple
    xp: 10
    cuerpo: |-
      ```ts
      for (let i = 0; i < n; i++)
        for (let j = i; j < n; j++) { /* ... */ }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Snippet B — anidado
    xp: 10
    cuerpo: |-
      ```ts
      for (let i = 0; i < n; i++)
        for (let j = i; j < n; j++) { /* ... */ }
      ```

      Cuenta iteraciones ≈ n(n+1)/2 → Θ(n²).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Análisis de bucles y recursión simple», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Análisis de bucles y
          recursión simple
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
      ¿Es recomendable en esta lección? “Contar mal bucles dependientes (`for i;
      for j=i`)."
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
          Analizar tres snippets (2 iterativos + 1 recursivo) en
          `docs/analisis-bucles.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Snippet C — recursión
    xp: 10
    cuerpo: >-
      `rec(n) = rec(n-1) + work` tipo factorial o suma. Unfolding hasta base;
      Θ(n) llamadas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `docs/analisis-bucles.md` con 3 snippets TS y su complejidad
        justificada.
      - Al menos uno recursivo con árbol o unfolding escrito.
      - 'Commit `docs(m08): analisis bucles y recursion`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Análisis de bucles y recursión simple

**~5.0 h · Semana 1**

Pasas de definiciones a contar operaciones en código que tú escribes.

## Objetivo

Analizar tres snippets (2 iterativos + 1 recursivo) en `docs/analisis-bucles.md`.

## Pasos

### 1. Snippet A — bucle simple (35 min)

Escribe un `sum(a: number[])` y justifica Θ(n) tiempo / Θ(1) extra.

### 2. Snippet B — anidado (50 min)

```ts
for (let i = 0; i < n; i++)
  for (let j = i; j < n; j++) { /* ... */ }
```

Cuenta iteraciones ≈ n(n+1)/2 → Θ(n²).

### 3. Snippet C — recursión (60 min)

`rec(n) = rec(n-1) + work` tipo factorial o suma. Unfolding hasta base; Θ(n) llamadas.

### 4. Contraste (40 min)

Añade binary search recursivo: profundidad log n. Enlaza a L01.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): analisis bucles y recursion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Contar iteraciones; árbol de recursión simple (T(n)=T(n-1)+O(1)) | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `docs/analisis-bucles.md` con **3** snippets TS y su complejidad justificada.
2. Al menos uno recursivo con árbol o unfolding escrito.
3. Commit `docs(m08): analisis bucles y recursion`.

## Errores comunes

- Contar mal bucles dependientes (`for i; for j=i`).
- Decir O(n²) a binary search recursivo.
- Snippets sin código real (solo prosa).

## Siguiente

[L04 — Tres problemas con complejidad escrita](L04-tres-problemas-con-complejidad-escrita.md)
