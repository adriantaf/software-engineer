#!/usr/bin/env python3
"""Generate M07/M08/M09 lesson markdown files (M01-style)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUR = ROOT / "curriculum" / "etapas" / "02-disciplinaria"


def slugify(t: str) -> str:
    t = t.lower()
    t = t.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


def lesson_md(
    *,
    lid: str,
    materia: str,
    orden: int,
    titulo: str,
    horas: float,
    semana: int,
    lectura: str,
    evidencia: str,
    intro: str,
    objetivo: str,
    pasos: str,
    lectura_table: str,
    hecho: str,
    errores: str,
    siguiente: str | None,
    siguiente_label: str | None = None,
) -> str:
    n = lid.replace("L", "")
    sig = ""
    if siguiente:
        label = siguiente_label or titulo.split("—")[-1].strip() if "—" in titulo else "siguiente"
        sig = f"\n## Siguiente\n\n[{siguiente_label or 'Siguiente lección'}]({siguiente})"
    return f"""---
id: {lid}
materia: {materia}
orden: {orden}
titulo: {titulo}
horas: {horas}
semana: {semana}
lectura: "{lectura}"
evidencia: "{evidencia}"
---

# {lid} — {titulo}

**~{horas} h · Semana {semana}**

{intro}

## Objetivo

{objetivo}

## Pasos

{pasos}

## Lectura de esta lección

{lectura_table}

## Hecho cuando

{hecho}

## Errores comunes

{errores}{sig}
"""


def write_lessons(materia: str, folder: str, lessons: list[dict], horas_default: float = 5.0) -> int:
    out_dir = CUR / folder
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, L in enumerate(lessons):
        orden = i + 1
        lid = f"L{orden:02d}"
        slug = slugify(L["titulo"])
        fname = f"{lid}-{slug}.md"
        next_link = None
        next_label = None
        if i + 1 < len(lessons):
            nslug = slugify(lessons[i + 1]["titulo"])
            next_link = f"L{i+2:02d}-{nslug}.md"
            next_label = f"L{i+2:02d} — {lessons[i+1]['titulo']}"
        elif L.get("siguiente_ficha"):
            next_link = None
            sig = L["siguiente_ficha"]
        else:
            sig = ""

        content = lesson_md(
            lid=lid,
            materia=materia,
            orden=orden,
            titulo=L["titulo"],
            horas=L.get("horas", horas_default),
            semana=L["semana"],
            lectura=L["lectura"],
            evidencia=L["evidencia"],
            intro=L["intro"],
            objetivo=L["objetivo"],
            pasos=L["pasos"],
            lectura_table=L.get("lectura_table", L.get("lectura_tbl", "| Fuente | Qué leer |\n|--------|----------|\n| Ver ficha | Capítulo de la semana |")),
            hecho=L["hecho"],
            errores=L["errores"],
            siguiente=next_link,
            siguiente_label=next_label,
        )
        if L.get("siguiente_ficha"):
            content = content.rstrip() + "\n\n## Siguiente\n\n" + L["siguiente_ficha"] + "\n"
        (out_dir / fname).write_text(content, encoding="utf-8")
    return len(lessons)


# --- M07 lessons (24) ---
M07 = [
    {
        "semana": 1,
        "titulo": "Entorno del proyecto y arrays dinámicos",
        "lectura": "ED Joyanes (o equivalente): arrays estáticos/dinámicos, amortizado",
        "evidencia": "projects/m07-estructuras/ con Vitest, DynamicArray + 5 tests",
        "intro": "Arrancas la librería de estructuras: TypeScript strict, tests desde el día 1 y tu primera estructura lineal con costos documentados.",
        "objetivo": "Levantar `projects/m07-estructuras/`, implementar un array dinámico tipado con capacidad explícita y anotar Big-O de acceso e inserción al final.",
        "pasos": """### 1. Proyecto y toolchain (45 min)

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

Lee el capítulo de **arrays** de tu texto ED. Commit: `feat(m07): dynamic array con tests`.""",
        "lectura_table": """| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Texto ED (Joyanes u otro) | Arrays: operaciones y costos | Implementación + tabla propia |
| MDN | [`Array`](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array) como contraste | Solo lectura |""",
        "hecho": """1. Proyecto TS strict con Vitest verde.
