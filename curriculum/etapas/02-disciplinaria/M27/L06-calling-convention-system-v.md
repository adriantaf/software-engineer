---
id: L06
materia: M27
orden: 6
titulo: Calling convention System V AMD64
horas: 5
semana: 2
lectura: System V AMD64 ABI — argument registers
evidencia: notas/abi-sysv.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Memorizar con práctica los registros de argumentos y el de
      retorno (`rax`).


      En Linux x86-64 los primeros args van en registros: `rdi, rsi, rdx, rcx,
      r8, r9`.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```c
      long sum3(long a, long b, long c) { return a + b + c; }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Calling convention System V AMD64" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/abi-sysv.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Estudiar cdecl de 32-bit como si
      fuera Linux 64."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Memorizar con práctica los registros de argumentos y el de retorno
          (`rax`).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Función de 3 args
    xp: 10
    cuerpo: >-
      ```c

      long sum3(long a, long b, long c) { return a + b + c; }

      ```


      Compila con `-S -O0` y busca dónde aparecen los args (L09 profundiza; hoy
      basta una pasada).
  - id: s7
    tipo: explicacion
    titulo: 3. Tabla propia
    xp: 10
    cuerpo: 'Completa: arg1→reg, …, retorno→reg. Sin mirar.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Tabla ABI en notas.
      - Al menos un `.s` o captura relacionada.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Calling convention System V AMD64

**~5.0 h · Semana 2**

En Linux x86-64 los primeros args van en registros: `rdi, rsi, rdx, rcx, r8, r9`.

## Objetivo

Memorizar con práctica los registros de argumentos y el de retorno (`rax`).

## Pasos

### 1. Lectura (50 min)

Tabla de registros System V AMD64 (args + return). Guarda referencia en `notas/abi-sysv.md`.

### 2. Función de 3 args (70 min)

```c
long sum3(long a, long b, long c) { return a + b + c; }
```

Compila con `-S -O0` y busca dónde aparecen los args (L09 profundiza; hoy basta una pasada).

### 3. Tabla propia (40 min)

Completa: arg1→reg, …, retorno→reg. Sin mirar.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | System V AMD64 ABI — argument registers | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla ABI en notas.
2. Al menos un `.s` o captura relacionada.
3. Commit.

## Errores comunes

- Estudiar cdecl de 32-bit como si fuera Linux 64.
- Confundir Windows x64 ABI con System V.

## Siguiente

[L07 — Heap: malloc, free y lifetime](L07-heap-malloc-free-y-lifetime.md)
