---
id: L04
materia: M27
orden: 4
titulo: Arrays, strings y buffers (P1)
horas: 5.0
semana: 1
lectura: "CSAPP: arrays/strings; man strncpy"
evidencia: src/buffers.c — cierra P1
---

# L04 — Arrays, strings y buffers (P1)

**~5.0 h · Semana 1**

Los strings C son buffers con terminador. Aquí nace buena parte de los overflows.

## Objetivo

Cerrar **P1**: arrays, `strlen`/`snprintf`, y una nota de por qué `gets` está prohibido.

## Pasos

### 1. Lectura (30 min)

Strings C y terminador `\\0`.

### 2. `buffers.c` (120 min)

- Copia segura con `snprintf` a un buffer fijo.
- Función que cuenta longitud sin `strlen` (recorrido hasta `\\0`).
- Comentario: qué pasaría con `strcpy` a buffer corto.

### 3. Evidencia P1 (45 min)

README o `notas/p1.md`: lista de archivos + qué demuestra cada uno (L01–L04).

### 4. Commit (15 min)

```bash
git commit -am "feat(m27): P1 buffers y strings"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: arrays/strings; man strncpy | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `buffers.c` compila con `-Wall` sin warnings nuevos.
2. Notas P1 enlazan L01–L04.
3. Commit.

## Errores comunes

- Usar `gets`.
- Olvidar espacio para `\0`.
- Cerrar P1 sin evidencia en git.

## Siguiente

[L05 — Stack frames intro](L05-stack-frames-intro.md)
