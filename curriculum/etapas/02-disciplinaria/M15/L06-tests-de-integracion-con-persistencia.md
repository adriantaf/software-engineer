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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Carpeta `tests/integration/` con evidencia P1 (segunda
      capa).


      El fake miente a veces. Un test real de persistencia ancla el Repository
      Postgres (o el que elegiste en M13).
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige estrategia
    xp: 10
    cuerpo: >-
      Documenta en README: Docker compose service `db_test`, o SQLite solo para
      spike.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests de integración con persistencia" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: tests/integration/ con Postgres o SQLite documentado
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
      ¿Es buena práctica en esta lección? “Usar la DB de desarrollo con datos
      del design partner."
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
        texto: Carpeta `tests/integration/` con evidencia P1 (segunda capa).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 4. Commit
    xp: 10
    cuerpo: '`test(m15): integracion persistencia`'
  - id: s7
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
