---
id: L05
materia: M15
orden: 5
titulo: Fake repositorio y reloj para tests rápidos
horas: 5
semana: 2
lectura: Fakes vs mocks; reloj inyectable
evidencia: InMemory repo + Clock fake + tests de servicio
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Fakes de repo y reloj cableados al service de pedidos.

      Los tests de application layer deben ser rápidos y deterministas.
  - id: s2
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: '`test(m15): fake repo y reloj`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Fake repositorio y reloj para tests rápidos" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: InMemory repo + Clock fake + tests de servicio
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
      ¿Es buena práctica en esta lección? “Mock de cada método del repo sin
      estado (frágil)."
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
        texto: Fakes de repo y reloj cableados al service de pedidos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `FakeClock` o `() => Date` inyectable; test de “pedido en el pasado”
        estable.
      - Repo in-memory usado por tests de application service.
      - 'Commit `test(m15): fake repo y reloj`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Fake repositorio y reloj para tests rápidos

**~5.0 h · Semana 2**

Los tests de application layer deben ser rápidos y deterministas.

## Objetivo

Fakes de repo y reloj cableados al service de pedidos.

## Pasos (hazlos en orden)

### 1. Puerto Clock (30 min)

### 2. InMemoryCitaRepository (50–60 min) — reutiliza M14 si existe

### 3. Tests de servicio (60–70 min)

### 4. Commit

`test(m15): fake repo y reloj`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Fakes: repo en memoria y reloj determinista | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `FakeClock` o `() => Date` inyectable; test de “pedido en el pasado” estable.
2. Repo in-memory usado por tests de application service.
3. Commit `test(m15): fake repo y reloj`.

## Errores comunes

- Mock de cada método del repo sin estado (frágil).
- `Date.now` global sin restore.
- Fake más complejo que producción.

## Siguiente

[L06 — Tests de integración con persistencia](L06-tests-de-integracion-con-persistencia.md)
