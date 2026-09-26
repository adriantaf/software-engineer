---
id: L12
materia: M08
orden: 12
titulo: Índice de patrones (5+ entradas)
horas: 5.0
semana: 3
lectura: Clasificación de problemas por patrón (P1 parcial)
evidencia: ≥5 patrones clasificados
---

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
