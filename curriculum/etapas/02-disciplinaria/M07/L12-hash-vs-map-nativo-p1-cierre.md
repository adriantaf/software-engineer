---
id: L12
materia: M07
orden: 12
titulo: Hash vs Map nativo (P1 cierre)
horas: 5.0
semana: 3
lectura: Contraste implementación propia vs Map/Set nativos
evidencia: "P1 completa: lista,pila,cola,hash + tabla comparativa nativo"
---

# L12 — Hash vs Map nativo (P1 cierre)

**~5.0 h · Semana 3**

P1 cierra aquí: estructuras básicas propias + honestidad frente a `Map`.

## Objetivo

Verificar evidencia P1 completa y documentar cuándo usarías `Map` nativo en producción frente a tu hash de aprendizaje.

## Pasos

### 1. Checklist automático (40 min)

```bash
cd projects/m07-estructuras
npm test
ls src/singly-linked-list.ts src/stack.ts src/queue.ts src/hash-map.ts
```

Arregla cualquier rojo.

### 2. Microbench informal (70 min)

`bench/hash-vs-map.ts`: N=50_000 set/get en tu HashMap vs `Map`. Imprime ms. **No** concluyas superioridad absoluta; anota que V8 está altamente optimizado.

### 3. Tabla comparativa (50 min)

README sección “P1 — Hash vs Map”: API, orden de claves, uso recomendado (prod → Map; curso → propio para entender colisiones).

### 4. Bitácora semana 3 (30 min)

`bitacora/semana-03.md`: una colisión real que viste y cómo el chaining la resolvió.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre P1 hash vs Map nativo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cuándo usar Map nativo vs hash propio (aprendizaje vs prod) | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist P1: lista, pila, cola, hash con tests verdes.
2. Tabla en README o `COMPLEJIDAD.md`: tu HashMap vs `Map` (ops, cuándo usar cada uno).
3. Commit `docs(m07): cierre P1 hash vs Map nativo`.

## Errores comunes

- Declarar P1 completa sin hash con rehash.
- Tabla que diga “el mío es más rápido” sin medir ni contextualizar aprendizaje.
- Olvidar exportar HashMap en `src/index.ts`.

## Siguiente

[L13 — BST: inserción y búsqueda](L13-bst-insercion-y-busqueda.md)
