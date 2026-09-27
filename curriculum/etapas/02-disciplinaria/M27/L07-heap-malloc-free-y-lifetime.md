---
id: L07
materia: M27
orden: 7
titulo: "Heap: malloc, free y lifetime"
horas: 5.0
semana: 2
lectura: man malloc; CSAPP dynamic memory intro
evidencia: src/heap_demo.c
---

# L07 — Heap: malloc, free y lifetime

**~5.0 h · Semana 2**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man malloc; CSAPP dynamic memory intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `heap_demo.c` correcto compila y corre.
2. Notas de UAF/leak.
3. Commit.

## Errores comunes

- `malloc` sin revisar `NULL` en código “serio”.
- Double-free.
- Devolver puntero a local (stack) pensando que es heap.

## Siguiente

[L08 — UB y sanitizers ASan/UBSan (P2)](L08-ub-y-sanitizers-p2.md)
