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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los tests de application layer deben ser rápidos y deterministas.


      **Objetivo de esta lección:** Fakes de repo y reloj cableados al service
      de pedidos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`test(m15): fake repo y reloj`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Fake repositorio y reloj para tests rápidos», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Fake repositorio y
          reloj para tests ráp…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Mock de cada método del repo sin estado
      (frágil)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: Fakes de repo y reloj cableados al service de pedidos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “`Date.now` global sin restore."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
