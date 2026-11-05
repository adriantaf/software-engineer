---
id: L15
materia: M06
orden: 15
titulo: 'Tests de borde: null, vacío, duplicados (P3)'
horas: 5
semana: 4
lectura: Código limpio cap. 9 intro (pruebas); Vitest docs
evidencia: ≥10 tests incluyendo null/undefined/vacío/duplicados; evidencia P3
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ampliar suite Vitest con casos null/undefined, colecciones
      vacías, IDs duplicados, strings vacíos; documentar matriz de bordes.


      La práctica **P3** exige bordes: donde el software real falla en
      producción.
  - id: s2
    tipo: ejemplo
    titulo: 1. Matriz de bordes
    xp: 10
    cuerpo: >-
      `tests/bordes.md`: filas = operación, columnas = null, vacío, duplicado,
      límite.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests de borde: null, vacío, duplicados (P3)" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: ≥10 tests incluyendo null/undefined/vacío/duplicados; evidencia P3
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
    pregunta: ¿Es buena práctica en esta lección? “Solo happy path."
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
          Ampliar suite Vitest con casos null/undefined, colecciones vacías, IDs
          duplicados, strings vacíos; documentar matriz de bordes.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación tests
    xp: 10
    cuerpo: Mínimo **10 tests** nuevos o reforzados. Usa `it.each` si conviene.
  - id: s7
    tipo: explicacion
    titulo: 3. Endurecer tipos
    xp: 10
    cuerpo: 'Entrada inválida: rechazo temprano con Result err claro.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Matriz cubierta por tests reales.
      - ≥10 casos de borde explícitos.
      - Suite verde estable.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Tests de borde: null, vacío, duplicados (P3)

**~5 h · Semana 4**

La práctica **P3** exige bordes: donde el software real falla en producción.

## Objetivo

Ampliar suite Vitest con casos null/undefined, colecciones vacías, IDs duplicados, strings vacíos; documentar matriz de bordes.

## Pasos

### 1. Matriz de bordes (45 min)

`tests/bordes.md`: filas = operación, columnas = null, vacío, duplicado, límite.

### 2. Implementación tests (150 min)

Mínimo **10 tests** nuevos o reforzados. Usa `it.each` si conviene.

### 3. Endurecer tipos (60 min)

Entrada inválida: rechazo temprano con Result err claro.

### 4. Regresión (30 min)

Corre suite completa ≥3 veces; flaky zero tolerance (investiga si falla intermitente).

### 5. Evidencia P3 (15 min)

Commit `test(m06): bordes P3 null vacio duplicados`.

Marca **P3** cuando la matriz y tests existan.

## Hecho cuando

1. Matriz cubierta por tests reales.
2. ≥10 casos de borde explícitos.
3. Suite verde estable.

## Errores comunes

- Solo happy path.
- Tests que no assertan mensaje/código de error.

## Siguiente

[L16 — Logging, diagnóstico y contratos de error](L16-logging-y-diagnostico.md)
