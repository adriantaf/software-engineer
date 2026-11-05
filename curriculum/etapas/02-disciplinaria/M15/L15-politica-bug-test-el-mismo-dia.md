---
id: L15
materia: M15
orden: 15
titulo: Política bug → test el mismo día
horas: 5
semana: 4
lectura: Regresión inmediata; ejemplo real
evidencia: docs/bug-test-mismo-dia.md + test de regresión
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Regla del plan: el bug no se cierra solo con el fix.


      **Objetivo de esta lección:** Política + una regresión demostrable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inyecta o usa un bug
    xp: 10
    cuerpo: Red (test falla) → fix → green.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`test(m15): regresion bug mismo dia`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Política bug → test el mismo día», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Política bug → test el
          mismo día
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
    pregunta: ¿Es recomendable en esta lección? “Política sin ejemplo."
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
        texto: Política + una regresión demostrable.
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
    pregunta: ¿Debes hacer esto? “Fix sin test."
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
      - Política escrita en el repo.
      - >-
        Al menos un bug (real o inyectado) con test de regresión añadido el
        mismo día (documentado).
      - 'Commit `test(m15): regresion bug mismo dia`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Política bug → test el mismo día

**~5.0 h · Semana 4**

Regla del plan: el bug no se cierra solo con el fix.

## Objetivo

Política + una regresión demostrable.

## Pasos (hazlos en orden)

### 1. Escribe la política (40 min)

### 2. Inyecta o usa un bug (60–80 min)

Red (test falla) → fix → green.

### 3. Commit

`test(m15): regresion bug mismo dia`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Todo bug encontrado genera test el mismo día | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita en el repo.
2. Al menos un bug (real o inyectado) con test de regresión añadido el mismo día (documentado).
3. Commit `test(m15): regresion bug mismo dia`.

## Errores comunes

- Política sin ejemplo.
- Fix sin test.
- Test que no falla ante el bug.

## Siguiente

[L16 — Cierre M15 — pipeline, coverage dominio, dominio](L16-cierre-m15-pipeline-coverage-dominio-dominio.md)
