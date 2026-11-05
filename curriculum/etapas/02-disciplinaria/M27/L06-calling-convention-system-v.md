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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      En Linux x86-64 los primeros args van en registros: `rdi, rsi, rdx, rcx,
      r8, r9`.


      **Objetivo de esta lección:** Memorizar con práctica los registros de
      argumentos y el de retorno (`rax`).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```c
      long sum3(long a, long b, long c) { return a + b + c; }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Función de 3 args
    xp: 10
    cuerpo: >-
      ```c

      long sum3(long a, long b, long c) { return a + b + c; }

      ```


      Compila con `-S -O0` y busca dónde aparecen los args (L09 profundiza; hoy
      basta una pasada).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Calling convention System V AMD64», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Calling convention
          System V AMD64
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Estudiar cdecl de 32-bit como si fuera
      Linux 64."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Memorizar con práctica los registros de argumentos y el de retorno
          (`rax`).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tabla propia
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
