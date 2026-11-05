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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Reescribir el problema de L17 (o uno nuevo) en bottom-up con
      tabla `dp[]`.


      Tabular elimina la pila de recursión y deja el orden de dependencias
      explícito.
  - id: s2
    tipo: ejemplo
    titulo: 1. Diseña el orden
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dp bottom-up"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Programación dinámica bottom-up" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: dp/bottom-up-ejemplo.ts
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

      `git commit -am "feat(m08): dp bottom-up"`
    comandoEsperado:
      - 'git commit -am "feat(m08): dp bottom-up"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): dp bottom-up"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Reescribir el problema de L17 (o uno nuevo) en bottom-up con tabla
          `dp[]`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: '`dp/bottom-up-ejemplo.ts`. Inicializa bases; loop hasta n.'
  - id: s7
    tipo: explicacion
    titulo: 3. Equivalencia
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
