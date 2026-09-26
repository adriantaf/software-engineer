---
id: L22
materia: M08
orden: 22
titulo: Implementación trie o índice
horas: 5.0
semana: 6
lectura: Implementar la estructura elegida en L21
evidencia: autocomplete/ código + tests
---

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
