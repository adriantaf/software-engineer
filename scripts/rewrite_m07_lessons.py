#!/usr/bin/env python3
"""Rewrite M07 lessons to M01/M09 quality (concrete timed steps, no boilerplate)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M07"
BIBLIO = "../../../bibliografia.md#m07-estructuras-de-datos"
JOYANES = "Joyanes / texto univ. ED (ed. ES)"
MDN_MAP = "https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map"
VISUALGO = "https://visualgo.net/en/list"


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


def lectura_block(que, enlace_titulo="MDN Map (contraste)", enlace=MDN_MAP):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {JOYANES} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07]({BIBLIO}) |
"""


def render(lesson: dict) -> str:
    pub = {
        "id": lesson["id"],
        "materia": "M07",
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
    }
    hecho = lesson["_hecho"].strip()
    errores = lesson["_errores"].strip()
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(lesson.get("_lectura_corta", lesson["lectura"]), **lesson.get("_enlace", {}))}

## Hecho cuando

Marca la lección **solo si**:

{hecho}

## Errores comunes

{errores}

## Siguiente

{lesson["siguiente"]}
"""


FILENAMES = {
    1: "L01-entorno-del-proyecto-y-arrays-dinamicos.md",
    2: "L02-lista-enlazada-simple.md",
    3: "L03-lista-doble-y-operaciones-indexadas.md",
    4: "L04-secuencias-repaso-de-costos-y-cierre-semana-1.md",
    5: "L05-pila-stack-tipada.md",
    6: "L06-cola-queue-y-cola-circular.md",
    7: "L07-deque-y-casos-de-uso.md",
    8: "L08-pilas-colas-y-cierre-p1-parcial.md",
    9: "L09-funcion-hash-y-mapa-conceptual.md",
    10: "L10-tabla-hash-con-encadenamiento.md",
    11: "L11-factor-de-carga-y-rehash.md",
    12: "L12-hash-vs-map-nativo-p1-cierre.md",
    13: "L13-bst-insercion-y-busqueda.md",
    14: "L14-recorridos-inorder-preorder-postorder.md",
    15: "L15-bst-minimo-maximo-y-sucesor.md",
    16: "L16-visualizacion-y-p2-parcial.md",
    17: "L17-modelo-de-heap-binario.md",
    18: "L18-heap-minimo-insert-y-extractmin.md",
    19: "L19-cola-de-prioridad.md",
    20: "L20-heap-vs-bst-para-prioridades.md",
    21: "L21-grafos-repaso-y-representacion.md",
    22: "L22-benchmark-p3-nativo-vs-propio.md",
    23: "L23-readme-cuando-usar-cada-estructura.md",
    24: "L24-cierre-m07-y-evidencias.md",
}

LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Entorno del proyecto y arrays dinámicos",
        horas=5.0,
        semana=1,
        lectura="Arrays estáticos/dinámicos, capacidad y costo amortizado de push",
        evidencia="projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests",
        _lectura_corta="Arrays estáticos vs dinámicos; crecimiento ×2 y amortizado",
        _enlace={"enlace_titulo": "VisuAlgo · Array", "enlace": "https://visualgo.net/en/array"},
        _hecho="""1. `projects/m07-estructuras/` tiene `package.json` con script `test` (Vitest) y `tsc` strict.
2. `src/dynamic-array.ts` implementa capacidad, `get`, `push` con resize ×2; ≥5 tests verdes.
3. `COMPLEJIDAD.md` documenta O(1) acceso y O(1) amortizado `push`; commit `feat(m07): dynamic array con tests`.""",
        _errores="""- Envolver `T[]` nativo y llamarlo “dynamic array” sin capacidad propia.
- No tener un test que dispare el redimensionamiento.
- Dejar `strict: false` o sin script `test`.""",
        siguiente="[L02 — Lista enlazada simple](L02-lista-enlazada-simple.md)",
        body=r"""
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
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Lista enlazada simple",
        horas=5.0,
        semana=1,
        lectura="Listas enlazadas singulares: head/tail, inserción y búsqueda",
        evidencia="SinglyLinkedList con insert head/tail, find, 5 tests",
        _lectura_corta="Listas simples: nodos, head/tail, costos de insert/find",
        _enlace={"enlace_titulo": "VisuAlgo · Linked List", "enlace": VISUALGO},
        _hecho="""1. `src/singly-linked-list.ts` con `prepend`, `append`, `find`, `toArray` y ≥5 tests verdes.
2. `COMPLEJIDAD.md` compara inserción en cabeza lista vs array.
3. Commit `feat(m07): lista enlazada simple`.""",
        _errores="""- Perder la referencia a `head` al hacer `prepend`.
- `append` O(n²) sin `tail` y sin documentarlo.
- Tests que solo insertan y nunca buscan.""",
        siguiente="[L03 — Lista doble y operaciones indexadas](L03-lista-doble-y-operaciones-indexadas.md)",
        body=r"""
# L02 — Lista enlazada simple

**~5.0 h · Semana 1**

Pasas de índices contiguos a nodos enlazados: trade-off memoria vs inserción en cabeza.

## Objetivo

Implementar `SinglyLinkedList<T>` con `prepend`/`append`/`find` y contrastar costos con `DynamicArray` en `COMPLEJIDAD.md`.

## Pasos

### 1. Dibuja antes de codificar (20 min)

En papel o Mermaid: lista vacía → prepend A → append B → find C (ausente). Anota qué punteros cambian.

### 2. Nodo y API (70–80 min)

`src/singly-linked-list.ts`:

```ts
class Node<T> {
  constructor(public value: T, public next: Node<T> | null = null) {}
}
```

Métodos: `prepend`, `append` (guarda `tail` si puedes), `find`, `get size`, `toArray()`.

### 3. Cinco tests (60 min)

Vacía; prepend múltiple (orden LIFO en cabeza); append mantiene orden; `find` ausente; `toArray` coherente tras mezcla prepend/append.

```bash
cd projects/m07-estructuras && npm test
```

### 4. Comparación escrita (40 min)

Añade fila a `COMPLEJIDAD.md`: inserción O(1) en cabeza vs O(n) mover elementos en array; búsqueda O(n) en ambos.

### 5. Commit (15 min)

```bash
git add projects/m07-estructuras
git commit -m "feat(m07): lista enlazada simple"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Lista doble y operaciones indexadas",
        horas=5.0,
        semana=1,
        lectura="Listas dobles: prev/next, borrado e indexación lineal",
        evidencia="DoublyLinkedList + deleteByValue; tests de borde",
        _lectura_corta="Listas doblemente enlazadas; borrado O(1) con nodo conocido",
        _enlace={"enlace_titulo": "VisuAlgo · Linked List", "enlace": VISUALGO},
        _hecho="""1. `src/doubly-linked-list.ts` con `append`, `deleteByValue` (o por nodo) y `at(i)` documentado O(n).
