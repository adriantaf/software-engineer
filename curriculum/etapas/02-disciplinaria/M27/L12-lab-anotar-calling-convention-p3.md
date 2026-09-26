---
id: L12
materia: M27
orden: 12
titulo: "Lab: anotar calling convention (P3)"
horas: 5.0
semana: 3
lectura: Repaso ABI System V
evidencia: asm anotado — cierra P3
---

# L12 — Lab: anotar calling convention (P3)

**~5.0 h · Semana 3**

Cierras **P3**: una función tuya con args en registros etiquetados.

## Objetivo

Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1 rdi */` etc.

## Pasos

### 1. Escribe función de dominio (60 min)

Ej. `cita_hash(cliente_id, servicio_id, ts)` que combine tres `long` (inventa la fórmula).

### 2. Genera y anota (120 min)

Asm comentado en `asm/cita_hash-anotado.s` (o `.md` con bloques).

### 3. Checklist P3 en README (30 min)

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Repaso ABI System V | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Asm anotado con registros de args y `rax` de retorno.
2. README marca P3.
3. Commit.

## Errores comunes

- Anotar un asm de internet que no compilaste tú.
- Usar -O2 y perder los movs de args.

## Siguiente

[L13 — Compilar vs linkar: .o y librerías](L13-compilar-vs-linkar.md)
