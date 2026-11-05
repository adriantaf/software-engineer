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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Resolver dos problemas de ventana y documentar el invariante
      de cada uno.


      La ventana mantiene un invariante local y se desliza en O(n) total.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura / bosquejo
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): sliding window"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Sliding window" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: 2 problemas ventana
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

      `git commit -am "feat(m08): sliding window"`
    comandoEsperado:
      - 'git commit -am "feat(m08): sliding window"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): sliding window"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Resolver dos problemas de ventana y documentar el invariante de cada
          uno.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Problema ventana fija
    xp: 10
    cuerpo: 'Implementa + tests (k > n, k=1, k=n).'
  - id: s7
    tipo: explicacion
    titulo: 3. Problema ventana variable
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
