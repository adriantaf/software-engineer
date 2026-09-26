---
id: L22
materia: M07
orden: 22
titulo: "Benchmark P3: nativo vs propio"
horas: 5.0
semana: 6
lectura: "Medir antes de opinar: microbenchmarks honestos"
evidencia: bench/ con tabla tiempos documentada
---

# L22 — Benchmark P3: nativo vs propio

**~5.0 h · Semana 6**

P3 exige números, no opiniones. Mides insert/lookup en tu hash y array vs nativos.

## Objetivo

Correr un bench reproducible y dejar tabla de tiempos en el repo.

## Pasos

### 1. Harness (50 min)

`bench/run.ts` con `performance.now()`, warmup 1 iter, luego mide. Parámetro `N` (default 100_000).

### 2. Casos (90 min)

Mínimo:

- `DynamicArray.push` vs `Array.push`
- `HashMap.set/get` vs `Map.set/get`

Opcional: heap extract vs array+sort periódico.

### 3. Ejecuta y pega (40 min)

```bash
npm run bench
# o: npx tsx bench/run.ts
```

Copia salida a `bench/RESULTADOS.md` con fecha y máquina (sin datos personales).

### 4. Lectura crítica (30 min)

Párrafo: por qué el nativo suele ganar y qué aprendiste implementando.

### 5. Commit (15 min)

```bash
git add projects/m07-estructuras/bench
git commit -m "feat(m07): bench P3 nativo vs propio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Metodología: warmup, N grande, no mentir con N=10 | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `bench/run.ts` compara ≥2 estructuras propias vs nativas (`Array`/`Map`).
2. Tabla de tiempos en `bench/RESULTADOS.md` (o README P3).
3. Commit `feat(m07): bench P3 nativo vs propio`.

## Errores comunes

- Benchmark con N trivial o sin warmup.
- Conclusiones absolutas (“soy más rápido que V8”).
- No versionar el comando para reproducir.

## Siguiente

[L23 — README cuándo usar cada estructura](L23-readme-cuando-usar-cada-estructura.md)
