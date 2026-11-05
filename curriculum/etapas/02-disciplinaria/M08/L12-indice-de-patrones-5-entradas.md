---
id: L12
materia: M08
orden: 12
titulo: Índice de patrones (5+ entradas)
horas: 5
semana: 3
lectura: Clasificación de problemas por patrón (P1 parcial)
evidencia: ≥5 patrones clasificados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El índice es el corazón de P1: sin clasificación, solo tienes código
      suelto.


      **Objetivo de esta lección:** Dejar `indice-patrones.md` con al menos
      cinco entradas verificables.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find problems -name 'enunciado.md' | sort
      ```

      Lista gaps.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Completar índice
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): indice patrones 5+ entradas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Índice de patrones (5+ entradas)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Índice de patrones (5+
          entradas)
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

      `find problems -name 'enunciado.md' | sort`
    comandoEsperado:
      - find problems -name 'enunciado.md' | sort
      - 'git commit -am "docs(m08): indice patrones 5+ entradas"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find problems -name ''enunciado.md'' | sort'
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
        texto: Dejar `indice-patrones.md` con al menos cinco entradas verificables.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Rellenar huecos
    xp: 10
    cuerpo: >-
      Si faltan patrones, añade un problema corto o reclasifica los existentes
      (binary search, hash, two pointers, window, sort).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`indice-patrones.md` con ≥5 entradas reales enlazando carpetas.'
      - Cada fila tiene complejidad y patrón nombrado.
      - 'Commit `docs(m08): indice patrones 5+ entradas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Índice de patrones (5+ entradas)

**~5.0 h · Semana 3**

El índice es el corazón de P1: sin clasificación, solo tienes código suelto.

## Objetivo

Dejar `indice-patrones.md` con al menos cinco entradas verificables.

## Pasos

### 1. Inventario (40 min)

```bash
find problems -name 'enunciado.md' | sort
```

Lista gaps.

### 2. Completar índice (70 min)

Tabla markdown: # | nombre | patrón | complejidad | ruta. Mínimo 5.

### 3. Rellenar huecos (60 min)

Si faltan patrones, añade un problema corto o reclasifica los existentes (binary search, hash, two pointers, window, sort).

### 4. QA enlaces (30 min)

Abre cada ruta; confirma que el enunciado menciona el patrón.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): indice patrones 5+ entradas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Índice vivo: binary search, hash, two pointers, window, sort… | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `indice-patrones.md` con **≥5** entradas reales enlazando carpetas.
2. Cada fila tiene complejidad y patrón nombrado.
3. Commit `docs(m08): indice patrones 5+ entradas`.

## Errores comunes

- Filas fantasma sin carpeta.
- Solo un patrón repetido cinco veces.
- Complejidad en blanco.

## Siguiente

[L13 — BFS repaso y cola](L13-bfs-repaso-y-cola.md)
