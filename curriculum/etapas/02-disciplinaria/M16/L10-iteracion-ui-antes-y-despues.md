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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Evidencia visual/código en `iteracion/`.

      P3: iteración documentada. Arreglas al menos lo más doloroso.
  - id: s2
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: '`feat(m16): iteracion UI antes-despues P3`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Iteración UI — antes y después" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: iteracion/ antes-despues (P3)
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
      ¿Es buena práctica en esta lección? “Solo promesas (“lo haremos en M17”)
      sin artefacto."
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
        texto: Evidencia visual/código en `iteracion/`.
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
        `iteracion/` con antes/después (capturas, HTML diff o Figma frames) de
        ≥1 hallazgo alto.
      - Notas de qué cambió y por qué.
      - 'Commit `feat(m16): iteracion UI antes-despues P3`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
