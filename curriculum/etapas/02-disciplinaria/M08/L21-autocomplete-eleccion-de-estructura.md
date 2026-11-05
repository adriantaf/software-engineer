---
id: L21
materia: M08
orden: 21
titulo: 'Autocomplete: elección de estructura'
horas: 5
semana: 6
lectura: Trie vs array filtrado vs inverted index — trade-offs
evidencia: autocomplete/DISENO.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El proyecto une M08 con Agenda Ops: sugerencias rápidas de
      clientes/servicios.


      **Objetivo de esta lección:** Dejar `autocomplete/DISENO.md` con decisión
      de estructura y complejidades objetivo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Contexto producto
    xp: 10
    cuerpo: |-
      ```ts
      insert(term: string): void
      suggest(prefix: string, k?: number): string[]
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Opciones
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m08-algoritmos/autocomplete
      git add projects/m08-algoritmos/autocomplete
      git commit -m "docs(m08): diseno autocomplete"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Autocomplete: elección de estructura», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Autocomplete: elección
          de estructura
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Elegir trie “porque suena avanzado” sin
      dataset size."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
          Dejar `autocomplete/DISENO.md` con decisión de estructura y
          complejidades objetivo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Decisión
    xp: 10
    cuerpo: >-
      Elige **una** para implementar en L22. Justifica con tamaño demo (p. ej.
      5k–50k strings) y k resultados.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `autocomplete/DISENO.md` elige estructura con tabla de trade-offs y
        complejidad objetivo de query.
      - Alcance del dataset Agenda Ops (clientes/servicios) definido.
      - 'Commit `docs(m08): diseno autocomplete`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L21 — Autocomplete: elección de estructura

**~5.0 h · Semana 6**

El proyecto une M08 con Agenda Ops: sugerencias rápidas de clientes/servicios.

## Objetivo

Dejar `autocomplete/DISENO.md` con decisión de estructura y complejidades objetivo.

## Pasos

### 1. Contexto producto (30 min)

Lee `curriculum/producto-saas.md` (Agenda Ops). Lista campos sugeribles: nombre cliente, nombre servicio.

### 2. Opciones (60 min)

Tabla en DISENO: scan lineal, array ordenado + binary search, trie, `Map` prefijo→lista. Pros/contras.

### 3. Decisión (50 min)

Elige **una** para implementar en L22. Justifica con tamaño demo (p. ej. 5k–50k strings) y k resultados.

### 4. API (40 min)

```ts
insert(term: string): void
suggest(prefix: string, k?: number): string[]
```

Más complejidad insert/query escritas.

### 5. Commit (15 min)

```bash
mkdir -p projects/m08-algoritmos/autocomplete
git add projects/m08-algoritmos/autocomplete
git commit -m "docs(m08): diseno autocomplete"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Prefijos: trie O(|p|) vs scan O(n·|p|) | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `autocomplete/DISENO.md` elige estructura con tabla de trade-offs y complejidad objetivo de query.
2. Alcance del dataset Agenda Ops (clientes/servicios) definido.
3. Commit `docs(m08): diseno autocomplete`.

## Errores comunes

- Elegir trie “porque suena avanzado” sin dataset size.
- No definir operaciones (insert, suggest(prefix, k)).
- Diseñar API HTTP entera en vez del núcleo de búsqueda.

## Siguiente

[L22 — Implementación trie o índice](L22-implementacion-trie-o-indice.md)
