---
id: L04
materia: M07
orden: 4
titulo: "Secuencias: repaso de costos y cierre semana 1"
horas: 5.0
semana: 1
lectura: "Joyanes / texto univ. ED (ed. ES): Arrays y listas enlazadas (costos, operaciones) — Repaso cap. arrays/listas; anota 5 preguntas de entrevista con respuesta"
evidencia: "COMPLEJIDAD.md completo semana 1 + bitácora semana"
---

# L04 — Secuencias: repaso de costos y cierre semana 1

**~5.0 h · Semana 1**

Consolidas la semana lineal antes de pilas: autoevaluación sin IDE.

## Objetivo

Completar tabla comparativa array dinámico / lista simple / lista doble / `Array` nativo y dejar bitácora honesta.

## Pasos

### 1. Tabla maestra (60 min)

| Estructura | Acceso | Insert head | Insert tail | Memoria extra |
|------------|--------|-------------|-------------|---------------|

Rellena con Θ/O correctos.

### 2. Kata oral (45 min)

Explica en voz alta por qué `push` amortizado es O(1). Graba nota o escribe párrafo en `bitacora/semana-01.md`.

### 3. Refactor (90 min)

Elimina duplicación entre listas (interface `Sequence<T>` opcional). Tests siguen verdes.

### 4. Benchmark micro (45 min)

Opcional: 10⁵ inserts — nativo vs tu dynamic array. No optimices prematuramente; documenta resultado.

### 5. Commit (30 min)

`docs(m07): cierre semana 1 secuencias`.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Semana 1: Arrays y listas enlazadas (costos, operaciones) — Repaso cap. arrays/listas; anota 5 preguntas de entrevista con respuesta | [MDN Map/Set (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

1. Tabla comparativa en repo.
2. Bitácora semana 1 con bloqueos.
3. Suite verde.

## Errores comunes

- Saltar bitácora “porque solo fue código”.
- Confundir peor caso de redimensionar con amortizado sin explicar.
## Siguiente

[L05 — Pila (Stack) tipada](L05-pila-stack-tipada.md)
