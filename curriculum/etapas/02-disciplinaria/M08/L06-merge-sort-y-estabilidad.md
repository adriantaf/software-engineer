---
id: L06
materia: M08
orden: 6
titulo: Merge sort y estabilidad
horas: 5
semana: 2
lectura: 'CLRS: divide y vencerás — merge sort'
evidencia: sorts/merge.ts + nota estabilidad
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar merge sort y demostrar estabilidad con un test o
      ejemplo documentado.


      Merge garantiza Θ(n log n) y puede ser estable si el merge elige bien ante
      empates.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): merge sort y estabilidad"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Merge sort y estabilidad" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sorts/merge.ts + nota estabilidad
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m08): merge sort y estabilidad"`
    comandoEsperado:
      - 'git commit -am "feat(m08): merge sort y estabilidad"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): merge sort y estabilidad"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar merge sort y demostrar estabilidad con un test o ejemplo
          documentado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `merge` + `mergeSort`
    xp: 10
    cuerpo: >-
      `sorts/merge.ts`. Al comparar iguales, toma primero del buffer izquierdo
      (estabilidad).
  - id: s7
    tipo: explicacion
    titulo: 3. Estabilidad
    xp: 10
    cuerpo: >-
      `sorts/estabilidad.md` + test con objetos `{k, id}`: mismos `k` preservan
      orden de `id`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`sorts/merge.ts` con `merge` + `mergeSort`.'
      - >-
        Nota de estabilidad con ejemplo de pares `(key, payload)` en
        `sorts/estabilidad.md`.
      - 'Tests verdes; commit `feat(m08): merge sort y estabilidad`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Merge sort y estabilidad

**~5.0 h · Semana 2**

Merge garantiza Θ(n log n) y puede ser estable si el merge elige bien ante empates.

## Objetivo

Implementar merge sort y demostrar estabilidad con un test o ejemplo documentado.

## Pasos

### 1. Lectura (40 min)

CLRS merge sort + VisuAlgo. Escribe la recurrencia T(n)=2T(n/2)+Θ(n).

### 2. `merge` + `mergeSort` (90 min)

`sorts/merge.ts`. Al comparar iguales, toma primero del buffer izquierdo (estabilidad).

### 3. Estabilidad (50 min)

`sorts/estabilidad.md` + test con objetos `{k, id}`: mismos `k` preservan orden de `id`.

### 4. Tests adicionales (30 min)

Random vs sort nativo; vacío; un elemento.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): merge sort y estabilidad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Merge sort Θ(n log n); estabilidad al fusionar | [VisuAlgo · Sorting](https://visualgo.net/en/sorting) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/merge.ts` con `merge` + `mergeSort`.
2. Nota de estabilidad con ejemplo de pares `(key, payload)` en `sorts/estabilidad.md`.
3. Tests verdes; commit `feat(m08): merge sort y estabilidad`.

## Errores comunes

- Merge que pisa el orden relativo de iguales (rompe estabilidad).
- Olvidar costo espacial Θ(n).
- Recursión sin caso base en length ≤ 1.

## Siguiente

[L07 — Quicksort y peor caso](L07-quicksort-y-peor-caso.md)
