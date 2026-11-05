---
id: L07
materia: M15
orden: 7
titulo: Tests HTTP de API — auth y validación
horas: 5
semana: 2
lectura: Supertest/fetch contra app; 401 y 400
evidencia: tests/http/ login/pedidos 401 y 400
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Tests 401/400 contra API de prueba del piloto.


      La pirámide necesita la capa que habla HTTP: el contrato que el front
      verá.
  - id: s2
    tipo: ejemplo
    titulo: 1. Mini app
    xp: 10
    cuerpo: 'Si M17 no existe, spike en `projects/m15-calidad/src/http/`.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests HTTP de API — auth y validación" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: tests/http/ login/pedidos 401 y 400
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
    pregunta: ¿Es buena práctica en esta lección? “Probar solo el happy path."
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
        texto: Tests 401/400 contra API de prueba del piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Casos
    xp: 10
    cuerpo: 'Tabla de la ficha M15: feliz opcional hoy; 401 y 400 obligatorios.'
  - id: s7
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`test(m15): http auth y validacion`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - App mínima (Express/Fastify/Hono o spike) con ruta protegida de pedidos.
      - 'Tests automatizados: sin cookie/token → 401; body inválido → 400.'
      - 'Commit `test(m15): http auth y validacion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Tests HTTP de API — auth y validación

**~5.0 h · Semana 2**

La pirámide necesita la capa que habla HTTP: el contrato que el front verá.

## Objetivo

Tests 401/400 contra API de prueba del piloto.

## Pasos (hazlos en orden)

### 1. Mini app (60–80 min)

Si M17 no existe, spike en `projects/m15-calidad/src/http/`.

### 2. Casos (60–70 min)

Tabla de la ficha M15: feliz opcional hoy; 401 y 400 obligatorios.

### 3. Commit

`test(m15): http auth y validacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | HTTP tests: sin auth → 401; body inválido → 400 | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. App mínima (Express/Fastify/Hono o spike) con ruta protegida de pedidos.
2. Tests automatizados: sin cookie/token → 401; body inválido → 400.
3. Commit `test(m15): http auth y validacion`.

## Errores comunes

- Probar solo el happy path.
- Servidor global compartido sin aislamiento.
- Hardcodear secrets de prod.

## Siguiente

[L08 — IDOR y roles — casos 403](L08-idor-y-roles-casos-403.md)
