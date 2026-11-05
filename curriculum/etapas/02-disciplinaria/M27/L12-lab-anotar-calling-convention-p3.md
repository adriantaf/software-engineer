---
id: L12
materia: M27
orden: 12
titulo: 'Lab: anotar calling convention (P3)'
horas: 5
semana: 3
lectura: Repaso ABI System V
evidencia: asm anotado — cierra P3
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras **P3**: una función tuya con args en registros etiquetados.


      **Objetivo de esta lección:** Función ≥3 parámetros; asm `-O0` con
      comentarios `/* arg1 rdi */` etc.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escribe función de dominio
    xp: 10
    cuerpo: >-
      Ej. `cita_hash(cliente_id, servicio_id, ts)` que combine tres `long`
      (inventa la fórmula).
  - id: s3
    tipo: ejemplo
    titulo: Genera y anota
    xp: 10
    cuerpo: Asm comentado en `asm/cita_hash-anotado.s` (o `.md` con bloques).
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lab: anotar calling convention (P3)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lab: anotar calling
          convention (P3)
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
      ¿Es recomendable en esta lección? “Anotar un asm de internet que no
      compilaste tú."
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
        texto: Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1 rdi */` etc.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Usar -O2 y perder los movs de args."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Asm anotado con registros de args y `rax` de retorno.
      - README marca P3.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Lab: anotar calling convention (P3)

**~5.0 h · Semana 3**

Cierras **P3**: una función tuya con args en registros etiquetados.

## Objetivo

Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1 rdi */` etc.

## Pasos

### 1. Escribe función de dominio (60 min)

Ej. `cita_hash(cliente_id, servicio_id, ts)` que combine tres `long` (inventa la fórmula).

### 2. Genera y anota (120 min)

Asm comentado en `asm/cita_hash-anotado.s` (o `.md` con bloques).

### 3. Checklist P3 en README (30 min)

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Repaso ABI System V | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Asm anotado con registros de args y `rax` de retorno.
2. README marca P3.
3. Commit.

## Errores comunes

- Anotar un asm de internet que no compilaste tú.
- Usar -O2 y perder los movs de args.

## Siguiente

[L13 — Compilar vs linkar: .o y librerías](L13-compilar-vs-linkar.md)
