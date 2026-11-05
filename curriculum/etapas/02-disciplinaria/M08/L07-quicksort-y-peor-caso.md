---
id: L07
materia: M08
orden: 7
titulo: Quicksort y peor caso
horas: 5
semana: 2
lectura: 'CLRS: quicksort — partición y peor caso'
evidencia: sorts/quick.ts + caso O(n²)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar quicksort, documentar el peor caso O(n²) y una
      mitigación concreta.


      Quicksort brilla en promedio y falla con pivotes ingenuos en datos
      ordenados.
  - id: s2
    tipo: ejemplo
    titulo: 1. Partición
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): quicksort y peor caso"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Quicksort y peor caso" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sorts/quick.ts + caso O(n²)
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

      `git commit -am "feat(m08): quicksort y peor caso"`
    comandoEsperado:
      - 'git commit -am "feat(m08): quicksort y peor caso"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): quicksort y peor caso"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar quicksort, documentar el peor caso O(n²) y una mitigación
          concreta.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Peor caso escrito
    xp: 10
    cuerpo: >-
      `sorts/quick-peor-caso.md`: secuencia que degenera con pivote `a[hi]`;
      contador de comparaciones opcional en modo debug.
  - id: s7
    tipo: explicacion
    titulo: 3. Mitigación
    xp: 10
    cuerpo: Implementa pivote aleatorio **o** median-of-three. Nota en el markdown.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`sorts/quick.ts` con partición documentada.'
      - >-
        `sorts/quick-peor-caso.md` explica entrada adversaria (ya ordenado +
        pivote fijo) y mitigación (pivote random/median-of-three).
      - 'Tests + commit `feat(m08): quicksort y peor caso`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Quicksort y peor caso

**~5.0 h · Semana 2**

Quicksort brilla en promedio y falla con pivotes ingenuos en datos ordenados.

## Objetivo

Implementar quicksort, documentar el peor caso O(n²) y una mitigación concreta.

## Pasos

### 1. Partición (70 min)

`sorts/quick.ts`: Lomuto o Hoare — elige una y comenta invariante.

### 2. Peor caso escrito (50 min)

`sorts/quick-peor-caso.md`: secuencia que degenera con pivote `a[hi]`; contador de comparaciones opcional en modo debug.

### 3. Mitigación (50 min)

Implementa pivote aleatorio **o** median-of-three. Nota en el markdown.

### 4. Tests (40 min)

Ordenado, invertido, duplicados, random vs nativo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): quicksort y peor caso"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Quicksort promedio vs peor caso n²; pivotes | [VisuAlgo · Sorting](https://visualgo.net/en/sorting) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/quick.ts` con partición documentada.
2. `sorts/quick-peor-caso.md` explica entrada adversaria (ya ordenado + pivote fijo) y mitigación (pivote random/median-of-three).
3. Tests + commit `feat(m08): quicksort y peor caso`.

## Errores comunes

- Afirmar “quicksort es O(n log n)” sin matizar peor caso.
- Partición incorrecta (loops infinitos).
- Sin test de array con muchos duplicados.

## Siguiente

[L08 — Tabla P2 sorts en README](L08-tabla-p2-sorts-en-readme.md)