2. ≥5 tests: vacío, un nodo, borrar cabeza/cola/medio, índice inválido.
3. Commit `feat(m07): lista doble e indexada`.""",
        _errores="""- Olvidar actualizar `prev` al borrar.
- Prometer acceso O(1) por índice en lista enlazada.
- Dejar `tail` huérfano tras borrar el último.""",
        siguiente="[L04 — Secuencias: repaso de costos y cierre semana 1](L04-secuencias-repaso-de-costos-y-cierre-semana-1.md)",
        body=r"""
# L03 — Lista doble y operaciones indexadas

**~5.0 h · Semana 1**

Con `prev` y `next` el borrado deja de ser un recorrido ciego desde `head` si ya tienes el nodo.

## Objetivo

Implementar `DoublyLinkedList<T>` con borrado por valor y acceso indexado lineal (`at(i)`), documentando que el índice **no** es O(1).

## Pasos

### 1. Lectura + sketch (40 min)

Capítulo de listas dobles. Dibuja borrado de nodo intermedio (4 punteros).

### 2. Implementación (90 min)

`src/doubly-linked-list.ts`: nodos con `prev`/`next`; `append`; `deleteByValue(v)` (o `delete(node)`); `at(i)` que recorre desde head (o desde el extremo más cercano si quieres bonus).

### 3. Tests de borde (60 min)

Borrar de lista vacía; borrar único nodo (head=tail=null); borrar cabeza; borrar cola; `at(-1)` / fuera de rango.

### 4. Documenta indexación (30 min)

En `COMPLEJIDAD.md`: `at(i)` es O(n). Una frase: “si necesitas índice frecuente, usa array”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): lista doble e indexada"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Secuencias: repaso de costos y cierre semana 1",
        horas=5.0,
        semana=1,
        lectura="Repaso arrays vs listas: cuándo cada una",
        evidencia="COMPLEJIDAD.md completo semana 1 + bitácora semana",
        _lectura_corta="Trade-offs arrays vs listas (tiempo y memoria)",
        _hecho="""1. `COMPLEJIDAD.md` tiene tabla comparativa array / lista simple / lista doble para insert head, append, acceso, delete.
2. Existe `bitacora/semana-01.md` (o sección en README) con 5–8 líneas de lo aprendido.
3. Suite `npm test` verde; commit `docs(m07): cierre semana 1 secuencias`.""",
        _errores="""- Tabla de costos inventada sin mirar tu código.
- Cerrar la semana con tests en rojo.
- Bitácora vacía o solo “terminé las lecciones”.""",
        siguiente="[L05 — Pila (Stack) tipada](L05-pila-stack-tipada.md)",
        body=r"""
# L04 — Secuencias: repaso de costos y cierre semana 1

**~5.0 h · Semana 1**

Cierras la semana de secuencias dejando una tabla defendible y la suite verde.

## Objetivo

Completar `COMPLEJIDAD.md` para array y listas, escribir bitácora de semana 1 y dejar tests verdes.

## Pasos

### 1. Auditoría de código (45 min)

```bash
cd projects/m07-estructuras
find src -name '*.ts' | sort
npm test
```

Anota gaps (métodos sin test, Big-O faltante).

### 2. Tabla unificada (75 min)

En `COMPLEJIDAD.md`, una tabla con columnas: operación | DynamicArray | Singly | Doubly. Filas: acceso, insert head, append, delete por valor, memoria extra por elemento.

### 3. Mini experimento (60 min)

Script `bench/sequences-smoke.ts` (o test de timing informal): 10_000 prepends en lista vs unshift en array nativo. Pega 3 números en la bitácora (no hace falta microbenchmark serio aún).

### 4. Bitácora (40 min)

```bash
mkdir -p bitacora
```

`bitacora/semana-01.md`: qué estructura elegirías para cola de impresión vs buffer de edición, en 2 frases cada una.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 1 secuencias"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Pila (Stack) tipada",
        horas=5.0,
        semana=2,
        lectura="Pilas LIFO: push, pop, peek e invariantes",
        evidencia="Stack<T> con push/pop/peek + 4 tests (inicio P1)",
        _lectura_corta="Pila LIFO; aplicaciones (paréntesis, undo)",
        _hecho="""1. `src/stack.ts` tipado con `push`/`pop`/`peek`/`isEmpty`; ≥4 tests verdes.
2. Un ejercicio (paréntesis o undo de 3 comandos) en `src/exercises/balanced.ts` o test dedicado.
3. Commit `feat(m07): stack tipado`.""",
        _errores="""- Exponer el array interno mutable.
- `pop` en vacío sin definir comportamiento (throw vs undefined).
- Implementar “pila” sin tests de LIFO.""",
        siguiente="[L06 — Cola (Queue) y cola circular](L06-cola-queue-y-cola-circular.md)",
        body=r"""
