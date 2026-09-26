# M27 — Sistemas a bajo nivel

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
