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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Arrancar `stories.md` con historias trazables.

      Las stories son el puente entrevista → SRS → tests (M15/M17).
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla de story
    xp: 10
    cuerpo: '```markdown'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Formato user story y trazabilidad" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: stories.md inicio
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
      ¿Es buena práctica en esta lección? “Stories técnicas (“como desarrollador
      quiero Postgres”)."
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
        texto: Arrancar `stories.md` con historias trazables.
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
      - '`stories.md` con ≥4 stories en formato estándar + ID (US-01…).'
      - Cada story enlaza a un problema P-xx o insight de entrevista.
      - 'Commit `docs(m12): l05 user stories base`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
