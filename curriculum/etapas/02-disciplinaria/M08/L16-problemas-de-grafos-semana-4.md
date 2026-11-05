---
id: L16
materia: M08
orden: 16
titulo: Problemas de grafos semana 4
horas: 5
semana: 4
lectura: 'Cierre semana grafos: +2 problemas en índice'
evidencia: problems/ +2 grafos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Sumar dos problemas de grafos bien empaquetados y actualizar
      el índice.


      Consolidás la semana 4 con dos prácticas más y el índice al día.
  - id: s2
    tipo: ejemplo
    titulo: 1. Selección
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos
      git commit -m "feat(m08): problemas grafos semana 4"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Problemas de grafos semana 4" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: problems/ +2 grafos
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

      `git add projects/m08-algoritmos`
    comandoEsperado:
      - git add projects/m08-algoritmos
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m08-algoritmos'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Sumar dos problemas de grafos bien empaquetados y actualizar el
          índice.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Problema 1
    xp: 10
    cuerpo: Plantilla completa + 3 tests.
  - id: s7
    tipo: explicacion
    titulo: 3. Problema 2
    xp: 10
    cuerpo: 'Igual. Si detectas ciclo, documenta complejidad.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        +2 problemas de grafos (además de L13–L15 si ya contaban, completa hasta
        tener evidencia clara de dos más o consolida carpetas).
      - '`indice-patrones.md` con filas bfs/dfs/camino.'
      - 'Commit `feat(m08): problemas grafos semana 4`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Problemas de grafos semana 4

**~5.0 h · Semana 4**

Consolidás la semana 4 con dos prácticas más y el índice al día.

## Objetivo

Sumar dos problemas de grafos bien empaquetados y actualizar el índice.

## Pasos

### 1. Selección (20 min)

Ideas: clone graph, course schedule (ciclo), flood fill, word ladder corto.

### 2. Problema 1 (80 min)

Plantilla completa + 3 tests.

### 3. Problema 2 (80 min)

Igual. Si detectas ciclo, documenta complejidad.

### 4. Índice + bitácora (30 min)

`bitacora/semana-04.md` opcional: qué patrón aún te cuesta.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): problemas grafos semana 4"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Práctica BFS/DFS adicional; índice ≥ entradas de grafos | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. **+2** problemas de grafos (además de L13–L15 si ya contaban, completa hasta tener evidencia clara de dos más o consolida carpetas).
2. `indice-patrones.md` con filas bfs/dfs/camino.
3. Commit `feat(m08): problemas grafos semana 4`.

## Errores comunes

- Reentregar el mismo archivo tres veces con otro nombre.
- Índice desactualizado.
- Tests flaky por orden de vecinos no determinista sin sort.

## Siguiente

[L17 — Memoización top-down](L17-memoizacion-top-down.md)
