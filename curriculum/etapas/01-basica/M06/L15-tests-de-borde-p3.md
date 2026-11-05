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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La práctica **P3** exige bordes: donde el software real falla en
      producción.


      **Objetivo de esta lección:** Ampliar suite Vitest con casos
      null/undefined, colecciones vacías, IDs duplicados, strings vacíos;
      documentar matriz de bordes.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Matriz de bordes
    xp: 10
    cuerpo: >-
      `tests/bordes.md`: filas = operación, columnas = null, vacío, duplicado,
      límite.
  - id: s3
    tipo: ejemplo
    titulo: Implementación tests
    xp: 10
    cuerpo: Mínimo **10 tests** nuevos o reforzados. Usa `it.each` si conviene.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests de borde: null, vacío, duplicados (P3)», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Matriz cubierta por tests reales.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests de borde: null,
          vacío, duplicados…
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
    pregunta: ¿Es recomendable en esta lección? “Solo happy path."
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
        texto: >-
          Ampliar suite Vitest con casos null/undefined, colecciones vacías, IDs
          duplicados, strings vacíos; documentar matriz de bordes.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Endurecer tipos
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
