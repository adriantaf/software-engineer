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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Evidencia de review aplicado.

      La checklist sin uso no cuenta para P3.
  - id: s2
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m15): review simulado P3`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Review simulado en PR o notas" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: review-ejemplo.md o comentarios en PR
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
    pregunta: ¿Es buena práctica en esta lección? “Checklist todo ✓ sin mirar el diff."
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
        texto: Evidencia de review aplicado.
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
      - >-
        `review-ejemplo.md` (o captura/enlace PR) aplicando el checklist a un
        diff tuyo.
      - Al menos 1 hallazgo real o “N/A justificado” por sección de seguridad.
      - 'Commit `docs(m15): review simulado P3`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
