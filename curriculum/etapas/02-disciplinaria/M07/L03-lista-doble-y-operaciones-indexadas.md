---
id: L03
materia: M07
orden: 3
titulo: Lista doble y operaciones indexadas
horas: 5.0
semana: 1
lectura: "Joyanes / texto univ. ED (ed. ES): Arrays y listas enlazadas (costos, operaciones) — ED: listas doblemente enlazadas; eliminación O(1) con referencia al nodo"
evidencia: "DoublyLinkedList + deleteByValue; tests de borde"
---

# L03 — Lista doble y operaciones indexadas

**~5.0 h · Semana 1**

La doble enlace permite recorrer hacia atrás y simplificar borrados; sigue sin acceso O(1) por índice.

## Objetivo

Implementar lista doble con `remove` y medir cuándo preferirla frente a simple o array.

## Pasos

### 1. Estructura (90 min)

Nodos `prev`/`next`, `insertAt(index)`, `removeAt(index)` con validación de índice.

### 2. Tests (90 min)

Insert/borrar en extremos y medio; índice inválido; lista de un elemento.

### 3. Nota de diseño (30 min)

En README semana 1: “¿Cuándo usar array nativo de JS?” — respuesta honesta (cache, API, V8 optimizado).

### 4. Lectura (60 min)

Sección listas dobles del texto.

### 5. Commit (30 min)

`feat(m07): lista doble e indexada`.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Semana 1: Arrays y listas enlazadas (costos, operaciones) — ED: listas doblemente enlazadas; eliminación O(1) con referencia al nodo | [MDN Map/Set (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

1. Lista doble operativa con remove.
2. Tests de índices y bordes.
3. Nota “cuándo nativo” en README o COMPLEJIDAD.

## Errores comunes

- Olvidar actualizar `prev` al borrar.
- Prometer acceso O(1) por índice en lista enlazada.
## Siguiente

[L04 — Secuencias: repaso de costos y cierre semana 1](L04-secuencias-repaso-de-costos-y-cierre-semana-1.md)
