---
id: L01
materia: M15
orden: 1
titulo: Entorno M15 y pirámide de tests
horas: 5
semana: 1
lectura: Pirámide de tests; Vitest setup Vitrina
evidencia: projects/m15-calidad/ + piramide.md + Vitest verde
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M14 te dejó reglas/services; M15 los blindan. M17 heredará este pipeline.


      **Objetivo de esta lección:** `projects/m15-calidad/` ejecutable +
      `piramide.md` concreto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m15-calidad

      npm init -y

      npm install -D typescript vitest @types/node

      # scripts.test = "vitest run"

      ```


      Estructura: Puedes reutilizar lógica de `projects/m14-patrones` (copia o
      path documentado).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Smoke test
    xp: 10
    cuerpo: |-
      ```text
      src/domain/
      src/application/
      tests/
      piramide.md
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Entorno M15 y pirámide de tests», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Entorno M15 y pirámide
          de tests
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `cd projects/m15-calidad`
    comandoEsperado:
      - cd projects/m15-calidad
      - npm init -y
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m15-calidad'
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
        texto: '`projects/m15-calidad/` ejecutable + `piramide.md` concreto.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: piramide.md
    xp: 10
    cuerpo: >-
      | Capa | Ejemplos Vitrina | Cantidad relativa |
      |------|---------------------|-------------------| | Unit | solape,
      precio, DTO validate | mayoría | | Integración | repo + Postgres test |
      media | | HTTP/API | 401/403 crear pedido | menos | | E2E UI | 1–2 flujos
      | mínimo |
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m15-calidad/` con Vitest y un test smoke verde.'
      - '`piramide.md` dibuja capas y qué irá en cada una para pedidos/auth.'
      - 'Commit `docs(m15): entorno y piramide de tests`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Entorno M15 y pirámide de tests

**~5.0 h · Semana 1**

Sin suite local, CI es teatro. Hoy levantas Vitest y decides la pirámide del piloto.

## Objetivo

`projects/m15-calidad/` ejecutable + `piramide.md` concreto.

## Por qué empieza así

M14 te dejó reglas/services; M15 los blindan. M17 heredará este pipeline.

## Pasos (hazlos en orden)

### 1. Scaffold (50–70 min)

```bash
cd projects/m15-calidad
npm init -y
npm install -D typescript vitest @types/node
# scripts.test = "vitest run"
```

Estructura:

```text
src/domain/
src/application/
tests/
piramide.md
```

Puedes reutilizar lógica de `projects/m14-patrones` (copia o path documentado).

### 2. Smoke test (30 min)

`tests/smoke.test.ts` assert `1+1` o import de un módulo dominio.

### 3. piramide.md (60–70 min)

| Capa | Ejemplos Vitrina | Cantidad relativa |
|------|---------------------|-------------------|
| Unit | solape, precio, DTO validate | mayoría |
| Integración | repo + Postgres test | media |
| HTTP/API | 401/403 crear pedido | menos |
| E2E UI | 1–2 flujos | mínimo |

### 4. Commit

`docs(m15): entorno y piramide de tests`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Pirámide: muchos unit, menos integración, pocos E2E | [Vitest — Getting Started](https://vitest.dev/guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m15-calidad/` con Vitest y un test smoke verde.
2. `piramide.md` dibuja capas y qué irá en cada una para pedidos/auth.
3. Commit `docs(m15): entorno y piramide de tests`.

## Errores comunes

- Pirámide invertida (todo E2E).
- Proyecto sin script `test`.
- Copiar pirámide genérica sin mapear a Vitrina.

## Siguiente

[L02 — Tests unitarios puros de reglas de pedido](L02-tests-unitarios-puros-de-reglas-de-pedido.md)
