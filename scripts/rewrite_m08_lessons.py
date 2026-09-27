#!/usr/bin/env python3
"""Rewrite M08 lessons to M01/M09 quality (concrete timed steps, no boilerplate)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M08"
BIBLIO = "../../../bibliografia.md#m08-analisis-de-algoritmos"
CLRS = "*Introducción a los algoritmos* — CLRS (ed. ES)"
VISUALGO = "https://visualgo.net/en"


def fm(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, str) and (":" in v or v.startswith("*") or '"' in v or "'" in v):
            safe = v.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def lectura_block(que, enlace_titulo="VisuAlgo", enlace=VISUALGO):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {CLRS} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08]({BIBLIO}) |
"""


def render(lesson: dict) -> str:
    pub = {
        "id": lesson["id"],
        "materia": "M08",
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
    }
    enlace = lesson.get("_enlace", {})
    hecho = lesson["_hecho"].strip()
    errores = lesson["_errores"].strip()
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(lesson.get("_lectura_corta", lesson["lectura"]), **enlace)}

## Hecho cuando

Marca la lección **solo si**:

{hecho}

## Errores comunes

{errores}

## Siguiente

{lesson["siguiente"]}
"""


FILENAMES = {
    1: "L01-entorno-y-binary-search-con-invariante.md",
    2: "L02-notacion-asintotica-o-y.md",
    3: "L03-analisis-de-bucles-y-recursion-simple.md",
    4: "L04-tres-problemas-con-complejidad-escrita.md",
    5: "L05-insertion-sort-implementado.md",
    6: "L06-merge-sort-y-estabilidad.md",
    7: "L07-quicksort-y-peor-caso.md",
    8: "L08-tabla-p2-sorts-en-readme.md",
    9: "L09-hash-maps-en-problemas-de-conteo.md",
    10: "L10-two-pointers-en-arrays-ordenados.md",
    11: "L11-sliding-window.md",
    12: "L12-indice-de-patrones-5-entradas.md",
    13: "L13-bfs-repaso-y-cola.md",
    14: "L14-dfs-y-componentes.md",
    15: "L15-caminos-en-grafos-no-ponderados.md",
    16: "L16-problemas-de-grafos-semana-4.md",
    17: "L17-memoizacion-top-down.md",
    18: "L18-programacion-dinamica-bottom-up.md",
    19: "L19-tres-problemas-dp-p3.md",
    20: "L20-patrones-dp-y-transiciones.md",
    21: "L21-autocomplete-eleccion-de-estructura.md",
    22: "L22-implementacion-trie-o-indice.md",
    23: "L23-dataset-agenda-ops-y-demo-cli.md",
    24: "L24-cierre-m08-y-evidencias.md",
}

LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Entorno y binary search con invariante",
        horas=5.0,
        semana=1,
        lectura="Búsqueda binaria e invariante del intervalo [lo, hi]",
        evidencia="binary-search.ts + analisis + 2 problemas arrays",
        _lectura_corta="Búsqueda binaria: invariante y O(log n)",
        _enlace={"enlace_titulo": "VisuAlgo · Binary Search", "enlace": "https://visualgo.net/en/binsearch"},
        _hecho="""1. `projects/m08-algoritmos/` con carpetas `problems/`, `sorts/`, `dp/`, `autocomplete/` y Vitest configurado.
2. `src/binary-search.ts` + `docs/binary-search-analisis.md` con invariante; ≥4 tests.
3. Dos problemas en `problems/` (enunciado + complejidad + 3 tests c/u); commit `feat(m08): binary search y 2 problemas arrays`.""",
        _errores="""- Binary search sin invariante escrito.
- Off-by-one en `hi = mid` vs `hi = mid-1`.
- Problemas sin complejidad ni casos borde.""",
        siguiente="[L02 — Notación asintótica Θ, O y Ω](L02-notacion-asintotica-o-y.md)",
        body=r"""
# L01 — Entorno y binary search con invariante

**~5.0 h · Semana 1**

M08 exige carpetas de evidencia y el hábito: invariante → código → complejidad → tests.

## Objetivo

Levantar `projects/m08-algoritmos/`, implementar binary search con invariante documentado y dejar dos problemas de arrays.

## Pasos (hazlos en orden)

### 1. Scaffold (25 min)

```bash
mkdir -p projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}
cd projects/m08-algoritmos
cat README.md
```

Si no hay toolchain:

