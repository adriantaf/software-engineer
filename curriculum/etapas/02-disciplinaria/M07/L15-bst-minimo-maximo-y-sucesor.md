---
id: L15
materia: M07
orden: 15
titulo: "BST: mínimo, máximo y sucesor"
horas: 5.0
semana: 4
lectura: Extremos y sucesor en BST; borrado de hoja intro
evidencia: min/max/delete leaf intro
---

# L15 — BST: mínimo, máximo y sucesor

**~5.0 h · Semana 4**

Min/max son caminatas a izquierda/derecha. El borrado completo puede esperar; hoy hojas y un hijo.

## Objetivo

Añadir `min`/`max`, opcional `successor`, y `delete` al menos para hojas (ideal: también un solo hijo).

## Pasos

### 1. Min/max (40 min)

Implementa y testa árbol vacío (throw o undefined) y árbol con varios nodos.

### 2. Sucesor (50 min)

Documenta algoritmo: si hay derecho, min del subárbol; si no, sube por padres (si guardas `parent`) o re-busca desde root. Test con claves conocidas.

### 3. Delete hoja / un hijo (90 min)

Implementa casos 0 y 1 hijo. Caso 2 hijos puede quedar como TODO documentado si te falta tiempo — dilo en README P2.

### 4. Tests de invariante (40 min)

Tras deletes, `inorder()` sigue ordenado y `contains` del borrado es false.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst min max delete hoja"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Min/max por rama; sucesor; borrar hoja y un hijo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `min()`, `max()` y al menos borrado de hoja (y preferible nodo con un hijo).
2. Tests para min/max en árbol no vacío y delete que mantiene invariante (inorder coherente).
3. Commit `feat(m07): bst min max delete hoja`.

## Errores comunes

- Borrar sin reenlazar padres.
- Sucesor mal calculado (olvidar el subárbol derecho).
- Dejar tests sin verificar inorder tras delete.

## Siguiente

[L16 — Visualización y P2 parcial](L16-visualizacion-y-p2-parcial.md)
