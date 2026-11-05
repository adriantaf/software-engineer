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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1
      rdi */` etc.


      Cierras **P3**: una función tuya con args en registros etiquetados.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe función de dominio
    xp: 10
    cuerpo: >-
      Ej. `cita_hash(cliente_id, servicio_id, ts)` que combine tres `long`
      (inventa la fórmula).
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Lab: anotar calling convention (P3)" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: asm anotado — cierra P3
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
      ¿Es buena práctica en esta lección? “Anotar un asm de internet que no
      compilaste tú."
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
        texto: Función ≥3 parámetros; asm `-O0` con comentarios `/* arg1 rdi */` etc.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Genera y anota
    xp: 10
    cuerpo: Asm comentado en `asm/cita_hash-anotado.s` (o `.md` con bloques).
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Asm anotado con registros de args y `rax` de retorno.
      - README marca P3.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
