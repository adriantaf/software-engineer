---
id: L04
materia: M08
orden: 4
titulo: Tres problemas con complejidad escrita
horas: 5
semana: 1
lectura: 'Plantilla de entrega: enunciado, complejidad, código, tests'
evidencia: problems/ con 3 entradas + complejidad
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar tres problemas completos en `problems/` e iniciar
      `indice-patrones.md`.


      Cierras la semana 1 con la plantilla P1 que usarás el resto del curso.
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla
    xp: 10
    cuerpo: |-
      ```text
      problems/NN-nombre/
        enunciado.md    # problema + complejidad objetivo
        solution.ts
        solution.test.ts
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tres problemas con complejidad escrita" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: problems/ con 3 entradas + complejidad
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

      `cd projects/m08-algoritmos && npm test`
    comandoEsperado:
      - cd projects/m08-algoritmos && npm test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m08-algoritmos && npm test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar tres problemas completos en `problems/` e iniciar
          `indice-patrones.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Completar / añadir hasta 3
    xp: 10
    cuerpo: >-
      Si L01 ya trajo 2, añade un tercero (p. ej. “mover ceros”, “intersección
      de arrays”). 30–45 min de intento serio antes de editorial propia.
  - id: s7
    tipo: explicacion
    titulo: 3. Índice
    xp: 10
    cuerpo: '`indice-patrones.md` tabla: id | patrón | archivo | complejidad | notas.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Tres carpetas bajo `problems/` (pueden incluir las de L01) cada una con
        enunciado, complejidad, solución y ≥3 tests.
      - Filas iniciales en `indice-patrones.md` (≥3).
      - 'Commit `feat(m08): tres problemas con complejidad`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Tres problemas con complejidad escrita

**~5.0 h · Semana 1**

Cierras la semana 1 con la plantilla P1 que usarás el resto del curso.

## Objetivo

Dejar tres problemas completos en `problems/` e iniciar `indice-patrones.md`.

## Pasos

### 1. Plantilla (20 min)

Cada problema:

```
problems/NN-nombre/
  enunciado.md    # problema + complejidad objetivo
  solution.ts
  solution.test.ts
```

### 2. Completar / añadir hasta 3 (120 min)

Si L01 ya trajo 2, añade un tercero (p. ej. “mover ceros”, “intersección de arrays”). 30–45 min de intento serio antes de editorial propia.

### 3. Índice (40 min)

`indice-patrones.md` tabla: id | patrón | archivo | complejidad | notas.

### 4. Suite (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): tres problemas con complejidad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Disciplina de evidencia por problema (P1) | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tres carpetas bajo `problems/` (pueden incluir las de L01) cada una con enunciado, complejidad, solución y ≥3 tests.
2. Filas iniciales en `indice-patrones.md` (≥3).
3. Commit `feat(m08): tres problemas con complejidad`.

## Errores comunes

- Código sin enunciado ni Big-O.
- Un solo test feliz.
- Índice vacío al cerrar la semana.

## Siguiente

[L05 — Insertion sort implementado](L05-insertion-sort-implementado.md)
