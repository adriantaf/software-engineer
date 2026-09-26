---
id: L11
materia: M07
orden: 11
titulo: Factor de carga y rehash
horas: 5.0
semana: 3
lectura: Load factor, umbral y rehashing
evidencia: Rehash al superar umbral; tests que fuerzan resize
---

# L11 — Factor de carga y rehash

**~5.0 h · Semana 3**

Sin rehash, el encadenamiento degenera a listas largas y pierdes el O(1) promedio.

## Objetivo

Hacer que tu `HashMap` redimensione al cruzar un umbral de load factor y probarlo con un test que fuerce el resize.

## Pasos

### 1. Define umbral (20 min)

Constante `MAX_LOAD = 0.75` (o la de tu texto). Documéntala en JSDoc y `COMPLEJIDAD.md`.

### 2. `_rehash(newCap)` (90 min)

Nuevo array de buckets; reinserta **todas** las entradas con el nuevo módulo; actualiza capacity/size. Llámalo desde `set` cuando `size/capacity > MAX_LOAD`.

### 3. Test de resize (60 min)

Capacidad inicial pequeña (4). Inserta 10 claves distintas; assert capacity ≥ 8 (o la esperada); todos los `get` siguen correctos; loadFactor ≤ MAX_LOAD tras rehash.

### 4. Nota amortizada (40 min)

Párrafo en `COMPLEJIDAD.md`: costo de rehash O(n) puntual, O(1) amortizado por insert si creces ×2.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): hashmap rehash por load factor"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Load factor α; cuándo rehash; costo amortizado | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Rehash automático al superar umbral (p. ej. α > 0.75) duplicando capacidad.
2. Test que inserta hasta forzar ≥1 resize y verifica gets posteriores.
3. Commit `feat(m07): hashmap rehash por load factor`.

## Errores comunes

- Rehash que no re-inserta (solo crece el array vacío).
- Umbral nunca documentado.
- Tests que no provocan resize.

## Siguiente

[L12 — Hash vs Map nativo (P1 cierre)](L12-hash-vs-map-nativo-p1-cierre.md)
