---
id: L05
materia: M27
orden: 5
titulo: Stack frames intro
horas: 5.0
semana: 2
lectura: "CSAPP: stack frame / machine-level intro"
evidencia: notas/stack-frame.md + src/stack_demo.c
---

# L05 — Stack frames intro

**~5.0 h · Semana 2**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: stack frame / machine-level intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Demo corre; anotaste el orden de direcciones.
2. Diagrama de frames en notas.
3. Commit.

## Errores comunes

- Creer que “el stack” es una estructura de datos de C.
- Confundir stack del proceso con call stack de JS async.

## Siguiente

[L06 — Calling convention System V AMD64](L06-calling-convention-system-v.md)
