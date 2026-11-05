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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `CitaRepository` + impl in-memory + ADR.

      P2: capas backend alineadas a M13. Empiezas por el puerto de persistencia.
  - id: s2
    tipo: ejemplo
    titulo: 3. Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): repository pedido sin sql`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Repository — interfaz Pedido sin SQL" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: src/pedidos/pedido-repository.ts + InMemory + ADR (P2 inicio)
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
      ¿Es buena práctica en esta lección? “Interfaz que expone `query(sql:
      string)`."
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
        texto: '`CitaRepository` + impl in-memory + ADR.'
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
        `CitaRepository` con `findById`/`save` (y filtro por dueño/negocio si
        aplica).
      - '`InMemoryCitaRepository` + tests; cero SQL en el dominio.'
      - 'Commit `feat(m14): repository pedido sin sql`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
