---
id: L06
materia: M12
orden: 6
titulo: Criterios de aceptación verificables
horas: 5
semana: 2
lectura: Given/When/Then intro
evidencia: stories.md criterios
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Endurecer `stories.md` con aceptación verificable.

      Si no puedes convertirlo en test, no es criterio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Reglas
    xp: 10
    cuerpo: |-
      ```text
      Given un owner autenticado
      When crea una pedido en un slot libre
      Then la pedido aparece en GET /api/pedidos?fecha=… con status 201 al crear
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Criterios de aceptación verificables" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: stories.md criterios
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
    pregunta: ¿Es buena práctica en esta lección? ““Que sea intuitivo”."
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
        texto: Endurecer `stories.md` con aceptación verificable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Reescribe
    xp: 10
    cuerpo: |-
      Ejemplo:

      ```text
      Given un owner autenticado
      When crea una pedido en un slot libre
      Then la pedido aparece en GET /api/pedidos?fecha=… con status 201 al crear
      ```

      Incluye 401/403 donde aplique (aunque el RNF formal llegue en L08).
  - id: s7
    tipo: explicacion
    titulo: 3. Revisión cruzada
    xp: 10
    cuerpo: Marca en amarillo (comentario) criterios vagos y corrígelos.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Cada story existente tiene ≥3 criterios verificables (Given/When/Then o
        lista numerada).
      - Al menos un criterio de error/permiso en 2 stories.
      - 'Commit `docs(m12): l06 criterios aceptacion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Criterios de aceptación verificables

**~5.0 h · Semana 2**

Si no puedes convertirlo en test, no es criterio.

## Objetivo

Endurecer `stories.md` con aceptación verificable.

## Pasos

### 1. Reglas (20 min)

Cada criterio: sujeto observable + condición + resultado. Preferible Given/When/Then.

### 2. Reescribe (90–110 min)

Ejemplo:

```text
Given un owner autenticado
When crea una pedido en un slot libre
Then la pedido aparece en GET /api/pedidos?fecha=… con status 201 al crear
```

Incluye 401/403 donde aplique (aunque el RNF formal llegue en L08).

### 3. Revisión cruzada (30 min)

Marca en amarillo (comentario) criterios vagos y corrígelos.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l06 criterios aceptacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Criterios testeables; happy path + error; nada de “se ve bien” | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Cada story existente tiene ≥3 criterios verificables (Given/When/Then o lista numerada).
2. Al menos un criterio de error/permiso en 2 stories.
3. Commit `docs(m12): l06 criterios aceptacion`.

## Errores comunes

- “Que sea intuitivo”.
- Criterios solo de UI visual.
- Sin casos de error.

## Siguiente

[L07 — Historias de vacío, duplicados y conflicto](L07-historias-de-vacio-duplicados-y-conflicto.md)
