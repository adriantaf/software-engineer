---
id: L24
materia: M07
orden: 24
titulo: Cierre M07 y evidencias
horas: 5.0
semana: 6
lectura: Checklist de dominio y evidencias en git
evidencia: bitácora + checklist dominio + progress
---

# L24 — Cierre M07 y evidencias

**~5.0 h · Semana 6**

Si no está en git con checklist, no cuenta. Hoy cierras la materia.

## Objetivo

Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de cierre y el README.

## Pasos

### 1. Checklist con rutas (60 min)

`bitacora/cierre-m07.md`:

- P1: rutas a lista/pila/cola/hash + tests
- P2: bst + recorridos
- P3: `bench/RESULTADOS.md`
- Proyecto: guía README

### 2. Criterios de dominio (50 min)

Grábate o escribe respuesta de 3 minutos: “¿cuándo un hash gana a un árbol?”. Pega el outline en la bitácora.

### 3. Regresión final (40 min)

```bash
cd projects/m07-estructuras && npm test
```

### 4. Limpieza (40 min)

Quita `console.log` de debug, asegura que no hay secretos, actualiza scripts del package.json.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Autoevaluación: explicar hash vs árbol en voz alta | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con rutas de archivo.
2. Suite verde y README de selección presente.
3. Commit `docs(m07): cierre materia y evidencias`.

## Errores comunes

- Marcar evidencias sin archivos en git.
- Checklist genérico sin rutas.
- Dejar benches o tests rotos “para después”.

## Siguiente

M07 cerrado — siguiente materia: [M08 · Análisis de algoritmos](../M08-analisis-de-algoritmos.md)
