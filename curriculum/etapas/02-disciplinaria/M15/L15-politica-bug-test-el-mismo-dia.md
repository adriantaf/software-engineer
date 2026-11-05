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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Política + una regresión demostrable.

      Regla del plan: el bug no se cierra solo con el fix.
  - id: s2
    tipo: ejemplo
    titulo: 2. Inyecta o usa un bug
    xp: 10
    cuerpo: Red (test falla) → fix → green.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Política bug → test el mismo día" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: docs/bug-test-mismo-dia.md + test de regresión
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
    pregunta: ¿Es buena práctica en esta lección? “Política sin ejemplo."
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
        texto: Política + una regresión demostrable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`test(m15): regresion bug mismo dia`'
  - id: s7
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
