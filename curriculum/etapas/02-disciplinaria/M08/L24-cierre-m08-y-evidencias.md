---
id: L24
materia: M08
orden: 24
titulo: Cierre M08 y evidencias
horas: 5
semana: 6
lectura: Checklist P1–P3 + proyecto; índice ≥15
evidencia: checklist + indice ≥15
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y
      autocomplete.


      **Objetivo de esta lección:** Completar índice ≥15, checklist de dominio y
      dejar el README raíz como mapa de evidencias.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Contar problemas
    xp: 10
    cuerpo: >-
      ```bash

      find problems -name 'enunciado.md' | wc -l

      ```


      Si <15, añade los faltantes hoy (plantilla corta) o recupera de semanas
      previas mal indexados.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Checklist
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
      Al terminar «Cierre M08 y evidencias», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Cierre M08 y evidencias
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

      `find problems -name 'enunciado.md' | wc -l`
    comandoEsperado:
      - find problems -name 'enunciado.md' | wc -l
      - cd projects/m08-algoritmos && npm test
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find problems -name ''enunciado.md'' | wc -l'
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
          Completar índice ≥15, checklist de dominio y dejar el README raíz como
          mapa de evidencias.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M08
    xp: 25
    enunciado: >-
      Cierra **Análisis de algoritmos** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: 15 problemas clasificados por patrón'
      - 'P2: Ordenamientos implementados + análisis'
      - 'P3: Búsqueda y DP intro (3 problemas)'
      - 'Proyecto: Autocomplete / búsqueda para el producto'
      - checklist + indice ≥15
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `indice-patrones.md` con ≥15 entradas; checklist en
          `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
      - id: r3
        criterio: '`npm test` verde; autocomplete documentado enlazado desde README raíz.'
      - id: r4
        criterio: 'Commit `docs(m08): cierre materia y evidencias`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `indice-patrones.md` con ≥15 entradas; checklist en
        `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
      - '`npm test` verde; autocomplete documentado enlazado desde README raíz.'
      - 'Commit `docs(m08): cierre materia y evidencias`.'
    siguiente: Materia M08 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M08 y evidencias

**~5.0 h · Semana 6**

Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y autocomplete.

## Objetivo

Completar índice ≥15, checklist de dominio y dejar el README raíz como mapa de evidencias.

## Pasos

### 1. Contar problemas (40 min)

```bash
find problems -name 'enunciado.md' | wc -l
```

Si <15, añade los faltantes hoy (plantilla corta) o recupera de semanas previas mal indexados.

### 2. Checklist (60 min)

`bitacora/cierre-m08.md` con rutas:

- P1 índice ≥15
- P2 `sorts/README.md`
- P3 `dp/` ×3
- Proyecto `autocomplete/` + DISENO + CLI

### 3. Dominio oral (40 min)

Outline escrito: resuelve two-sum / ventana en voz alta con complejidad.

### 4. Regresión (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Autoevaluación: explicar un medio de arrays/hash en voz alta | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `indice-patrones.md` con **≥15** entradas; checklist en `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
2. `npm test` verde; autocomplete documentado enlazado desde README raíz.
3. Commit `docs(m08): cierre materia y evidencias`.

## Errores comunes

- Índice inflado con filas vacías.
- Marcar P3 sin tres DP.
- Autocomplete sin complejidad de query.

## Siguiente

M08 cerrado — siguiente materia: [M09 · Bases de datos](../M09-bases-de-datos.md)
