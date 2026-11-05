---
id: L18
materia: M08
orden: 18
titulo: Programación dinámica bottom-up
horas: 5
semana: 5
lectura: DP bottom-up / tabulación
evidencia: dp/bottom-up-ejemplo.ts
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Tabular elimina la pila de recursión y deja el orden de dependencias
      explícito.


      **Objetivo de esta lección:** Reescribir el problema de L17 (o uno nuevo)
      en bottom-up con tabla `dp[]`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Diseña el orden
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dp bottom-up"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dp bottom-up"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Programación dinámica bottom-up», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Programación dinámica
          bottom-up
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

      `git commit -am "feat(m08): dp bottom-up"`
    comandoEsperado:
      - 'git commit -am "feat(m08): dp bottom-up"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): dp bottom-up"'
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
          Reescribir el problema de L17 (o uno nuevo) en bottom-up con tabla
          `dp[]`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Equivalencia
    xp: 10
    cuerpo: 'Test: para n en 0..20, memo === bottom-up.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `dp/bottom-up-ejemplo.ts` con tabulación del mismo problema que L17 (o
        coin change simple).
      - Comparas espacial (optimización de variables opcionales) en nota corta.
      - 'Commit `feat(m08): dp bottom-up`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Programación dinámica bottom-up

**~5.0 h · Semana 5**

Tabular elimina la pila de recursión y deja el orden de dependencias explícito.

## Objetivo

Reescribir el problema de L17 (o uno nuevo) en bottom-up con tabla `dp[]`.

## Pasos

### 1. Diseña el orden (30 min)

En papel: de qué celda depende `dp[i]`.

### 2. Implementación (70 min)

`dp/bottom-up-ejemplo.ts`. Inicializa bases; loop hasta n.

### 3. Equivalencia (40 min)

Test: para n en 0..20, memo === bottom-up.

### 4. Nota espacial (40 min)

¿Puedes usar 2 variables en fib? Documéntalo; no es obligatorio optimizar.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dp bottom-up"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Tabla dp[]; orden de llenado; equivalencia con memo | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `dp/bottom-up-ejemplo.ts` con tabulación del mismo problema que L17 (o coin change simple).
2. Comparas espacial (optimización de variables opcionales) en nota corta.
3. Commit `feat(m08): dp bottom-up`.

## Errores comunes

- Llenar la tabla en orden incorrecto.
- Off-by-one en índices.
- Copiar memo y llamarlo bottom-up sin array dp.

## Siguiente

[L19 — Tres problemas DP (P3)](L19-tres-problemas-dp-p3.md)
