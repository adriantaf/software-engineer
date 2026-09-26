---
id: L11
materia: M27
orden: 11
titulo: Optimización -O0 vs -O2 (lectura)
horas: 5.0
semana: 3
lectura: Comparar -O0/-O2 en Godbolt
evidencia: notas/o0-vs-o2.md
---

# L11 — Optimización -O0 vs -O2 (lectura)

**~5.0 h · Semana 3**

`-O2` borra tu “historia pedagógica” del asm. Hoy contrastas.

## Objetivo

Misma función en `-O0` y `-O2`; lista 3 diferencias observables.

## Pasos

### 1. Genera ambos (60 min)

```bash
gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
diff -u asm/sum3-O0.s asm/sum3-O2.s | head
```

### 2. Escribe (90 min)

En notas: ¿inlining? ¿menos spills a stack? ¿instrucciones totales?

### 3. Regla de estudio (30 min)

“Para aprender ABI uso `-O0`; para rendimiento miro `-O2`”.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Comparar -O0/-O2 en Godbolt | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos archivos `.s` o diff documentado.
2. ≥3 diferencias escritas.
3. Commit.

## Errores comunes

- Depurar asm -O2 sin símbolos claros el primer día.
- Creer que -O0 es “lo que corre en producción”.

## Siguiente

[L12 — Lab: anotar calling convention (P3)](L12-lab-anotar-calling-convention-p3.md)
