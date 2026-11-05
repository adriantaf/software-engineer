---
id: L05
materia: M12
orden: 5
titulo: Formato user story y trazabilidad
horas: 5
semana: 2
lectura: Plantilla + historias INVEST
evidencia: stories.md inicio
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Las stories son el puente entrevista → SRS → tests (M15/M17).


      **Objetivo de esta lección:** Arrancar `stories.md` con historias
      trazables.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla de story
    xp: 10
    cuerpo: '```markdown'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Formato user story y trazabilidad», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Formato user story y
          trazabilidad
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
      ¿Es recomendable en esta lección? “Stories técnicas (“como desarrollador
      quiero Postgres”)."
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
        texto: Arrancar `stories.md` con historias trazables.
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
    pregunta: ¿Debes hacer esto? “Sin ID ni trazabilidad."
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
      - '`stories.md` con ≥4 stories en formato estándar + ID (US-01…).'
      - Cada story enlaza a un problema P-xx o insight de entrevista.
      - 'Commit `docs(m12): l05 user stories base`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Formato user story y trazabilidad

**~5.0 h · Semana 2**

Las stories son el puente entrevista → SRS → tests (M15/M17).

## Objetivo

Arrancar `stories.md` con historias trazables.

## Pasos

### 1. Plantilla de story (30 min)

```markdown
## US-01 — …
**Como** owner **quiero** … **para** …
**Problema:** P-01
**Prioridad:** (luego MoSCoW)
```

### 2. Escribe ≥4 (90 min)

Cobertura mínima: agendar pedido, ver agenda del día, alta de cliente, cancelar/reagendar. Lenguaje del glosario.

### 3. Mapa (30 min)

Tabla `US-xx → P-xx → sección SRS futura`.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l05 user stories base"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Como/quiero/para; INVEST; trazabilidad story→problema→SRS | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `stories.md` con ≥4 stories en formato estándar + ID (US-01…).
2. Cada story enlaza a un problema P-xx o insight de entrevista.
3. Commit `docs(m12): l05 user stories base`.

## Errores comunes

- Stories técnicas (“como desarrollador quiero Postgres”).
- Sin ID ni trazabilidad.
- Épicas enormes sin partir.

## Siguiente

[L06 — Criterios de aceptación verificables](L06-criterios-de-aceptacion-verificables.md)
