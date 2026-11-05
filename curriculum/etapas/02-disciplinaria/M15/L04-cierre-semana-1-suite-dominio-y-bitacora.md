---
id: L04
materia: M15
orden: 4
titulo: Cierre semana 1 — suite dominio y bitácora
horas: 5
semana: 1
lectura: Cierre suite dominio; bitácora
evidencia: bitacora-semana-1.md + piramide actualizada
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Bitácora + pirámide con números reales.

      Consolida la base unitaria antes de fakes e HTTP.
  - id: s2
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: '`docs(m15): cierre semana 1 suite dominio`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre semana 1 — suite dominio y bitácora" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: bitacora-semana-1.md + piramide actualizada
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
    pregunta: ¿Es buena práctica en esta lección? “Suite flaky ignorada."
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
        texto: Bitácora + pirámide con números reales.
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
      - '`npm test` verde; bitácora lista reglas cubiertas.'
      - piramide.md actualizada con conteo real de tests unitarios.
      - 'Commit `docs(m15): cierre semana 1 suite dominio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre semana 1 — suite dominio y bitácora

**~5.0 h · Semana 1**

Consolida la base unitaria antes de fakes e HTTP.

## Objetivo

Bitácora + pirámide con números reales.

## Pasos (hazlos en orden)

### 1. Corre suite + cov (30 min)

### 2. Bitácora (50 min)

### 3. Deuda (30 min) — qué falta en integración

### 4. Commit

`docs(m15): cierre semana 1 suite dominio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Cierre semana 1: unitarios de dominio estables | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `npm test` verde; bitácora lista reglas cubiertas.
2. piramide.md actualizada con conteo real de tests unitarios.
3. Commit `docs(m15): cierre semana 1 suite dominio`.

## Errores comunes

- Suite flaky ignorada.
- Bitácora sin números.
- Marcar avance sin coverage script.

## Siguiente

[L05 — Fake repositorio y reloj para tests rápidos](L05-fake-repositorio-y-reloj-para-tests-rapidos.md)