```bash
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

Script `"test": "vitest run"`.

### 2. Binary search (75 min)

`src/binary-search.ts`:

```ts
/** Invariante: si t está en a, está en a[lo..hi] inclusive. */
export function binarySearch(a: number[], t: number): number
```

Define convención con duplicados (p. ej. cualquier índice, o el primero).

### 3. Análisis (35 min)

`docs/binary-search-analisis.md`: invariante, por qué O(log n), qué pasa si el array no está ordenado.

### 4. Tests + 2 problemas (90 min)

Tests: vacío, uno, ausente, presente, duplicados.

Luego `problems/01-two-sum/` y `problems/02-max-subarray/` (o nombres claros): cada uno con `enunciado.md`, `solution.ts`, `solution.test.ts` (3 casos), línea de complejidad en el enunciado. 30–45 min atascado antes de mirar pistas.

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): binary search y 2 problemas arrays"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Notación asintótica Θ, O y Ω",
        horas=5.0,
        semana=1,
        lectura="CLRS: crecimiento de funciones — O, Ω, Θ",
        evidencia="notacion.md + 5 funciones clasificadas",
        _lectura_corta="Definiciones O, Ω, Θ; peores vs cotas ajustadas",
        _hecho="""1. `docs/notacion.md` define O/Ω/Θ con tus palabras + 1 ejemplo gráfico/tabla.
2. Clasificas **5** funciones/algoritmos (código o fórmulas) con justificación de 2–3 líneas c/u.
3. Commit `docs(m08): notacion asintotica O Omega Theta`.""",
        _errores="""- Usar O como sinónimo de “exactamente” sin Θ.
- Confundir peor caso del algoritmo con cota de una función.
- Lista de 5 sin justificación (“es O(n) porque sí”).""",
        siguiente="[L03 — Análisis de bucles y recursión simple](L03-analisis-de-bucles-y-recursion-simple.md)",
        body=r"""
# L02 — Notación asintótica Θ, O y Ω

**~5.0 h · Semana 1**

Sin lenguaje común de cotas, el resto de M08 es opinión.

## Objetivo

Escribir `docs/notacion.md` con definiciones operativas y clasificar cinco ejemplos concretos.

## Pasos

### 1. Lectura CLRS (60–75 min)

Capítulo de crecimiento/notación. Anota definiciones formales y una intuición (“O = techo, Ω = piso, Θ = ajustado”).

### 2. Documento base (45 min)

`docs/notacion.md`: definiciones + tabla `n`, `n log n`, `n²`, `2ⁿ` con valores a n=2,8,32 (calculadora).

### 3. Cinco clasificaciones (70 min)

Incluye: binary search; un doble bucle triangular; `push` amortizado de array dinámico (referencia M07); factorial recursivo ingenuo; merge de dos arrays ordenados. Para cada uno: Θ o O + peor caso.

### 4. Autocomprobación (30 min)

Explica en voz alta la diferencia O vs Θ con un ejemplo; resume en 4 líneas al final del doc.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): notacion asintotica O Omega Theta"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Análisis de bucles y recursión simple",
        horas=5.0,
        semana=1,
        lectura="Sumas de bucles anidados y recurrencias simples",
        evidencia="3 snippets analizados en markdown",
        _lectura_corta="Contar iteraciones; árbol de recursión simple (T(n)=T(n-1)+O(1))",
        _hecho="""1. `docs/analisis-bucles.md` con **3** snippets TS y su complejidad justificada.
2. Al menos uno recursivo con árbol o unfolding escrito.
3. Commit `docs(m08): analisis bucles y recursion`.""",
        _errores="""- Contar mal bucles dependientes (`for i; for j=i`).
- Decir O(n²) a binary search recursivo.
- Snippets sin código real (solo prosa).""",
        siguiente="[L04 — Tres problemas con complejidad escrita](L04-tres-problemas-con-complejidad-escrita.md)",
        body=r"""
# L03 — Análisis de bucles y recursión simple

**~5.0 h · Semana 1**

Pasas de definiciones a contar operaciones en código que tú escribes.

## Objetivo

Analizar tres snippets (2 iterativos + 1 recursivo) en `docs/analisis-bucles.md`.

## Pasos

### 1. Snippet A — bucle simple (35 min)

Escribe un `sum(a: number[])` y justifica Θ(n) tiempo / Θ(1) extra.

### 2. Snippet B — anidado (50 min)

```ts
for (let i = 0; i < n; i++)
  for (let j = i; j < n; j++) { /* ... */ }
```

Cuenta iteraciones ≈ n(n+1)/2 → Θ(n²).

### 3. Snippet C — recursión (60 min)

`rec(n) = rec(n-1) + work` tipo factorial o suma. Unfolding hasta base; Θ(n) llamadas.

### 4. Contraste (40 min)

Añade binary search recursivo: profundidad log n. Enlaza a L01.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): analisis bucles y recursion"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Tres problemas con complejidad escrita",
        horas=5.0,
        semana=1,
        lectura="Plantilla de entrega: enunciado, complejidad, código, tests",
        evidencia="problems/ con 3 entradas + complejidad",
        _lectura_corta="Disciplina de evidencia por problema (P1)",
        _hecho="""1. Tres carpetas bajo `problems/` (pueden incluir las de L01) cada una con enunciado, complejidad, solución y ≥3 tests.
2. Filas iniciales en `indice-patrones.md` (≥3).
3. Commit `feat(m08): tres problemas con complejidad`.""",
        _errores="""- Código sin enunciado ni Big-O.
- Un solo test feliz.
- Índice vacío al cerrar la semana.""",
        siguiente="[L05 — Insertion sort implementado](L05-insertion-sort-implementado.md)",
        body=r"""
# L04 — Tres problemas con complejidad escrita

**~5.0 h · Semana 1**

Cierras la semana 1 con la plantilla P1 que usarás el resto del curso.

## Objetivo

Dejar tres problemas completos en `problems/` e iniciar `indice-patrones.md`.

## Pasos

### 1. Plantilla (20 min)

Cada problema:

```
problems/NN-nombre/
  enunciado.md    # problema + complejidad objetivo
  solution.ts
  solution.test.ts
