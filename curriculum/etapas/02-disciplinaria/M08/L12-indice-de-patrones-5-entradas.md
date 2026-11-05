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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `indice-patrones.md` con al menos cinco entradas
      verificables.


      El índice es el corazón de P1: sin clasificación, solo tienes código
      suelto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find problems -name 'enunciado.md' | sort
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Índice de patrones (5+ entradas)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: ≥5 patrones clasificados
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

      `find problems -name 'enunciado.md' | sort`
    comandoEsperado:
      - find problems -name 'enunciado.md' | sort
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find problems -name ''enunciado.md'' | sort'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Dejar `indice-patrones.md` con al menos cinco entradas verificables.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Completar índice
    xp: 10
    cuerpo: 'Tabla markdown: # | nombre | patrón | complejidad | ruta. Mínimo 5.'
  - id: s7
    tipo: explicacion
    titulo: 3. Rellenar huecos
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
