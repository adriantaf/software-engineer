---
id: L14
materia: M07
orden: 14
titulo: Recorridos inorder, preorder, postorder
horas: 5.0
semana: 4
lectura: "Recorridos de árbol: inorden, preorden, postorden"
evidencia: Tres recorridos + snapshots en tests
---

# L14 — Recorridos inorder, preorder, postorder

**~5.0 h · Semana 4**

Inorder en un BST es el sorted dump. Preorden y postorden aparecen en serialización y borrado de directorios.

## Objetivo

Exponer tres recorridos con tests de snapshot sobre un árbol fijo.

## Pasos

### 1. Repaso teórico (25 min)

Escribe en `docs/bst-semana4.md` una línea por recorrido: orden de visita.

### 2. Implementación recursiva (70 min)

En `src/bst.ts`: `inorder()`, `preorder()`, `postorder()` → arrays. Opcional: versión iterativa bonus.

### 3. Tests snapshot (60 min)

Árbol 8,3,10,1,6,14,4:

- inorder: `[1,3,4,8,10,14]` (ajusta si tu set difiere)
- preorder / postorder según tu dibujo VisuAlgo

### 4. Uso didáctico (40 min)

Función `toSortedArray()` = inorder. Test de propiedad: insertar permutación y sorted es el mismo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst recorridos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Inorder ordena claves BST; pre/post usos | [VisuAlgo · BST](https://visualgo.net/en/bst) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Métodos `inorder`, `preorder`, `postorder` que devuelven `number[]` (o visitor).
2. Tests con snapshot de la secuencia 8,3,10,1,6 (inorder = ordenado).
3. Commit `feat(m07): bst recorridos`.

## Errores comunes

- Inorder que no queda ordenado → invariante roto en insert.
- Recorridos mutando el árbol.
- Solo implementar inorder y fingir los otros.

## Siguiente

[L15 — BST: mínimo, máximo y sucesor](L15-bst-minimo-maximo-y-sucesor.md)
