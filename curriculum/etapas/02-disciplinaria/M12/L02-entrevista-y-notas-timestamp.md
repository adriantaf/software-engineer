---
id: L02
materia: M12
orden: 2
titulo: Entrevista y notas timestamp
horas: 5
semana: 1
lectura: Técnicas elicitación (plantilla + tu guion)
evidencia: entrevistas/notas-YYYY-MM-DD.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Completar una sesión con notas timestamp en `entrevistas/`.

      P1 exige evidencia de entrevista. Hoy la corres y dejas notas auditables.
  - id: s2
    tipo: ejemplo
    titulo: 1. Prep
    xp: 10
    cuerpo: >-
      Imprime o ten abierto `guion-v1.md`. Acuerda duración (~45 min). Si es
      simulación: briefing escrito del personaje (dueño de X).
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Entrevista y notas timestamp" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: entrevistas/notas-YYYY-MM-DD.md
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
      ¿Es buena práctica en esta lección? “Notas que solo dicen “quiere una
      app”."
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
        texto: Completar una sesión con notas timestamp en `entrevistas/`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Sesión
    xp: 10
    cuerpo: |-
      Formato de notas:

      ```markdown
      Entrevista — 2026-09-26 — Partner A
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Archivo `entrevistas/notas-YYYY-MM-DD.md` con ≥30 min de sesión (real o
        roleplay serio).
      - >-
        Cada bloque marca tiempo + texto; al final: 5 insights y 5 preguntas
        abiertas.
      - 'Commit `docs(m12): l02 notas entrevista`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Entrevista y notas timestamp

**~5.0 h · Semana 1**

P1 exige evidencia de entrevista. Hoy la corres y dejas notas auditables.

## Objetivo

Completar una sesión con notas timestamp en `entrevistas/`.

## Pasos

### 1. Prep (20 min)

Imprime o ten abierto `guion-v1.md`. Acuerda duración (~45 min). Si es simulación: briefing escrito del personaje (dueño de X).

### 2. Sesión (45–60 min)

Formato de notas:

```markdown
# Entrevista — 2026-09-26 — Partner A
## 00:00–00:05 Rapport
…
## 00:05–00:20 Flujo actual
> pedido textual breve
Interpretación: …
```

### 3. Debrief (45 min)

Al final del archivo: insights, dolores rankeados, datos sensibles mencionados, contradicciones, follow-ups.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/entrevistas
git commit -m "docs(m12): l02 notas entrevista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Notas con timestamp; separar pedido textual vs interpretación | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Archivo `entrevistas/notas-YYYY-MM-DD.md` con ≥30 min de sesión (real o roleplay serio).
2. Cada bloque marca tiempo + texto; al final: 5 insights y 5 preguntas abiertas.
3. Commit `docs(m12): l02 notas entrevista`.

## Errores comunes

- Notas que solo dicen “quiere una app”.
- Mezclar lo que dijo con lo que tú inventaste.
- Grabar sin consentimiento si es persona real.

## Siguiente

[L03 — Problemas observados y glosario](L03-problemas-observados-y-glosario.md)
