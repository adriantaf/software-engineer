---
id: L09
materia: M27
orden: 9
titulo: De C a asm con -S y objdump
horas: 5
semana: 3
lectura: man gcc (-S); man objdump
evidencia: asm/sum3.s generado por tu gcc
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El compilador es un traductor. Hoy le pides el asm y lo guardas.


      **Objetivo de esta lección:** Generar y guardar asm de una función
      pequeña; listar símbolos con `objdump`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Genera asm
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -Wextra -O0 -S -o asm/sum3.s src/sum3.c   # crea sum3.c si falta
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: objdump
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -g -O0 -c -o out/sum3.o src/sum3.c
      objdump -d out/sum3.o | head -n 80
      ```

      Guarda extracto en `asm/sum3-objdump.txt`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «De C a asm con -S y objdump», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de De C a asm con -S y
          objdump
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
    pregunta: ¿Es recomendable en esta lección? “Commitear solo el binario."
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
          Generar y guardar asm de una función pequeña; listar símbolos con
          `objdump`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Compara Godbolt
    xp: 10
    cuerpo: >-
      Misma función en [godbolt.org](https://godbolt.org/) con gcc -O0. Nota
      diferencias cosméticas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`asm/sum3.s` en git.'
      - Extracto objdump guardado.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — De C a asm con -S y objdump

**~5.0 h · Semana 3**

El compilador es un traductor. Hoy le pides el asm y lo guardas.

## Objetivo

Generar y guardar asm de una función pequeña; listar símbolos con `objdump`.

## Pasos

### 1. Genera asm (45 min)

```bash
gcc -Wall -Wextra -O0 -S -o asm/sum3.s src/sum3.c   # crea sum3.c si falta
```

### 2. objdump (60 min)

```bash
gcc -Wall -g -O0 -c -o out/sum3.o src/sum3.c
objdump -d out/sum3.o | head -n 80
```

Guarda extracto en `asm/sum3-objdump.txt`.

### 3. Compara Godbolt (45 min)

Misma función en [godbolt.org](https://godbolt.org/) con gcc -O0. Nota diferencias cosméticas.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man gcc (-S); man objdump | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `asm/sum3.s` en git.
2. Extracto objdump guardado.
3. Commit.

## Errores comunes

- Commitear solo el binario.
- Leer asm de ARM pensando que es x86 (documenta tu ISA).

## Siguiente

[L10 — Registros x86-64 y mov/add/call](L10-registros-x86-64-y-mov-add-call.md)
