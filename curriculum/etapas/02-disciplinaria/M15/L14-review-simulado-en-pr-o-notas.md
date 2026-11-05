---
id: L14
materia: M15
orden: 14
titulo: Review simulado en PR o notas
horas: 5
semana: 4
lectura: Aplicar checklist a un cambio real
evidencia: review-ejemplo.md o comentarios en PR
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La checklist sin uso no cuenta para P3.


      **Objetivo de esta lección:** Evidencia de review aplicado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m15): review simulado P3`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Review simulado en PR o notas», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Review simulado en PR o
          notas
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
    pregunta: ¿Es recomendable en esta lección? “Checklist todo ✓ sin mirar el diff."
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
        texto: Evidencia de review aplicado.
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
    pregunta: ¿Debes hacer esto? “Review de código ajeno inventado."
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
      - >-
        `review-ejemplo.md` (o captura/enlace PR) aplicando el checklist a un
        diff tuyo.
      - Al menos 1 hallazgo real o “N/A justificado” por sección de seguridad.
      - 'Commit `docs(m15): review simulado P3`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Review simulado en PR o notas

**~5.0 h · Semana 4**

La checklist sin uso no cuenta para P3.

## Objetivo

Evidencia de review aplicado.

## Pasos (hazlos en orden)

### 1. Elige un diff (20 min) — idealmente de M14/M15

### 2. Llena review-ejemplo.md (80–100 min)

### 3. Commit

`docs(m15): review simulado P3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Evidencia de uso del checklist en un cambio | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `review-ejemplo.md` (o captura/enlace PR) aplicando el checklist a un diff tuyo.
2. Al menos 1 hallazgo real o “N/A justificado” por sección de seguridad.
3. Commit `docs(m15): review simulado P3`.

## Errores comunes

- Checklist todo ✓ sin mirar el diff.
- Review de código ajeno inventado.
- Sin enlace al commit/diff revisado.

## Siguiente

[L15 — Política bug → test el mismo día](L15-politica-bug-test-el-mismo-dia.md)
