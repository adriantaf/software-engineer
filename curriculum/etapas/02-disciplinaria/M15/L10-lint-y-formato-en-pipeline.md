---
id: L10
materia: M15
orden: 10
titulo: Lint y formato en pipeline
horas: 5
semana: 3
lectura: ESLint/Prettier o oxlint; fail on lint
evidencia: script lint en CI
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Lint (y opcional format check) en local + Actions.

      CI sin lint deja pasar basura que los tests no ven.
  - id: s2
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: '`ci(m15): lint en pipeline`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Lint y formato en pipeline" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: script lint en CI
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
    pregunta: ¿Es buena práctica en esta lección? “Lint solo warning ignorado."
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
        texto: Lint (y opcional format check) en local + Actions.
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
      - Script `npm run lint` local verde.
      - Paso de lint en el workflow (falla el job si lint falla).
      - 'Commit `ci(m15): lint en pipeline`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Lint y formato en pipeline

**~5.0 h · Semana 3**

CI sin lint deja pasar basura que los tests no ven.

## Objetivo

Lint (y opcional format check) en local + Actions.

## Pasos (hazlos en orden)

### 1. Config ESLint o equivalente (60–70 min)

### 2. Añade step al workflow (30 min)

### 3. Commit

`ci(m15): lint en pipeline`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Lint en CI: mismo estándar local y remoto | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Script `npm run lint` local verde.
2. Paso de lint en el workflow (falla el job si lint falla).
3. Commit `ci(m15): lint en pipeline`.

## Errores comunes

- Lint solo warning ignorado.
- Reglas tan estrictas que nadie corre local.
- Formatear en CI sin config en repo.

## Siguiente

[L11 — npm audit y política de dependencias](L11-npm-audit-y-politica-de-dependencias.md)
