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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aplicar CC 1–3 al código del dominio; registrar
      antes/después en notas para **P2** (refactor formal en L08).


      Cierras la semana 1 puliendo legibilidad: nombres que revelan intención y
      funciones que caben en una pantalla.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura CC 1–3
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Nombres y funciones pequeñas (CC 1–3)" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: >-
          Refactor de nombres + funciones ≤15 líneas; semana-0001 bitácora
          opcional
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"`
    comandoEsperado:
      - 'git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git commit -am "refactor(m06): nombres y funciones pequeñas CC
      1-3"
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Aplicar CC 1–3 al código del dominio; registrar antes/después en notas
          para **P2** (refactor formal en L08).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario de olores
    xp: 10
    cuerpo: >-
      Lista: nombres ambiguos (`data`, `handle`, `process`), funciones largas,
      números mágicos.
  - id: s7
    tipo: explicacion
    titulo: 3. Refactor mecánico
    xp: 10
    cuerpo: >-
      - Renombra con IDE (tests verdes tras cada paso).

      - Extrae funciones; sustituye magic numbers por constantes nombradas.

      - Guarda `git diff` o captura en `refactor-notas.md` (**antes** snapshot:
      tag o commit `pre-refactor-semana1`).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - No quedan funciones públicas >~20 líneas sin justificación documentada.
      - '`refactor-notas.md` lista cambios principales.'
      - Tests verdes.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
