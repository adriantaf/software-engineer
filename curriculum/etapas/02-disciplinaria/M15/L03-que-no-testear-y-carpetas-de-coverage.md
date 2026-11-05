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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Coverage es brújula, no religión. Hoy apuntas el medidor al dominio.


      **Objetivo de esta lección:** Config de coverage + política escrita.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Instala provider
    xp: 10
    cuerpo: '`npm i -D @vitest/coverage-v8` y script `test:cov`.'
  - id: s3
    tipo: ejemplo
    titulo: no-testear.md
    xp: 10
    cuerpo: 'Ejemplos: wrappers del framework, generados, `main.ts` de boot.'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Qué no testear y carpetas de coverage», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Qué no testear y
          carpetas de coverage
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
    pregunta: ¿Es recomendable en esta lección? “100% en DTOs vacíos y 0% en solape."
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
        texto: Config de coverage + política escrita.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
