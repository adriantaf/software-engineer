---
id: L10
materia: M27
orden: 10
titulo: Registros x86-64 y mov/add/call
horas: 5
semana: 3
lectura: 'CSAPP machine-level: mov, add, call/ret'
evidencia: notas/asm-basico.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Glosario propio: `mov`, `add`, `sub`, `call`, `ret`,
      `push`/`pop` (idea), registros `rax`…`r9`.


      Pocas instrucciones bastan para leer el 80% del asm de estudiantes.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: Enfócate en transferencias y llamadas.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Registros x86-64 y mov/add/call" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/asm-basico.md
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
    pregunta: ¿Es buena práctica en esta lección? “Memorizar encoding de opcodes."
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
          Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop`
          (idea), registros `rax`…`r9`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Anota tu `sum3.s`
    xp: 10
    cuerpo: >-
      Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a
      lado.
  - id: s7
    tipo: explicacion
    titulo: 3. Quiz auto
    xp: 10
    cuerpo: 'Sin mirar: ¿dónde está el return value? ¿primer argumento?'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Asm anotado o notas equivalentes.
      - Respondiste el auto-quiz en notas.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Registros x86-64 y mov/add/call

**~5.0 h · Semana 3**

Pocas instrucciones bastan para leer el 80% del asm de estudiantes.

## Objetivo

Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop` (idea), registros `rax`…`r9`.

## Pasos

### 1. Lectura (60 min)

Enfócate en transferencias y llamadas.

### 2. Anota tu `sum3.s` (90 min)

Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a lado.

### 3. Quiz auto (30 min)

Sin mirar: ¿dónde está el return value? ¿primer argumento?

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP machine-level: mov, add, call/ret | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Asm anotado o notas equivalentes.
2. Respondiste el auto-quiz en notas.
3. Commit.

## Errores comunes

- Memorizar encoding de opcodes.
- Ignorar que AT&T (`gcc -S`) pone dest a la derecha.

## Siguiente

[L11 — Optimización -O0 vs -O2](L11-optimizacion-o0-vs-o2.md)
