---
id: L15
materia: M27
orden: 15
titulo: Cómo el SO carga un binario
horas: 5.0
semana: 4
lectura: "CSAPP: loading; man execve"
evidencia: notas/loader.md
---

# L15 — Cómo el SO carga un binario

**~5.0 h · Semana 4**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: loading; man execve | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Nota loader completa.
2. Al menos una línea real de `strace` o equivalente.
3. Commit.

## Errores comunes

- Decir que el compilador “ejecuta” el programa.
- Ignorar que el dynamic linker también carga libc.

## Siguiente

[L16 — Syscalls vs libc](L16-syscalls-vs-libc.md)
