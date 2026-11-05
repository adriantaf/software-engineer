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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Si no puedes convertirlo en test, no es criterio.


      **Objetivo de esta lección:** Endurecer `stories.md` con aceptación
      verificable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Reglas
    xp: 10
    cuerpo: |-
      ```text
      Given un owner autenticado
      When crea una pedido en un slot libre
      Then la pedido aparece en GET /api/pedidos?fecha=… con status 201 al crear
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Reescribe
    xp: 10
    cuerpo: >-
      ```text

      Given un owner autenticado

      When crea una pedido en un slot libre

      Then la pedido aparece en GET /api/pedidos?fecha=… con status 201 al crear

      ```


      Ejemplo: Incluye 401/403 donde aplique (aunque el RNF formal llegue en
      L08).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Criterios de aceptación verificables», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Criterios de aceptación
          verificables
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
    pregunta: ¿Es recomendable en esta lección? ““Que sea intuitivo”."
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
        texto: Endurecer `stories.md` con aceptación verificable.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Revisión cruzada
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
