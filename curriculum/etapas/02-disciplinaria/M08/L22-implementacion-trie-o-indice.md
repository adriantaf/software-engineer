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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `insert`/`suggest` según `DISENO.md` con tests
      sólidos.


      Hoy el diseño se vuelve código testeable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Esqueleto
    xp: 10
    cuerpo: '`autocomplete/src/index.ts` (o `trie.ts`) exportando la API acordada.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Implementación trie o índice" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: autocomplete/ código + tests
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

      `npm test`
    comandoEsperado:
      - npm test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Implementar `insert`/`suggest` según `DISENO.md` con tests sólidos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Insert
    xp: 10
    cuerpo: >-
      Normaliza strings (lowercase trim — documenta). Inserta carácter a
      carácter si trie; o actualiza índice.
  - id: s7
    tipo: explicacion
    titulo: 3. Suggest
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
