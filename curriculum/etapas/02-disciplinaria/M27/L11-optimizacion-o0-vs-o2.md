---
id: L11
materia: M27
orden: 11
titulo: Optimización -O0 vs -O2 (lectura)
horas: 5
semana: 3
lectura: Comparar -O0/-O2 en Godbolt
evidencia: notas/o0-vs-o2.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      `-O2` borra tu “historia pedagógica” del asm. Hoy contrastas.


      **Objetivo de esta lección:** Misma función en `-O0` y `-O2`; lista 3
      diferencias observables.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Genera ambos
    xp: 10
    cuerpo: |-
      ```bash
      gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
      gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
      diff -u asm/sum3-O0.s asm/sum3-O2.s | head
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Escribe
    xp: 10
    cuerpo: |-
      ```bash
      gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
      gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
      diff -u asm/sum3-O0.s asm/sum3-O2.s | head
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Optimización -O0 vs -O2 (lectura)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Optimización -O0 vs -O2
          (lectura)
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
      ¿Es recomendable en esta lección? “Depurar asm -O2 sin símbolos claros el
      primer día."
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
        texto: Misma función en `-O0` y `-O2`; lista 3 diferencias observables.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Regla de estudio
    xp: 10
    cuerpo: “Para aprender ABI uso `-O0`; para rendimiento miro `-O2`”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Dos archivos `.s` o diff documentado.
      - ≥3 diferencias escritas.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Optimización -O0 vs -O2 (lectura)

**~5.0 h · Semana 3**

`-O2` borra tu “historia pedagógica” del asm. Hoy contrastas.

## Objetivo

Misma función en `-O0` y `-O2`; lista 3 diferencias observables.

## Pasos

### 1. Genera ambos (60 min)

```bash
gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
diff -u asm/sum3-O0.s asm/sum3-O2.s | head
```

### 2. Escribe (90 min)

En notas: ¿inlining? ¿menos spills a stack? ¿instrucciones totales?

### 3. Regla de estudio (30 min)

“Para aprender ABI uso `-O0`; para rendimiento miro `-O2`”.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Comparar -O0/-O2 en Godbolt | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos archivos `.s` o diff documentado.
2. ≥3 diferencias escritas.
3. Commit.

## Errores comunes

- Depurar asm -O2 sin símbolos claros el primer día.
- Creer que -O0 es “lo que corre en producción”.

## Siguiente

[L12 — Lab: anotar calling convention (P3)](L12-lab-anotar-calling-convention-p3.md)
