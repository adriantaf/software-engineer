---
id: L03
materia: M27
orden: 3
titulo: Punteros y direcciones
horas: 5.0
semana: 1
lectura: "CSAPP / K&R: pointers"
evidencia: src/pointers.c + diagrama en notas/
---

# L03 — Punteros y direcciones

**~5.0 h · Semana 1**

Un puntero es una dirección con tipo. Hoy dejas de temerle imprimiendo direcciones reales.

## Objetivo

Código que muestra `&x`, `*p`, aritmética básica de punteros a `int`, y un diagrama tuyo.

## Pasos

### 1. Lectura (40 min)

Punteros: declaración, `*`, `&`, `NULL`.

### 2. Experimentos (120 min)

En `src/pointers.c`: variable local, puntero a ella, modificar vía `*p`, array + aritmética `p+1`. Imprime valores y direcciones con `%p`.

### 3. Diagrama (45 min)

`notas/punteros.md`: dibuja stack con `x` y `p` (ASCII está bien).

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP / K&R: pointers | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Programa corre e imprime direcciones.
2. Diagrama en notas.
3. Commit.

## Errores comunes

- Dereferenciar `NULL`.
- Confundir `int *p` con “int que se llama *p”.
- Aritmética de punteros en `void*` sin cast.

## Siguiente

[L04 — Arrays, strings y buffers (P1)](L04-arrays-strings-y-buffers-p1.md)
