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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Generar y guardar asm de una función pequeña; listar
      símbolos con `objdump`.


      El compilador es un traductor. Hoy le pides el asm y lo guardas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Genera asm
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -Wextra -O0 -S -o asm/sum3.s src/sum3.c   # crea sum3.c si falta
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "De C a asm con -S y objdump" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: asm/sum3.s generado por tu gcc
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
    pregunta: ¿Es buena práctica en esta lección? “Commitear solo el binario."
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
          Generar y guardar asm de una función pequeña; listar símbolos con
          `objdump`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. objdump
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -g -O0 -c -o out/sum3.o src/sum3.c
      objdump -d out/sum3.o | head -n 80
      ```

      Guarda extracto en `asm/sum3-objdump.txt`.
  - id: s7
    tipo: explicacion
    titulo: 3. Compara Godbolt
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
