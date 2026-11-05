---
id: L03
materia: M15
orden: 3
titulo: Qué no testear y carpetas de coverage
horas: 5
semana: 1
lectura: Coverage útil; exclusiones conscientes
evidencia: vitest coverage en domain/ + docs/no-testear.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Config de coverage + política escrita.

      Coverage es brújula, no religión. Hoy apuntas el medidor al dominio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Instala provider
    xp: 10
    cuerpo: '`npm i -D @vitest/coverage-v8` y script `test:cov`.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Qué no testear y carpetas de coverage" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: vitest coverage en domain/ + docs/no-testear.md
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
    pregunta: ¿Es buena práctica en esta lección? “100% en DTOs vacíos y 0% en solape."
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
        texto: Config de coverage + política escrita.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. no-testear.md
    xp: 10
    cuerpo: 'Ejemplos: wrappers del framework, generados, `main.ts` de boot.'
  - id: s7
    tipo: explicacion
    titulo: 4. Commit
    xp: 10
    cuerpo: '`test(m15): coverage dominio y politica no-testear`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Coverage configurado enfocando `src/domain/` (o carpeta equivalente).
      - >-
        `docs/no-testear.md` lista ≥3 cosas que no testearás (ORM glue,
        framework).
      - 'Commit `test(m15): coverage dominio y politica no-testear`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Qué no testear y carpetas de coverage

**~5.0 h · Semana 1**

Coverage es brújula, no religión. Hoy apuntas el medidor al dominio.

## Objetivo

Config de coverage + política escrita.

## Pasos (hazlos en orden)

### 1. Instala provider (30 min)

`npm i -D @vitest/coverage-v8` y script `test:cov`.

### 2. include domain (40 min)

### 3. no-testear.md (50 min)

Ejemplos: wrappers del framework, generados, `main.ts` de boot.

### 4. Commit

`test(m15): coverage dominio y politica no-testear`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | No perseguir 100% en boilerplate; coverage en domain/ | [Vitest — Coverage](https://vitest.dev/guide/coverage.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Coverage configurado enfocando `src/domain/**` (o carpeta equivalente).
2. `docs/no-testear.md` lista ≥3 cosas que no testearás (ORM glue, framework).
3. Commit `test(m15): coverage dominio y politica no-testear`.

## Errores comunes

- 100% en DTOs vacíos y 0% en solape.
- Excluir `domain/` “porque es difícil”.
- Subir reportes HTML enormes al repo sin necesidad.

## Siguiente

[L04 — Cierre semana 1 — suite dominio y bitácora](L04-cierre-semana-1-suite-dominio-y-bitacora.md)
