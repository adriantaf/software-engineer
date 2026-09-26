---
id: L08
materia: M27
orden: 8
titulo: UB y sanitizers ASan/UBSan (P2)
horas: 5.0
semana: 2
lectura: Clang/GCC sanitizers docs
evidencia: notas/sanitizer-p2.md — cierra P2
---

# L08 — UB y sanitizers ASan/UBSan (P2)

**~5.0 h · Semana 2**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Clang/GCC sanitizers docs | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tienes reporte de sanitizer + versión arreglada.
2. Notas P2 completas.
3. Commit.

## Errores comunes

- Dejar el bug sin arreglar como único artefacto.
- Correr sin `-g` y no entender el stack trace.
- Pensar que sanitizer = antivirus.

## Siguiente

[L09 — De C a asm con -S y objdump](L09-de-c-a-asm-con-s-y-objdump.md)
