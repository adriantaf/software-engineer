---
id: L22
materia: M08
orden: 22
titulo: Implementación trie o índice
horas: 5
semana: 6
lectura: Implementar la estructura elegida en L21
evidencia: autocomplete/ código + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Hoy el diseño se vuelve código testeable.


      **Objetivo de esta lección:** Implementar `insert`/`suggest` según
      `DISENO.md` con tests sólidos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Esqueleto
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): autocomplete estructura base"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Insert
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): autocomplete estructura base"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Implementación trie o índice», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Implementación trie o
          índice
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

      `npm test`
    comandoEsperado:
      - npm test
      - 'git commit -am "feat(m08): autocomplete estructura base"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm test'
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
        texto: Implementar `insert`/`suggest` según `DISENO.md` con tests sólidos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Suggest
    xp: 10
    cuerpo: >-
      Baja al nodo prefijo; DFS/BFS recolectando hasta k. Si elegiste binary
      search sobre lista ordenada, implementa lower_bound.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Código en `autocomplete/` alineado al DISENO (trie u otra) con
        `insert`/`suggest`.
      - >-
        ≥5 tests: vacío, prefijo sin matches, prefijo corto, k limit, case
        policy documentada.
      - 'Commit `feat(m08): autocomplete estructura base`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Implementación trie o índice

**~5.0 h · Semana 6**

Hoy el diseño se vuelve código testeable.

## Objetivo

Implementar `insert`/`suggest` según `DISENO.md` con tests sólidos.

## Pasos

### 1. Esqueleto (30 min)

`autocomplete/src/index.ts` (o `trie.ts`) exportando la API acordada.

### 2. Insert (60 min)

Normaliza strings (lowercase trim — documenta). Inserta carácter a carácter si trie; o actualiza índice.

### 3. Suggest (70 min)

Baja al nodo prefijo; DFS/BFS recolectando hasta k. Si elegiste binary search sobre lista ordenada, implementa lower_bound.

### 4. Tests (50 min)

```bash
npm test
```

Incluye case folding según política.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): autocomplete estructura base"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Trie nodes / índice: insert y suggest correctos | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Código en `autocomplete/` alineado al DISENO (trie u otra) con `insert`/`suggest`.
2. ≥5 tests: vacío, prefijo sin matches, prefijo corto, k limit, case policy documentada.
3. Commit `feat(m08): autocomplete estructura base`.

## Errores comunes

- Implementar otra estructura distinta al DISENO sin actualizarlo.
- Suggest O(n) silencioso cuando prometiste trie.
- Sin tests de k.

## Siguiente

[L23 — Dataset Agenda Ops y demo CLI](L23-dataset-agenda-ops-y-demo-cli.md)
