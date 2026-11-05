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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `autocomplete/DISENO.md` con decisión de estructura y
      complejidades objetivo.


      El proyecto une M08 con Agenda Ops: sugerencias rápidas de
      clientes/servicios.
  - id: s2
    tipo: ejemplo
    titulo: 1. Contexto producto
    xp: 10
    cuerpo: |-
      ```ts
      insert(term: string): void
      suggest(prefix: string, k?: number): string[]
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Autocomplete: elección de estructura" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: autocomplete/DISENO.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Elegir trie “porque suena avanzado”
      sin dataset size."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar `autocomplete/DISENO.md` con decisión de estructura y
          complejidades objetivo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Opciones
    xp: 10
    cuerpo: >-
      Tabla en DISENO: scan lineal, array ordenado + binary search, trie, `Map`
      prefijo→lista. Pros/contras.
  - id: s7
    tipo: explicacion
    titulo: 3. Decisión
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