# L05 — Pila (Stack) tipada

**~5.0 h · Semana 2**

LIFO es la base de undo, parsers y DFS. Hoy la implementas tipada y la usas en un ejercicio corto.

## Objetivo

Entregar `Stack<T>` con API mínima, tests LIFO y un caso de uso (paréntesis balanceados o undo).

## Pasos

### 1. Lectura (30 min)

Sección de pilas en tu texto ED. Anota precondiciones de `pop`/`peek`.

### 2. Implementación (60 min)

`src/stack.ts` — puedes basarte en array **privado** o en tu lista; no reexportes mutadores internos.

```ts
export class Stack<T> {
  push(x: T): void
  pop(): T          // o T | undefined — documenta
  peek(): T
  get size(): number
  isEmpty(): boolean
}
```

### 3. Tests LIFO (45 min)

Push A,B,C → pop C,B,A; peek no modifica size; pop vacío; size tras N operaciones.

### 4. Ejercicio (70 min)

`src/exercises/balanced.ts`: `isBalanced(s: string): boolean` usando `Stack<string>`. Tests: `()`, `([]){}`, `([)]`, vacío, `(((`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): stack tipado"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Cola (Queue) y cola circular",
        horas=5.0,
        semana=2,
        lectura="Colas FIFO; cola circular con buffer fijo",
        evidencia="Queue<T> + tests; opcional CircularQueue",
        _lectura_corta="Cola FIFO; buffer circular head/tail",
        _hecho="""1. `src/queue.ts` con `enqueue`/`dequeue`/`front` y ≥4 tests FIFO.
2. `src/circular-queue.ts` (o sección en el mismo archivo) con capacidad fija y overflow definido.
3. Commit `feat(m07): queue y cola circular`.""",
        _errores="""- Usar `Array.shift` sin documentar O(n) (si lo usas, dilo y prefiere head index o lista).
- Circular: confundir “lleno” y “vacío” sin sentinel o size.
- Tests solo enqueue sin dequeue.""",
        siguiente="[L07 — Deque y casos de uso](L07-deque-y-casos-de-uso.md)",
        body=r"""
# L06 — Cola (Queue) y cola circular

**~5.0 h · Semana 2**

FIFO alimenta BFS y buffers de trabajo. La cola circular evita desplazamientos en un buffer fijo.

## Objetivo

Implementar `Queue<T>` correcta en costos y una `CircularQueue` de capacidad fija con política de overflow explícita.

## Pasos

### 1. Queue lineal (70 min)

`src/queue.ts`: `enqueue`, `dequeue`, `front`/`peek`, `size`. Preferible lista con head/tail o índices sobre buffer — **no** `shift` silencioso O(n) sin nota.

### 2. Tests FIFO (40 min)

Orden de salida; vacía; un elemento; secuencia enqueue/dequeue intercalada.

### 3. CircularQueue (80 min)

`src/circular-queue.ts`: capacidad N; índices `head`/`tail` módulo N; distingue lleno vs vacío (`size` o slot sentinela). Overflow: throw o return false — elige y documéntalo en JSDoc.

### 4. Tests circulares (40 min)

Llenar hasta capacidad; overflow; vaciar tras wrap-around (enqueue que da la vuelta al buffer).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): queue y cola circular"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Deque y casos de uso",
        horas=5.0,
        semana=2,
        lectura="Deque: inserción/borrado en ambos extremos",
        evidencia="Deque mínimo o cola doble + 3 tests",
        _lectura_corta="Deque / cola doble extremos",
        _hecho="""1. `src/deque.ts` con `pushFront`/`pushBack`/`popFront`/`popBack` (o nombres equivalentes).
2. ≥3 tests + un caso de uso escrito (sliding window / undo-redo / palíndromo).
3. Commit `feat(m07): deque y ejercicio`.""",
        _errores="""- Deque que solo envuelve dos stacks sin documentar costos amortizados.
- Olvidar actualizar size en un extremo.
- Caso de uso genérico (“sirve para todo”) sin ejemplo concreto.""",
        siguiente="[L08 — Pilas, colas y cierre P1 parcial](L08-pilas-colas-y-cierre-p1-parcial.md)",
        body=r"""
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
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Pilas, colas y cierre P1 parcial",
        horas=5.0,
        semana=2,
        lectura="Repaso LIFO/FIFO y checklist P1 parcial",
        evidencia="README sección LIFO/FIFO + bitácora semana 2",
        _lectura_corta="Cuándo pila vs cola vs deque",
        _hecho="""1. README tiene sección “LIFO / FIFO / Deque” con cuándo usar cada una (tabla o bullets).
2. `bitacora/semana-02.md` + `npm test` verde para stack/queue/deque.
3. Commit `docs(m07): cierre semana 2 pilas y colas`.""",
        _errores="""- README genérico sin mencionar tus archivos `src/*.ts`.
- Dejar ejercicios de paréntesis rotos.
- Marcar P1 “parcial” sin lista/pila/cola presentes.""",
        siguiente="[L09 — Función hash y mapa conceptual](L09-funcion-hash-y-mapa-conceptual.md)",
        body=r"""
# L08 — Pilas, colas y cierre P1 parcial

**~5.0 h · Semana 2**

P1 pide lista, pila, cola y hash. Hoy cierras la mitad LIFO/FIFO con documentación clara.

## Objetivo

Dejar documentado el uso de stack/queue/deque, bitácora de semana 2 y suite verde antes de hash.

## Pasos

### 1. Checklist de archivos (30 min)

```bash
ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
npm test
```

Arregla fallos antes de documentar.

### 2. Sección README (75 min)

Añade tabla: estructura | orden | ops tipicas | ejemplo producto (Agenda Ops: undo de cita, cola de espera, etc.).

### 3. Export barrel (45 min)

`src/index.ts` reexporta Stack, Queue, Deque, listas, DynamicArray. Verifica `npm run build` si tienes `tsc`.

### 4. Bitácora (40 min)

`bitacora/semana-02.md`: un bug que cazaste (p. ej. circular lleno/vacío) y cómo lo viste en un test.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 2 pilas y colas"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Función hash y mapa conceptual",
        horas=5.0,
        semana=3,
        lectura="Funciones hash, universo de claves y colisiones",
        evidencia="Hash notes + función hash string→number con tests deterministas",
        _lectura_corta="Hash: distribución, colisiones, por qué no usar solo key.length",
        _hecho="""1. `src/hash/fnv1a.ts` (o similar) hash string→uint32 determinista con ≥4 tests fijos.
