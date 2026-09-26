---
id: L16
materia: M27
orden: 16
titulo: Syscalls vs libc
horas: 5.0
semana: 4
lectura: man 2 write; man 3 printf
evidencia: notas/syscall-vs-libc.md
---

# L16 — Syscalls vs libc

**~5.0 h · Semana 4**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man 2 write; man 3 printf | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla syscall vs libc.
2. Evidencia strace.
3. Commit.

## Errores comunes

- Llamar “syscall” a cualquier función de libc.
- Usar syscall numbers crudos sin necesidad.

## Siguiente

[L17 — Documentar un stack frame real](L17-documentar-un-stack-frame-real.md)
