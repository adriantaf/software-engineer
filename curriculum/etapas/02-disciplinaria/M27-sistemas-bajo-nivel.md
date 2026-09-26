---
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
