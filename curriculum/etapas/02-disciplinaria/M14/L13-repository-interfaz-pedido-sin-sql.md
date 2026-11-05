---
id: L13
materia: M14
orden: 13
titulo: Repository — interfaz Pedido sin SQL
horas: 5
semana: 4
lectura: Repository; puerto de persistencia
evidencia: src/pedidos/pedido-repository.ts + InMemory + ADR (P2 inicio)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2: capas backend alineadas a M13. Empiezas por el puerto de persistencia.


      **Objetivo de esta lección:** `CitaRepository` + impl in-memory + ADR.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): repository pedido sin sql`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Repository — interfaz Pedido sin SQL», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Repository — interfaz
          Pedido sin SQL
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
      ¿Es recomendable en esta lección? “Interfaz que expone `query(sql:
      string)`."
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
        texto: '`CitaRepository` + impl in-memory + ADR.'
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
    pregunta: ¿Debes hacer esto? “Repo que es solo un alias del ORM entity."
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
        `CitaRepository` con `findById`/`save` (y filtro por dueño/negocio si
        aplica).
      - '`InMemoryCitaRepository` + tests; cero SQL en el dominio.'
      - 'Commit `feat(m14): repository pedido sin sql`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Repository — interfaz Pedido sin SQL

**~5.0 h · Semana 4**

P2: capas backend alineadas a M13. Empiezas por el puerto de persistencia.

## Objetivo

`CitaRepository` + impl in-memory + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de dominio Pedido (30 min) — alineados a M13

### 2. Interfaz + InMemory (70–90 min)

### 3. Tests + ADR + commit

`feat(m14): repository pedido sin sql`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Repository: interfaz de dominio sin SQL; impl in-memory | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `CitaRepository` con `findById`/`save` (y filtro por dueño/negocio si aplica).
2. `InMemoryCitaRepository` + tests; **cero** SQL en el dominio.
3. Commit `feat(m14): repository pedido sin sql`.

## Errores comunes

- Interfaz que expone `query(sql: string)`.
- Repo que es solo un alias del ORM entity.
- Sin tests del in-memory.

## Siguiente

[L14 — Service — capa aplicación de pedidos](L14-service-capa-aplicacion-de-pedidos.md)
