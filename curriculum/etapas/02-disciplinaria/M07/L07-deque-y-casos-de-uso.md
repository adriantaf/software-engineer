---
id: L07
materia: M07
orden: 7
titulo: Deque y casos de uso
horas: 5.0
semana: 2
lectura: "Deque: inserción/borrado en ambos extremos"
evidencia: Deque mínimo o cola doble + 3 tests
---

# L07 — Deque y casos de uso

**~5.0 h · Semana 2**

Un deque cubre patrones (ventana deslizante, BFS 0-1) que pila o cola solas no cubren bien.

## Objetivo

Implementar un deque mínimo tipado y justificar un caso de uso real en 5–8 líneas.

## Pasos

### 1. API (20 min)

Decide nombres y anótalos en el README bajo “API semana 2”.

### 2. Implementación (90 min)

`src/deque.ts` sobre lista doble o buffer circular. Cuatro operaciones de extremo en O(1) amortizado/peor caso documentado.

### 3. Tests (45 min)

Mezcla front/back; vaciar por un extremo tras llenar por el otro; size coherente.

### 4. Caso de uso (60 min)

En `docs/casos-deque.md` (o sección README): elige **uno** — comprobar palíndromo con deque, o bosquejo de sliding-window máximo. Pseudocódigo + complejidad.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): deque y ejercicio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Deque / cola doble extremos | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/deque.ts` con `pushFront`/`pushBack`/`popFront`/`popBack` (o nombres equivalentes).
2. ≥3 tests + un caso de uso escrito (sliding window / undo-redo / palíndromo).
3. Commit `feat(m07): deque y ejercicio`.

## Errores comunes

- Deque que solo envuelve dos stacks sin documentar costos amortizados.
- Olvidar actualizar size en un extremo.
- Caso de uso genérico (“sirve para todo”) sin ejemplo concreto.

## Siguiente

[L08 — Pilas, colas y cierre P1 parcial](L08-pilas-colas-y-cierre-p1-parcial.md)
