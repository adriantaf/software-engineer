---
id: L14
materia: M27
orden: 14
titulo: ELF con readelf (headers)
horas: 5
semana: 4
lectura: man readelf; ELF overview
evidencia: notas/elf.md con salida readelf
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      En Linux el ejecutable es ELF. Hoy miras headers sin miedo.


      **Objetivo de esta lección:** `readelf -h` y `readelf -S` (o `-s`) sobre
      tu binario; interpreta 5 campos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Headers
    xp: 10
    cuerpo: |-
      ```bash
      readelf -h out/hello
      readelf -S out/hello | head
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Símbolos
    xp: 10
    cuerpo: |-
      ```bash
      nm out/hello | head
      readelf -s out/hello | head -n 40
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «ELF con readelf (headers)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de ELF con readelf
          (headers)
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
      ¿Es recomendable en esta lección? “Analizar un binario stripped sin
      contexto el primer día."
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
          `readelf -h` y `readelf -S` (o `-s`) sobre tu binario; interpreta 5
          campos.
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
    cuerpo: 'Qué es entry point, secciones `.text` / `.data` / `.bss` en tus palabras.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Salidas pegadas (recortadas) en notas.
      - Explicas `.text` vs `.data`.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — ELF con readelf (headers)

**~5.0 h · Semana 4**

En Linux el ejecutable es ELF. Hoy miras headers sin miedo.

## Objetivo

`readelf -h` y `readelf -S` (o `-s`) sobre tu binario; interpreta 5 campos.

## Pasos

### 1. Headers (60 min)

```bash
readelf -h out/hello
readelf -S out/hello | head
```

### 2. Símbolos (60 min)

```bash
nm out/hello | head
readelf -s out/hello | head -n 40
```

### 3. Notas (60 min)

Qué es entry point, secciones `.text` / `.data` / `.bss` en tus palabras.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man readelf; ELF overview | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Salidas pegadas (recortadas) en notas.
2. Explicas `.text` vs `.data`.
3. Commit.

## Errores comunes

- Analizar un binario stripped sin contexto el primer día.
- En macOS: usa `otool`/`size` y documenta que no es ELF.

## Siguiente

[L15 — Cómo el SO carga un binario](L15-como-el-so-carga-un-binario.md)
