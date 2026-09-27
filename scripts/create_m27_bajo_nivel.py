#!/usr/bin/env python3
"""Create M27 Sistemas a bajo nivel: catalog entry, ficha, lessons, scaffold."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUR = ROOT / "curriculum"
OUT = CUR / "etapas/02-disciplinaria/M27"
FICHA = CUR / "etapas/02-disciplinaria/M27-sistemas-bajo-nivel.md"
PROJ = ROOT / "projects/m27-bajo-nivel"
BIBLIO = "../../../bibliografia.md#m27-sistemas-a-bajo-nivel"
CSAPP = "*Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP)"
GCC = "https://gcc.gnu.org/onlinedocs/"
GODBOLT = "https://godbolt.org/"


def quote_fm(v: str) -> str:
    if any(c in v for c in ':"\'*#'):
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return v


def write_lesson(
    orden: int,
    slug: str,
    titulo: str,
    horas: float,
    semana: int,
    lectura: str,
    evidencia: str,
    body: str,
    hecho: str,
    errores: str,
    siguiente: str,
):
    lid = f"L{orden:02d}"
    fm = "\n".join(
        [
            "---",
            f"id: {lid}",
            "materia: M27",
            f"orden: {orden}",
            f"titulo: {quote_fm(titulo)}",
            f"horas: {horas}",
            f"semana: {semana}",
            f"lectura: {quote_fm(lectura)}",
            f"evidencia: {quote_fm(evidencia)}",
            "---",
        ]
    )
    lectura_tbl = f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {CSAPP} | {lectura} | [Compiler Explorer]({GODBOLT}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27]({BIBLIO}) |
"""
    text = f"""{fm}

# {lid} — {titulo}

**~{horas} h · Semana {semana}**

{body.strip()}

{lectura_tbl}

## Hecho cuando

Marca la lección **solo si**:

{hecho.strip()}

## Errores comunes

{errores.strip()}

## Siguiente

{siguiente}
"""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{lid}-{slug}.md"
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def update_catalog():
    path = CUR / "catalog.json"
    cat = json.loads(path.read_text())
    entry = {
        "id": "M27",
        "slug": "M27-sistemas-bajo-nivel",
        "titulo": "Sistemas a bajo nivel",
        "etapa": "disciplinaria",
        "orden": 12,
        "semanas": 5,
        "horas": 100,
        "analogos": [],
    }
    ids = [m["id"] for m in cat["materias"]]
    if "M27" not in ids:
        for m in cat["materias"]:
            if m["orden"] >= 12:
                m["orden"] += 1
        idx = next(i for i, m in enumerate(cat["materias"]) if m["id"] == "M11")
        cat["materias"].insert(idx + 1, entry)
        print("catalog: inserted M27 after M11; bumped orden M12+")
    else:
        cat["materias"] = [m for m in cat["materias"] if m["id"] != "M27"]
        for m in cat["materias"]:
            if m["id"] != "M27" and m["orden"] >= 12 and m["orden"] < 12 + 20:
                pass  # keep bumped orders
        # ensure M12+ have orden >= 13
        for m in cat["materias"]:
            if m["id"].startswith("M") and m["id"] not in ("M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11"):
                num = int(m["id"][1:])
                if 12 <= num <= 26 and m["orden"] == num:
                    m["orden"] = num + 1
        idx = next(i for i, m in enumerate(cat["materias"]) if m["id"] == "M11")
        cat["materias"].insert(idx + 1, entry)
        print("catalog: refreshed M27 position")
    path.write_text(json.dumps(cat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


FICHA_MD = r'''---
id: M27
titulo: Sistemas a bajo nivel
etapa: disciplinaria
orden: 12
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: "C: tipos, punteros y buffers con evidencia"
  - id: p2
    titulo: Stack, heap y sanitizers (ASan/UBSan)
  - id: p3
    titulo: Leer asm generado y calling convention
proyecto:
  id: proj
  titulo: Informe "viaje de un binario" (compile → link → run)
---

# M27 — Sistemas a bajo nivel

## Por qué existe

M05 te dio el mapa de la máquina; M11 te enseñó a operar procesos y contenedores. Aquí bajas un piso: **C, memoria, ABI y ensamblador x86-64** para dejar de tratar el runtime como magia. Eso mejora depuración, AppSec (overflows) y, más adelante, compiladores (M28).

**En resumen:** escribes C pequeño, lees el asm que genera el compilador y documentas cómo un binario llega a ejecutarse.

**Prerrequisito recomendado:** M05 + M11 (o al menos M05 + comodidad con Linux/WSL).

## Objetivos de aprendizaje

Al terminar debes poder:

1. Compilar y linkar programas C con `gcc`/`clang` y flags útiles (`-Wall -Wextra -g -O0/-O2`).
2. Explicar punteros, `sizeof`, stack vs heap y un stack frame típico (System V AMD64).
3. Usar AddressSanitizer/UBSan para cazar errores de memoria.
4. Leer asm x86-64 básico generado por el compilador (`-S` / Compiler Explorer).
5. Describir compile → link → load → `_start` / `main` → exit en Linux.
6. Relacionar un overflow de buffer con riesgo de seguridad (puente a M18).

## Cómo estudiar esta materia (lecciones)

1. Orden **L01 → L18**; marca solo con “Hecho cuando”.
2. Trabaja en **Linux o WSL2** (x86-64). macOS Apple Silicon sirve con notas; documenta diferencias.
3. Cada concepto → un `.c` o captura `objdump`/`readelf` en `projects/m27-bajo-nivel/`.
4. No memorices tablas de opcodes: **lee** lo que emite *tu* compilador.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| C + memoria | 6–8 | L01–L08 |
| Asm + ABI | 6–8 | L09–L12 |
| Linking / proceso | 4–6 | L13–L16 |
| Proyecto | 2–4 | L17–L18 |

Si solo tienes 2 h: **una lección con código compilado**, no solo lectura.

## Lecciones

### Semana 1 — Toolchain y C esencial (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Toolchain C y carpeta de evidencia](M27/L01-toolchain-c-y-carpeta-de-evidencia.md) | 5 |
| L02 | [Tipos, sizeof y representación](M27/L02-tipos-sizeof-y-representacion.md) | 5 |
| L03 | [Punteros y direcciones](M27/L03-punteros-y-direcciones.md) | 5 |
| L04 | [Arrays, strings y buffers (P1)](M27/L04-arrays-strings-y-buffers-p1.md) | 5 |

### Semana 2 — Stack, heap y UB (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Stack frames intro](M27/L05-stack-frames-intro.md) | 5 |
| L06 | [Calling convention System V AMD64](M27/L06-calling-convention-system-v.md) | 5 |
| L07 | [Heap: malloc, free y lifetime](M27/L07-heap-malloc-free-y-lifetime.md) | 5 |
| L08 | [UB y sanitizers ASan/UBSan (P2)](M27/L08-ub-y-sanitizers-p2.md) | 5 |

### Semana 3 — Ensamblador generado (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [De C a asm con -S y objdump](M27/L09-de-c-a-asm-con-s-y-objdump.md) | 5 |
| L10 | [Registros x86-64 y mov/add/call](M27/L10-registros-x86-64-y-mov-add-call.md) | 5 |
| L11 | [Optimización -O0 vs -O2 (lectura)](M27/L11-optimizacion-o0-vs-o2.md) | 5 |
| L12 | [Lab: anotar calling convention (P3)](M27/L12-lab-anotar-calling-convention-p3.md) | 5 |

### Semana 4 — Linking y proceso (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Compilar vs linkar: .o y librerías](M27/L13-compilar-vs-linkar.md) | 5 |
| L14 | [ELF con readelf (headers)](M27/L14-elf-con-readelf.md) | 5 |
| L15 | [Cómo el SO carga un binario](M27/L15-como-el-so-carga-un-binario.md) | 5 |
| L16 | [Syscalls vs libc](M27/L16-syscalls-vs-libc.md) | 5 |

### Semana 5 — Proyecto y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Documentar un stack frame real](M27/L17-documentar-un-stack-frame-real.md) | 5 |
| L18 | [Viaje de un binario y cierre M27](M27/L18-viaje-de-un-binario-y-cierre.md) | 5 |

Empieza por **L01** hoy (después de M11, o con M05 sólido).

## Lecturas (mapa rápido)

Canon: *Computer Systems: A Programmer's Perspective* (CSAPP) — Bryant & O'Hallaron. Alternativa gratis: docs GCC + [Compiler Explorer](https://godbolt.org/) + man pages. Ver [bibliografía](../../bibliografia.md#m27-sistemas-a-bajo-nivel).

| Semana | Lecciones | Foco CSAPP / práctica |
|--------|-----------|------------------------|
| 1 | L01–L04 | Representación de datos + C |
| 2 | L05–L08 | Machine-level / memoria / UB |
| 3 | L09–L12 | Asm x86-64 generado |
| 4 | L13–L16 | Linking + programa y SO |
| 5 | L17–L18 | Síntesis / proyecto |

## Ejemplo — overflow de buffer (idea)

```c
char buf[8];
// Mal: gets(buf) o strcpy sin límite.
// Bien: fgets(buf, sizeof buf, stdin);
```

En M18 verás el ángulo AppSec; aquí basta entender **por qué** el stack se corrompe.

## Prácticas

1. **P1 — C esencial:** programas + notas de tipos/punteros/buffers — L01–L04.
2. **P2 — Sanitizers:** al menos un bug cazado con ASan o UBSan — L08.
3. **P3 — ABI/asm:** anotación de registros en una función tuya — L12.

## Proyecto útil

**Viaje de un binario** en `projects/m27-bajo-nivel/viaje-binario.md`:

- Comandos exactos de compile/link.
- Fragmento de asm de `main` (o función elegida).
- Diagrama: fuente → `.o` → ejecutable → proceso.
- Una frase de puente a M18 (memoria insegura) y a M28 (lo que hace un compilador).

## Errores comunes

- Estudiar asm de tutoriales de 16-bit / DOS.
- Compilar solo con defaults y nunca mirar `-Wall`.
- Usar `malloc` sin `free` “porque el proceso muere” y no documentar el lifetime.
- Marcar lecciones sin un `.c` o captura en git.

## Evidencia de hecho

- **P1:** código C + `notas/` de tipos/punteros en `projects/m27-bajo-nivel/`.
- **P2:** log o nota de sanitizer cazando un bug real tuyo.
- **P3:** `asm/` o notas con calling convention anotada.
- **Proyecto:** `viaje-binario.md` completo enlazado desde el README.

## Criterios de dominio

- [ ] Explicas stack vs heap con un dibujo y un ejemplo C.
- [ ] Lees un fragmento corto de asm x86-64 generado y dices qué hace.
- [ ] Describes compile → link → run sin “magia”.
- [ ] Nombras un riesgo de buffer overflow en lenguaje llano.
'''


LESSONS: list[dict] = []


def L(**kw):
    LESSONS.append(kw)


L(
    orden=1,
    slug="toolchain-c-y-carpeta-de-evidencia",
    titulo="Toolchain C y carpeta de evidencia",
    horas=5.0,
    semana=1,
    lectura="CSAPP intro / tooling; man gcc",
    evidencia="projects/m27-bajo-nivel/ con hello.c que compila",
    body=r"""
Sin toolchain no hay bajo nivel usable. Hoy dejas C compilando en tu máquina y evidencia en git.

## Objetivo

Tener `gcc` o `clang`, carpeta `projects/m27-bajo-nivel/` y un `hello` que imprime y termina con código 0.

## Por qué empieza así

Todo lo demás (asm, sanitizers, ELF) asume que puedes emitir un binario local.

## Pasos (hazlos en orden)

### 1. Entorno (30–40 min)

En Linux/WSL:

```bash
gcc --version || clang --version
which gcc clang make
```

Si falta: `sudo apt update && sudo apt install build-essential gdb binutils` (o equivalente).

Anota versiones en `projects/m27-bajo-nivel/entorno.md`.

### 2. Scaffold (20 min)

```bash
mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}
cp -n projects/m27-bajo-nivel/README.md projects/m27-bajo-nivel/README.md 2>/dev/null || true
```

Revisa el README del scaffold del plan.

### 3. Hello (45–60 min)

Crea `projects/m27-bajo-nivel/src/hello.c`:

```c
#include <stdio.h>

int main(void) {
  puts("hola m27");
  return 0;
}
```

```bash
cd projects/m27-bajo-nivel
gcc -Wall -Wextra -g -O0 -o out/hello src/hello.c
./out/hello
echo exit:$?
```

### 4. Flags en notas (40 min)

En `notas/flags.md`: qué hace `-Wall`, `-Wextra`, `-g`, `-O0` (una línea cada uno).

### 5. Commit (15 min)

```bash
git add projects/m27-bajo-nivel
git commit -m "feat(m27): toolchain y hello.c"
```
""",
    hecho="""1. `gcc` o `clang` disponible; versión en `entorno.md`.
2. `out/hello` corre e imprime el mensaje.
3. Commit con el scaffold + hello.""",
    errores="""- Instalar un IDE enorme y no compilar desde terminal.
- Commitear binarios `out/*` (debe estar en `.gitignore`).
- Usar un compilador online sin dejar evidencia local.""",
    siguiente="[L02 — Tipos, sizeof y representación](L02-tipos-sizeof-y-representacion.md)",
)

L(
    orden=2,
    slug="tipos-sizeof-y-representacion",
    titulo="Tipos, sizeof y representación",
    horas=5.0,
    semana=1,
    lectura="CSAPP: data sizes / integer representation intro",
    evidencia="src/sizes.c + notas/sizes.md",
    body=r"""
C hace visibles los anchos de tipo. Hoy mides y relacionas con M05 (enteros / overflow).

## Objetivo

Programa que imprime `sizeof` de tipos comunes y notas sobre signed vs unsigned.

## Pasos

### 1. Lectura corta (40 min)

CSAPP (tamaños de datos) o equivalen docs. Relaciona con lo que viste en M05.

### 2. `sizes.c` (90 min)

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
  printf("char=%zu int=%zu long=%zu\n", sizeof(char), sizeof(int), sizeof(long));
  printf("void*=%zu size_t=%zu\n", sizeof(void*), sizeof(size_t));
  printf("int32=%zu int64=%zu\n", sizeof(int32_t), sizeof(int64_t));
  return 0;
}
```

Compila y pega la salida en `notas/sizes.md`. Explica por qué `long` puede diferir entre plataformas.

### 3. Overflow consciente (60 min)

Añade un ejemplo signed overflow (con comentario de que es UB en C) y uno unsigned que wrappea bien definido. Documenta la diferencia.

### 4. Commit (15 min)
""",
    hecho="""1. `sizes.c` corre; salida pegada en notas.
2. Explicas al menos una diferencia de tamaño entre plataformas.
3. Commit.""",
    errores="""- Asumir que `int` siempre es 32 bits.
- Ignorar `stdint.h` cuando necesitas anchos fijos.
- Tratar overflow signed como “siempre wrappea”.""",
    siguiente="[L03 — Punteros y direcciones](L03-punteros-y-direcciones.md)",
)

L(
    orden=3,
    slug="punteros-y-direcciones",
    titulo="Punteros y direcciones",
    horas=5.0,
    semana=1,
    lectura="CSAPP / K&R: pointers",
    evidencia="src/pointers.c + diagrama en notas/",
    body=r"""
Un puntero es una dirección con tipo. Hoy dejas de temerle imprimiendo direcciones reales.

## Objetivo

Código que muestra `&x`, `*p`, aritmética básica de punteros a `int`, y un diagrama tuyo.

## Pasos

### 1. Lectura (40 min)

Punteros: declaración, `*`, `&`, `NULL`.

### 2. Experimentos (120 min)

En `src/pointers.c`: variable local, puntero a ella, modificar vía `*p`, array + aritmética `p+1`. Imprime valores y direcciones con `%p`.

### 3. Diagrama (45 min)

`notas/punteros.md`: dibuja stack con `x` y `p` (ASCII está bien).

### 4. Commit (15 min)
""",
    hecho="""1. Programa corre e imprime direcciones.
2. Diagrama en notas.
3. Commit.""",
    errores="""- Dereferenciar `NULL`.
- Confundir `int *p` con “int que se llama *p”.
- Aritmética de punteros en `void*` sin cast.""",
    siguiente="[L04 — Arrays, strings y buffers (P1)](L04-arrays-strings-y-buffers-p1.md)",
)

L(
    orden=4,
    slug="arrays-strings-y-buffers-p1",
    titulo="Arrays, strings y buffers (P1)",
    horas=5.0,
    semana=1,
    lectura="CSAPP: arrays/strings; man strncpy",
    evidencia="src/buffers.c — cierra P1",
    body=r"""
Los strings C son buffers con terminador. Aquí nace buena parte de los overflows.

## Objetivo

Cerrar **P1**: arrays, `strlen`/`snprintf`, y una nota de por qué `gets` está prohibido.

## Pasos

### 1. Lectura (30 min)

Strings C y terminador `\\0`.

### 2. `buffers.c` (120 min)

- Copia segura con `snprintf` a un buffer fijo.
- Función que cuenta longitud sin `strlen` (recorrido hasta `\\0`).
- Comentario: qué pasaría con `strcpy` a buffer corto.

### 3. Evidencia P1 (45 min)

README o `notas/p1.md`: lista de archivos + qué demuestra cada uno (L01–L04).

### 4. Commit (15 min)

```bash
git commit -am "feat(m27): P1 buffers y strings"
```
""",
    hecho="""1. `buffers.c` compila con `-Wall` sin warnings nuevos.
2. Notas P1 enlazan L01–L04.
3. Commit.""",
    errores="""- Usar `gets`.
- Olvidar espacio para `\\0`.
- Cerrar P1 sin evidencia en git.""",
    siguiente="[L05 — Stack frames intro](L05-stack-frames-intro.md)",
)

L(
    orden=5,
    slug="stack-frames-intro",
    titulo="Stack frames intro",
    horas=5.0,
    semana=2,
    lectura="CSAPP: stack frame / machine-level intro",
    evidencia="notas/stack-frame.md + src/stack_demo.c",
    body=r"""
Cada llamada crea un marco. Hoy lo ves con variables locales y una función anidada.

## Objetivo

Explicar en tus palabras qué hay en un stack frame y demostrarlo con direcciones de locales.

## Pasos

### 1. Lectura (45 min)

Return address, saved frame pointer (idea), locals, arguments (visión).

### 2. Demo (90 min)

`stack_demo.c`: `main` llama `f` llama `g`; imprime `&` de locales en cada una. Observa si las direcciones crecen hacia abajo (típico x86-64).

### 3. Nota (60 min)

Dibuja tres frames. Relaciona con M05 (memoria) y M11 (espacio de direcciones del proceso).

### 4. Commit (15 min)
""",
    hecho="""1. Demo corre; anotaste el orden de direcciones.
2. Diagrama de frames en notas.
3. Commit.""",
    errores="""- Creer que “el stack” es una estructura de datos de C.
- Confundir stack del proceso con call stack de JS async.""",
    siguiente="[L06 — Calling convention System V AMD64](L06-calling-convention-system-v.md)",
)

L(
    orden=6,
    slug="calling-convention-system-v",
    titulo="Calling convention System V AMD64",
    horas=5.0,
    semana=2,
    lectura="System V AMD64 ABI — argument registers",
    evidencia="notas/abi-sysv.md",
    body=r"""
En Linux x86-64 los primeros args van en registros: `rdi, rsi, rdx, rcx, r8, r9`.

## Objetivo

Memorizar con práctica los registros de argumentos y el de retorno (`rax`).

## Pasos

### 1. Lectura (50 min)

Tabla de registros System V AMD64 (args + return). Guarda referencia en `notas/abi-sysv.md`.

### 2. Función de 3 args (70 min)

```c
long sum3(long a, long b, long c) { return a + b + c; }
```

Compila con `-S -O0` y busca dónde aparecen los args (L09 profundiza; hoy basta una pasada).

### 3. Tabla propia (40 min)

Completa: arg1→reg, …, retorno→reg. Sin mirar.

### 4. Commit (15 min)
""",
    hecho="""1. Tabla ABI en notas.
2. Al menos un `.s` o captura relacionada.
3. Commit.""",
    errores="""- Estudiar cdecl de 32-bit como si fuera Linux 64.
- Confundir Windows x64 ABI con System V.""",
    siguiente="[L07 — Heap: malloc, free y lifetime](L07-heap-malloc-free-y-lifetime.md)",
)

L(
    orden=7,
    slug="heap-malloc-free-y-lifetime",
    titulo="Heap: malloc, free y lifetime",
    horas=5.0,
    semana=2,
    lectura="man malloc; CSAPP dynamic memory intro",
    evidencia="src/heap_demo.c",
    body=r"""
El heap vive hasta `free` (o fin del proceso). Hoy practicas lifetime explícito.

## Objetivo

Programa que `malloc` / usa / `free`, y notas de use-after-free y leak.

## Pasos

### 1. Lectura (30 min)

`malloc`, `free`, `NULL` check básico.

### 2. Demo (100 min)

Alloca un array de `int`, llénalo, imprímelo, `free`. Intenta (en rama comentada) use-after-free y explica por qué es UB.

### 3. Leak consciente (40 min)

Omite un `free` a propósito; documenta cómo lo verías con sanitizer (L08).

### 4. Commit (15 min)
""",
    hecho="""1. `heap_demo.c` correcto compila y corre.
2. Notas de UAF/leak.
3. Commit.""",
    errores="""- `malloc` sin revisar `NULL` en código “serio”.
- Double-free.
- Devolver puntero a local (stack) pensando que es heap.""",
    siguiente="[L08 — UB y sanitizers ASan/UBSan (P2)](L08-ub-y-sanitizers-p2.md)",
)

L(
    orden=8,
    slug="ub-y-sanitizers-p2",
    titulo="UB y sanitizers ASan/UBSan (P2)",
    horas=5.0,
    semana=2,
    lectura="Clang/GCC sanitizers docs",
    evidencia="notas/sanitizer-p2.md — cierra P2",
    body=r"""
Los sanitizers transforman UB en errores ruidosos. Hoy cazas un bug a propósito.

## Objetivo

Cerrar **P2**: reproducir un error de memoria y ver el reporte de ASan o UBSan.

## Pasos

### 1. Lectura (30 min)

AddressSanitizer y UndefinedBehaviorSanitizer (idea).

### 2. Bug deliberado (60 min)

Programa con OOB write o UAF **solo en** `src/bug_demo.c` (nunca en libs).

### 3. Compila con sanitizer (60 min)

```bash
gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug src/bug_demo.c
./out/bug
```

Pega el resumen del reporte en `notas/sanitizer-p2.md` (sin dumps enormes).

### 4. Arregla y verifica limpio (40 min)

### 5. Commit (15 min)
""",
    hecho="""1. Tienes reporte de sanitizer + versión arreglada.
2. Notas P2 completas.
3. Commit.""",
    errores="""- Dejar el bug sin arreglar como único artefacto.
- Correr sin `-g` y no entender el stack trace.
- Pensar que sanitizer = antivirus.""",
    siguiente="[L09 — De C a asm con -S y objdump](L09-de-c-a-asm-con-s-y-objdump.md)",
)

L(
    orden=9,
    slug="de-c-a-asm-con-s-y-objdump",
    titulo="De C a asm con -S y objdump",
    horas=5.0,
    semana=3,
    lectura="man gcc (-S); man objdump",
    evidencia="asm/sum3.s generado por tu gcc",
    body=r"""
El compilador es un traductor. Hoy le pides el asm y lo guardas.

## Objetivo

Generar y guardar asm de una función pequeña; listar símbolos con `objdump`.

## Pasos

### 1. Genera asm (45 min)

```bash
gcc -Wall -Wextra -O0 -S -o asm/sum3.s src/sum3.c   # crea sum3.c si falta
```

### 2. objdump (60 min)

```bash
gcc -Wall -g -O0 -c -o out/sum3.o src/sum3.c
objdump -d out/sum3.o | head -n 80
```

Guarda extracto en `asm/sum3-objdump.txt`.

### 3. Compara Godbolt (45 min)

Misma función en [godbolt.org](https://godbolt.org/) con gcc -O0. Nota diferencias cosméticas.

### 4. Commit (15 min)
""",
    hecho="""1. `asm/sum3.s` en git.
2. Extracto objdump guardado.
3. Commit.""",
    errores="""- Commitear solo el binario.
- Leer asm de ARM pensando que es x86 (documenta tu ISA).""",
    siguiente="[L10 — Registros x86-64 y mov/add/call](L10-registros-x86-64-y-mov-add-call.md)",
)

L(
    orden=10,
    slug="registros-x86-64-y-mov-add-call",
    titulo="Registros x86-64 y mov/add/call",
    horas=5.0,
    semana=3,
    lectura="CSAPP machine-level: mov, add, call/ret",
    evidencia="notas/asm-basico.md",
    body=r"""
Pocas instrucciones bastan para leer el 80% del asm de estudiantes.

## Objetivo

Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop` (idea), registros `rax`…`r9`.

## Pasos

### 1. Lectura (60 min)

Enfócate en transferencias y llamadas.

### 2. Anota tu `sum3.s` (90 min)

Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a lado.

### 3. Quiz auto (30 min)

Sin mirar: ¿dónde está el return value? ¿primer argumento?

### 4. Commit (15 min)
""",
    hecho="""1. Asm anotado o notas equivalentes.
2. Respondiste el auto-quiz en notas.
3. Commit.""",
    errores="""- Memorizar encoding de opcodes.
- Ignorar que AT&T (`gcc -S`) pone dest a la derecha.""",
    siguiente="[L11 — Optimización -O0 vs -O2](L11-optimizacion-o0-vs-o2.md)",
)

L(
    orden=11,
    slug="optimizacion-o0-vs-o2",
    titulo="Optimización -O0 vs -O2 (lectura)",
    horas=5.0,
    semana=3,
    lectura="Comparar -O0/-O2 en Godbolt",
    evidencia="notas/o0-vs-o2.md",
    body=r"""
`-O2` borra tu “historia pedagógica” del asm. Hoy contrastas.

## Objetivo

Misma función en `-O0` y `-O2`; lista 3 diferencias observables.

## Pasos

### 1. Genera ambos (60 min)

```bash
gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
diff -u asm/sum3-O0.s asm/sum3-O2.s | head
```

### 2. Escribe (90 min)

En notas: ¿inlining? ¿menos spills a stack? ¿instrucciones totales?

### 3. Regla de estudio (30 min)

“Para aprender ABI uso `-O0`; para rendimiento miro `-O2`”.

### 4. Commit (15 min)
""",
    hecho="""1. Dos archivos `.s` o diff documentado.
2. ≥3 diferencias escritas.
3. Commit.""",
    errores="""- Depurar asm -O2 sin símbolos claros el primer día.
- Creer que -O0 es “lo que corre en producción”.""",
    siguiente="[L12 — Lab: anotar calling convention (P3)](L12-lab-anotar-calling-convention-p3.md)",
)

L(
    orden=12,
    slug="lab-anotar-calling-convention-p3",
    titulo="Lab: anotar calling convention (P3)",
    horas=5.0,
    semana=3,
    lectura="Repaso ABI System V",
    evidencia="asm anotado — cierra P3",
    body=r"""
Cierras **P3**: una función tuya con args en registros etiquetados.

## Objetivo

Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1 rdi */` etc.

## Pasos

### 1. Escribe función de dominio (60 min)

Ej. `cita_hash(cliente_id, servicio_id, ts)` que combine tres `long` (inventa la fórmula).

### 2. Genera y anota (120 min)

Asm comentado en `asm/cita_hash-anotado.s` (o `.md` con bloques).

### 3. Checklist P3 en README (30 min)

### 4. Commit (15 min)
""",
    hecho="""1. Asm anotado con registros de args y `rax` de retorno.
2. README marca P3.
3. Commit.""",
    errores="""- Anotar un asm de internet que no compilaste tú.
- Usar -O2 y perder los movs de args.""",
    siguiente="[L13 — Compilar vs linkar: .o y librerías](L13-compilar-vs-linkar.md)",
)

L(
    orden=13,
    slug="compilar-vs-linkar",
    titulo="Compilar vs linkar: .o y librerías",
    horas=5.0,
    semana=4,
    lectura="CSAPP linking intro; man ld",
    evidencia="two-file program .o + link",
    body=r"""
Compilar (.c→.o) y linkar (.o→exe) son pasos distintos.

## Objetivo

Dos `.c` + un header; producir `.o` separados y linkar a un ejecutable.

## Pasos

### 1. Split (90 min)

`util.c` / `util.h` / `main.c`. Compila por partes:

```bash
gcc -Wall -c -o out/util.o src/util.c
gcc -Wall -c -o out/main.o src/main.c
gcc -o out/prog out/main.o out/util.o
```

### 2. Error de link a propósito (45 min)

Quita un símbolo y lee el error del linker. Anótalo.

### 3. Notas (40 min)

`notas/linking.md`: compile vs link en 6 líneas.

### 4. Commit (15 min)
""",
    hecho="""1. Programa multiparche corre.
2. Error de link documentado.
3. Commit.""",
    errores="""- Incluir `.c` desde otro `.c` en vez de linkar.
- Confundir error de compile con undefined reference.""",
    siguiente="[L14 — ELF con readelf](L14-elf-con-readelf.md)",
)

L(
    orden=14,
    slug="elf-con-readelf",
    titulo="ELF con readelf (headers)",
    horas=5.0,
    semana=4,
    lectura="man readelf; ELF overview",
    evidencia="notas/elf.md con salida readelf",
    body=r"""
En Linux el ejecutable es ELF. Hoy miras headers sin miedo.

## Objetivo

`readelf -h` y `readelf -S` (o `-s`) sobre tu binario; interpreta 5 campos.

## Pasos

### 1. Headers (60 min)

```bash
readelf -h out/hello
readelf -S out/hello | head
```

### 2. Símbolos (60 min)

```bash
nm out/hello | head
readelf -s out/hello | head -n 40
```

### 3. Notas (60 min)

Qué es entry point, secciones `.text` / `.data` / `.bss` en tus palabras.

### 4. Commit (15 min)
""",
    hecho="""1. Salidas pegadas (recortadas) en notas.
2. Explicas `.text` vs `.data`.
3. Commit.""",
    errores="""- Analizar un binario stripped sin contexto el primer día.
- En macOS: usa `otool`/`size` y documenta que no es ELF.""",
    siguiente="[L15 — Cómo el SO carga un binario](L15-como-el-so-carga-un-binario.md)",
)

L(
    orden=15,
    slug="como-el-so-carga-un-binario",
    titulo="Cómo el SO carga un binario",
    horas=5.0,
    semana=4,
    lectura="CSAPP: loading; man execve",
    evidencia="notas/loader.md",
    body=r"""
`./out/hello` pide al kernel un `exec`. Hoy unes M11 (procesos) con el formato ELF.

## Objetivo

Narrativa paso a paso: shell → `execve` → loader → `_start` → `main` → `exit`.

## Pasos

### 1. Lectura (50 min)

Loading / process image.

### 2. Observa (60 min)

```bash
strace -e execve,exit_group ./out/hello
```

(o `strace ./out/hello 2>&1 | head`).

### 3. Escribe (70 min)

`notas/loader.md` con el viaje. Enlaza M11.

### 4. Commit (15 min)
""",
    hecho="""1. Nota loader completa.
2. Al menos una línea real de `strace` o equivalente.
3. Commit.""",
    errores="""- Decir que el compilador “ejecuta” el programa.
- Ignorar que el dynamic linker también carga libc.""",
    siguiente="[L16 — Syscalls vs libc](L16-syscalls-vs-libc.md)",
)

L(
    orden=16,
    slug="syscalls-vs-libc",
    titulo="Syscalls vs libc",
    horas=5.0,
    semana=4,
    lectura="man 2 write; man 3 printf",
    evidencia="notas/syscall-vs-libc.md",
    body=r"""
`printf` no es syscall: es libc que eventualmente llama `write`.

## Objetivo

Contrastar una llamada de biblioteca con la syscall subyacente vista en `strace`.

## Pasos

### 1. strace write (60 min)

Programa con `write(1, …)` vs `puts`. Compara rastros.

### 2. Notas (90 min)

Tabla: API C → libc → syscall (ejemplos: open/read/write/exit).

### 3. Puente AppSec (30 min)

Una frase: validar en tu código no basta si pasas buffers mal a APIs C.

### 4. Commit (15 min)
""",
    hecho="""1. Tabla syscall vs libc.
2. Evidencia strace.
3. Commit.""",
    errores="""- Llamar “syscall” a cualquier función de libc.
- Usar syscall numbers crudos sin necesidad.""",
    siguiente="[L17 — Documentar un stack frame real](L17-documentar-un-stack-frame-real.md)",
)

L(
    orden=17,
    slug="documentar-un-stack-frame-real",
    titulo="Documentar un stack frame real",
    horas=5.0,
    semana=5,
    lectura="Repaso stack + ABI",
    evidencia="notas/frame-real.md",
    body=r"""
Síntesis parcial: un frame de **tu** función con evidencias cruzadas (C + asm + diagrama).

## Objetivo

Paquete corto: fuente, asm `-O0`, diagrama, lista de slots (retorno, regs, locals).

## Pasos

### 1. Elige función (20 min)

Una de P3 o `sum3`.

### 2. Empaqueta (150 min)

`notas/frame-real.md` con los tres artefactos.

### 3. Revisión (40 min)

¿Podrías explicarlo en voz alta en 5 minutos?

### 4. Commit (15 min)
""",
    hecho="""1. `frame-real.md` completo.
2. Commit.""",
    errores="""- Diagrama que no coincide con el asm.
- Mezclar -O2 en la evidencia del frame didáctico.""",
    siguiente="[L18 — Viaje de un binario y cierre M27](L18-viaje-de-un-binario-y-cierre.md)",
)

L(
    orden=18,
    slug="viaje-de-un-binario-y-cierre",
    titulo="Viaje de un binario y cierre M27",
    horas=5.0,
    semana=5,
    lectura="Síntesis proyecto",
    evidencia="viaje-binario.md — cierra proyecto M27",
    body=r"""
Cierras el **proyecto**: el relato completo compile → link → run, con puente a M18 y M28.

## Objetivo

`viaje-binario.md` + README actualizado; checklist P1–P3 verde.

## Pasos

### 1. Escribe el viaje (120 min)

Plantilla del scaffold: pregunta → comandos → asm extracto → diagrama → riesgos → siguiente (M28 compiladores).

### 2. Checklist (60 min)

P1 buffers, P2 sanitizer, P3 ABI, proyecto.

### 3. Simulación (40 min)

Otro “yo” solo con README: ¿compila hello?

### 4. Commit de cierre (15 min)

```bash
git commit -am "docs(m27): cierre viaje de un binario"
```
""",
    hecho="""1. `viaje-binario.md` existe y está enlazado.
2. P1–P3 referenciados.
3. Commit de cierre.""",
    errores="""- Informe sin comandos reproducibles.
- Marcar proyecto sin asm ni diagrama.""",
    siguiente="Cierra la [ficha M27](../M27-sistemas-bajo-nivel.md). Siguiente en el plan: **M12** (o M28 cuando exista).",
)


def write_scaffold():
    PROJ.mkdir(parents=True, exist_ok=True)
    (PROJ / "src").mkdir(exist_ok=True)
    (PROJ / "asm").mkdir(exist_ok=True)
    (PROJ / "notas").mkdir(exist_ok=True)
    (PROJ / "out").mkdir(exist_ok=True)
    (PROJ / ".gitignore").write_text("out/\n*.o\n*.out\na.out\n.DS_Store\n", encoding="utf-8")
    (PROJ / "src" / "hello.c").write_text(
        '#include <stdio.h>\n\nint main(void) {\n  puts("hola m27");\n  return 0;\n}\n',
        encoding="utf-8",
    )
    (PROJ / "src" / "sum3.c").write_text(
        "long sum3(long a, long b, long c) {\n  return a + b + c;\n}\n",
        encoding="utf-8",
    )
    (PROJ / "viaje-binario.md").write_text(
        """# Viaje de un binario (proyecto M27)

## Comandos (compile / link)

```bash
# pega los tuyos
```

## Extracto asm

```asm
# función elegida, -O0
```

## Diagrama

```
fuente.c → .o → ejecutable → proceso (loader) → main → exit
```

## Riesgo de memoria (puente M18)

-

## Qué hace el compilador aquí (puente M28)

-
""",
        encoding="utf-8",
    )
    (PROJ / "README.md").write_text(
        """# M27 — Sistemas a bajo nivel

Evidencia: C, asm generado, sanitizers y el informe del binario.

## Arranque

```bash
cd projects/m27-bajo-nivel
gcc -Wall -Wextra -g -O0 -o out/hello src/hello.c
./out/hello
```

Requiere Linux o WSL2 x86-64 (recomendado). Documenta si usas otra ISA.

## Estructura

```
src/     código C
asm/     .s y extractos objdump
notas/   diagrams, ABI, sanitizer
out/     binarios (gitignored)
viaje-binario.md
```

## Lecciones → artefactos

| Semana | Lecciones | Artefactos |
|--------|-----------|------------|
| 1 | L01–L04 | hello, sizes, pointers, buffers (P1) |
| 2 | L05–L08 | stack/heap demos + sanitizer (P2) |
| 3 | L09–L12 | asm anotado (P3) |
| 4 | L13–L16 | linking, ELF, loader, syscalls |
| 5 | L17–L18 | frame-real + viaje-binario |

## Checklist

- **P1:** tipos/punteros/buffers en `src/` + `notas/p1.md`
- **P2:** `notas/sanitizer-p2.md`
- **P3:** asm calling convention anotado
- **Proyecto:** `viaje-binario.md`

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M27-sistemas-bajo-nivel.md`
- Plan: `/materia/M27/`
""",
        encoding="utf-8",
    )
    print("scaffold", PROJ.relative_to(ROOT))


def patch_docs():
    # bibliografia
    bib = CUR / "bibliografia.md"
    text = bib.read_text(encoding="utf-8")
    if "m27-sistemas-a-bajo-nivel" not in text:
        text = text.replace(
            "| M11 | Sistemas operativos | [→](#m11-sistemas-operativos) |\n| M12 |",
            "| M11 | Sistemas operativos | [→](#m11-sistemas-operativos) |\n| M27 | Sistemas a bajo nivel | [→](#m27-sistemas-a-bajo-nivel) |\n| M12 |",
        )
        block = """
## M27 — Sistemas a bajo nivel

- **Principal:** *Computer Systems: A Programmer's Perspective* (CSAPP) — Bryant & O'Hallaron
- **Gratis:** [Compiler Explorer](https://godbolt.org/) · docs GCC/Clang · `man gcc` / `man readelf`
- **Ficha:** [M27](etapas/02-disciplinaria/M27-sistemas-bajo-nivel.md)

"""
        text = text.replace(
            "## M12 — Requerimientos",
            block + "## M12 — Requerimientos",
        )
        bib.write_text(text, encoding="utf-8")
        print("bibliografia: M27")

    # INDEX
    idx = CUR / "INDEX.md"
    t = idx.read_text(encoding="utf-8")
    t = t.replace("26 materias", "27 materias")
    t = t.replace(
        "2. [Etapa Disciplinaria](etapas/02-disciplinaria/README.md) — M07–M20 (~11–13 meses)",
        "2. [Etapa Disciplinaria](etapas/02-disciplinaria/README.md) — M07–M20 + **M27** (~12–14 meses)",
    )
    if "M27" not in t.split("Pista de ciberseguridad")[0]:
        t = t.replace(
            "**Producto / capstone:**",
            "**Sistemas profundos:** [M05](etapas/01-basica/M05-organizacion-computadoras.md) → [M11](etapas/02-disciplinaria/M11-sistemas-operativos.md) → [M27 Bajo nivel](etapas/02-disciplinaria/M27-sistemas-bajo-nivel.md) → (luego) M28 compiladores\n\n**Producto / capstone:**",
        )
    idx.write_text(t, encoding="utf-8")
    print("INDEX updated")

    # etapa README
    er = CUR / "etapas/02-disciplinaria/README.md"
    et = er.read_text(encoding="utf-8")
    if "M27" not in et:
        et = et.replace(
            "| M11 | [Sistemas operativos](M11-sistemas-operativos.md) | 4 | 80 |\n| M12 |",
            "| M11 | [Sistemas operativos](M11-sistemas-operativos.md) | 4 | 80 |\n| M27 | [Sistemas a bajo nivel](M27-sistemas-bajo-nivel.md) | 5 | 100 |\n| M12 |",
        )
        et = et.replace(
            "**Duración:** ~11–13 meses @ ≥20 h/semana.",
            "**Duración:** ~12–14 meses @ ≥20 h/semana (incluye M27).",
        )
        er.write_text(et, encoding="utf-8")
        print("etapa README")

    # projects README
    pr = ROOT / "projects/README.md"
    pt = pr.read_text(encoding="utf-8")
    if "m27" not in pt:
        pt = pt.replace(
            "| M11 | [`m11-so/`](m11-so/) |\n| M12 |",
            "| M11 | [`m11-so/`](m11-so/) |\n| M27 | [`m27-bajo-nivel/`](m27-bajo-nivel/) |\n| M12 |",
        )
        pr.write_text(pt, encoding="utf-8")
        print("projects README")


def bridge_m05_m11():
    m05 = CUR / "etapas/01-basica/M05-organizacion-computadoras.md"
    t = m05.read_text(encoding="utf-8")
    if "M27" not in t:
        t = t.replace(
            "## Criterios de dominio",
            """## Siguiente profundidad

Cuando termines M11, continúa en **[M27 — Sistemas a bajo nivel](../02-disciplinaria/M27-sistemas-bajo-nivel.md)** (C, asm x86-64, linking). M05 es el mapa; M27 es bajar al terreno.

## Criterios de dominio""",
        )
        m05.write_text(t, encoding="utf-8")
        print("bridge M05")

    m11 = CUR / "etapas/02-disciplinaria/M11-sistemas-operativos.md"
    t = m11.read_text(encoding="utf-8")
    if "M27" not in t:
        # find Siguiente or end criteria
        if "## Criterios de dominio" in t:
            t = t.replace(
                "## Criterios de dominio",
                """## Siguiente

**[M27 — Sistemas a bajo nivel](M27-sistemas-bajo-nivel.md)** (recomendado antes de seguir a M12 si quieres profundidad de sistemas). Luego M12 requerimientos / hilo Agenda Ops.

## Criterios de dominio""",
            )
        m11.write_text(t, encoding="utf-8")
        print("bridge M11")


def main():
    update_catalog()
    FICHA.write_text(FICHA_MD.lstrip(), encoding="utf-8")
    print("ficha", FICHA.relative_to(ROOT))
    write_scaffold()
    for spec in LESSONS:
        write_lesson(**spec)
    patch_docs()
    bridge_m05_m11()
    print("done lessons", len(LESSONS))


if __name__ == "__main__":
    main()