2. `DynamicArray` con redimensionamiento probado.
3. Big-O documentado para acceso y `push`.
4. Commit en git.""",
        "errores": """- Implementar solo con `T[]` nativo y llamarlo “dynamic array”.
- No probar el caso que dispara redimensionar.
- Omitir documentación de costos.""",
    },
    {
        "semana": 1,
        "titulo": "Lista enlazada simple",
        "lectura": "ED: listas enlazadas singulares, punteros head/tail",
        "evidencia": "SinglyLinkedList con insert head/tail, find, 5 tests",
        "intro": "Pasas de índices contiguos a nodos enlazados: trade-off memoria vs inserción en cabeza.",
        "objetivo": "Implementar lista simple con `append`, `prepend`, búsqueda lineal y comparar con `DynamicArray` en `COMPLEJIDAD.md`.",
        "pasos": """### 1. Nodo y API (60 min)

```ts
class Node<T> { constructor(public value: T, public next?: Node<T>) {} }
```

Métodos mínimos: `prepend`, `append`, `find`, `toArray()` para tests.

### 2. Tests (75 min)

Lista vacía, prepend múltiple, append mantiene orden, find ausente, toArray coherente.

### 3. Comparación escrita (45 min)

Añade fila a `COMPLEJIDAD.md`: inserción O(1) en cabeza vs O(n) en array sin espacio extra.

### 4. Lectura (60 min)

Capítulo listas enlazadas. Dibuja 3 operaciones en papel antes de codificar.

### 5. Commit (30 min)

`feat(m07): lista enlazada simple`.""",
        "hecho": """1. Lista simple con tests verdes.
2. Comparación array vs lista documentada.
3. Commit atómico.""",
        "errores": """- Perder referencia a `head` al prepend.
- `append` O(n²) por recorrer desde head cada vez sin `tail` (aceptable si lo documentas; mejor guardar tail).""",
    },
    {
        "semana": 1,
        "titulo": "Lista doble y operaciones indexadas",
        "lectura": "ED: listas doblemente enlazadas; eliminación O(1) con referencia al nodo",
        "evidencia": "DoublyLinkedList + deleteByValue; tests de borde",
        "intro": "La doble enlace permite recorrer hacia atrás y simplificar borrados; sigue sin acceso O(1) por índice.",
        "objetivo": "Implementar lista doble con `remove` y medir cuándo preferirla frente a simple o array.",
        "pasos": """### 1. Estructura (90 min)

Nodos `prev`/`next`, `insertAt(index)`, `removeAt(index)` con validación de índice.

### 2. Tests (90 min)

Insert/borrar en extremos y medio; índice inválido; lista de un elemento.

### 3. Nota de diseño (30 min)

En README semana 1: “¿Cuándo usar array nativo de JS?” — respuesta honesta (cache, API, V8 optimizado).

### 4. Lectura (60 min)

Sección listas dobles del texto.

### 5. Commit (30 min)

`feat(m07): lista doble e indexada`.""",
        "hecho": """1. Lista doble operativa con remove.
2. Tests de índices y bordes.
3. Nota “cuándo nativo” en README o COMPLEJIDAD.""",
        "errores": """- Olvidar actualizar `prev` al borrar.
- Prometer acceso O(1) por índice en lista enlazada.""",
    },
    {
        "semana": 1,
        "titulo": "Secuencias: repaso de costos y cierre semana 1",
        "lectura": "Repaso cap. arrays/listas; anota 5 preguntas de entrevista con respuesta",
        "evidencia": "COMPLEJIDAD.md completo semana 1 + bitácora semana",
        "intro": "Consolidas la semana lineal antes de pilas: autoevaluación sin IDE.",
        "objetivo": "Completar tabla comparativa array dinámico / lista simple / lista doble / `Array` nativo y dejar bitácora honesta.",
        "pasos": """### 1. Tabla maestra (60 min)

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

`docs(m07): cierre semana 1 secuencias`.""",
        "hecho": """1. Tabla comparativa en repo.
2. Bitácora semana 1 con bloqueos.
3. Suite verde.""",
        "errores": """- Saltar bitácora “porque solo fue código”.
