---
id: L11
materia: M15
orden: 11
titulo: npm audit y política de dependencias
horas: 5
semana: 3
lectura: npm audit; política high/critical
evidencia: audit en CI + docs/politica-deps.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Audit en pipeline + política escrita (P2 completo con
      lint+test+audit).


      El piloto también tiene supply chain. Hoy el audit deja de ser opcional.
  - id: s2
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: '`ci(m15): npm audit y politica deps`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "npm audit y política de dependencias" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: audit en CI + docs/politica-deps.md
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
      ¿Es buena práctica en esta lección? “`--audit-level=critical` sin mirar
      high."
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
        texto: >-
          Audit en pipeline + política escrita (P2 completo con
          lint+test+audit).
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
      - '`npm audit --audit-level=high` (o equivalente) en workflow o script CI.'
      - '`docs/politica-deps.md` describe qué hacer con vulns y excepciones.'
      - 'Commit `ci(m15): npm audit y politica deps`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — npm audit y política de dependencias

**~5.0 h · Semana 3**

El piloto también tiene supply chain. Hoy el audit deja de ser opcional.

## Objetivo

Audit en pipeline + política escrita (P2 completo con lint+test+audit).

## Pasos (hazlos en orden)

### 1. Corre audit local (30 min)

### 2. Añade a CI (40 min)

### 3. política-deps.md (50 min)

### 4. Commit

`ci(m15): npm audit y politica deps`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Audit en CI; excepciones con ticket/motivo | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `npm audit --audit-level=high` (o equivalente) en workflow o script CI.
2. `docs/politica-deps.md` describe qué hacer con vulns y excepciones.
3. Commit `ci(m15): npm audit y politica deps`.

## Errores comunes

- `--audit-level=critical` sin mirar high.
- Silenciar audit con flag oculto permanente.
- No pinear versiones y vivir en builds flaky.

## Siguiente

[L12 — Badge README y artefacto de test](L12-badge-readme-y-artefacto-de-test.md)
