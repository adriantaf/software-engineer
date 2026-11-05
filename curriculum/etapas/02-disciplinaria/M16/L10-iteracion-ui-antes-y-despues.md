---
id: L10
materia: M16
orden: 10
titulo: Iteración UI — antes y después
horas: 5
semana: 3
lectura: Implementar o wireframear fixes; evidencia visual
evidencia: iteracion/ antes-despues (P3)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3: iteración documentada. Arreglas al menos lo más doloroso.


      **Objetivo de esta lección:** Evidencia visual/código en `iteracion/`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`feat(m16): iteracion UI antes-despues P3`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Iteración UI — antes y después», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Iteración UI — antes y
          después
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
      ¿Es recomendable en esta lección? “Solo promesas (“lo haremos en M17”) sin
      artefacto."
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
        texto: Evidencia visual/código en `iteracion/`.
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
    pregunta: ¿Debes hacer esto? “Rediseño total sin trazabilidad al hallazgo."
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
        `iteracion/` con antes/después (capturas, HTML diff o Figma frames) de
        ≥1 hallazgo alto.
      - Notas de qué cambió y por qué.
      - 'Commit `feat(m16): iteracion UI antes-despues P3`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Iteración UI — antes y después

**~5.0 h · Semana 3**

P3: iteración documentada. Arreglas al menos lo más doloroso.

## Objetivo

Evidencia visual/código en `iteracion/`.

## Pasos (hazlos en orden)

### 1. Implementa o wireframea top hallazgos (120–150 min)

### 2. Capturas antes/después (30 min)

### 3. Commit

`feat(m16): iteracion UI antes-despues P3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Cambios concretos con evidencia antes/después | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. `iteracion/` con antes/después (capturas, HTML diff o Figma frames) de ≥1 hallazgo alto.
2. Notas de qué cambió y por qué.
3. Commit `feat(m16): iteracion UI antes-despues P3`.

## Errores comunes

- Solo promesas (“lo haremos en M17”) sin artefacto.
- Rediseño total sin trazabilidad al hallazgo.
- Después igual al antes.

## Siguiente

[L11 — Informe de usabilidad para stakeholders](L11-informe-de-usabilidad-para-stakeholders.md)