- Confundir peor caso de redimensionar con amortizado sin explicar.""",
    },
    {
        "semana": 2,
        "titulo": "Pila (Stack) tipada",
        "lectura": "ED: pilas LIFO, aplicaciones (paréntesis, undo)",
        "evidencia": "Stack<T> con push/pop/peek + 4 tests (inicio P1)",
        "intro": "La pila es la interfaz LIFO: implementación sobre array o lista, pero API propia.",
        "objetivo": "Implementar pila genérica con tests y documentar O(1) en operaciones core.",
        "pasos": """### 1. API (60 min)

`push`, `pop`, `peek`, `size`, `isEmpty`. Decide: `pop` en vacío lanza error tipado.

### 2. Tests (75 min)

LIFO orden, pop vacío, peek no muta, muchos pushes.

### 3. Aplicación mini (60 min)

`balanceParentesis(s: string): boolean` usando tu pila.

### 4. Lectura (45 min)

Capítulo pilas.

### 5. Commit (30 min)

`feat(m07): stack tipado`.""",
        "hecho": """1. Stack con 4+ tests.
2. Ejercicio paréntesis funcionando.
3. Big-O en COMPLEJIDAD.""",
        "errores": """- Exponer array interno mutable.
- `peek` que hace pop por error.""",
    },
    {
        "semana": 2,
        "titulo": "Cola (Queue) y cola circular",
        "lectura": "ED: colas FIFO; cola circular para evitar desplazamientos",
        "evidencia": "Queue<T> + tests; opcional CircularQueue",
        "intro": "FIFO es el buffer de BFS y de trabajos; la cola circular evita O(n) por shift ingenuo.",
        "objetivo": "Implementar cola eficiente (circular o lista con tail) con dequeue O(1) amortizado.",
        "pasos": """### 1. Cola base (90 min)

`enqueue`, `dequeue`, `front`. Evita `array.shift()` en hot path sin documentar O(n).

### 2. Circular (opcional 60 min)

Arreglo fijo + índices head/tail; test de wrap-around.

### 3. Tests (75 min)

FIFO, cola vacía, llenar circular y reusar espacio.

### 4. Lectura (45 min)

Capítulo colas.

### 5. Commit (30 min)

`feat(m07): queue y cola circular`.""",
        "hecho": """1. Cola con dequeue O(1) documentado.
2. Tests FIFO y bordes.
3. Commit.""",
        "errores": """- Usar shift en array grande sin medir.
- Confundir tail de lista con cola circular.""",
    },
    {
        "semana": 2,
        "titulo": "Deque y casos de uso",
        "lectura": "ED: deque; aplicaciones (sliding window, BFS 0-1 intro)",
        "evidencia": "Deque mínimo o cola doble + 3 tests",
        "intro": "Insertar/quitar en ambos extremos aparece en ventanas deslizantes y ciertos algoritmos de grafos.",
        "objetivo": "Implementar deque (o documentar por qué usas dos pilas) y resolver un ejercicio que requiera ambos extremos.",
        "pasos": """### 1. Deque API (90 min)

`pushFront`, `pushBack`, `popFront`, `popBack`.

### 2. Ejercicio (75 min)

Palíndromo ignorando espacios con deque, o ventana máxima de tamaño k (versión simple).

### 3. Tests (60 min)

Operaciones alternadas en ambos lados.

### 4. Lectura (30 min)

Sección deque / variantes.

### 5. Commit (45 min)

`feat(m07): deque y ejercicio`.""",
        "hecho": """1. Deque operativo.
2. Ejercicio resuelto con tests.
3. Costos anotados.""",
        "errores": """- Deque sobre array con shift O(n) sin advertencia.""",
    },
    {
        "semana": 2,
        "titulo": "Pilas, colas y cierre P1 parcial",
        "lectura": "Repaso pilas/colas; MDN Map no aplica aún",
        "evidencia": "README sección LIFO/FIFO + bitácora semana 2",
        "intro": "Verificas que P1 avanza: pila, cola y evidencia clara antes de tablas hash.",
        "objetivo": "Integrar stack/queue/deque en README de la librería y checklist P1 (lista pendiente si falta).",
        "pasos": """### 1. Checklist P1 (30 min)

Marca en README: lista ✓, pila ✓, cola ✓, hash pendiente.

