---
id: L20
materia: M13
orden: 20
titulo: Cierre M13 — trazabilidad y dominio
horas: 5
semana: 5
lectura: Criterios de dominio ficha M13; trazabilidad SRS↔diagramas
evidencia: trazabilidad.md + README final; criterios de dominio autoevaluados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la materia demostrando que cada diagrama sirve a un requisito — y
      que puedes defender el monolito modular.


      **Objetivo de esta lección:** Matriz de trazabilidad + autoevaluación de
      criterios de dominio de la ficha.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Matriz
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Criterios de dominio
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M13 — trazabilidad y dominio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M13 —
          trazabilidad y dominio
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/m13-diseno`
    comandoEsperado:
      - git add projects/m13-diseno
      - 'git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m13-diseno'
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
        texto: >-
          Matriz de trazabilidad + autoevaluación de criterios de dominio de la
          ficha.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M13
    xp: 25
    enunciado: >-
      Cierra **Análisis y diseño de software** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Casos de uso / flujos principales'
      - 'P2: Diagrama de clases y secuencia'
      - 'P3: Arquitectura en capas + trust boundaries'
      - 'Proyecto: Paquete de diseño del producto (ADR + diagramas)'
      - trazabilidad.md + README final; criterios de dominio autoevaluados
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: '`trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.'
      - id: r3
        criterio: Autoevaluación de criterios de dominio en bitácora o README (honesta).
      - id: r4
        criterio: 'Commit `docs(m13): cierre trazabilidad y criterios de dominio`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.'
      - Autoevaluación de criterios de dominio en bitácora o README (honesta).
      - 'Commit `docs(m13): cierre trazabilidad y criterios de dominio`.'
    siguiente: Materia M13 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Cierre M13 — trazabilidad y dominio

**~5.0 h · Semana 5**

Cierras la materia demostrando que cada diagrama sirve a un requisito — y que puedes defender el monolito modular.

## Objetivo

Matriz de trazabilidad + autoevaluación de criterios de dominio de la ficha.

## Pasos (hazlos en orden)

### 1. Matriz (70–90 min)

`trazabilidad.md`:

| Historia SRS | UC | Diagrama / ADR |
|--------------|----|----------------|
| H-pedido-01 | UC-03 | secuencia-crear-pedido, ADR 002 |

Borra artefactos huérfanos o enlázalos.

### 2. Criterios de dominio (40–50 min)

De la ficha M13 — responde en `bitacora-cierre.md`:

- ¿Defiendes monolito modular con trade-offs?
- ¿Sabes dónde se valida el rol?
- ¿Un compañero puede empezar M17 con SRS + este paquete?

### 3. Pulido README (30 min)

Estado: “Paquete listo para M17” + fecha.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Trazabilidad requisito→diseño; autoevaluación criterios de dominio | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.
2. Autoevaluación de criterios de dominio en bitácora o README (honesta).
3. Commit `docs(m13): cierre trazabilidad y criterios de dominio`.

## Errores comunes

- Diagramas sin fila en la matriz de trazabilidad.
- Autoevaluación todo ✓ sin evidencia.
- Microservicios reintroducidos en el cierre.

## Siguiente

Materia siguiente: [M14 — Patrones](../M14-patrones.md) · L01 en `../M14/`.
