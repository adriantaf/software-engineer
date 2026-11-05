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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 exige evidencia de entrevista. Hoy la corres y dejas notas auditables.


      **Objetivo de esta lección:** Completar una sesión con notas timestamp en
      `entrevistas/`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Prep
    xp: 10
    cuerpo: >-
      Imprime o ten abierto `guion-v1.md`. Acuerda duración (~45 min). Si es
      simulación: briefing escrito del personaje (dueño de X).
  - id: s3
    tipo: ejemplo
    titulo: Sesión
    xp: 10
    cuerpo: 'Formato de notas: ```markdown # Entrevista — 2026-09-26 — Partner A'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Entrevista y notas timestamp», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Entrevista y notas
          timestamp
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
    pregunta: ¿Es recomendable en esta lección? “Notas que solo dicen “quiere una app”."
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
        texto: Completar una sesión con notas timestamp en `entrevistas/`.
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
    pregunta: ¿Debes hacer esto? “Mezclar lo que dijo con lo que tú inventaste."
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
      - >-
        Archivo `entrevistas/notas-YYYY-MM-DD.md` con ≥30 min de sesión (real o
        roleplay serio).
      - >-
        Cada bloque marca tiempo + texto; al final: 5 insights y 5 preguntas
        abiertas.
      - 'Commit `docs(m12): l02 notas entrevista`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
