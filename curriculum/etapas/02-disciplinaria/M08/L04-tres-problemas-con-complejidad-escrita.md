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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana 1 con la plantilla P1 que usarás el resto del curso.


      **Objetivo de esta lección:** Dejar tres problemas completos en
      `problems/` e iniciar `indice-patrones.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla
    xp: 10
    cuerpo: |-
      ```text
      problems/NN-nombre/
        enunciado.md    # problema + complejidad objetivo
        solution.ts
        solution.test.ts
      ```

      Cada problema:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Completar / añadir hasta 3
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m08-algoritmos && npm test
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tres problemas con complejidad escrita», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tres problemas con
          complejidad escrita
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

      `cd projects/m08-algoritmos && npm test`
    comandoEsperado:
      - cd projects/m08-algoritmos && npm test
      - git add projects/m08-algoritmos
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m08-algoritmos && npm test'
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
          Dejar tres problemas completos en `problems/` e iniciar
          `indice-patrones.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Índice
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
