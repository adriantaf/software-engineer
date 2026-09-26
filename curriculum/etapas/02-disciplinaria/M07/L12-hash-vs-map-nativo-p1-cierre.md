---
id: L12
materia: M07
orden: 12
titulo: Hash vs Map nativo (P1 cierre)
horas: 5.0
semana: 3
lectura: "Joyanes / texto univ. ED (ed. ES): Tablas hash (función, colisiones, load factor) — MDN Map/Set"
evidencia: "P1 completa: lista,pila,cola,hash + tabla comparativa nativo"
---

# L12 — Hash vs Map nativo (P1 cierre)

**~5.0 h · Semana 3**

Semana 3 de M07: rigor en implementación, tests y documentación de costos.

## Objetivo

Avanzar evidencia `P1 completa: lista,pila,cola,hash + tabla comparativa nativo` con código TS, tests Vitest y notas en COMPLEJIDAD/README.

## Pasos

### 1. Lectura dirigida (60 min)

Lee la sección indicada en tu texto ED sobre **Hash vs Map nativo (P1 cierre)**. Anota definiciones formales (pre/post condiciones).

### 2. Implementación (120 min)

Crea o extiende módulos bajo `src/` con tipos explícitos. Sin `any`. Exporta API mínima documentada en comentario JSDoc breve.

### 3. Tests (90 min)

Mínimo **5** tests: feliz, vacío, borde, caso que fuerza estructura interna (p. ej. colisión, rotación simple, heapify), regresión.

### 4. Documentación (30 min)

Actualiza `COMPLEJIDAD.md` o README con Big-O de operaciones nuevas. Si comparas con nativo, di **cuándo** gana cada uno.

### 5. Commit (30 min)

Mensaje `feat(m07)` o `docs(m07)` descriptivo en español.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Semana 3: Tablas hash (función, colisiones, load factor) — MDN Map/Set | [MDN Map/Set (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

1. Código + tests verdes para el foco de la lección.
2. Costos documentados.
3. Commit en git.

## Errores comunes

- Copiar implementación sin entender invariantes.
- Tests solo “felices”.
- Omitir commit.
## Siguiente

[L13 — BST: inserción y búsqueda](L13-bst-insercion-y-busqueda.md)
