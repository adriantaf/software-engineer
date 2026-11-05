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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Misma función en `-O0` y `-O2`; lista 3 diferencias
      observables.


      `-O2` borra tu “historia pedagógica” del asm. Hoy contrastas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Genera ambos
    xp: 10
    cuerpo: |-
      ```bash
      gcc -O0 -S -o asm/sum3-O0.s src/sum3.c
      gcc -O2 -S -o asm/sum3-O2.s src/sum3.c
      diff -u asm/sum3-O0.s asm/sum3-O2.s | head
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Optimización -O0 vs -O2 (lectura)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/o0-vs-o2.md
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
      ¿Es buena práctica en esta lección? “Depurar asm -O2 sin símbolos claros
      el primer día."
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
        texto: Misma función en `-O0` y `-O2`; lista 3 diferencias observables.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe
    xp: 10
    cuerpo: 'En notas: ¿inlining? ¿menos spills a stack? ¿instrucciones totales?'
  - id: s7
    tipo: explicacion
    titulo: 3. Regla de estudio
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
