---
id: L03
materia: M08
orden: 3
titulo: Análisis de bucles y recursión simple
horas: 5.0
semana: 1
lectura: Sumas de bucles anidados y recurrencias simples
evidencia: 3 snippets analizados en markdown
---

# L03 — Análisis de bucles y recursión simple

**~5.0 h · Semana 1**

Pasas de definiciones a contar operaciones en código que tú escribes.

## Objetivo

Analizar tres snippets (2 iterativos + 1 recursivo) en `docs/analisis-bucles.md`.

## Pasos

### 1. Snippet A — bucle simple (35 min)

Escribe un `sum(a: number[])` y justifica Θ(n) tiempo / Θ(1) extra.

### 2. Snippet B — anidado (50 min)

```ts
for (let i = 0; i < n; i++)
  for (let j = i; j < n; j++) { /* ... */ }
```

Cuenta iteraciones ≈ n(n+1)/2 → Θ(n²).

### 3. Snippet C — recursión (60 min)

`rec(n) = rec(n-1) + work` tipo factorial o suma. Unfolding hasta base; Θ(n) llamadas.

### 4. Contraste (40 min)

Añade binary search recursivo: profundidad log n. Enlaza a L01.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): analisis bucles y recursion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Contar iteraciones; árbol de recursión simple (T(n)=T(n-1)+O(1)) | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `docs/analisis-bucles.md` con **3** snippets TS y su complejidad justificada.
2. Al menos uno recursivo con árbol o unfolding escrito.
3. Commit `docs(m08): analisis bucles y recursion`.

## Errores comunes

- Contar mal bucles dependientes (`for i; for j=i`).
- Decir O(n²) a binary search recursivo.
- Snippets sin código real (solo prosa).

## Siguiente

[L04 — Tres problemas con complejidad escrita](L04-tres-problemas-con-complejidad-escrita.md)
