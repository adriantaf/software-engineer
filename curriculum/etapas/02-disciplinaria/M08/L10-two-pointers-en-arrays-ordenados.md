---
id: L10
materia: M08
orden: 10
titulo: Two pointers en arrays ordenados
horas: 5
semana: 3
lectura: Two pointers / left-right en secuencias ordenadas
evidencia: 2 problemas two pointers
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar dos soluciones two-pointers bien testeadas e
      indexadas.


      Con orden, left/right reemplazan búsquedas anidadas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Patrón en papel
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): two pointers arrays ordenados"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Two pointers en arrays ordenados" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: 2 problemas two pointers
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

      `git commit -am "feat(m08): two pointers arrays ordenados"`
    comandoEsperado:
      - 'git commit -am "feat(m08): two pointers arrays ordenados"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): two pointers arrays ordenados"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Entregar dos soluciones two-pointers bien testeadas e indexadas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Problema A — pair sum
    xp: 10
    cuerpo: '`problems/…-pair-sum/`. Tests: hay par, no hay, duplicados, negativos.'
  - id: s7
    tipo: explicacion
    titulo: 3. Problema B
    xp: 10
    cuerpo: >-
      Ej. contenedor de agua, squaring sorted array, merge dos ordenados
      in-place conceptual. Misma plantilla.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Dos problemas two-pointers con arrays ordenados (o justificación de por
        qué ordenas antes).
      - Complejidad O(n) tras ordenar si aplica — dilo explícito.
      - 'Commit `feat(m08): two pointers arrays ordenados`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Two pointers en arrays ordenados

**~5.0 h · Semana 3**

Con orden, left/right reemplazan búsquedas anidadas.

## Objetivo

Entregar dos soluciones two-pointers bien testeadas e indexadas.

## Pasos

### 1. Patrón en papel (25 min)

Dibuja pair-sum = target en array ordenado. Anota cuándo mueves left vs right.

### 2. Problema A — pair sum (60 min)

`problems/…-pair-sum/`. Tests: hay par, no hay, duplicados, negativos.

### 3. Problema B (70 min)

Ej. contenedor de agua, squaring sorted array, merge dos ordenados in-place conceptual. Misma plantilla.

### 4. Índice + nota (30 min)

Compara con hash two-sum: trade-off ordenar+O(n) vs hash O(n) promedio.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): two pointers arrays ordenados"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Punteros extremos; pair sum en array ordenado | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas two-pointers con arrays ordenados (o justificación de por qué ordenas antes).
2. Complejidad O(n) tras ordenar si aplica — dilo explícito.
3. Commit `feat(m08): two pointers arrays ordenados`.

## Errores comunes

- Two pointers en no ordenado sin ordenar ni justificar.
- Índices que se cruzan mal (loop infinito).
- No cubrir caso sin solución.

## Siguiente

[L11 — Sliding window](L11-sliding-window.md)