2. `docs/hash-notes.md` explica colisión y por qué modulo tabla.
3. Commit `feat(m07): funcion hash string`.""",
        _errores="""- Hash no determinista (usa Date/random).
- Confundir “buen hash” con “encriptación”.
- Tests que solo chequean “es un número” sin valores esperados.""",
        siguiente="[L10 — Tabla hash con encadenamiento](L10-tabla-hash-con-encadenamiento.md)",
        body=r"""
# L09 — Función hash y mapa conceptual

**~5.0 h · Semana 3**

Sin una función hash defendible, la tabla de la próxima lección es decorado.

## Objetivo

Implementar un hash string→número determinista, documentar colisiones y dejar tests con valores esperados fijos.

## Pasos

### 1. Lectura (45 min)

Capítulo de tablas hash: universo, colisión, preferencia por distribución uniforme. Anota 5 términos en `docs/hash-notes.md`.

### 2. Implementa FNV-1a (u otra simple) (75 min)

```bash
mkdir -p src/hash
```

`src/hash/fnv1a.ts`: `hashString(s: string): number` (uint32). Misma entrada → misma salida siempre.

### 3. Tests deterministas (50 min)

```ts
expect(hashString("")).toBe(/* valor fijo */)
expect(hashString("agenda")).toBe(/* ... */)
expect(hashString("Agenda")).not.toBe(hashString("agenda")) // si tu fn es case-sensitive
```

Incluye dos strings distintos que colisionen **módulo 8** (búsqueda corta o documenta el par).

### 4. Notas de diseño (40 min)

En `docs/hash-notes.md`: dibuja “clave → hash → índice = h % m”. Una frase sobre por qué `m` primo o potencia de 2 (elige postura y justifica).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): funcion hash string"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Tabla hash con encadenamiento",
        horas=5.0,
        semana=3,
        lectura="Encadenamiento (chaining): buckets y listas",
        evidencia="HashMapChaining con set/get/delete + load factor logged",
        _lectura_corta="Hash map con encadenamiento; set/get/delete",
        _hecho="""1. `src/hash-map.ts` con `set`/`get`/`delete`/`has` y buckets por encadenamiento.
2. Tests cubren overwrite, delete, get ausente; logueas o expones `loadFactor`.
3. Commit `feat(m07): hashmap encadenamiento`.""",
        _errores="""- Open addressing sin decirlo (esta lección es chaining).
- No manejar update de clave existente.
- Usar `Map` nativo por dentro y llamarlo implementación propia.""",
        siguiente="[L11 — Factor de carga y rehash](L11-factor-de-carga-y-rehash.md)",
        body=r"""
# L10 — Tabla hash con encadenamiento

**~5.0 h · Semana 3**

Cada bucket es una lista (o array) de pares clave-valor. Hoy montas el mapa usable.

## Objetivo

Entregar `HashMap<K,V>` (string keys al inicio está bien) con encadenamiento, API set/get/delete y `loadFactor` visible.

## Pasos

### 1. Diseño de buckets (30 min)

Escribe en `docs/hash-notes.md` la forma de cada entrada `{ key, value }` y cómo resuelves igualdad de claves.

### 2. Implementación (100 min)

`src/hash-map.ts`: array de buckets (capacidad inicial 8 o 16); `set` inserta o actualiza; `get`/`has`; `delete` remueve de la cadena; getter `loadFactor = size/capacity`.

### 3. Tests (60 min)

set+get; overwrite; delete + get undefined; has false; varias claves en mismo bucket (usa el par colisionante de L09 o fuerza módulo pequeño en test).

### 4. Smoke manual (20 min)

```bash
npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."
```

O un test de integración corto.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): hashmap encadenamiento"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Factor de carga y rehash",
        horas=5.0,
        semana=3,
        lectura="Load factor, umbral y rehashing",
        evidencia="Rehash al superar umbral; tests que fuerzan resize",
        _lectura_corta="Load factor α; cuándo rehash; costo amortizado",
        _hecho="""1. Rehash automático al superar umbral (p. ej. α > 0.75) duplicando capacidad.
2. Test que inserta hasta forzar ≥1 resize y verifica gets posteriores.
3. Commit `feat(m07): hashmap rehash por load factor`.""",
        _errores="""- Rehash que no re-inserta (solo crece el array vacío).
- Umbral nunca documentado.
- Tests que no provocan resize.""",
        siguiente="[L12 — Hash vs Map nativo (P1 cierre)](L12-hash-vs-map-nativo-p1-cierre.md)",
        body=r"""
# L11 — Factor de carga y rehash

**~5.0 h · Semana 3**

Sin rehash, el encadenamiento degenera a listas largas y pierdes el O(1) promedio.

## Objetivo

Hacer que tu `HashMap` redimensione al cruzar un umbral de load factor y probarlo con un test que fuerce el resize.

## Pasos

### 1. Define umbral (20 min)

Constante `MAX_LOAD = 0.75` (o la de tu texto). Documéntala en JSDoc y `COMPLEJIDAD.md`.

### 2. `_rehash(newCap)` (90 min)

Nuevo array de buckets; reinserta **todas** las entradas con el nuevo módulo; actualiza capacity/size. Llámalo desde `set` cuando `size/capacity > MAX_LOAD`.

