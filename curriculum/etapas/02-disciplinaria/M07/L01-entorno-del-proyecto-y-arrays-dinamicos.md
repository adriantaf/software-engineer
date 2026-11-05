---
id: L01
materia: M07
orden: 1
titulo: Entorno del proyecto y arrays dinámicos
horas: 5
semana: 1
lectura: 'Arrays estáticos/dinámicos, capacidad y costo amortizado de push'
evidencia: 'projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `projects/m07-estructuras/` usable con TypeScript
      strict, Vitest y un `DynamicArray<T>` con costos documentados.


      Sin toolchain y evidencia en git, el resto de M07 no cuenta. Hoy levantas
      la librería y tu primera estructura lineal.
  - id: s2
    tipo: ejemplo
    titulo: 1. Revisa el scaffold
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m07-estructuras
      cat projects/m07-estructuras/README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Entorno del proyecto y arrays dinámicos" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: 'projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests'
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `ls projects/m07-estructuras`
    comandoEsperado:
      - ls projects/m07-estructuras
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls projects/m07-estructuras'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar `projects/m07-estructuras/` usable con TypeScript strict, Vitest
          y un `DynamicArray<T>` con costos documentados.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Toolchain TypeScript + Vitest
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m07-estructuras

      npm init -y

      npm install -D typescript tsx vitest @types/node

      npx tsc --init --strict --rootDir src --outDir dist --module nodenext
      --moduleResolution nodenext --target ES2022

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
  - id: s7
    tipo: explicacion
    titulo: 3. `DynamicArray<T>`
    xp: 10
    cuerpo: >-
      Crea `src/dynamic-array.ts` con buffer interno (p. ej. `Array<T |
      undefined>` o `new Array(cap)`), `length`, `capacity`, `get(i)`, `push(x)`
      que duplique capacidad al llenarse. **No** uses `Array.push` como única
      lógica: tú controlas el resize.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m07-estructuras/` tiene `package.json` con script `test`
        (Vitest) y `tsc` strict.
      - >-
        `src/dynamic-array.ts` implementa capacidad, `get`, `push` con resize
        ×2; ≥5 tests verdes.
      - >-
        `COMPLEJIDAD.md` documenta O(1) acceso y O(1) amortizado `push`; commit
        `feat(m07): dynamic array con tests`.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