### 2. Diagrama (45 min)

Dibuja flujo BFS genérico usando cola (pseudo, enlace a M03 si ya lo hiciste).

### 3. Tests integración (90 min)

Un test que use pila y cola en el mismo escenario (simulación simple).

### 4. Bitácora (30 min)

`bitacora/semana-02.md`.

### 5. Commit (45 min)

`docs(m07): cierre semana 2 pilas y colas`.""",
        "hecho": """1. README actualizado con LIFO/FIFO.
2. Bitácora semana 2.
3. Pila y cola con tests en repo.""",
        "errores": """- Marcar P1 completa sin hash.""",
    },
]

# Extend M07 with weeks 3-6 (16 more lessons) - abbreviated in script for length
M07_EXT = [
    ("3", "Función hash y mapa conceptual", "ED: hash, universos, colisiones", "Hash notes + función hash string→number con tests deterministas"),
    ("3", "Tabla hash con encadenamiento", "ED: separate chaining", "HashMapChaining con set/get/delete + load factor logged"),
    ("3", "Factor de carga y rehash", "ED: rehashing", "Rehash al superar umbral; tests que fuerzan resize"),
    ("3", "Hash vs Map nativo (P1 cierre)", "MDN Map/Set", "P1 completa: lista,pila,cola,hash + tabla comparativa nativo"),
    ("4", "BST: inserción y búsqueda", "ED: árboles binarios de búsqueda", "BST insert/contains + tests ordenados"),
    ("4", "Recorridos inorder, preorder, postorder", "ED: recorridos", "Tres recorridos + snapshots en tests"),
    ("4", "BST: mínimo, máximo y sucesor", "ED: operaciones BST", "min/max/delete leaf intro"),
    ("4", "Visualización y P2 parcial", "VisuAlgo BST", "export traverse a string + README P2"),
    ("5", "Modelo de heap binario", "ED: heaps", "array-backed heap model + heapifyUp/Down"),
    ("5", "Heap mínimo: insert y extractMin", "ED: priority queue", "MinHeap operativo + tests"),
    ("5", "Cola de prioridad", "ED: aplicaciones heap", "PriorityQueue API + 3 casos"),
    ("5", "Heap vs BST para prioridades", "Comparativa ED", "COMPLEJIDAD heap vs BST"),
    ("6", "Grafos: repaso y representación", "Repaso M03 + ED grafos", "Adjacency list en TS reutilizable"),
    ("6", "Benchmark P3: nativo vs propio", "Metodología benchmark", "bench/ con tabla tiempos documentada"),
    ("6", "README cuándo usar cada estructura", "Proyecto lib ED", "README guía de selección + API pública"),
    ("6", "Cierre M07 y evidencias", "Repaso total ED", "bitácora + checklist dominio + progress"),
]

def expand_m07_ext(base: list[dict]) -> list[dict]:
    out = base[:]
    sem_map = {"3": 3, "4": 4, "5": 5, "6": 6}
    for sem, titulo, lectura, evidencia in M07_EXT:
        sem_i = sem_map[sem]
        out.append({
            "semana": sem_i,
            "titulo": titulo,
            "lectura": lectura,
            "evidencia": evidencia,
            "intro": f"Semana {sem_i} de M07: rigor en implementación, tests y documentación de costos.",
            "objetivo": f"Avanzar evidencia `{evidencia}` con código TS, tests Vitest y notas en COMPLEJIDAD/README.",
            "pasos": f"""### 1. Lectura dirigida (60 min)

Lee la sección indicada en tu texto ED sobre **{titulo.split(':')[0]}**. Anota definiciones formales (pre/post condiciones).

### 2. Implementación (120 min)

Crea o extiende módulos bajo `src/` con tipos explícitos. Sin `any`. Exporta API mínima documentada en comentario JSDoc breve.

### 3. Tests (90 min)

Mínimo **5** tests: feliz, vacío, borde, caso que fuerza estructura interna (p. ej. colisión, rotación simple, heapify), regresión.

### 4. Documentación (30 min)

Actualiza `COMPLEJIDAD.md` o README con Big-O de operaciones nuevas. Si comparas con nativo, di **cuándo** gana cada uno.

### 5. Commit (30 min)

