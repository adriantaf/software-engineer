---
id: L09
materia: M27
orden: 9
titulo: De C a asm con -S y objdump
horas: 5.0
semana: 3
lectura: man gcc (-S); man objdump
evidencia: asm/sum3.s generado por tu gcc
---

# L09 — De C a asm con -S y objdump

**~5.0 h · Semana 3**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man gcc (-S); man objdump | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `asm/sum3.s` en git.
2. Extracto objdump guardado.
3. Commit.

## Errores comunes

- Commitear solo el binario.
- Leer asm de ARM pensando que es x86 (documenta tu ISA).

## Siguiente

[L10 — Registros x86-64 y mov/add/call](L10-registros-x86-64-y-mov-add-call.md)