### 3. Test de resize (60 min)

Capacidad inicial pequeña (4). Inserta 10 claves distintas; assert capacity ≥ 8 (o la esperada); todos los `get` siguen correctos; loadFactor ≤ MAX_LOAD tras rehash.

### 4. Nota amortizada (40 min)

Párrafo en `COMPLEJIDAD.md`: costo de rehash O(n) puntual, O(1) amortizado por insert si creces ×2.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): hashmap rehash por load factor"
```
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Hash vs Map nativo (P1 cierre)",
        horas=5.0,
        semana=3,
        lectura="Contraste implementación propia vs Map/Set nativos",
        evidencia="P1 completa: lista,pila,cola,hash + tabla comparativa nativo",
        _lectura_corta="Cuándo usar Map nativo vs hash propio (aprendizaje vs prod)",
        _hecho="""1. Checklist P1: lista, pila, cola, hash con tests verdes.
2. Tabla en README o `COMPLEJIDAD.md`: tu HashMap vs `Map` (ops, cuándo usar cada uno).
3. Commit `docs(m07): cierre P1 hash vs Map nativo`.""",
        _errores="""- Declarar P1 completa sin hash con rehash.
- Tabla que diga “el mío es más rápido” sin medir ni contextualizar aprendizaje.
- Olvidar exportar HashMap en `src/index.ts`.""",
        siguiente="[L13 — BST: inserción y búsqueda](L13-bst-insercion-y-busqueda.md)",
        body=r"""
# L12 — Hash vs Map nativo (P1 cierre)

**~5.0 h · Semana 3**

P1 cierra aquí: estructuras básicas propias + honestidad frente a `Map`.

## Objetivo

Verificar evidencia P1 completa y documentar cuándo usarías `Map` nativo en producción frente a tu hash de aprendizaje.

## Pasos

### 1. Checklist automático (40 min)

```bash
cd projects/m07-estructuras
npm test
ls src/singly-linked-list.ts src/stack.ts src/queue.ts src/hash-map.ts
```

Arregla cualquier rojo.

### 2. Microbench informal (70 min)

`bench/hash-vs-map.ts`: N=50_000 set/get en tu HashMap vs `Map`. Imprime ms. **No** concluyas superioridad absoluta; anota que V8 está altamente optimizado.

### 3. Tabla comparativa (50 min)

README sección “P1 — Hash vs Map”: API, orden de claves, uso recomendado (prod → Map; curso → propio para entender colisiones).

### 4. Bitácora semana 3 (30 min)

`bitacora/semana-03.md`: una colisión real que viste y cómo el chaining la resolvió.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre P1 hash vs Map nativo"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="BST: inserción y búsqueda",
        horas=5.0,
        semana=4,
        lectura="Árboles binarios de búsqueda: invariante e insert/contains",
        evidencia="BST insert/contains + tests ordenados",
        _lectura_corta="BST: hijo izq < nodo < der; insert y search",
        _enlace={"enlace_titulo": "VisuAlgo · BST", "enlace": "https://visualgo.net/en/bst"},
        _hecho="""1. `src/bst.ts` con `insert` y `contains` respetando invariante BST.
2. ≥5 tests (vacío, cadena ordenada, duplicado definido, contains true/false).
3. Commit `feat(m07): bst insert y contains`.""",
        _errores="""- Insertar sin respetar orden (rompe invariante).
- Duplicados silenciosos sin política (ignorar / contar / throw).
- Confundir BST con heap.""",
        siguiente="[L14 — Recorridos inorder, preorder, postorder](L14-recorridos-inorder-preorder-postorder.md)",
        body=r"""
# L13 — BST: inserción y búsqueda

**~5.0 h · Semana 4**

P2 empieza con el invariante: izquierda < nodo < derecha.

## Objetivo

Implementar un BST de números (o `T` comparable) con `insert` y `contains`, más tests que demuestren el orden.

## Pasos

### 1. Lectura + VisuAlgo (40 min)

Inserta la secuencia 8,3,10,1,6 en VisuAlgo BST. Copia el dibujo a `docs/bst-semana4.md`.

### 2. Nodos e insert (90 min)

`src/bst.ts`:

```ts
class BstNode { left: BstNode | null; right: BstNode | null; constructor(public key: number) {} }
export class BST { insert(key: number): void; contains(key: number): boolean }
```

Define política de duplicados en un comentario de una línea.

### 3. Tests (60 min)

Vacío contains false; insert uno; secuencia 8,3,10,1,6 contains todos; ausente; duplicado según política.

### 4. Complejidad (20 min)

`COMPLEJIDAD.md`: O(h) con h altura; peor caso cadena O(n).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst insert y contains"
```
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="Recorridos inorder, preorder, postorder",
        horas=5.0,
        semana=4,
        lectura="Recorridos de árbol: inorden, preorden, postorden",
        evidencia="Tres recorridos + snapshots en tests",
        _lectura_corta="Inorder ordena claves BST; pre/post usos",
        _enlace={"enlace_titulo": "VisuAlgo · BST", "enlace": "https://visualgo.net/en/bst"},
        _hecho="""1. Métodos `inorder`, `preorder`, `postorder` que devuelven `number[]` (o visitor).
2. Tests con snapshot de la secuencia 8,3,10,1,6 (inorder = ordenado).
3. Commit `feat(m07): bst recorridos`.""",
        _errores="""- Inorder que no queda ordenado → invariante roto en insert.
- Recorridos mutando el árbol.
- Solo implementar inorder y fingir los otros.""",
        siguiente="[L15 — BST: mínimo, máximo y sucesor](L15-bst-minimo-maximo-y-sucesor.md)",
        body=r"""
# L14 — Recorridos inorder, preorder, postorder

**~5.0 h · Semana 4**

Inorder en un BST es el sorted dump. Preorden y postorden aparecen en serialización y borrado de directorios.

## Objetivo

Exponer tres recorridos con tests de snapshot sobre un árbol fijo.

## Pasos

### 1. Repaso teórico (25 min)

Escribe en `docs/bst-semana4.md` una línea por recorrido: orden de visita.

### 2. Implementación recursiva (70 min)

En `src/bst.ts`: `inorder()`, `preorder()`, `postorder()` → arrays. Opcional: versión iterativa bonus.

### 3. Tests snapshot (60 min)

Árbol 8,3,10,1,6,14,4:

- inorder: `[1,3,4,8,10,14]` (ajusta si tu set difiere)
- preorder / postorder según tu dibujo VisuAlgo

### 4. Uso didáctico (40 min)

Función `toSortedArray()` = inorder. Test de propiedad: insertar permutación y sorted es el mismo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst recorridos"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="BST: mínimo, máximo y sucesor",
        horas=5.0,
        semana=4,
        lectura="Extremos y sucesor en BST; borrado de hoja intro",
        evidencia="min/max/delete leaf intro",
        _lectura_corta="Min/max por rama; sucesor; borrar hoja y un hijo",
        _hecho="""1. `min()`, `max()` y al menos borrado de hoja (y preferible nodo con un hijo).
