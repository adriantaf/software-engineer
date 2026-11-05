---
id: L11
materia: M08
orden: 11
titulo: Sliding window
horas: 5
semana: 3
lectura: Ventana deslizante fija y variable
evidencia: 2 problemas ventana
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La ventana mantiene un invariante local y se desliza en O(n) total.


      **Objetivo de esta lección:** Resolver dos problemas de ventana y
      documentar el invariante de cada uno.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura / bosquejo
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): sliding window"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Problema ventana fija
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): sliding window"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sliding window», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Sliding window
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

      `git commit -am "feat(m08): sliding window"`
    comandoEsperado:
      - 'git commit -am "feat(m08): sliding window"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): sliding window"'
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
          Resolver dos problemas de ventana y documentar el invariante de cada
          uno.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema ventana variable
    xp: 10
    cuerpo: 'Map/set de frecuencia; mueve `right`, encoge `left`. Complejidad O(n).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Dos problemas sliding window (fija y/o variable) con análisis.
      - Tests incluyen ventana más grande que el array.
      - 'Commit `feat(m08): sliding window`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Sliding window

**~5.0 h · Semana 3**

La ventana mantiene un invariante local y se desliza en O(n) total.

## Objetivo

Resolver dos problemas de ventana y documentar el invariante de cada uno.

## Pasos

### 1. Lectura / bosquejo (30 min)

Fija (max sum subarray size k) vs variable (longest substring without repeat).

### 2. Problema ventana fija (60 min)

Implementa + tests (k > n, k=1, k=n).

### 3. Problema ventana variable (80 min)

Map/set de frecuencia; mueve `right`, encoge `left`. Complejidad O(n).

### 4. Índice (20 min)

Patrón `sliding-window`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): sliding window"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Window fija vs variable; invariante de la ventana | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas sliding window (fija y/o variable) con análisis.
2. Tests incluyen ventana más grande que el array.
3. Commit `feat(m08): sliding window`.

## Errores comunes

- Recalcular la ventana desde cero cada paso (O(nk) disfrazado).
- Olvidar encoger la ventana en la variante variable.
- Sin invariante escrito.

## Siguiente

[L12 — Índice de patrones (5+ entradas)](L12-indice-de-patrones-5-entradas.md)
