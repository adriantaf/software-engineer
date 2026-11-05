---
id: L04
materia: M06
orden: 4
titulo: Nombres y funciones pequeñas (CC 1–3)
horas: 5
semana: 1
lectura: Código limpio caps. 1–3 completos
evidencia: Refactor de nombres + funciones ≤15 líneas; semana-0001 bitácora opcional
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana 1 puliendo legibilidad: nombres que revelan intención y
      funciones que caben en una pantalla.


      **Objetivo de esta lección:** Aplicar CC 1–3 al código del dominio;
      registrar antes/después en notas para **P2** (refactor formal en L08).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura CC 1–3
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario de olores
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Nombres y funciones pequeñas (CC 1–3)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          No quedan funciones públicas >~20 líneas sin justificación
          documentada.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Nombres y funciones
          pequeñas (CC 1–3)
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

      `git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"`
    comandoEsperado:
      - 'git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git commit -am "refactor(m06): nombres y funciones pequeñas CC
      1-3"
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
          Aplicar CC 1–3 al código del dominio; registrar antes/después en notas
          para P2 (refactor formal en L08).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Refactor mecánico
    xp: 10
    cuerpo: >-
      - Renombra con IDE (tests verdes tras cada paso). - Extrae funciones;
      sustituye magic numbers por constantes nombradas. - Guarda `git diff` o
      captura en `refactor-notas.md` (**antes** snapshot: tag o commit
      `pre-refactor-semana1`).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - No quedan funciones públicas >~20 líneas sin justificación documentada.
      - '`refactor-notas.md` lista cambios principales.'
      - Tests verdes.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Nombres y funciones pequeñas (CC 1–3)

**~5 h · Semana 1**

Cierras la semana 1 puliendo legibilidad: nombres que revelan intención y funciones que caben en una pantalla.

## Objetivo

Aplicar CC 1–3 al código del dominio; registrar antes/después en notas para **P2** (refactor formal en L08).

## Pasos

### 1. Lectura CC 1–3 (60 min)

Subraya 10 reglas accionables. No decorativas.

### 2. Inventario de olores (45 min)

Lista: nombres ambiguos (`data`, `handle`, `process`), funciones largas, números mágicos.

### 3. Refactor mecánico (150 min)

- Renombra con IDE (tests verdes tras cada paso).
- Extrae funciones; sustituye magic numbers por constantes nombradas.
- Guarda `git diff` o captura en `refactor-notas.md` (**antes** snapshot: tag o commit `pre-refactor-semana1`).

### 4. Revisión entre pares (opcional, 30 min)

Si estudias solo, lee en voz alta el módulo principal; corrige lo que tropezó.

### 5. Commit (15 min)

```bash
git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"
```

## Hecho cuando

1. No quedan funciones públicas >~20 líneas sin justificación documentada.
2. `refactor-notas.md` lista cambios principales.
3. Tests verdes.

## Errores comunes

- Renombrar sin correr tests.
- Abstracciones de una sola línea inútiles.

## Siguiente

[L05 — Interfaces y contratos de dominio](L05-interfaces-y-contratos.md)