Mensaje `feat(m07)` o `docs(m07)` descriptivo en español.""",
            "hecho": """1. Código + tests verdes para el foco de la lección.
2. Costos documentados.
3. Commit en git.""",
            "errores": """- Copiar implementación sin entender invariantes.
- Tests solo “felices”.
- Omitir commit.""",
        })
    out[-1]["siguiente_ficha"] = "Vuelve a la [ficha M07](../M07-estructuras-de-datos.md), marca lecciones y prácticas con evidencia, y continúa con **M08 — Análisis de algoritmos**."
    out[-1]["pasos"] = """### 1. Checklist de evidencias (60 min)

| Ítem | Evidencia |
|------|-----------|
| **P1** | Lista, pila, cola, hash con tests |
| **P2** | BST + recorridos |
| **P3** | Benchmark vs nativo |
| **Proyecto** | README “cuándo usar cada una” |

### 2. Criterios de dominio (45 min)

Responde sí/no + frase en `bitacora/cierre-m07.md`:
- ¿Cuándo hash gana a árbol?
- ¿Puedes reimplementar pila desde cero en 15 min?

### 3. Suite completa (90 min)

`npm test` verde. Arregla flaky tests.

### 4. Bitácora final (30 min)

Qué repetirías si tuvieras 4 h extra.

### 5. Marca progreso (15 min)

Solo lecciones con “Hecho cuando” cumplido. Commit `docs(m07): cierre materia`."""
    return out


M07_ALL = expand_m07_ext(M07)

# M08 - 24 lessons
def m08_lesson(semana, titulo, lectura, evidencia, extra_pasos=""):
    return {
        "semana": semana,
        "titulo": titulo,
        "lectura": lectura,
        "evidencia": evidencia,
        "intro": "M08 conecta teoría CLRS con problemas clasificados y el autocomplete del producto.",
        "objetivo": f"Producir evidencia en `projects/m08-algoritmos/` alineada con: {evidencia}.",
        "pasos": f"""### 1. Setup / repaso (30 min)

Confirma carpetas: `problems/`, `sorts/`, `dp/`, `autocomplete/`. README con comandos test.

### 2. Trabajo central (150 min)

{extra_pasos or "Implementa o resuelve el foco de hoy en TypeScript strict. Escribe enunciado en Markdown si es problema externo."}

### 3. Análisis escrito (45 min)

Archivo `*-analisis.md`: complejidad temporal y espacial, peor caso, justificación en 5–8 frases.

### 4. Tests (45 min)

Tres casos mínimo por función: borde incluido.

### 5. Commit (30 min)

`feat(m08): ...` atómico.""" ,
        "lectura_table": """| Fuente | Qué leer |
|--------|----------|
| CLRS (Cormen et al.) | Sección de la semana en ficha M08 |
| Alternativa | VisuAlgo + notas propias |""",
        "hecho": """1. Evidencia en repo según objetivo.
2. Complejidad escrita.
3. Commit.""",
        "errores": """- Copiar solución sin invariante.