```

### 2. Completar / añadir hasta 3 (120 min)

Si L01 ya trajo 2, añade un tercero (p. ej. “mover ceros”, “intersección de arrays”). 30–45 min de intento serio antes de editorial propia.

### 3. Índice (40 min)

`indice-patrones.md` tabla: id | patrón | archivo | complejidad | notas.

### 4. Suite (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): tres problemas con complejidad"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Insertion sort implementado",
        horas=5.0,
        semana=2,
        lectura="CLRS: insertion sort — invariante del prefijo ordenado",
        evidencia="sorts/insertion.ts + tests",
        _lectura_corta="Insertion sort: Θ(n²) peor / Θ(n) casi ordenado",
        _enlace={"enlace_titulo": "VisuAlgo · Sorting", "enlace": "https://visualgo.net/en/sorting"},
        _hecho="""1. `sorts/insertion.ts` ordena números (o genérico comparable) in-place o documentando copia.
2. Tests: vacío, uno, invertido, ya ordenado, duplicados.
3. `sorts/insertion-analisis.md` con peor/mejor caso; commit `feat(m08): insertion sort`.""",
        _errores="""- Llamar a `Array.sort` y presentarlo como insertion.
- No probar el caso ya ordenado (mejor caso).
- Olvidar estabilidad (aunque insertion es estable — menciónalo).""",
        siguiente="[L06 — Merge sort y estabilidad](L06-merge-sort-y-estabilidad.md)",
        body=r"""
# L05 — Insertion sort implementado

**~5.0 h · Semana 2**

Insertion es el sort didáctico: invariante “a[0..i) ordenado” y base de la semana P2.

## Objetivo

Implementar insertion sort, analizarlo y dejar tests que cubran mejor y peor caso.

## Pasos

### 1. VisuAlgo (20 min)

Modo insertion; anota cuántas escrituras ves en un array invertido vs casi ordenado.

### 2. Implementación (70 min)

`sorts/insertion.ts` — `export function insertionSort(a: number[]): number[]` (mutando o devolviendo copia; dilo en JSDoc).

### 3. Análisis (40 min)

`sorts/insertion-analisis.md`: peor Θ(n²), mejor Θ(n), espacial, estabilidad = sí.

### 4. Tests (50 min)

Incluye array de 100 elementos random vs `[...a].sort((x,y)=>x-y)`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/sorts
git commit -m "feat(m08): insertion sort"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Merge sort y estabilidad",
        horas=5.0,
        semana=2,
        lectura="CLRS: divide y vencerás — merge sort",
        evidencia="sorts/merge.ts + nota estabilidad",
        _lectura_corta="Merge sort Θ(n log n); estabilidad al fusionar",
        _enlace={"enlace_titulo": "VisuAlgo · Sorting", "enlace": "https://visualgo.net/en/sorting"},
        _hecho="""1. `sorts/merge.ts` con `merge` + `mergeSort`.
2. Nota de estabilidad con ejemplo de pares `(key, payload)` en `sorts/estabilidad.md`.
3. Tests verdes; commit `feat(m08): merge sort y estabilidad`.""",
        _errores="""- Merge que pisa el orden relativo de iguales (rompe estabilidad).
- Olvidar costo espacial Θ(n).
- Recursión sin caso base en length ≤ 1.""",
        siguiente="[L07 — Quicksort y peor caso](L07-quicksort-y-peor-caso.md)",
        body=r"""
# L06 — Merge sort y estabilidad

**~5.0 h · Semana 2**

Merge garantiza Θ(n log n) y puede ser estable si el merge elige bien ante empates.

## Objetivo

Implementar merge sort y demostrar estabilidad con un test o ejemplo documentado.

## Pasos

### 1. Lectura (40 min)

CLRS merge sort + VisuAlgo. Escribe la recurrencia T(n)=2T(n/2)+Θ(n).

### 2. `merge` + `mergeSort` (90 min)

`sorts/merge.ts`. Al comparar iguales, toma primero del buffer izquierdo (estabilidad).

### 3. Estabilidad (50 min)

`sorts/estabilidad.md` + test con objetos `{k, id}`: mismos `k` preservan orden de `id`.

### 4. Tests adicionales (30 min)

Random vs sort nativo; vacío; un elemento.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): merge sort y estabilidad"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Quicksort y peor caso",
        horas=5.0,
        semana=2,
        lectura="CLRS: quicksort — partición y peor caso",
        evidencia="sorts/quick.ts + caso O(n²)",
        _lectura_corta="Quicksort promedio vs peor caso n²; pivotes",
        _enlace={"enlace_titulo": "VisuAlgo · Sorting", "enlace": "https://visualgo.net/en/sorting"},
        _hecho="""1. `sorts/quick.ts` con partición documentada.
2. `sorts/quick-peor-caso.md` explica entrada adversaria (ya ordenado + pivote fijo) y mitigación (pivote random/median-of-three).
3. Tests + commit `feat(m08): quicksort y peor caso`.""",
        _errores="""- Afirmar “quicksort es O(n log n)” sin matizar peor caso.
- Partición incorrecta (loops infinitos).
- Sin test de array con muchos duplicados.""",
        siguiente="[L08 — Tabla P2 sorts en README](L08-tabla-p2-sorts-en-readme.md)",
        body=r"""
# L07 — Quicksort y peor caso

**~5.0 h · Semana 2**

Quicksort brilla en promedio y falla con pivotes ingenuos en datos ordenados.

## Objetivo

Implementar quicksort, documentar el peor caso O(n²) y una mitigación concreta.

## Pasos

### 1. Partición (70 min)

`sorts/quick.ts`: Lomuto o Hoare — elige una y comenta invariante.

### 2. Peor caso escrito (50 min)

`sorts/quick-peor-caso.md`: secuencia que degenera con pivote `a[hi]`; contador de comparaciones opcional en modo debug.

### 3. Mitigación (50 min)

Implementa pivote aleatorio **o** median-of-three. Nota en el markdown.

### 4. Tests (40 min)

Ordenado, invertido, duplicados, random vs nativo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): quicksort y peor caso"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Tabla P2 sorts en README",
        horas=5.0,
        semana=2,
        lectura="Comparativa de ordenamientos P2",
        evidencia="sorts/README.md P2 parcial",
        _lectura_corta="Tabla peor/promedio/espacial/estable por sort",
        _hecho="""1. `sorts/README.md` con tabla insertion/merge/quick (y nativo como referencia).
2. Suite de sorts verde; enlace desde README raíz del proyecto.
3. Commit `docs(m08): tabla P2 sorts`.""",
        _errores="""- Tabla copiada de Internet sin alinear a tu código.
- Omitir estabilidad o memoria.
- Dejar quick sin nota de peor caso.""",
        siguiente="[L09 — Hash maps en problemas de conteo](L09-hash-maps-en-problemas-de-conteo.md)",
        body=r"""
# L08 — Tabla P2 sorts en README

**~5.0 h · Semana 2**

P2 parcial: tres sorts propios + tabla defendible.

## Objetivo

Publicar `sorts/README.md` comparativo y verificar tests de la carpeta sorts.

## Pasos

### 1. Auditoría (30 min)

```bash
ls sorts/*.ts
npm test
```

### 2. Tabla (70 min)

Columnas: algoritmo | peor | promedio | espacial | estable | cuándo usarlo. Filas: insertion, merge, quick, `Array.sort` (motor).

### 3. Microbench opcional (60 min)

`sorts/bench.ts` N=5_000 — pega números en el README (honestos).

### 4. Enlace raíz (30 min)

Desde `projects/m08-algoritmos/README.md` → sección P2.

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): tabla P2 sorts"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Hash maps en problemas de conteo",
        horas=5.0,
        semana=3,
        lectura="Patrón hashing / conteo de frecuencias",
        evidencia="2 problemas patrón hash",
        _lectura_corta="Frequency map; anagramas; two-sum con hash",
        _hecho="""1. Dos problemas en `problems/` con patrón hash/conteo, complejidad y ≥3 tests c/u.
2. Actualizas `indice-patrones.md` con esas filas.
3. Commit `feat(m08): problemas hash conteo`.""",
        _errores="""- Solución O(n²) presentada como hash.
- Usar sort+two pointers sin reconocer que no es el patrón de hoy.
- Índice sin enlazar archivos.""",
        siguiente="[L10 — Two pointers en arrays ordenados](L10-two-pointers-en-arrays-ordenados.md)",
        body=r"""
# L09 — Hash maps en problemas de conteo

**~5.0 h · Semana 3**

El mapa de frecuencias convierte muchos O(n²) en O(n) promedio.

## Objetivo

Resolver dos problemas de conteo/hash con evidencia completa e índice actualizado.

## Pasos

### 1. Elige problemas (15 min)

Ejemplos: anagramas (`isAnagram`), two-sum con `Map`, primer carácter único, conteo de votos. Dos bastan.

### 2. Problema A (70 min)

Carpeta `problems/…`: enunciado, solución con `Map`, complejidad, 3 tests (borde: vacío / un elemento).

### 3. Problema B (70 min)

Igual plantilla. Si two-sum ya existía con fuerza bruta, reescribe con hash y anota mejora.

### 4. Índice (30 min)

Patrón `hash-conteo` en `indice-patrones.md`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): problemas hash conteo"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Two pointers en arrays ordenados",
        horas=5.0,
        semana=3,
        lectura="Two pointers / left-right en secuencias ordenadas",
        evidencia="2 problemas two pointers",
        _lectura_corta="Punteros extremos; pair sum en array ordenado",
        _hecho="""1. Dos problemas two-pointers con arrays ordenados (o justificación de por qué ordenas antes).
2. Complejidad O(n) tras ordenar si aplica — dilo explícito.
3. Commit `feat(m08): two pointers arrays ordenados`.""",
        _errores="""- Two pointers en no ordenado sin ordenar ni justificar.
- Índices que se cruzan mal (loop infinito).
- No cubrir caso sin solución.""",
        siguiente="[L11 — Sliding window](L11-sliding-window.md)",
        body=r"""
# L10 — Two pointers en arrays ordenados

**~5.0 h · Semana 3**

Con orden, left/right reemplazan búsquedas anidadas.

## Objetivo

Entregar dos soluciones two-pointers bien testeadas e indexadas.

## Pasos

### 1. Patrón en papel (25 min)

Dibuja pair-sum = target en array ordenado. Anota cuándo mueves left vs right.

### 2. Problema A — pair sum (60 min)

`problems/…-pair-sum/`. Tests: hay par, no hay, duplicados, negativos.

### 3. Problema B (70 min)

Ej. contenedor de agua, squaring sorted array, merge dos ordenados in-place conceptual. Misma plantilla.

### 4. Índice + nota (30 min)

Compara con hash two-sum: trade-off ordenar+O(n) vs hash O(n) promedio.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): two pointers arrays ordenados"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Sliding window",
        horas=5.0,
        semana=3,
        lectura="Ventana deslizante fija y variable",
        evidencia="2 problemas ventana",
        _lectura_corta="Window fija vs variable; invariante de la ventana",
        _hecho="""1. Dos problemas sliding window (fija y/o variable) con análisis.
2. Tests incluyen ventana más grande que el array.
3. Commit `feat(m08): sliding window`.""",
        _errores="""- Recalcular la ventana desde cero cada paso (O(nk) disfrazado).
- Olvidar encoger la ventana en la variante variable.
- Sin invariante escrito.""",
        siguiente="[L12 — Índice de patrones (5+ entradas)](L12-indice-de-patrones-5-entradas.md)",
        body=r"""
# L11 — Sliding window

**~5.0 h · Semana 3**

La ventana mantiene un invariante local y se desliza en O(n) total.

## Objetivo

Resolver dos problemas de ventana y documentar el invariante de cada uno.

## Pasos

### 1. Lectura / bosquejo (30 min)

Fija (max sum subarray size k) vs variable (longest substring without repeat).

### 2. Problema ventana fija (60 min)

Implementa + tests (k > n, k=1, k=n).

### 3. Problema ventana variable (80 min)

Map/set de frecuencia; mueve `right`, encoge `left`. Complejidad O(n).

### 4. Índice (20 min)

Patrón `sliding-window`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): sliding window"
```
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Índice de patrones (5+ entradas)",
        horas=5.0,
        semana=3,
        lectura="Clasificación de problemas por patrón (P1 parcial)",
        evidencia="≥5 patrones clasificados",
        _lectura_corta="Índice vivo: binary search, hash, two pointers, window, sort…",
        _hecho="""1. `indice-patrones.md` con **≥5** entradas reales enlazando carpetas.
2. Cada fila tiene complejidad y patrón nombrado.
3. Commit `docs(m08): indice patrones 5+ entradas`.""",
        _errores="""- Filas fantasma sin carpeta.
- Solo un patrón repetido cinco veces.
- Complejidad en blanco.""",
        siguiente="[L13 — BFS repaso y cola](L13-bfs-repaso-y-cola.md)",
        body=r"""
# L12 — Índice de patrones (5+ entradas)

**~5.0 h · Semana 3**

El índice es el corazón de P1: sin clasificación, solo tienes código suelto.

## Objetivo

Dejar `indice-patrones.md` con al menos cinco entradas verificables.

## Pasos

### 1. Inventario (40 min)

```bash
find problems -name 'enunciado.md' | sort
```

Lista gaps.

### 2. Completar índice (70 min)

Tabla markdown: # | nombre | patrón | complejidad | ruta. Mínimo 5.

### 3. Rellenar huecos (60 min)

Si faltan patrones, añade un problema corto o reclasifica los existentes (binary search, hash, two pointers, window, sort).

### 4. QA enlaces (30 min)

Abre cada ruta; confirma que el enunciado menciona el patrón.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): indice patrones 5+ entradas"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="BFS repaso y cola",
        horas=5.0,
        semana=4,
        lectura="BFS sobre grafos / grids con cola",
        evidencia="1 problema BFS + grafo test",
        _lectura_corta="BFS: cola, visitados, capas O(V+E)",
        _enlace={"enlace_titulo": "VisuAlgo · BFS", "enlace": "https://visualgo.net/en/dfsbfs"},
        _hecho="""1. Utilidad de grafo o grid + `bfs` que retorna orden de visita o distancias.
2. Un problema en `problems/` resuelto con BFS + ≥3 tests.
3. Commit `feat(m08): bfs con cola`.""",
        _errores="""- BFS con stack (eso es DFS).
- No marcar visitados → loops.
- Complejidad sin hablar de V y E.""",
        siguiente="[L14 — DFS y componentes](L14-dfs-y-componentes.md)",
        body=r"""
# L13 — BFS repaso y cola

**~5.0 h · Semana 4**

BFS explora por capas; la cola es obligatoria.

## Objetivo

Implementar BFS reutilizable y resolver un problema con evidencia P1.

## Pasos

### 1. Grafo de prueba (40 min)

`src/graph.ts` (lista de adyacencia) o reusa el de M07 copiando lo mínimo. Tests de vecinos.

### 2. `bfs(start)` (70 min)

Cola + set visitados; opcional mapa `dist`. Complejidad O(V+E) en análisis corto `docs/bfs.md`.

### 3. Problema (70 min)

Ej. número de islas (grid), shortest path en grid sin pesos, o “grados de separación”. Carpeta en `problems/`.

### 4. Índice (20 min)

Patrón `bfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): bfs con cola"
```
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="DFS y componentes",
        horas=5.0,
        semana=4,
        lectura="DFS y componentes conexas",
        evidencia="problema componentes conexas",
        _lectura_corta="DFS recursivo/iterativo; contar componentes",
        _enlace={"enlace_titulo": "VisuAlgo · DFS", "enlace": "https://visualgo.net/en/dfsbfs"},
        _hecho="""1. `connectedComponents(graph)` (o problema equivalente) con tests.
2. Documentas recursivo vs stack explícito en 5–8 líneas.
3. Commit `feat(m08): dfs componentes conexas`.""",
        _errores="""- Contar nodos en vez de componentes.
- No resetear visitados entre componentes.
- Stack overflow en grafos grandes sin mencionar límite de recursión.""",
        siguiente="[L15 — Caminos en grafos no ponderados](L15-caminos-en-grafos-no-ponderados.md)",
        body=r"""
# L14 — DFS y componentes

**~5.0 h · Semana 4**

DFS recorre profundo; sirve para marcar componentes y ciclos introductorios.

## Objetivo

Contar componentes conexas (o resolver problema equivalente) con DFS y tests.

## Pasos

### 1. DFS base (50 min)

`dfs(v, visited)` recursivo. Versión iterativa opcional.

### 2. Componentes (70 min)

Algoritmo: para cada vértice no visitado, DFS y ++count. Tests con 1 componente, 3 componentes, grafo vacío.

### 3. Problema empaquetado (60 min)

`problems/…-componentes/` con enunciado de red social / salas conectadas.

### 4. Índice (20 min)

Patrón `dfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dfs componentes conexas"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="Caminos en grafos no ponderados",
        horas=5.0,
        semana=4,
        lectura="Camino más corto en aristas unitarias = BFS",
        evidencia="camino mínimo en aristas no peso",
        _lectura_corta="BFS distancias; reconstruir camino con parent[]",
        _hecho="""1. Función que devuelve distancia y/o camino start→goal en grafo no ponderado.
2. Tests: alcanzable, inalcanzable, start=goal.
3. Commit `feat(m08): camino minimo no ponderado BFS`.""",
        _errores="""- Usar Dijkstra “porque sí” en grafos unitarios sin justificar.
- No reconstruir camino cuando se pide.
- Distancia mal inicializada (0 vs Infinity).""",
        siguiente="[L16 — Problemas de grafos semana 4](L16-problemas-de-grafos-semana-4.md)",
        body=r"""
# L15 — Caminos en grafos no ponderados

**~5.0 h · Semana 4**

Con peso uniforme, BFS da el camino con menos aristas.

## Objetivo

Calcular distancia (y camino) mínimo start→goal con BFS y parents.

## Pasos

### 1. Extiende BFS (60 min)

Guarda `parent` o `prev`. Al llegar a goal, reconstruye lista invirtiendo.

### 2. API clara (40 min)

`shortestPath(graph, start, goal): { dist: number, path: string[] } | null`

### 3. Tests (50 min)

Camino simple; sin camino; start=goal dist 0; grafo con ciclo no se cuelga.

### 4. Problema / doc (40 min)

Enunciado tipo “mínimas citas de referencias entre clientes” (grafo demo) en `problems/` o `docs/`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): camino minimo no ponderado BFS"
```
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Problemas de grafos semana 4",
        horas=5.0,
        semana=4,
        lectura="Cierre semana grafos: +2 problemas en índice",
        evidencia="problems/ +2 grafos",
        _lectura_corta="Práctica BFS/DFS adicional; índice ≥ entradas de grafos",
        _hecho="""1. **+2** problemas de grafos (además de L13–L15 si ya contaban, completa hasta tener evidencia clara de dos más o consolida carpetas).
2. `indice-patrones.md` con filas bfs/dfs/camino.
3. Commit `feat(m08): problemas grafos semana 4`.""",
        _errores="""- Reentregar el mismo archivo tres veces con otro nombre.
- Índice desactualizado.
- Tests flaky por orden de vecinos no determinista sin sort.""",
        siguiente="[L17 — Memoización top-down](L17-memoizacion-top-down.md)",
        body=r"""
# L16 — Problemas de grafos semana 4

**~5.0 h · Semana 4**

Consolidás la semana 4 con dos prácticas más y el índice al día.

## Objetivo

Sumar dos problemas de grafos bien empaquetados y actualizar el índice.

## Pasos

### 1. Selección (20 min)

Ideas: clone graph, course schedule (ciclo), flood fill, word ladder corto.

### 2. Problema 1 (80 min)

Plantilla completa + 3 tests.

### 3. Problema 2 (80 min)

Igual. Si detectas ciclo, documenta complejidad.

### 4. Índice + bitácora (30 min)

`bitacora/semana-04.md` opcional: qué patrón aún te cuesta.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): problemas grafos semana 4"
```
""",
    )
)

# ---------- L17 ----------
LESSONS.append(
    dict(
        id="L17",
        orden=17,
        titulo="Memoización top-down",
        horas=5.0,
        semana=5,
        lectura="CLRS DP intro — top-down con memo",
        evidencia="dp/memo-ejemplo.ts",
        _lectura_corta="Recursión + mapa memo; overlapping subproblems",
        _hecho="""1. `dp/memo-ejemplo.ts` (fib o paths) con y sin memo, o contador de llamadas.
2. Tests de valores conocidos; nota de complejidad en `dp/README.md` borrador.
3. Commit `feat(m08): memoizacion top-down`.""",
        _errores="""- Memoizar sin clave correcta (olvidar argumentos).
- Creer que memo cambia la respuesta (solo el tiempo).
- Sin caso base.""",
        siguiente="[L18 — Programación dinámica bottom-up](L18-programacion-dinamica-bottom-up.md)",
        body=r"""
# L17 — Memoización top-down

**~5.0 h · Semana 5**

DP empieza viendo subproblemas solapados: fibonacci es el laboratorio.

## Objetivo

Implementar una solución top-down con memo y demostrar el ahorro de llamadas.

## Pasos

### 1. Lectura (40 min)

CLRS intro DP: overlapping subproblems + optimal substructure. Anota en `dp/README.md`.

### 2. Fib (u otro) naive vs memo (70 min)

`dp/memo-ejemplo.ts`: versión ingenua (solo para n pequeño) y `fibMemo` con `Map`/`array`. Contador de llamadas.

### 3. Tests (40 min)

fib(0..10) conocidos; n=40 memo termina en ms.

### 4. Definición de estado (40 min)

Escribe: estado = `__`, transición = `__`, base = `__`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): memoizacion top-down"
```
""",
    )
)

# ---------- L18 ----------
LESSONS.append(
    dict(
        id="L18",
        orden=18,
        titulo="Programación dinámica bottom-up",
        horas=5.0,
        semana=5,
        lectura="DP bottom-up / tabulación",
        evidencia="dp/bottom-up-ejemplo.ts",
        _lectura_corta="Tabla dp[]; orden de llenado; equivalencia con memo",
        _hecho="""1. `dp/bottom-up-ejemplo.ts` con tabulación del mismo problema que L17 (o coin change simple).
2. Comparas espacial (optimización de variables opcionales) en nota corta.
3. Commit `feat(m08): dp bottom-up`.""",
        _errores="""- Llenar la tabla en orden incorrecto.
- Off-by-one en índices.
- Copiar memo y llamarlo bottom-up sin array dp.""",
        siguiente="[L19 — Tres problemas DP (P3)](L19-tres-problemas-dp-p3.md)",
        body=r"""
# L18 — Programación dinámica bottom-up

**~5.0 h · Semana 5**

Tabular elimina la pila de recursión y deja el orden de dependencias explícito.

## Objetivo

Reescribir el problema de L17 (o uno nuevo) en bottom-up con tabla `dp[]`.

## Pasos

### 1. Diseña el orden (30 min)

En papel: de qué celda depende `dp[i]`.

### 2. Implementación (70 min)

`dp/bottom-up-ejemplo.ts`. Inicializa bases; loop hasta n.

### 3. Equivalencia (40 min)

Test: para n en 0..20, memo === bottom-up.

### 4. Nota espacial (40 min)

¿Puedes usar 2 variables en fib? Documéntalo; no es obligatorio optimizar.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dp bottom-up"
```
""",
    )
)

# ---------- L19 ----------
LESSONS.append(
    dict(
        id="L19",
        orden=19,
        titulo="Tres problemas DP (P3)",
        horas=5.0,
        semana=5,
        lectura="P3: tres problemas DP con caso base explícito",
        evidencia="dp/ tres carpetas con caso base",
        _lectura_corta="Plantilla: estado, base, transición, complejidad",
        _hecho="""1. Tres carpetas bajo `dp/` (o `dp/p1`, `dp/p2`, `dp/p3`) cada una con enunciado, caso base, transición, código y tests.
2. P3 checklist enlazada desde README.
3. Commit `feat(m08): tres problemas DP P3`.""",
        _errores="""- Tres variantes del mismo fib.
- Sin caso base escrito.
- Complejidad espacial omitida.""",
        siguiente="[L20 — Patrones DP y transiciones](L20-patrones-dp-y-transiciones.md)",
        body=r"""
# L19 — Tres problemas DP (P3)

**~5.0 h · Semana 5**

P3 exige tres problemas con caso base y transición explícitos — no solo fib.

## Objetivo

Entregar tres DP distintos empaquetados como evidencia P3.

## Pasos

### 1. Elige trio (20 min)

Ejemplos: climbing stairs, min coin change, unique paths, house robber, LCS intro corta. Evita tres fibs.

### 2. Problema 1 (70 min)

Carpeta con `enunciado.md` (estado/base/transición), `solution.ts`, tests.

### 3. Problemas 2 y 3 (110 min)

Misma plantilla. Uno puede ser top-down y otro bottom-up.

### 4. README P3 (20 min)

Lista las tres rutas en `dp/README.md`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): tres problemas DP P3"
```
""",
    )
)

# ---------- L20 ----------
LESSONS.append(
    dict(
        id="L20",
        orden=20,
        titulo="Patrones DP y transiciones",
        horas=5.0,
        semana=5,
        lectura="Catálogo personal de patrones DP",
        evidencia="dp/README patrones",
        _lectura_corta="1D, knapsack 0/1 intro, paths en grid",
        _hecho="""1. `dp/README.md` con tabla de patrones → problemas tuyos.
2. Cada problema P3 referenciado; bitácora semana 5 opcional.
3. Commit `docs(m08): patrones DP y transiciones`.""",
        _errores="""- Catálogo genérico sin tus rutas.
- Transiciones incorrectas copiadas.
- No enlazar desde README raíz.""",
        siguiente="[L21 — Autocomplete: elección de estructura](L21-autocomplete-eleccion-de-estructura.md)",
        body=r"""
# L20 — Patrones DP y transiciones

**~5.0 h · Semana 5**

Cierras la semana DP dejando un mapa mental reutilizable.

## Objetivo

Documentar patrones DP ligados a tus tres problemas y preparar el salto al proyecto autocomplete.

## Pasos

### 1. Tabla de patrones (60 min)

En `dp/README.md`: patrón | estado típico | transición | tu archivo.

### 2. Relee transiciones (50 min)

Corrige cualquier enunciado ambiguo de L19.

### 3. Flashcards (40 min)

5 preguntas autoevaluación al final del README (“¿qué es overlapping…?”).

### 4. Enlace raíz (30 min)

README del proyecto: sección P3 completa.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): patrones DP y transiciones"
```
""",
    )
)

# ---------- L21 ----------
LESSONS.append(
    dict(
        id="L21",
        orden=21,
        titulo="Autocomplete: elección de estructura",
        horas=5.0,
        semana=6,
        lectura="Trie vs array filtrado vs inverted index — trade-offs",
        evidencia="autocomplete/DISENO.md",
        _lectura_corta="Prefijos: trie O(|p|) vs scan O(n·|p|)",
        _hecho="""1. `autocomplete/DISENO.md` elige estructura con tabla de trade-offs y complejidad objetivo de query.
2. Alcance del dataset Agenda Ops (clientes/servicios) definido.
3. Commit `docs(m08): diseno autocomplete`.""",
        _errores="""- Elegir trie “porque suena avanzado” sin dataset size.
- No definir operaciones (insert, suggest(prefix, k)).
- Diseñar API HTTP entera en vez del núcleo de búsqueda.""",
        siguiente="[L22 — Implementación trie o índice](L22-implementacion-trie-o-indice.md)",
        body=r"""
# L21 — Autocomplete: elección de estructura

**~5.0 h · Semana 6**

El proyecto une M08 con Agenda Ops: sugerencias rápidas de clientes/servicios.

## Objetivo

Dejar `autocomplete/DISENO.md` con decisión de estructura y complejidades objetivo.

## Pasos

### 1. Contexto producto (30 min)

Lee `curriculum/producto-saas.md` (Agenda Ops). Lista campos sugeribles: nombre cliente, nombre servicio.

### 2. Opciones (60 min)

Tabla en DISENO: scan lineal, array ordenado + binary search, trie, `Map` prefijo→lista. Pros/contras.

### 3. Decisión (50 min)

Elige **una** para implementar en L22. Justifica con tamaño demo (p. ej. 5k–50k strings) y k resultados.

### 4. API (40 min)

```ts
insert(term: string): void
suggest(prefix: string, k?: number): string[]
```

Más complejidad insert/query escritas.

### 5. Commit (15 min)

```bash
mkdir -p projects/m08-algoritmos/autocomplete
git add projects/m08-algoritmos/autocomplete
git commit -m "docs(m08): diseno autocomplete"
```
""",
    )
)

# ---------- L22 ----------
LESSONS.append(
    dict(
        id="L22",
        orden=22,
        titulo="Implementación trie o índice",
        horas=5.0,
        semana=6,
        lectura="Implementar la estructura elegida en L21",
        evidencia="autocomplete/ código + tests",
        _lectura_corta="Trie nodes / índice: insert y suggest correctos",
        _hecho="""1. Código en `autocomplete/` alineado al DISENO (trie u otra) con `insert`/`suggest`.
2. ≥5 tests: vacío, prefijo sin matches, prefijo corto, k limit, case policy documentada.
3. Commit `feat(m08): autocomplete estructura base`.""",
        _errores="""- Implementar otra estructura distinta al DISENO sin actualizarlo.
- Suggest O(n) silencioso cuando prometiste trie.
- Sin tests de k.""",
        siguiente="[L23 — Dataset Agenda Ops y demo CLI](L23-dataset-agenda-ops-y-demo-cli.md)",
        body=r"""
# L22 — Implementación trie o índice

**~5.0 h · Semana 6**

Hoy el diseño se vuelve código testeable.

## Objetivo

Implementar `insert`/`suggest` según `DISENO.md` con tests sólidos.

## Pasos

### 1. Esqueleto (30 min)

`autocomplete/src/index.ts` (o `trie.ts`) exportando la API acordada.

### 2. Insert (60 min)

Normaliza strings (lowercase trim — documenta). Inserta carácter a carácter si trie; o actualiza índice.

### 3. Suggest (70 min)

Baja al nodo prefijo; DFS/BFS recolectando hasta k. Si elegiste binary search sobre lista ordenada, implementa lower_bound.

### 4. Tests (50 min)

```bash
npm test
```

Incluye case folding según política.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): autocomplete estructura base"
```
""",
    )
)

# ---------- L23 ----------
LESSONS.append(
    dict(
        id="L23",
        orden=23,
        titulo="Dataset Agenda Ops y demo CLI",
        horas=5.0,
        semana=6,
        lectura="Dataset realista + CLI de demostración",
        evidencia="CSV/JSON demo + CLI",
        _lectura_corta="Cargar N términos; latencia de suggest en máquina local",
        _hecho="""1. Dataset `autocomplete/data/` (CSV o JSON) con clientes/servicios demo (≥100 filas; ideal ≥1000).
2. CLI `npx tsx autocomplete/cli.ts --prefix cor` (o similar) imprime sugerencias.
3. README autocomplete con comando y nota de latencia; commit `feat(m08): dataset y CLI autocomplete`.""",
        _errores="""- Dataset de 5 filas presentado como demo seria.
- CLI sin documentar en README.
- Medir latencia una sola vez con N minúscula y generalizar.""",
        siguiente="[L24 — Cierre M08 y evidencias](L24-cierre-m08-y-evidencias.md)",
        body=r"""
# L23 — Dataset Agenda Ops y demo CLI

**~5.0 h · Semana 6**

Sin datos y sin demo, el autocomplete no es evidencia de proyecto.

## Objetivo

Cargar un dataset tipo Agenda Ops y exponer un CLI reproducible.

## Pasos

### 1. Dataset (50 min)

`autocomplete/data/servicios.json` (o csv): nombres realistas (corte, barba, tinte…). Genera ≥100 entradas (script corto aceptable).

### 2. Loader (40 min)

Función `loadAndBuild(path)` inserta todos los términos.

### 3. CLI (70 min)

`autocomplete/cli.ts`:

```bash
npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json --prefix ti --k 5
```

### 4. Latencia (40 min)

Cronometra suggest en frío/caliente; pega ms en `autocomplete/README.md` junto a N y estructura.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/autocomplete
git commit -m "feat(m08): dataset y CLI autocomplete"
```
""",
    )
)

# ---------- L24 ----------
LESSONS.append(
    dict(
        id="L24",
        orden=24,
        titulo="Cierre M08 y evidencias",
        horas=5.0,
        semana=6,
        lectura="Checklist P1–P3 + proyecto; índice ≥15",
        evidencia="checklist + indice ≥15",
        _lectura_corta="Autoevaluación: explicar un medio de arrays/hash en voz alta",
        _hecho="""1. `indice-patrones.md` con **≥15** entradas; checklist en `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
2. `npm test` verde; autocomplete documentado enlazado desde README raíz.
3. Commit `docs(m08): cierre materia y evidencias`.""",
        _errores="""- Índice inflado con filas vacías.
- Marcar P3 sin tres DP.
- Autocomplete sin complejidad de query.""",
        siguiente="M08 cerrado — siguiente materia: [M09 · Bases de datos](../M09-bases-de-datos.md)",
        body=r"""
# L24 — Cierre M08 y evidencias

**~5.0 h · Semana 6**

Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y autocomplete.

## Objetivo

Completar índice ≥15, checklist de dominio y dejar el README raíz como mapa de evidencias.

## Pasos

### 1. Contar problemas (40 min)

```bash
find problems -name 'enunciado.md' | wc -l
```

Si <15, añade los faltantes hoy (plantilla corta) o recupera de semanas previas mal indexados.

### 2. Checklist (60 min)

`bitacora/cierre-m08.md` con rutas:

- P1 índice ≥15
- P2 `sorts/README.md`
- P3 `dp/` ×3
- Proyecto `autocomplete/` + DISENO + CLI

### 3. Dominio oral (40 min)

Outline escrito: resuelve two-sum / ventana en voz alta con complejidad.

### 4. Regresión (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): cierre materia y evidencias"
```
""",
    )
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(LESSONS) == 24, len(LESSONS)
    for lesson in LESSONS:
        path = OUT / FILENAMES[lesson["orden"]]
        text = render(lesson)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
