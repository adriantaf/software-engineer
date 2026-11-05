---
id: L02
materia: M08
orden: 2
titulo: 'Notación asintótica Θ, O y Ω'
horas: 5
semana: 1
lectura: 'CLRS: crecimiento de funciones — O, Ω, Θ'
evidencia: notacion.md + 5 funciones clasificadas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin lenguaje común de cotas, el resto de M08 es opinión.


      **Objetivo de esta lección:** Escribir `docs/notacion.md` con definiciones
      operativas y clasificar cinco ejemplos concretos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura CLRS
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): notacion asintotica O Omega Theta"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Documento base
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): notacion asintotica O Omega Theta"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Notación asintótica Θ, O y Ω», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Notación asintótica Θ,
          O y Ω
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "docs(m08): notacion asintotica O Omega Theta"`
    comandoEsperado:
      - 'git commit -am "docs(m08): notacion asintotica O Omega Theta"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m08): notacion asintotica O Omega Theta"'
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
          Escribir `docs/notacion.md` con definiciones operativas y clasificar
          cinco ejemplos concretos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cinco clasificaciones
    xp: 10
    cuerpo: >-
      Incluye: binary search; un doble bucle triangular; `push` amortizado de
      array dinámico (referencia M07); factorial recursivo ingenuo; merge de dos
      arrays ordenados. Para cada uno: Θ o O + peor caso.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `docs/notacion.md` define O/Ω/Θ con tus palabras + 1 ejemplo
        gráfico/tabla.
      - >-
        Clasificas 5 funciones/algoritmos (código o fórmulas) con justificación
        de 2–3 líneas c/u.
      - 'Commit `docs(m08): notacion asintotica O Omega Theta`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Notación asintótica Θ, O y Ω

**~5.0 h · Semana 1**

Sin lenguaje común de cotas, el resto de M08 es opinión.

## Objetivo

Escribir `docs/notacion.md` con definiciones operativas y clasificar cinco ejemplos concretos.

## Pasos

### 1. Lectura CLRS (60–75 min)

Capítulo de crecimiento/notación. Anota definiciones formales y una intuición (“O = techo, Ω = piso, Θ = ajustado”).

### 2. Documento base (45 min)

`docs/notacion.md`: definiciones + tabla `n`, `n log n`, `n²`, `2ⁿ` con valores a n=2,8,32 (calculadora).

### 3. Cinco clasificaciones (70 min)

Incluye: binary search; un doble bucle triangular; `push` amortizado de array dinámico (referencia M07); factorial recursivo ingenuo; merge de dos arrays ordenados. Para cada uno: Θ o O + peor caso.

### 4. Autocomprobación (30 min)

Explica en voz alta la diferencia O vs Θ con un ejemplo; resume en 4 líneas al final del doc.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): notacion asintotica O Omega Theta"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Definiciones O, Ω, Θ; peores vs cotas ajustadas | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `docs/notacion.md` define O/Ω/Θ con tus palabras + 1 ejemplo gráfico/tabla.
2. Clasificas **5** funciones/algoritmos (código o fórmulas) con justificación de 2–3 líneas c/u.
3. Commit `docs(m08): notacion asintotica O Omega Theta`.

## Errores comunes

- Usar O como sinónimo de “exactamente” sin Θ.
- Confundir peor caso del algoritmo con cota de una función.
- Lista de 5 sin justificación (“es O(n) porque sí”).

## Siguiente

[L03 — Análisis de bucles y recursión simple](L03-analisis-de-bucles-y-recursion-simple.md)