- Confundir O promedio con peor caso.""",
    }

M08_TITLES = [
    (1, "Entorno y binary search con invariante", "CLRS: inserción ordenada / búsqueda binaria", "binary-search.ts + analisis + 2 problemas arrays"),
    (1, "Notación asintótica Θ, O y Ω", "CLRS cap. crecimiento de funciones", "notacion.md + 5 funciones clasificadas"),
    (1, "Análisis de bucles y recursión simple", "CLRS: análisis divide", "3 snippets analizados en markdown"),
    (1, "Tres problemas con complejidad escrita", "CLRS + problem set propio", "problems/ con 3 entradas + complejidad"),
    (2, "Insertion sort implementado", "CLRS insertion sort", "sorts/insertion.ts + tests"),
    (2, "Merge sort y estabilidad", "CLRS merge sort", "sorts/merge.ts + nota estabilidad"),
    (2, "Quicksort y peor caso", "CLRS quicksort", "sorts/quick.ts + caso O(n²)"),
    (2, "Tabla P2 sorts en README", "Comparativa sorts", "sorts/README.md P2 parcial"),
    (3, "Hash maps en problemas de conteo", "CLRS hashing cap intro", "2 problemas patrón hash"),
    (3, "Two pointers en arrays ordenados", "Notas M08", "2 problemas two pointers"),
    (3, "Sliding window", "Notas M08", "2 problemas ventana"),
    (3, "Índice de patrones (5+ entradas)", "indice-patrones.md", "≥5 patrones clasificados"),
    (4, "BFS repaso y cola", "CLRS BFS", "1 problema BFS + grafo test"),
    (4, "DFS y componentes", "CLRS DFS", "problema componentes conexas"),
    (4, "Caminos en grafos no ponderados", "CLRS grafos", "camino mínimo en aristas no peso"),
    (4, "Problemas de grafos semana 4", "VisuAlgo Graph", "problems/ +2 grafos"),
    (5, "Memoización top-down", "CLRS DP intro", "dp/memo-ejemplo.ts"),
    (5, "Programación dinámica bottom-up", "CLRS DP", "dp/bottom-up-ejemplo.ts"),
    (5, "Tres problemas DP (P3)", "CLRS clásicos", "dp/ tres carpetas con caso base"),
    (5, "Patrones DP y transiciones", "Editorial propia", "dp/README patrones"),
    (6, "Autocomplete: elección de estructura", "Trie / prefix map", "autocomplete/DISENO.md"),
    (6, "Implementación trie o índice", "CLRS no aplica", "autocomplete/ código + tests"),
    (6, "Dataset Agenda Ops y demo CLI", "producto-saas.md", "CSV/JSON demo + CLI"),
    (6, "Cierre M08 y evidencias", "Repaso P1–P3", "checklist + indice ≥15"),
]

M08 = []
for i, (sem, tit, lect, ev) in enumerate(M08_TITLES):
    L = m08_lesson(sem, tit, lect, ev)
    if i == 0:
        L["pasos"] = """### 1. Carpetas (15 min)

```bash
mkdir -p projects/m08-algoritmos/{problems,sorts,dp,autocomplete}
```

### 2. Binary search (90 min)

Reescribe con invariante `[lo,hi]`. Tests: vacío, uno, ausente, duplicados (define convención).

### 3. Análisis (45 min)

`binary-search-analisis.md` — O(log n) peor caso.

### 4. Dos problemas arrays (90 min)

p. ej. two sum, max subarray — sin mirar solución 30 min; luego editorial propia.

### 5. Commit (30 min)

`feat(m08): binary search + 2 problemas`."""
    if i == len(M08_TITLES) - 1:
        L["siguiente_ficha"] = "Cierra la [ficha M08](../M08-analisis-de-algoritmos.md) y pasa a **M09 — Bases de datos**."
        L["pasos"] = """### 1. P1: 15 problemas (60 min)

Verifica `indice-patrones.md` ≥15 entradas alineadas.

### 2. P2/P3 y proyecto (90 min)

Sorts README, 3 DP, autocomplete demo.

### 3. Dominio (45 min)

Resuelve un medio sin notas — regístralo en bitácora.

### 4. Commit cierre (15 min)

