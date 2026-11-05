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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar tres DP distintos empaquetados como evidencia P3.


      P3 exige tres problemas con caso base y transición explícitos — no solo
      fib.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige trio
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/dp
      git commit -m "feat(m08): tres problemas DP P3"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Tres problemas DP (P3)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: dp/ tres carpetas con caso base
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

      `git add projects/m08-algoritmos/dp`
    comandoEsperado:
      - git add projects/m08-algoritmos/dp
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m08-algoritmos/dp'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Entregar tres DP distintos empaquetados como evidencia P3.
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
    cuerpo: 'Carpeta con `enunciado.md` (estado/base/transición), `solution.ts`, tests.'
  - id: s7
    tipo: explicacion
    titulo: 3. Problemas 2 y 3
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
