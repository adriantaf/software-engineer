---
id: L23
materia: M07
orden: 23
titulo: README cuándo usar cada estructura
horas: 5.0
semana: 6
lectura: Guía de selección de estructuras
evidencia: README guía de selección + API pública
---

# L23 — README cuándo usar cada estructura

**~5.0 h · Semana 6**

El proyecto útil es una librería documentada, no solo archivos sueltos.

## Objetivo

Redactar la guía de selección y dejar la API pública exportada y testeada.

## Pasos

### 1. Inventario (30 min)

Lista clases en `src/` y márcalas P1/P2/P3.

### 2. Guía de selección (90 min)

En README: preguntas → estructura (¿acceso aleatorio? ¿LIFO? ¿prioridad? ¿prefijo? → “eso es M08”). Tabla resumen + enlace a `COMPLEJIDAD.md`.

### 3. API y ejemplo (60 min)

`src/index.ts` limpio. Bloque “Quick start” de 15 líneas en README importando Stack/HashMap/BST.

### 4. QA (30 min)

```bash
npm test && npm run build
```

### 5. Commit (15 min)

```bash
git commit -am "docs(m07): guia cuando usar cada estructura"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Árbol de decisión: acceso, orden, prioridad, grafo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. README con guía “cuándo usar cada una” (todas las estructuras del curso).
2. `src/index.ts` exporta la API pública; `npm test` verde.
3. Commit `docs(m07): guia cuando usar cada estructura`.

## Errores comunes

- Guía genérica de Internet sin tus nombres de clase.
- Olvidar heap/grafo en la tabla.
- README sin cómo correr tests.

## Siguiente

[L24 — Cierre M07 y evidencias](L24-cierre-m07-y-evidencias.md)
