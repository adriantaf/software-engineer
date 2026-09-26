---
id: L13
materia: M27
orden: 13
titulo: "Compilar vs linkar: .o y librerías"
horas: 5.0
semana: 4
lectura: CSAPP linking intro; man ld
evidencia: two-file program .o + link
---

# L13 — Compilar vs linkar: .o y librerías

**~5.0 h · Semana 4**

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP linking intro; man ld | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Programa multiparche corre.
2. Error de link documentado.
3. Commit.

## Errores comunes

- Incluir `.c` desde otro `.c` en vez de linkar.
- Confundir error de compile con undefined reference.

## Siguiente

[L14 — ELF con readelf](L14-elf-con-readelf.md)
