---
id: L02
materia: M27
orden: 2
titulo: Tipos, sizeof y representación
horas: 5.0
semana: 1
lectura: "CSAPP: data sizes / integer representation intro"
evidencia: src/sizes.c + notas/sizes.md
---

# L02 — Tipos, sizeof y representación

**~5.0 h · Semana 1**

C hace visibles los anchos de tipo. Hoy mides y relacionas con M05 (enteros / overflow).

## Objetivo

Programa que imprime `sizeof` de tipos comunes y notas sobre signed vs unsigned.

## Pasos

### 1. Lectura corta (40 min)

CSAPP (tamaños de datos) o equivalen docs. Relaciona con lo que viste en M05.

### 2. `sizes.c` (90 min)

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
  printf("char=%zu int=%zu long=%zu\n", sizeof(char), sizeof(int), sizeof(long));
  printf("void*=%zu size_t=%zu\n", sizeof(void*), sizeof(size_t));
  printf("int32=%zu int64=%zu\n", sizeof(int32_t), sizeof(int64_t));
  return 0;
}
```

Compila y pega la salida en `notas/sizes.md`. Explica por qué `long` puede diferir entre plataformas.

### 3. Overflow consciente (60 min)

Añade un ejemplo signed overflow (con comentario de que es UB en C) y uno unsigned que wrappea bien definido. Documenta la diferencia.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: data sizes / integer representation intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `sizes.c` corre; salida pegada en notas.
2. Explicas al menos una diferencia de tamaño entre plataformas.
3. Commit.

## Errores comunes

- Asumir que `int` siempre es 32 bits.
- Ignorar `stdint.h` cuando necesitas anchos fijos.
- Tratar overflow signed como “siempre wrappea”.

## Siguiente

[L03 — Punteros y direcciones](L03-punteros-y-direcciones.md)
