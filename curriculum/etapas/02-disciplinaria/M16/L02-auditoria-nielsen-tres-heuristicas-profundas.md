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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `heuristicas/parcial-3.md` con hallazgos severizados.


      Profundizas tres heurísticas que más duelen en scheduling: estado del
      sistema, lenguaje del negocio, prevención de errores.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige tres
    xp: 10
    cuerpo: >-
      Recomendadas: (#1) visibilidad de estado, (#2) match con el mundo real
      (jerga del salón/clínica), (#5) prevención de errores.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Auditoría Nielsen — tres heurísticas profundas" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: heuristicas/parcial-3.md
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
      ¿Es buena práctica en esta lección? “Las 10 heurísticas en una línea cada
      una."
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
        texto: '`heuristicas/parcial-3.md` con hallazgos severizados.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Audita con capturas o URLs
    xp: 10
    cuerpo: 'Tabla como en la ficha M16 (ID, heurística, hallazgo, severidad, fix).'
  - id: s7
    tipo: explicacion
    titulo: 4. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
