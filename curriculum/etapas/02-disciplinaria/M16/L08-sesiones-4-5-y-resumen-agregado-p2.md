---
id: L08
materia: M16
orden: 8
titulo: Sesiones 4–5 y resumen agregado P2
horas: 5
semana: 2
lectura: Síntesis de patrones; cierre P2
evidencia: participante-4..5 + resumen-5-usuarios.md (P2)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Cerrar sesiones y `resumen-5-usuarios.md`.

      P2 exige 5 personas + síntesis.
  - id: s2
    tipo: ejemplo
    titulo: 2. Matriz de patrones
    xp: 10
    cuerpo: |-
      | Hallazgo | # participantes | Severidad |
      |----------|-----------------|-----------|
      | No encuentra “Nueva pedido” | 4/5 | alta |
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sesiones 4–5 y resumen agregado P2" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: participante-4..5 + resumen-5-usuarios.md (P2)
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
    pregunta: ¿Es buena práctica en esta lección? “Cinco clones de la misma nota."
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
        texto: Cerrar sesiones y `resumen-5-usuarios.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m16): resumen 5 usuarios cierre P2`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Cinco sesiones documentadas.
      - '`sesiones/resumen-5-usuarios.md` con patrones (no solo anécdotas) — P2.'
      - 'Commit `docs(m16): resumen 5 usuarios cierre P2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Sesiones 4–5 y resumen agregado P2

**~5.0 h · Semana 2**

P2 exige 5 personas + síntesis.

## Objetivo

Cerrar sesiones y `resumen-5-usuarios.md`.

## Pasos (hazlos en orden)

### 1. Sesiones 4–5 (60–90 min netos)

### 2. Matriz de patrones (60–70 min)

| Hallazgo | # participantes | Severidad |
|----------|-----------------|-----------|
| No encuentra “Nueva pedido” | 4/5 | alta |

### 3. Commit

`docs(m16): resumen 5 usuarios cierre P2`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Cinco sesiones + resumen agregado de patrones | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Cinco sesiones documentadas.
2. `sesiones/resumen-5-usuarios.md` con patrones (no solo anécdotas) — P2.
3. Commit `docs(m16): resumen 5 usuarios cierre P2`.

## Errores comunes

- Cinco clones de la misma nota.
- Resumen sin frecuencias.
- Ignorar hallazgos que contradicen tu ego de diseño.

## Siguiente

[L09 — Priorizar top 5 hallazgos](L09-priorizar-top-5-hallazgos.md)