`docs(m08): cierre materia`."""
    M08.append(L)

# M09 - 20 lessons
M09_TITLES = [
    (1, "PostgreSQL local y carpeta de evidencia", "Elmasri: intro SGBD", "README conexión + docker opcional"),
    (1, "Entidades Cliente, Servicio, Cita", "Elmasri ER", "er-agenda.md borrador"),
    (1, "Cardinalidades y reglas de negocio", "Elmasri relaciones", "ER revisado con FKs planeadas"),
    (1, "Glosario alineado al dominio", "SRS M12 si existe", "glosario.md"),
    (2, "Primera forma normal y anomalías", "Elmasri 1FN", "ejercicio descomposición 1FN"),
    (2, "Segunda forma normal", "Elmasri 2FN", "tablas split + justificación"),
    (2, "Tercera forma normal (P1)", "Elmasri 3FN", "er-agenda.md hasta 3FN"),
    (2, "Trade-offs de desnormalización", "Notas diseño", "sección trade-offs en ER doc"),
    (3, "Joins inner y left", "Elmasri SQL", "sql/joins-*.sql ejecutados"),
    (3, "Agregaciones y GROUP BY", "Elmasri", "sql/reportes-agregados.sql"),
    (3, "Subconsultas y HAVING", "PostgreSQL docs", "sql/subconsultas.sql"),
    (3, "Cinco consultas P2 comentadas", "Tutorial PG", "sql/ ≥5 archivos"),
    (4, "Índices B-tree intro", "Elmasri índices", "notas indice.md"),
    (4, "EXPLAIN ANALYZE en consultas reales", "PG EXPLAIN", "explain-notas.md primera entrada"),
    (4, "Optimizar query lenta de reporte", "PG performance", "índice creado + antes/después"),
    (4, "Documentar planes de ejecución", "PG docs", "explain-notas.md ≥2 queries"),
    (5, "Transacciones ACID", "Elmasri transacciones", "sql/transaccion-cita.sql"),
    (5, "Migraciones versionadas", "Herramienta elegida", "migrations/ primera + segunda"),
    (5, "Least privilege (P3)", "hilos/seguridad.md", "roles.md + rol app"),
    (5, "Reportes, seeds y cierre M09", "Proyecto CRM", "reportes.md + seeds + README"),
]

M09 = []
for i, (sem, tit, lect, ev) in enumerate(M09_TITLES):
    L = {
        "semana": sem,
        "titulo": tit,
        "lectura": lect,
        "evidencia": ev,
        "intro": "Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.",
        "objetivo": f"Entregar `{ev}` con SQL ejecutado (no solo leído).",
        "pasos": """### 1. Lectura (45 min)

Capítulo Elmasri indicado. Subraya definiciones (entidad, relación, dependencia funcional, ACID).

### 2. Trabajo en repo (150 min)

Ejecuta contra tu BD local. **Nunca** pegues contraseñas en git; usa `.env` ignorado y `README` con variables.

### 3. Query parametrizada (30 min)

Si aplica capa TS, muestra `$1` placeholders; si solo SQL, usa variables psql `\\set`.

### 4. Evidencia en git (45 min)

Archivos `.sql` o migraciones + salida ejemplo en comentario o `samples/`.

### 5. Commit (30 min)

`feat(m09): ...` descriptivo.""",
        "lectura_table": """| Fuente | Qué leer |
|--------|----------|
| Elmasri & Navathe | Sección de la semana |
| PostgreSQL docs | Tema equivalente (Query, EXPLAIN, Roles) |""",
        "hecho": """1. Artefacto pedido existe y fue ejecutado.
2. Sin secretos en git.
3. Commit.""",
        "errores": """- SQL concatenado estilo injection demo.
- Usuario superuser para la app.
- Migraciones solo en local sin historial.""",
    }
    if i == 0:
        L["pasos"] = """### 1. Carpetas (15 min)

```bash
mkdir -p projects/m09-bases-datos/{migrations,sql}
```

### 2. PostgreSQL (60 min)

Docker Compose o nativo. Documenta host/puerto/db en README (sin password).

### 3. ER borrador (90 min)

`er-agenda.md`: Cliente, Servicio, Cita — atributos y cardinalidades.

### 4. Migración inicial (60 min)

Tres tablas + FKs + timestamps.

### 5. Rol app + seed + join (45 min)

Usuario sin superuser; `sql/citas-con-cliente.sql`; commit `feat(m09): esquema inicial`."""
    if i == len(M09_TITLES) - 1:
        L["siguiente_ficha"] = "Cierra la [ficha M09](../M09-bases-de-datos.md). Siguiente materia disciplinaria según tu plan."
        L["pasos"] = """### 1. Seeds completos (90 min)

Datos realistas en varios estados de cita.

### 2. Dos reportes (60 min)

`reportes.md`: pregunta de negocio, SQL, ejemplo salida.

### 3. Checklist P1–P3 y proyecto (60 min)

ER 3FN, sql/, explain, migrations, roles.md.

### 4. Dominio (30 min)

Recrear BD solo con README en máquina limpia (simulación).

### 5. Commit (30 min)

`docs(m09): cierre materia`."""
    M09.append(L)


def main():
    n7 = write_lessons("M07", "M07", M07_ALL, 5.0)
    n8 = write_lessons("M08", "M08", M08, 5.0)
    n9 = write_lessons("M09", "M09", M09, 5.0)
    print(f"M07: {n7}, M08: {n8}, M09: {n9}, total: {n7+n8+n9}")


if __name__ == "__main__":
    main()
