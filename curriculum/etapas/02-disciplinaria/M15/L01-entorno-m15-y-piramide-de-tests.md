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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `projects/m15-calidad/` ejecutable + `piramide.md` concreto.

      M14 te dejó reglas/services; M15 los blindan. M17 heredará este pipeline.
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m15-calidad
      npm init -y
      npm install -D typescript vitest @types/node
      # scripts.test = "vitest run"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Entorno M15 y pirámide de tests" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m15-calidad/ + piramide.md + Vitest verde
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `cd projects/m15-calidad`
    comandoEsperado:
      - cd projects/m15-calidad
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m15-calidad'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`projects/m15-calidad/` ejecutable + `piramide.md` concreto.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Smoke test
    xp: 10
    cuerpo: '`tests/smoke.test.ts` assert `1+1` o import de un módulo dominio.'
  - id: s7
    tipo: explicacion
    titulo: 3. piramide.md
    xp: 10
    cuerpo: |-
      | Capa | Ejemplos Vitrina | Cantidad relativa |
      |------|---------------------|-------------------|
      | Unit | solape, precio, DTO validate | mayoría |
      | Integración | repo + Postgres test | media |
      | HTTP/API | 401/403 crear pedido | menos |
      | E2E UI | 1–2 flujos | mínimo |
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m15-calidad/` con Vitest y un test smoke verde.'
      - '`piramide.md` dibuja capas y qué irá en cada una para pedidos/auth.'
      - 'Commit `docs(m15): entorno y piramide de tests`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
