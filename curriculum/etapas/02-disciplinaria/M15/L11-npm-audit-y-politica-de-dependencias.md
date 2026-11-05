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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El piloto también tiene supply chain. Hoy el audit deja de ser opcional.


      **Objetivo de esta lección:** Audit en pipeline + política escrita (P2
      completo con lint+test+audit).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`ci(m15): npm audit y politica deps`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «npm audit y política de dependencias», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de npm audit y política de
          dependencias
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
    pregunta: >-
      ¿Es recomendable en esta lección? “`--audit-level=critical` sin mirar
      high."
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
        texto: >-
          Audit en pipeline + política escrita (P2 completo con
          lint+test+audit).
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
    pregunta: ¿Debes hacer esto? “Silenciar audit con flag oculto permanente."
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
      - '`npm audit --audit-level=high` (o equivalente) en workflow o script CI.'
      - '`docs/politica-deps.md` describe qué hacer con vulns y excepciones.'
      - 'Commit `ci(m15): npm audit y politica deps`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
