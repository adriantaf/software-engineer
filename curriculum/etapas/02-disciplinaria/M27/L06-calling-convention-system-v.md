---
id: L06
materia: M27
orden: 6
titulo: Calling convention System V AMD64
horas: 5.0
semana: 2
lectura: System V AMD64 ABI — argument registers
evidencia: notas/abi-sysv.md
---

# L06 — Calling convention System V AMD64

**~5.0 h · Semana 2**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | System V AMD64 ABI — argument registers | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla ABI en notas.
2. Al menos un `.s` o captura relacionada.
3. Commit.

## Errores comunes

- Estudiar cdecl de 32-bit como si fuera Linux 64.
- Confundir Windows x64 ABI con System V.

## Siguiente

[L07 — Heap: malloc, free y lifetime](L07-heap-malloc-free-y-lifetime.md)
