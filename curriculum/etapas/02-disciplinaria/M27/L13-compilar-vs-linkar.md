---
id: L13
materia: M27
orden: 13
titulo: 'Compilar vs linkar: .o y librerías'
horas: 5
semana: 4
lectura: CSAPP linking intro; man ld
evidencia: two-file program .o + link
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Compilar (.c→.o) y linkar (.o→exe) son pasos distintos.


      **Objetivo de esta lección:** Dos `.c` + un header; producir `.o`
      separados y linkar a un ejecutable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Split
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -c -o out/util.o src/util.c
      gcc -Wall -c -o out/main.o src/main.c
      gcc -o out/prog out/main.o out/util.o
      ```

      `util.c` / `util.h` / `main.c`. Compila por partes:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Error de link a propósito
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -c -o out/util.o src/util.c
      gcc -Wall -c -o out/main.o src/main.c
      gcc -o out/prog out/main.o out/util.o
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Compilar vs linkar: .o y librerías», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Compilar vs linkar: .o
          y librerías
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
      ¿Es recomendable en esta lección? “Incluir `.c` desde otro `.c` en vez de
      linkar."
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
          Dos `.c` + un header; producir `.o` separados y linkar a un
          ejecutable.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Notas
    xp: 10
    cuerpo: '`notas/linking.md`: compile vs link en 6 líneas.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Programa multiparche corre.
      - Error de link documentado.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Compilar vs linkar: .o y librerías

**~5.0 h · Semana 4**

Compilar (.c→.o) y linkar (.o→exe) son pasos distintos.

## Objetivo

Dos `.c` + un header; producir `.o` separados y linkar a un ejecutable.

## Pasos

### 1. Split (90 min)

`util.c` / `util.h` / `main.c`. Compila por partes:

```bash
gcc -Wall -c -o out/util.o src/util.c
gcc -Wall -c -o out/main.o src/main.c
gcc -o out/prog out/main.o out/util.o
```

### 2. Error de link a propósito (45 min)

Quita un símbolo y lee el error del linker. Anótalo.

### 3. Notas (40 min)

`notas/linking.md`: compile vs link en 6 líneas.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP linking intro; man ld | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Programa multiparche corre.
2. Error de link documentado.
3. Commit.

## Errores comunes

- Incluir `.c` desde otro `.c` en vez de linkar.
- Confundir error de compile con undefined reference.

## Siguiente

[L14 — ELF con readelf](L14-elf-con-readelf.md)
