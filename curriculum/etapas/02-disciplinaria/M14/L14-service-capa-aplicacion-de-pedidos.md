---
id: L14
materia: M14
orden: 14
titulo: Service — capa aplicación de pedidos
horas: 5
semana: 4
lectura: Application service; orquestación y authz
evidencia: src/pedidos/pedido-service.ts + tests (P2)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El service es lo que M13 llamó application layer: orquesta dominio +
      puertos.


      **Objetivo de esta lección:** `CitaService` testeable sin HTTP.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: API del service
    xp: 10
    cuerpo: '`crear`, `cancelar`, `listarDelDia`.'
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: Inyecta repo (+ clock + notifier opcionales).
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Service — capa aplicación de pedidos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Service — capa
          aplicación de pedidos
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
    pregunta: ¿Es recomendable en esta lección? “Service que importa Express."
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
        texto: '`CitaService` testeable sin HTTP.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests P2 + README + commit
    xp: 10
    cuerpo: '`feat(m14): service capa aplicacion pedidos`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `CitaService` usa `CitaRepository` y valida solape/rol (stub de auth
        ok).
      - Tests de servicio con repo in-memory (P2 evidenciado).
      - 'Commit `feat(m14): service capa aplicacion pedidos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Service — capa aplicación de pedidos

**~5.0 h · Semana 4**

El service es lo que M13 llamó application layer: orquesta dominio + puertos.

## Objetivo

`CitaService` testeable sin HTTP.

## Pasos (hazlos en orden)

### 1. API del service (40 min)

`crear`, `cancelar`, `listarDelDia`.

### 2. Implementación (70–90 min)

Inyecta repo (+ clock + notifier opcionales).

### 3. Tests P2 + README + commit

`feat(m14): service capa aplicacion pedidos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Service de aplicación: reglas + repo; sin HTTP ni SQL | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `CitaService` usa `CitaRepository` y valida solape/rol (stub de auth ok).
2. Tests de servicio con repo in-memory (P2 evidenciado).
3. Commit `feat(m14): service capa aplicacion pedidos`.

## Errores comunes

- Service que importa Express.
- Authz solo “si rol en string del DTO” sin explicación.
- Duplicar facade y service sin roles claros — documenta relación.

## Siguiente

[L15 — Refactor P3 — módulo legacy antes y después](L15-refactor-p3-modulo-legacy-antes-y-despues.md)
