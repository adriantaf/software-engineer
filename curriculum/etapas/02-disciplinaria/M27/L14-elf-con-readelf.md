---
id: L14
materia: M27
orden: 14
titulo: ELF con readelf (headers)
horas: 5.0
semana: 4
lectura: man readelf; ELF overview
evidencia: notas/elf.md con salida readelf
---

# L14 — ELF con readelf (headers)

**~5.0 h · Semana 4**

En Linux el ejecutable es ELF. Hoy miras headers sin miedo.

## Objetivo

`readelf -h` y `readelf -S` (o `-s`) sobre tu binario; interpreta 5 campos.

## Pasos

### 1. Headers (60 min)

```bash
readelf -h out/hello
readelf -S out/hello | head
```

### 2. Símbolos (60 min)

```bash
nm out/hello | head
readelf -s out/hello | head -n 40
```

### 3. Notas (60 min)

Qué es entry point, secciones `.text` / `.data` / `.bss` en tus palabras.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man readelf; ELF overview | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Salidas pegadas (recortadas) en notas.
2. Explicas `.text` vs `.data`.
3. Commit.

## Errores comunes

- Analizar un binario stripped sin contexto el primer día.
- En macOS: usa `otool`/`size` y documenta que no es ELF.

## Siguiente

[L15 — Cómo el SO carga un binario](L15-como-el-so-carga-un-binario.md)
