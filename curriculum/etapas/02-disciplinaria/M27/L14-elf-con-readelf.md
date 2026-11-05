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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `readelf -h` y `readelf -S` (o `-s`) sobre tu binario;
      interpreta 5 campos.


      En Linux el ejecutable es ELF. Hoy miras headers sin miedo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Headers
    xp: 10
    cuerpo: |-
      ```bash
      readelf -h out/hello
      readelf -S out/hello | head
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "ELF con readelf (headers)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: notas/elf.md con salida readelf
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
      ¿Es buena práctica en esta lección? “Analizar un binario stripped sin
      contexto el primer día."
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
          `readelf -h` y `readelf -S` (o `-s`) sobre tu binario; interpreta 5
          campos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Símbolos
    xp: 10
    cuerpo: |-
      ```bash
      nm out/hello | head
      readelf -s out/hello | head -n 40
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Notas
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