2. Tests para min/max en árbol no vacío y delete que mantiene invariante (inorder coherente).
3. Commit `feat(m07): bst min max delete hoja`.""",
        _errores="""- Borrar sin reenlazar padres.
- Sucesor mal calculado (olvidar el subárbol derecho).
- Dejar tests sin verificar inorder tras delete.""",
        siguiente="[L16 — Visualización y P2 parcial](L16-visualizacion-y-p2-parcial.md)",
        body=r"""
# L15 — BST: mínimo, máximo y sucesor

**~5.0 h · Semana 4**

Min/max son caminatas a izquierda/derecha. El borrado completo puede esperar; hoy hojas y un hijo.

## Objetivo

Añadir `min`/`max`, opcional `successor`, y `delete` al menos para hojas (ideal: también un solo hijo).

## Pasos

### 1. Min/max (40 min)

Implementa y testa árbol vacío (throw o undefined) y árbol con varios nodos.

### 2. Sucesor (50 min)

Documenta algoritmo: si hay derecho, min del subárbol; si no, sube por padres (si guardas `parent`) o re-busca desde root. Test con claves conocidas.

### 3. Delete hoja / un hijo (90 min)

Implementa casos 0 y 1 hijo. Caso 2 hijos puede quedar como TODO documentado si te falta tiempo — dilo en README P2.

### 4. Tests de invariante (40 min)

Tras deletes, `inorder()` sigue ordenado y `contains` del borrado es false.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst min max delete hoja"
```
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Visualización y P2 parcial",
        horas=5.0,
        semana=4,
        lectura="Serializar árbol para depuración; cierre P2 parcial",
        evidencia="export traverse a string + README P2",
        _lectura_corta="Debug visual de BST; checklist P2",
        _hecho="""1. `format()` o `toString()` del BST legible (líneas o Mermaid).
2. README sección P2 con API BST + estado de delete (qué casos cubres).
3. Commit `docs(m07): cierre P2 parcial BST`.""",
        _errores="""- Visualización que no corresponde al árbol real.
- Marcar P2 “hecho” sin recorridos.
- README sin enlazar `src/bst.ts`.""",
        siguiente="[L17 — Modelo de heap binario](L17-modelo-de-heap-binario.md)",
        body=r"""
# L16 — Visualización y P2 parcial

**~5.0 h · Semana 4**

Cierras P2 parcial dejando el BST inspeccionable y documentado.

## Objetivo

Exportar una representación textual/Mermaid del árbol y actualizar el README de P2 con la API.

## Pasos

### 1. Formatter (70 min)

`format(node): string` indentado por profundidad, o generador Mermaid `graph TD`. Test: árbol pequeño produce string estable (snapshot).

### 2. README P2 (60 min)

Sección “P2 — BST”: métodos, política de duplicados, límites del delete, ejemplo de uso de 10 líneas.

### 3. Suite verde (40 min)

```bash
npm test
```

Añade test de regresión si encontraste un bug al formatear.

### 4. Bitácora semana 4 (30 min)

`bitacora/semana-04.md`: peor caso del BST (datos ordenados) y qué estructura usarías en su lugar (AVL/hash) — una frase.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre P2 parcial BST"
```
""",
    )
)

# ---------- L17 ----------
LESSONS.append(
    dict(
        id="L17",
        orden=17,
        titulo="Modelo de heap binario",
        horas=5.0,
        semana=5,
        lectura="Heap binario como array: índices padre/hijos",
        evidencia="array-backed heap model + heapifyUp/Down",
        _lectura_corta="Heap shape + heap property; índices 2i+1 / 2i+2",
        _enlace={"enlace_titulo": "VisuAlgo · Heap", "enlace": "https://visualgo.net/en/heap"},
        _hecho="""1. Módulo con helpers `parent`/`left`/`right` y `heapifyUp`/`heapifyDown` sobre array.
2. Tests unitarios de índices y de un heapify sobre array casi-heap.
3. Commit `feat(m07): modelo heap binario`.""",
        _errores="""- Confundir índices 0-based y 1-based.
- Heapify que no restaura la propiedad.
- Tratar el heap como BST ordenado inorder.""",
        siguiente="[L18 — Heap mínimo: insert y extractMin](L18-heap-minimo-insert-y-extractmin.md)",
        body=r"""
# L17 — Modelo de heap binario

**~5.0 h · Semana 5**

El heap vive en un array: padre en `(i-1)>>1`, hijos `2i+1` y `2i+2`.

## Objetivo

Codificar el modelo (índices + heapify up/down) antes de la API insert/extractMin.

## Pasos

