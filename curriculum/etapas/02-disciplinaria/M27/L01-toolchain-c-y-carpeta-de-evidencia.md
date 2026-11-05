---
id: L01
materia: M27
orden: 1
titulo: Toolchain C y carpeta de evidencia
horas: 5
semana: 1
lectura: CSAPP intro / tooling; man gcc
evidencia: projects/m27-bajo-nivel/ con hello.c que compila
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Todo lo demás (asm, sanitizers, ELF) asume que puedes emitir un binario
      local.


      **Objetivo de esta lección:** Tener `gcc` o `clang`, carpeta
      `projects/m27-bajo-nivel/` y un `hello` que imprime y termina con código
      0.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Entorno
    xp: 10
    cuerpo: >-
      ```bash

      gcc --version || clang --version

      which gcc clang make

      ```


      En Linux/WSL: Si falta: `sudo apt update && sudo apt install
      build-essential gdb binutils` (o equivalente). Anota versiones en
      `projects/m27-bajo-nivel/entorno.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Scaffold
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}

      cp -n projects/m27-bajo-nivel/README.md projects/m27-bajo-nivel/README.md
      2>/dev/null || true

      ```


      Revisa el README del scaffold del plan.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Toolchain C y carpeta de evidencia», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Toolchain C y carpeta
          de evidencia
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}`
    comandoEsperado:
      - 'mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}'
      - >-
        cp -n projects/m27-bajo-nivel/README.md
        projects/m27-bajo-nivel/README.md 2>/dev/null || true
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}'
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
          Tener `gcc` o `clang`, carpeta `projects/m27-bajo-nivel/` y un `hello`
          que imprime y termina con código 0.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Hello
    xp: 10
    cuerpo: 'Crea `projects/m27-bajo-nivel/src/hello.c`:'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`gcc` o `clang` disponible; versión en `entorno.md`.'
      - '`out/hello` corre e imprime el mensaje.'
      - Commit con el scaffold + hello.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Toolchain C y carpeta de evidencia

**~5.0 h · Semana 1**

Sin toolchain no hay bajo nivel usable. Hoy dejas C compilando en tu máquina y evidencia en git.

## Objetivo

Tener `gcc` o `clang`, carpeta `projects/m27-bajo-nivel/` y un `hello` que imprime y termina con código 0.

## Por qué empieza así

Todo lo demás (asm, sanitizers, ELF) asume que puedes emitir un binario local.

## Pasos (hazlos en orden)

### 1. Entorno (30–40 min)

En Linux/WSL:

```bash
gcc --version || clang --version
which gcc clang make
```

Si falta: `sudo apt update && sudo apt install build-essential gdb binutils` (o equivalente).

Anota versiones en `projects/m27-bajo-nivel/entorno.md`.

### 2. Scaffold (20 min)

```bash
mkdir -p projects/m27-bajo-nivel/{src,asm,notas,out}
cp -n projects/m27-bajo-nivel/README.md projects/m27-bajo-nivel/README.md 2>/dev/null || true
```

Revisa el README del scaffold del plan.

### 3. Hello (45–60 min)

Crea `projects/m27-bajo-nivel/src/hello.c`:

```c
#include <stdio.h>

int main(void) {
  puts("hola m27");
  return 0;
}
```

```bash
cd projects/m27-bajo-nivel
gcc -Wall -Wextra -g -O0 -o out/hello src/hello.c
./out/hello
echo exit:$?
```

### 4. Flags en notas (40 min)

En `notas/flags.md`: qué hace `-Wall`, `-Wextra`, `-g`, `-O0` (una línea cada uno).

### 5. Commit (15 min)

```bash
git add projects/m27-bajo-nivel
git commit -m "feat(m27): toolchain y hello.c"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP intro / tooling; man gcc | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `gcc` o `clang` disponible; versión en `entorno.md`.
2. `out/hello` corre e imprime el mensaje.
3. Commit con el scaffold + hello.

## Errores comunes

- Instalar un IDE enorme y no compilar desde terminal.
- Commitear binarios `out/*` (debe estar en `.gitignore`).
- Usar un compilador online sin dejar evidencia local.

## Siguiente

[L02 — Tipos, sizeof y representación](L02-tipos-sizeof-y-representacion.md)
