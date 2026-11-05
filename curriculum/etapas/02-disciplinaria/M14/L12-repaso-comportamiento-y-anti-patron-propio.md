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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Criterio de dominio: un patrón que **rechazaste** y un olor que sí
      tuviste.


      **Objetivo de esta lección:** Documento honesto
      `docs/anti-patron-propio.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige un olor
    xp: 10
    cuerpo: 'God service, SQL en controller, Singleton de config, etc.'
  - id: s3
    tipo: ejemplo
    titulo: Escribe antes → después
    xp: 10
    cuerpo: Fragmentos de código o pseudocódigo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Repaso comportamiento y anti-patrón propio», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Repaso comportamiento y
          anti-patrón pro…
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
      ¿Es recomendable en esta lección? “Hablar de anti-patrones abstractos sin
      tu código."
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
        texto: Documento honesto `docs/anti-patron-propio.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
