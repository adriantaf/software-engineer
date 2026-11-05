---
id: L18
materia: M27
orden: 18
titulo: Viaje de un binario y cierre M27
horas: 5
semana: 5
lectura: Síntesis proyecto
evidencia: viaje-binario.md — cierra proyecto M27
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras el **proyecto**: el relato completo compile → link → run, con
      puente a M18 y a compiladores (opcional futuro).


      **Objetivo de esta lección:** `viaje-binario.md` + README actualizado;
      checklist P1–P3 verde.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escribe el viaje
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m27): cierre viaje de un binario"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Checklist
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m27): cierre viaje de un binario"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Viaje de un binario y cierre M27», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Viaje de un binario y
          cierre M27
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

      `git commit -am "docs(m27): cierre viaje de un binario"`
    comandoEsperado:
      - 'git commit -am "docs(m27): cierre viaje de un binario"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m27): cierre viaje de un binario"'
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
        texto: '`viaje-binario.md` + README actualizado; checklist P1–P3 verde.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M27
    xp: 25
    enunciado: >-
      Cierra **Sistemas a bajo nivel** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: C: tipos, punteros y buffers con evidencia'
      - 'P2: Stack, heap y sanitizers (ASan/UBSan)'
      - 'P3: Leer asm generado y calling convention'
      - 'Proyecto: Informe "viaje de un binario" (compile → link → run)'
      - viaje-binario.md — cierra proyecto M27
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: '`viaje-binario.md` existe y está enlazado.'
      - id: r3
        criterio: P1–P3 referenciados.
      - id: r4
        criterio: Commit de cierre.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`viaje-binario.md` existe y está enlazado.'
      - P1–P3 referenciados.
      - Commit de cierre.
    siguiente: Materia M27 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Viaje de un binario y cierre M27

**~5.0 h · Semana 5**

Cierras el **proyecto**: el relato completo compile → link → run, con puente a M18 y a compiladores (opcional futuro).

## Objetivo

`viaje-binario.md` + README actualizado; checklist P1–P3 verde.

## Pasos

### 1. Escribe el viaje (120 min)

Plantilla del scaffold: pregunta → comandos → asm extracto → diagrama → riesgos → siguiente (compiladores, opcional futuro).

### 2. Checklist (60 min)

P1 buffers, P2 sanitizer, P3 ABI, proyecto.

### 3. Simulación (40 min)

Otro “yo” solo con README: ¿compila hello?

### 4. Commit de cierre (15 min)

```bash
git commit -am "docs(m27): cierre viaje de un binario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Síntesis proyecto | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `viaje-binario.md` existe y está enlazado.
2. P1–P3 referenciados.
3. Commit de cierre.

## Errores comunes

- Informe sin comandos reproducibles.
- Marcar proyecto sin asm ni diagrama.

## Siguiente

Cierra la [ficha M27](../M27-sistemas-bajo-nivel.md). Siguiente en el plan: **M12**. Compiladores quedan como estudio opcional futuro, fuera del catálogo.