### 1. VisuAlgo + notas (40 min)

Observa un min-heap. En `docs/heap.md` escribe la propiedad de heap y la forma completa de niveles.

### 2. Helpers (50 min)

`src/heap-model.ts`:

```ts
export const parent = (i: number) => (i - 1) >> 1
export const left = (i: number) => 2 * i + 1
export const right = (i: number) => 2 * i + 2
```

Tests de índices 0..10.

### 3. heapifyUp / heapifyDown (90 min)

Funciones que mutan `number[]` asumiendo min-heap. Casos de prueba: subir una hoja menor que el padre; bajar una raíz mayor que un hijo.

### 4. Diagrama array↔árbol (30 min)

En `docs/heap.md`, tabla índice→valor para un heap de ejemplo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): modelo heap binario"
```
""",
    )
)

# ---------- L18 ----------
LESSONS.append(
    dict(
        id="L18",
        orden=18,
        titulo="Heap mínimo: insert y extractMin",
        horas=5.0,
        semana=5,
        lectura="Operaciones insert y extract-min en heap",
        evidencia="MinHeap operativo + tests",
        _lectura_corta="insert O(log n); extractMin O(log n); peek O(1)",
        _enlace={"enlace_titulo": "VisuAlgo · Heap", "enlace": "https://visualgo.net/en/heap"},
        _hecho="""1. `src/min-heap.ts` con `insert`, `extractMin`, `peek`, `size`.
2. ≥5 tests: orden de extracción, vacío, un elemento, secuencia aleatoria vs sort.
3. Commit `feat(m07): minheap insert extractMin`.""",
        _errores="""- extractMin sin heapifyDown.
- Insert solo con `push` al array sin subir.
- Tests que no verifican orden de salida.""",
        siguiente="[L19 — Cola de prioridad](L19-cola-de-prioridad.md)",
        body=r"""
# L18 — Heap mínimo: insert y extractMin

**~5.0 h · Semana 5**

Con el modelo listo, montas la estructura usable.

## Objetivo

Entregar `MinHeap` completo con insert/extractMin/peek y tests de orden.

## Pasos

### 1. Clase MinHeap (90 min)

`src/min-heap.ts` usa `heap-model.ts`. `insert`: push + heapifyUp. `extractMin`: swap root/último, pop, heapifyDown.

### 2. Tests (70 min)

Insertar `{5,3,8,1}` → extract 1,3,5,8; peek no muta; extract vacío; 100 random vs `[...].sort((a,b)=>a-b)`.

### 3. Complejidad (30 min)

Filas en `COMPLEJIDAD.md` para heap.

### 4. Export (20 min)

Reexporta desde `src/index.ts`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): minheap insert extractMin"
```
""",
    )
)

# ---------- L19 ----------
LESSONS.append(
    dict(
        id="L19",
        orden=19,
        titulo="Cola de prioridad",
        horas=5.0,
        semana=5,
        lectura="Priority queue sobre heap; API de tareas",
        evidencia="PriorityQueue API + 3 casos",
        _lectura_corta="PQ: enqueue con prioridad, dequeue del mínimo/máximo",
        _hecho="""1. `src/priority-queue.ts` genérica (prioridad numérica o comparator).
2. Tres casos de prueba de dominio (p. ej. turnos Agenda Ops: urgente < normal).
3. Commit `feat(m07): priority queue`.""",
        _errores="""- PQ que es solo un array sorted en cada insert sin decir O(n).
- Prioridades invertidas sin documentar (min vs max).
- Casos de prueba sin prioridades distintas.""",
        siguiente="[L20 — Heap vs BST para prioridades](L20-heap-vs-bst-para-prioridades.md)",
        body=r"""
# L19 — Cola de prioridad

**~5.0 h · Semana 5**

La PQ es la fachada del heap para el dominio (turnos, jobs, eventos).

## Objetivo

Envolver el MinHeap en `PriorityQueue<T>` con tres casos de uso testeados.

## Pasos

### 1. API (30 min)

```ts
enqueue(item: T, priority: number): void
dequeue(): T
peek(): T
```

Menor `priority` sale primero (documenta si inviertes).

### 2. Implementación (70 min)

Guarda `{ item, priority }` en el heap; compara por priority (tie-break opcional por orden de llegada).

### 3. Tres casos (70 min)

Tests: (1) turnos `{cliente, prioridad}`; (2) vaciar cola; (3) mismas prioridades — orden estable o documentado.

### 4. Nota de producto (30 min)

