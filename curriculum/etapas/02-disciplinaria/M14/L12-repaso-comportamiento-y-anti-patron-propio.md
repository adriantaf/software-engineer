---
id: L12
materia: M14
orden: 12
titulo: Repaso comportamiento y anti-patrón propio
horas: 5
semana: 3
lectura: Anti-patrón detectado en tu código
evidencia: docs/anti-patron-propio.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documento honesto `docs/anti-patron-propio.md`.


      Criterio de dominio: un patrón que **rechazaste** y un olor que sí
      tuviste.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige un olor
    xp: 10
    cuerpo: 'God service, SQL en controller, Singleton de config, etc.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Repaso comportamiento y anti-patrón propio" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: docs/anti-patron-propio.md
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
      ¿Es buena práctica en esta lección? “Hablar de anti-patrones abstractos
      sin tu código."
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
        texto: Documento honesto `docs/anti-patron-propio.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe antes → después
    xp: 10
    cuerpo: Fragmentos de código o pseudocódigo.
  - id: s7
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m14): anti-patron propio`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `anti-patron-propio.md` describe código tuyo (plan o spike) con olor y
        alternativa.
      - Enlaza al patrón de M14 que lo evita.
      - 'Commit `docs(m14): anti-patron propio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Repaso comportamiento y anti-patrón propio

**~5.0 h · Semana 3**

Criterio de dominio: un patrón que **rechazaste** y un olor que sí tuviste.

## Objetivo

Documento honesto `docs/anti-patron-propio.md`.

## Pasos (hazlos en orden)

### 1. Elige un olor (30 min)

God service, SQL en controller, Singleton de config, etc.

### 2. Escribe antes → después (80–100 min)

Fragmentos de código o pseudocódigo.

### 3. Commit

`docs(m14): anti-patron propio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Documentar un anti-patrón propio y el refactor mental | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `anti-patron-propio.md` describe código tuyo (plan o spike) con olor y alternativa.
2. Enlaza al patrón de M14 que lo evita.
3. Commit `docs(m14): anti-patron propio`.

## Errores comunes

- Hablar de anti-patrones abstractos sin tu código.
- Inventar un pecado que no cometiste.
- No proponer fix.

## Siguiente

[L13 — Repository — interfaz Pedido sin SQL](L13-repository-interfaz-pedido-sin-sql.md)
