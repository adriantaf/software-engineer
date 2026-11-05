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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `CitaService` testeable sin HTTP.


      El service es lo que M13 llamó application layer: orquesta dominio +
      puertos.
  - id: s2
    tipo: ejemplo
    titulo: 1. API del service
    xp: 10
    cuerpo: '`crear`, `cancelar`, `listarDelDia`.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Service — capa aplicación de pedidos" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: src/pedidos/pedido-service.ts + tests (P2)
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
    pregunta: ¿Es buena práctica en esta lección? “Service que importa Express."
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
        texto: '`CitaService` testeable sin HTTP.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: Inyecta repo (+ clock + notifier opcionales).
  - id: s7
    tipo: explicacion
    titulo: 3. Tests P2 + README + commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
