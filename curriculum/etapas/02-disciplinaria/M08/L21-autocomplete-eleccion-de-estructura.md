---
id: L21
materia: M08
orden: 21
titulo: "Autocomplete: elección de estructura"
horas: 5.0
semana: 6
lectura: Trie vs array filtrado vs inverted index — trade-offs
evidencia: autocomplete/DISENO.md
---

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
