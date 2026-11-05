---
id: L02
materia: M16
orden: 2
titulo: Auditoría Nielsen — tres heurísticas profundas
horas: 5
semana: 1
lectura: Tres heurísticas Nielsen a fondo sobre el piloto
evidencia: heuristicas/parcial-3.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Profundizas tres heurísticas que más duelen en scheduling: estado del
      sistema, lenguaje del negocio, prevención de errores.


      **Objetivo de esta lección:** `heuristicas/parcial-3.md` con hallazgos
      severizados.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige tres
    xp: 10
    cuerpo: >-
      Recomendadas: (#1) visibilidad de estado, (#2) match con el mundo real
      (jerga del salón/clínica), (#5) prevención de errores.
  - id: s3
    tipo: ejemplo
    titulo: Audita con capturas o URLs
    xp: 10
    cuerpo: 'Tabla como en la ficha M16 (ID, heurística, hallazgo, severidad, fix).'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Auditoría Nielsen — tres heurísticas profundas», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Auditoría Nielsen —
          tres heurísticas pr…
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
      ¿Es recomendable en esta lección? “Las 10 heurísticas en una línea cada
      una."
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
        texto: '`heuristicas/parcial-3.md` con hallazgos severizados.'
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
    cuerpo: '`docs(m16): auditoria parcial tres heuristicas`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Documento con 3 heurísticas profundas y ≥2 hallazgos cada una (severidad
        1–3 o baja/media/alta).
      - Hallazgos trazan a pantallas del piloto (agenda/pedido/login).
      - 'Commit `docs(m16): auditoria parcial tres heuristicas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Auditoría Nielsen — tres heurísticas profundas

**~5.0 h · Semana 1**

Profundizas tres heurísticas que más duelen en scheduling: estado del sistema, lenguaje del negocio, prevención de errores.

## Objetivo

`heuristicas/parcial-3.md` con hallazgos severizados.

## Pasos (hazlos en orden)

### 1. Elige tres (20 min)

Recomendadas: (#1) visibilidad de estado, (#2) match con el mundo real (jerga del salón/clínica), (#5) prevención de errores.

### 2. Audita con capturas o URLs (90–110 min)

Tabla como en la ficha M16 (ID, heurística, hallazgo, severidad, fix).

### 3. Cruza con fricciones L01 (30 min)

### 4. Commit

`docs(m16): auditoria parcial tres heuristicas`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Visibilidad de estado, match mundo real, prevención de errores | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Documento con 3 heurísticas profundas y ≥2 hallazgos cada una (severidad 1–3 o baja/media/alta).
2. Hallazgos trazan a pantallas del piloto (agenda/pedido/login).
3. Commit `docs(m16): auditoria parcial tres heuristicas`.

## Errores comunes

- Las 10 heurísticas en una línea cada una.
- Severidad inflada en todo.
- Hallazgos genéricos (“mejorar UX”).

## Siguiente

[L03 — Estados vacío, carga y error en agenda](L03-estados-vacio-carga-y-error-en-menu.md)
