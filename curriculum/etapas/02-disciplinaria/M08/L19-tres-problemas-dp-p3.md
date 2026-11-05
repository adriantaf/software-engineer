---
id: L19
materia: M08
orden: 19
titulo: Tres problemas DP (P3)
horas: 5
semana: 5
lectura: 'P3: tres problemas DP con caso base explícito'
evidencia: dp/ tres carpetas con caso base
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 exige tres problemas con caso base y transición explícitos — no solo
      fib.


      **Objetivo de esta lección:** Entregar tres DP distintos empaquetados como
      evidencia P3.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige trio
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/dp
      git commit -m "feat(m08): tres problemas DP P3"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Problema 1
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/dp
      git commit -m "feat(m08): tres problemas DP P3"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tres problemas DP (P3)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Tres problemas DP (P3)
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

      `git add projects/m08-algoritmos/dp`
    comandoEsperado:
      - git add projects/m08-algoritmos/dp
      - 'git commit -m "feat(m08): tres problemas DP P3"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m08-algoritmos/dp'
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
        texto: Entregar tres DP distintos empaquetados como evidencia P3.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problemas 2 y 3
    xp: 10
    cuerpo: Misma plantilla. Uno puede ser top-down y otro bottom-up.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Tres carpetas bajo `dp/` (o `dp/p1`, `dp/p2`, `dp/p3`) cada una con
        enunciado, caso base, transición, código y tests.
      - P3 checklist enlazada desde README.
      - 'Commit `feat(m08): tres problemas DP P3`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Tres problemas DP (P3)

**~5.0 h · Semana 5**

P3 exige tres problemas con caso base y transición explícitos — no solo fib.

## Objetivo

Entregar tres DP distintos empaquetados como evidencia P3.

## Pasos

### 1. Elige trio (20 min)

Ejemplos: climbing stairs, min coin change, unique paths, house robber, LCS intro corta. Evita tres fibs.

### 2. Problema 1 (70 min)

Carpeta con `enunciado.md` (estado/base/transición), `solution.ts`, tests.

### 3. Problemas 2 y 3 (110 min)

Misma plantilla. Uno puede ser top-down y otro bottom-up.

### 4. README P3 (20 min)

Lista las tres rutas en `dp/README.md`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): tres problemas DP P3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Plantilla: estado, base, transición, complejidad | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tres carpetas bajo `dp/` (o `dp/p1`, `dp/p2`, `dp/p3`) cada una con enunciado, caso base, transición, código y tests.
2. P3 checklist enlazada desde README.
3. Commit `feat(m08): tres problemas DP P3`.

## Errores comunes

- Tres variantes del mismo fib.
- Sin caso base escrito.
- Complejidad espacial omitida.

## Siguiente

[L20 — Patrones DP y transiciones](L20-patrones-dp-y-transiciones.md)
