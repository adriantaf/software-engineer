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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dos `.c` + un header; producir `.o` separados y linkar a un
      ejecutable.


      Compilar (.c→.o) y linkar (.o→exe) son pasos distintos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Split
    xp: 10
    cuerpo: |-
      ```bash
      gcc -Wall -c -o out/util.o src/util.c
      gcc -Wall -c -o out/main.o src/main.c
      gcc -o out/prog out/main.o out/util.o
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Compilar vs linkar: .o y librerías" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: two-file program .o + link
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
      ¿Es buena práctica en esta lección? “Incluir `.c` desde otro `.c` en vez
      de linkar."
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
          Dos `.c` + un header; producir `.o` separados y linkar a un
          ejecutable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Error de link a propósito
    xp: 10
    cuerpo: Quita un símbolo y lee el error del linker. Anótalo.
  - id: s7
    tipo: explicacion
    titulo: 3. Notas
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
