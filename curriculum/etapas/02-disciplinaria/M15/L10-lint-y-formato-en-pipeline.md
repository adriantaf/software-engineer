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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      CI sin lint deja pasar basura que los tests no ven.


      **Objetivo de esta lección:** Lint (y opcional format check) en local +
      Actions.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`ci(m15): lint en pipeline`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lint y formato en pipeline», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lint y formato en
          pipeline
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
    pregunta: ¿Es recomendable en esta lección? “Lint solo warning ignorado."
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
        texto: Lint (y opcional format check) en local + Actions.
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
    pregunta: ¿Debes hacer esto? “Reglas tan estrictas que nadie corre local."
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
      - Script `npm run lint` local verde.
      - Paso de lint en el workflow (falla el job si lint falla).
      - 'Commit `ci(m15): lint en pipeline`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
