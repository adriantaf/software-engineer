---
id: L10
materia: M27
orden: 10
titulo: Registros x86-64 y mov/add/call
horas: 5.0
semana: 3
lectura: "CSAPP machine-level: mov, add, call/ret"
evidencia: notas/asm-basico.md
---

# L10 — Registros x86-64 y mov/add/call

**~5.0 h · Semana 3**

Pocas instrucciones bastan para leer el 80% del asm de estudiantes.

## Objetivo

Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop` (idea), registros `rax`…`r9`.

## Pasos

### 1. Lectura (60 min)

Enfócate en transferencias y llamadas.

### 2. Anota tu `sum3.s` (90 min)

Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a lado.

### 3. Quiz auto (30 min)

Sin mirar: ¿dónde está el return value? ¿primer argumento?

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP machine-level: mov, add, call/ret | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Asm anotado o notas equivalentes.
2. Respondiste el auto-quiz en notas.
3. Commit.

## Errores comunes

- Memorizar encoding de opcodes.
- Ignorar que AT&T (`gcc -S`) pone dest a la derecha.

## Siguiente

[L11 — Optimización -O0 vs -O2](L11-optimizacion-o0-vs-o2.md)
