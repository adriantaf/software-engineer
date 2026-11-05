---
id: L01
materia: M05
orden: 1
titulo: Modelo von Neumann e introducción
horas: 5
semana: 1
lectura: >-
  Stallings — intro y estructura/función del computador (caps. de introducción
  según tu ed.)
evidencia: >-
  projects/m05-como-corre/notas-L01.md con definiciones y primera lista de
  componentes
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin un mapa, “rendimiento” y “memoria” son etiquetas sueltas. Hoy
      construyes el mapa que usarás en las 11 lecciones siguientes.


      **Objetivo de esta lección:** Explicar el modelo von Neumann (programa y
      datos en memoria; CPU ejecuta secuencialmente) y enumerar los componentes
      principales de una máquina moderna.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura dirigida
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m05-como-corre
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Carpeta de evidencia
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m05-como-corre

      ```


      Crea `projects/m05-como-corre/notas-L01.md` con encabezado `# M05 — Notas
      L01`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Modelo von Neumann e introducción», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Existe `projects/m05-como-corre/notas-L01.md` con definiciones,
          diagrama (ASCII o imagen enlazada) y respuestas al ejercicio con
          `node`.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Modelo von Neumann e
          introducción
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

      `mkdir -p projects/m05-como-corre`
    comandoEsperado:
      - mkdir -p projects/m05-como-corre
      - node -e "console.log('hola arquitectura')"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m05-como-corre'
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
          Explicar el modelo von Neumann (programa y datos en memoria; CPU
          ejecuta secuencialmente) y enumerar los componentes principales de una
          máquina moderna.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Diagrama en borrador
    xp: 10
    cuerpo: >-
      En papel o en el mismo archivo, dibuja **cajas y flechas**: - CPU (dentro:
      UC + ALU + registros, aunque sea esquemático). - Memoria principal (RAM).
      - Módulos de E/S (disco, red, teclado/pantalla como ejemplos). - Bus que
      conecta CPU ↔ memoria ↔ E/S. Etiqueta al menos **cinco flujos** (ej.:
      “instrucción fetch”, “dato load”, “writeback”).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        Existe `projects/m05-como-corre/notas-L01.md` con definiciones, diagrama
        (ASCII o imagen enlazada) y respuestas al ejercicio con `node`.
      - Puedes explicar en 60 s el modelo von Neumann sin leer apuntes.
      - Distinguiste arquitectura de organización con un ejemplo.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Modelo von Neumann e introducción

**~5 h · Semana 1**

Primera lección de arquitectura: ubicas CPU, memoria y E/S en un mismo diagrama mental antes de medir nada.

## Objetivo

Explicar el modelo von Neumann (programa y datos en memoria; CPU ejecuta secuencialmente) y enumerar los componentes principales de una máquina moderna.

## Por qué empieza así

Sin un mapa, “rendimiento” y “memoria” son etiquetas sueltas. Hoy construyes el mapa que usarás en las 11 lecciones siguientes.

## Conceptos

- **Arquitectura** vs **organización** (qué expone el ISA vs cómo se implementa).
- **Programa almacenado**: instrucciones y datos comparten memoria.
- **Unidad de control** y **ALU** como roles, no como marcas comerciales.
- **Cuello de botella von Neumann**: CPU y memoria comparten bus.

## Pasos

### 1. Lectura dirigida (60–90 min)

Lee en Stallings la introducción y el capítulo de **estructura y función** (o equivalente en Tanenbaum). Anota:

- Tres definiciones con tus palabras (CPU, memoria principal, E/S).
- Una analogía útil y una que **no** sirve (ej.: “CPU = cerebro” sin matiz).

### 2. Carpeta de evidencia (15 min)

```bash
mkdir -p projects/m05-como-corre
```

Crea `projects/m05-como-corre/notas-L01.md` con encabezado `# M05 — Notas L01`.

### 3. Diagrama en borrador (60–90 min)

En papel o en el mismo archivo, dibuja **cajas y flechas**:

- CPU (dentro: UC + ALU + registros, aunque sea esquemático).
- Memoria principal (RAM).
- Módulos de E/S (disco, red, teclado/pantalla como ejemplos).
- Bus que conecta CPU ↔ memoria ↔ E/S.

Etiqueta al menos **cinco flujos** (ej.: “instrucción fetch”, “dato load”, “writeback”).

### 4. Conexión con software (45–60 min)

Desde la raíz del repo, ejecuta un script mínimo (puede ser uno de M02):

```bash
node -e "console.log('hola arquitectura')"
```

En `notas-L01.md`, responde por escrito (párrafo corto cada uno):

1. ¿Qué proceso crea el SO al invocar `node`?
2. ¿Dónde vive el bytecode/interpreter mientras corre?
3. ¿Qué E/S ocurre al imprimir en terminal?

No necesitas ser exacto al 100 %; necesitas **hipótesis falsables** que refinarás en L12.

### 5. Glosario inicial (30 min)

Añade a `notas-L01.md` una tabla: término → definición → dónde lo verás al correr un programa.

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Stallings | Intro + estructura/función | Tanenbaum, capítulos paralelos |
| Plan | [Cómo estudiar](../../../como-estudiar.md) (repaso 10 min) | — |
| Catálogo | Entrada M05 | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Existe `projects/m05-como-corre/notas-L01.md` con definiciones, diagrama (ASCII o imagen enlazada) y respuestas al ejercicio con `node`.
2. Puedes explicar en 60 s el modelo von Neumann sin leer apuntes.
3. Distinguiste arquitectura de organización con un ejemplo.

## Errores comunes

- Copiar un diagrama del libro sin poder explicar cada flecha.
- Confundir “memoria” con “disco” porque ambos “guardan”.
- Saltar la conexión con un programa real.

## Siguiente

[L02 — CPU, registros y ciclo de instrucción](L02-cpu-registros-y-ciclo-instruccion.md)