En README: cómo Agenda Ops usaría PQ para “siguiente en cola VIP”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): priority queue"
```
""",
    )
)

# ---------- L20 ----------
LESSONS.append(
    dict(
        id="L20",
        orden=20,
        titulo="Heap vs BST para prioridades",
        horas=5.0,
        semana=5,
        lectura="Trade-offs heap vs BST para colas de prioridad",
        evidencia="COMPLEJIDAD heap vs BST",
        _lectura_corta="Heap: mejor extract-min; BST: ordered scan / delete arbitrario",
        _hecho="""1. Sección en `COMPLEJIDAD.md` o `docs/heap-vs-bst.md` con tabla de ops.
2. Bitácora semana 5 con una decisión (“para scheduler usaría…”).
3. Commit `docs(m07): heap vs bst prioridades`.""",
        _errores="""- Decir que BST siempre es O(log n) sin hablar del peor caso degenerado.
- Afirmar que heap permite search arbitrario O(log n).
- Tabla sin ops concretas (insert/extract/search).""",
        siguiente="[L21 — Grafos: repaso y representación](L21-grafos-repaso-y-representacion.md)",
        body=r"""
# L20 — Heap vs BST para prioridades

**~5.0 h · Semana 5**

No todo “ordenado” necesita un árbol. Hoy eliges con tabla, no con intuición.

## Objetivo

Documentar trade-offs heap vs BST para prioridades y dejar una decisión escrita de diseño.

## Pasos

### 1. Tabla de operaciones (60 min)

Filas: insert, find-min, extract-min, delete arbitrario, sorted iterate. Columnas: MinHeap, BST, `Map`+sort (referencia).

### 2. Experimento mental / microbench (70 min)

Inserta N=10_000 prioridades y extrae N/2. Compara tu heap vs extraer min de un BST (si tienes min). Anota tiempos en la doc.

### 3. Decisión (40 min)

`docs/heap-vs-bst.md`: párrafo “En Agenda Ops para cola VIP usaría ___ porque ___”.

### 4. Bitácora (30 min)

`bitacora/semana-05.md`.

### 5. Commit (15 min)

```bash
git commit -am "docs(m07): heap vs bst prioridades"
```
""",
    )
)

# ---------- L21 ----------
LESSONS.append(
    dict(
        id="L21",
        orden=21,
        titulo="Grafos: repaso y representación",
        horas=5.0,
        semana=6,
        lectura="Grafos: lista de adyacencia vs matriz",
        evidencia="Adjacency list en TS reutilizable",
        _lectura_corta="Lista de adyacencia; dirigido vs no dirigido",
        _enlace={"enlace_titulo": "VisuAlgo · Graph", "enlace": "https://visualgo.net/en/graphds"},
        _hecho="""1. `src/graph.ts` con `addVertex`, `addEdge`, `neighbors`.
2. Tests: grafo pequeño no dirigido; edge bidireccional; vecino ausente.
3. Commit `feat(m07): grafo lista de adyacencia`.""",
        _errores="""- Matriz densa para grafo sparse sin justificar.
- Olvidar simetría en no dirigido.
- API sin tipos (arrays `any`).""",
        siguiente="[L22 — Benchmark P3: nativo vs propio](L22-benchmark-p3-nativo-vs-propio.md)",
        body=r"""
# L21 — Grafos: repaso y representación

**~5.0 h · Semana 6**

Repasas M03 con una API TypeScript reutilizable (base para M08 BFS/DFS).

## Objetivo

Implementar grafo por lista de adyacencia con tests claros.

## Pasos

### 1. Lectura corta (30 min)

Lista vs matriz: memoria y costo de `neighbors`. Elige lista para el curso.

### 2. API (80 min)

`src/graph.ts`:

```ts
export class Graph {
  addVertex(v: string): void
  addEdge(a: string, b: string, undirected = true): void
  neighbors(v: string): string[]
  vertices(): string[]
}
```

### 3. Tests (50 min)

Triángulo A-B-C; dirigido vs no dirigido; vértice aislado.

### 4. Ejemplo dominio (40 min)

En `docs/grafo-agenda.md`: clientes/servicios como “quién recomienda a quién” (3 nodos). Solo documentación.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): grafo lista de adyacencia"
```
""",
    )
)

# ---------- L22 ----------
LESSONS.append(
    dict(
        id="L22",
        orden=22,
        titulo="Benchmark P3: nativo vs propio",
        horas=5.0,
        semana=6,
        lectura="Medir antes de opinar: microbenchmarks honestos",
        evidencia="bench/ con tabla tiempos documentada",
        _lectura_corta="Metodología: warmup, N grande, no mentir con N=10",
        _hecho="""1. `bench/run.ts` compara ≥2 estructuras propias vs nativas (`Array`/`Map`).
2. Tabla de tiempos en `bench/RESULTADOS.md` (o README P3).
3. Commit `feat(m07): bench P3 nativo vs propio`.""",
        _errores="""- Benchmark con N trivial o sin warmup.
- Conclusiones absolutas (“soy más rápido que V8”).
- No versionar el comando para reproducir.""",
        siguiente="[L23 — README cuándo usar cada estructura](L23-readme-cuando-usar-cada-estructura.md)",
        body=r"""
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
""",
    )
)

# ---------- L23 ----------
LESSONS.append(
    dict(
        id="L23",
        orden=23,
        titulo="README cuándo usar cada estructura",
        horas=5.0,
        semana=6,
        lectura="Guía de selección de estructuras",
        evidencia="README guía de selección + API pública",
        _lectura_corta="Árbol de decisión: acceso, orden, prioridad, grafo",
        _hecho="""1. README con guía “cuándo usar cada una” (todas las estructuras del curso).
2. `src/index.ts` exporta la API pública; `npm test` verde.
3. Commit `docs(m07): guia cuando usar cada estructura`.""",
        _errores="""- Guía genérica de Internet sin tus nombres de clase.
- Olvidar heap/grafo en la tabla.
- README sin cómo correr tests.""",
        siguiente="[L24 — Cierre M07 y evidencias](L24-cierre-m07-y-evidencias.md)",
        body=r"""
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
""",
    )
)

# ---------- L24 ----------
LESSONS.append(
    dict(
        id="L24",
        orden=24,
        titulo="Cierre M07 y evidencias",
        horas=5.0,
        semana=6,
        lectura="Checklist de dominio y evidencias en git",
        evidencia="bitácora + checklist dominio + progress",
        _lectura_corta="Autoevaluación: explicar hash vs árbol en voz alta",
        _hecho="""1. `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con rutas de archivo.
2. Suite verde y README de selección presente.
3. Commit `docs(m07): cierre materia y evidencias`.""",
        _errores="""- Marcar evidencias sin archivos en git.
- Checklist genérico sin rutas.
- Dejar benches o tests rotos “para después”.""",
        siguiente="M07 cerrado — siguiente materia: [M08 · Análisis de algoritmos](../M08-analisis-de-algoritmos.md)",
        body=r"""
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
""",
    )
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(LESSONS) == 24, len(LESSONS)
    for lesson in LESSONS:
        path = OUT / FILENAMES[lesson["orden"]]
        # merge optional _enlace into lectura_block via render
        text = render(lesson)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
