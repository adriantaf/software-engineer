---
id: L01
materia: M07
orden: 1
titulo: Entorno del proyecto y arrays dinámicos
horas: 5.0
semana: 1
lectura: "ED Joyanes (o equivalente): arrays estáticos/dinámicos, amortizado"
evidencia: "projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests"
---

# L01 — Entorno del proyecto y arrays dinámicos

**~5.0 h · Semana 1**

Arrancas la librería de estructuras: TypeScript strict, tests desde el día 1 y tu primera estructura lineal con costos documentados.

## Objetivo

Levantar `projects/m07-estructuras/`, implementar un array dinámico tipado con capacidad explícita y anotar Big-O de acceso e inserción al final.

## Pasos

### 1. Proyecto y toolchain (45 min)

```bash
mkdir -p projects/m07-estructuras/src
cd projects/m07-estructuras
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init
```

`strict: true`. Scripts: `"test": "vitest run"`, `"build": "tsc"`. Enlaza esta carpeta desde `projects/m07-estructuras/README.md`.

### 2. `DynamicArray<T>` (90 min)

Implementa capacidad, `length`, `get(i)`, `push(x)` con redimensionamiento (×2). **No** uses `Array` interno como atajo permanente: el objetivo es entender amortizado.

### 3. Tabla de costos (30 min)

En `COMPLEJIDAD.md` (o README): O(1) acceso indexado, O(1) amortizado `push`, O(n) insert en medio (aún no implementado — anótalo).

### 4. Cinco tests (60 min)

Vacío, un elemento, redimensiona al llenar capacidad, `get` fuera de rango (define comportamiento: throw o undefined), secuencia larga.

### 5. Lectura + commit (45 min)

Lee el capítulo de **arrays** de tu texto ED. Commit: `feat(m07): dynamic array con tests`.

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Texto ED (Joyanes u otro) | Arrays: operaciones y costos | Implementación + tabla propia |
| MDN | [`Array`](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array) como contraste | Solo lectura |

## Hecho cuando

1. Proyecto TS strict con Vitest verde.
2. `DynamicArray` con redimensionamiento probado.
3. Big-O documentado para acceso y `push`.
4. Commit en git.

## Errores comunes

- Implementar solo con `T[]` nativo y llamarlo “dynamic array”.
- No probar el caso que dispara redimensionar.
- Omitir documentación de costos.
## Siguiente

[L02 — Lista enlazada simple](L02-lista-enlazada-simple.md)
