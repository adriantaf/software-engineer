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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 exige 5 personas + síntesis.


      **Objetivo de esta lección:** Cerrar sesiones y `resumen-5-usuarios.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Matriz de patrones
    xp: 10
    cuerpo: >-
      | Hallazgo | # participantes | Severidad |
      |----------|-----------------|-----------| | No encuentra “Nueva pedido” |
      4/5 | alta |
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m16): resumen 5 usuarios cierre P2`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sesiones 4–5 y resumen agregado P2», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Sesiones 4–5 y resumen
          agregado P2
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
    pregunta: ¿Es recomendable en esta lección? “Cinco clones de la misma nota."
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
        texto: Cerrar sesiones y `resumen-5-usuarios.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Resumen sin frecuencias."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Cinco sesiones documentadas.
      - '`sesiones/resumen-5-usuarios.md` con patrones (no solo anécdotas) — P2.'
      - 'Commit `docs(m16): resumen 5 usuarios cierre P2`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
