---
id: L24
materia: M07
orden: 24
titulo: Cierre M07 y evidencias
horas: 5
semana: 6
lectura: Checklist de dominio y evidencias en git
evidencia: bitácora + checklist dominio + progress
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Si no está en git con checklist, no cuenta. Hoy cierras la materia.


      **Objetivo de esta lección:** Dejar evidencia P1–P3 + proyecto enlazada
      desde bitácora de cierre y el README.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist con rutas
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras && npm test
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Criterios de dominio
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras
      git commit -m "docs(m07): cierre materia y evidencias"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M07 y evidencias», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Cierre M07 y evidencias
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

      `cd projects/m07-estructuras && npm test`
    comandoEsperado:
      - cd projects/m07-estructuras && npm test
      - git add projects/m07-estructuras
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m07-estructuras && npm test'
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
          Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de cierre y
          el README.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M07
    xp: 25
    enunciado: >-
      Cierra **Estructuras de datos** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Implementar lista, pila, cola y hash map'
      - 'P2: Árboles BST + recorridos'
      - 'P3: Benchmarks de tus estructuras vs nativas'
      - 'Proyecto: Librería de ED con tests y documentación'
      - bitácora + checklist dominio + progress
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con
          rutas de archivo.
      - id: r3
        criterio: Suite verde y README de selección presente.
      - id: r4
        criterio: 'Commit `docs(m07): cierre materia y evidencias`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con
        rutas de archivo.
      - Suite verde y README de selección presente.
      - 'Commit `docs(m07): cierre materia y evidencias`.'
    siguiente: Materia M07 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M07 y evidencias

**~5.0 h · Semana 6**

Si no está en git con checklist, no cuenta. Hoy cierras la materia.

## Objetivo

Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de cierre y el README.

## Pasos

### 1. Checklist con rutas (60 min)

`bitacora/cierre-m07.md`:

- P1: rutas a lista/pila/cola/hash + tests
- P2: bst + recorridos
- P3: `bench/RESULTADOS.md`
- Proyecto: guía README

### 2. Criterios de dominio (50 min)

Grábate o escribe respuesta de 3 minutos: “¿cuándo un hash gana a un árbol?”. Pega el outline en la bitácora.

### 3. Regresión final (40 min)

```bash
cd projects/m07-estructuras && npm test
```

### 4. Limpieza (40 min)

Quita `console.log` de debug, asegura que no hay secretos, actualiza scripts del package.json.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Autoevaluación: explicar hash vs árbol en voz alta | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con rutas de archivo.
2. Suite verde y README de selección presente.
3. Commit `docs(m07): cierre materia y evidencias`.

## Errores comunes

- Marcar evidencias sin archivos en git.
- Checklist genérico sin rutas.
- Dejar benches o tests rotos “para después”.

## Siguiente

M07 cerrado — siguiente materia: [M08 · Análisis de algoritmos](../M08-analisis-de-algoritmos.md)
