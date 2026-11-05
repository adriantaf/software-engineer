---
id: L06
materia: M15
orden: 6
titulo: Tests de integración con persistencia
horas: 5
semana: 2
lectura: Tests de integración DB; isolation
evidencia: tests/integration/ con Postgres o SQLite documentado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El fake miente a veces. Un test real de persistencia ancla el Repository
      Postgres (o el que elegiste en M13).


      **Objetivo de esta lección:** Carpeta `tests/integration/` con evidencia
      P1 (segunda capa).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige estrategia
    xp: 10
    cuerpo: >-
      Documenta en README: Docker compose service `db_test`, o SQLite solo para
      spike.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`test(m15): integracion persistencia`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests de integración con persistencia», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests de integración
          con persistencia
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
      ¿Es recomendable en esta lección? “Usar la DB de desarrollo con datos del
      design partner."
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
        texto: Carpeta `tests/integration/` con evidencia P1 (segunda capa).
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
    pregunta: ¿Debes hacer esto? “Tests de integración mezclados sin tag/carpeta."
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
      - >-
        Al menos 1 test de integración que escribe/lee pedido en DB de prueba
        (Docker PG, Testcontainers, o SQLite — documenta cuál).
      - Setup/teardown o transacciones que no dejen basura.
      - 'Commit `test(m15): integracion persistencia`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Tests de integración con persistencia

**~5.0 h · Semana 2**

El fake miente a veces. Un test real de persistencia ancla el Repository Postgres (o el que elegiste en M13).

## Objetivo

Carpeta `tests/integration/` con evidencia P1 (segunda capa).

## Pasos (hazlos en orden)

### 1. Elige estrategia (40 min)

Documenta en README: Docker compose service `db_test`, o SQLite solo para spike.

### 2. Test save/find (80–100 min)

### 3. Script npm `test:integration` (30 min)

### 4. Commit

`test(m15): integracion persistencia`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Integración: repository real contra DB de prueba | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Al menos 1 test de integración que escribe/lee pedido en DB de prueba (Docker PG, Testcontainers, o SQLite — documenta cuál).
2. Setup/teardown o transacciones que no dejen basura.
3. Commit `test(m15): integracion persistencia`.

## Errores comunes

- Usar la DB de desarrollo con datos del design partner.
- Tests de integración mezclados sin tag/carpeta.
- Sin documentar cómo levantar la DB en README.

## Siguiente

[L07 — Tests HTTP de API — auth y validación](L07-tests-http-de-api-auth-y-validacion.md)
