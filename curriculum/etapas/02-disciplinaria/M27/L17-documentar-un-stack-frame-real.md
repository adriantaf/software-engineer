---
id: L17
materia: M27
orden: 17
titulo: Documentar un stack frame real
horas: 5.0
semana: 5
lectura: Repaso stack + ABI
evidencia: notas/frame-real.md
---

# L17 — Documentar un stack frame real

**~5.0 h · Semana 5**

Síntesis parcial: un frame de **tu** función con evidencias cruzadas (C + asm + diagrama).

## Objetivo

Paquete corto: fuente, asm `-O0`, diagrama, lista de slots (retorno, regs, locals).

## Pasos

### 1. Elige función (20 min)

Una de P3 o `sum3`.

### 2. Empaqueta (150 min)

`notas/frame-real.md` con los tres artefactos.

### 3. Revisión (40 min)

¿Podrías explicarlo en voz alta en 5 minutos?

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Repaso stack + ABI | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `frame-real.md` completo.
2. Commit.

## Errores comunes

- Diagrama que no coincide con el asm.
- Mezclar -O2 en la evidencia del frame didáctico.

## Siguiente

[L18 — Viaje de un binario y cierre M27](L18-viaje-de-un-binario-y-cierre.md)
