---
id: L01
materia: M07
orden: 1
titulo: Entorno del proyecto y arrays dinámicos
horas: 5.0
semana: 1
lectura: Arrays estáticos/dinámicos, capacidad y costo amortizado de push
evidencia: projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests
---

# L01 — Entorno del proyecto y arrays dinámicos

**~5.0 h · Semana 1**

Sin toolchain y evidencia en git, el resto de M07 no cuenta. Hoy levantas la librería y tu primera estructura lineal.

## Objetivo

Dejar `projects/m07-estructuras/` usable con TypeScript strict, Vitest y un `DynamicArray<T>` con costos documentados.

## Pasos (hazlos en orden)

### 1. Revisa el scaffold (15 min)

```bash
ls projects/m07-estructuras
cat projects/m07-estructuras/README.md
```

No borres la estructura; amplíala. Crea carpetas si faltan:

```bash
mkdir -p projects/m07-estructuras/{src,tests,bench}
```

### 2. Toolchain TypeScript + Vitest (45–60 min)

```bash
cd projects/m07-estructuras
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

En `package.json` añade:

```json
"scripts": {
  "test": "vitest run",
  "test:watch": "vitest",
  "build": "tsc",
  "bench": "tsx bench/run.ts"
}
```

Confirma `strict: true` en `tsconfig.json`.

### 3. `DynamicArray<T>` (90 min)

Crea `src/dynamic-array.ts` con buffer interno (p. ej. `Array<T | undefined>` o `new Array(cap)`), `length`, `capacity`, `get(i)`, `push(x)` que duplique capacidad al llenarse. **No** uses `Array.push` como única lógica: tú controlas el resize.

### 4. Cinco tests (60 min)

`tests/dynamic-array.test.ts`: vacío; un elemento; push que fuerza resize; `get` fuera de rango (throw o `undefined` — elige y documenta); secuencia de 100 pushes.

```bash
npm test
```

### 5. Costos + commit (30–40 min)

Escribe `COMPLEJIDAD.md` con filas: acceso indexado, `push` amortizado, insert en medio (aún no). Luego:

```bash
git add projects/m07-estructuras
git commit -m "feat(m07): dynamic array con tests"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Arrays estáticos vs dinámicos; crecimiento ×2 y amortizado | [VisuAlgo · Array](https://visualgo.net/en/array) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m07-estructuras/` tiene `package.json` con script `test` (Vitest) y `tsc` strict.
2. `src/dynamic-array.ts` implementa capacidad, `get`, `push` con resize ×2; ≥5 tests verdes.
3. `COMPLEJIDAD.md` documenta O(1) acceso y O(1) amortizado `push`; commit `feat(m07): dynamic array con tests`.

## Errores comunes

- Envolver `T[]` nativo y llamarlo “dynamic array” sin capacidad propia.
- No tener un test que dispare el redimensionamiento.
- Dejar `strict: false` o sin script `test`.

## Siguiente

[L02 — Lista enlazada simple](L02-lista-enlazada-simple.md)
