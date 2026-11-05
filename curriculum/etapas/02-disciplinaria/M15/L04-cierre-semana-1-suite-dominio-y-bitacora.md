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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Consolida la base unitaria antes de fakes e HTTP.


      **Objetivo de esta lección:** Bitácora + pirámide con números reales.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m15): cierre semana 1 suite dominio`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre semana 1 — suite dominio y bitácora», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre semana 1 — suite
          dominio y bitác…
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
    pregunta: ¿Es recomendable en esta lección? “Suite flaky ignorada."
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
        texto: Bitácora + pirámide con números reales.
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
    pregunta: ¿Debes hacer esto? “Bitácora sin números."
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
      - '`npm test` verde; bitácora lista reglas cubiertas.'
      - piramide.md actualizada con conteo real de tests unitarios.
      - 'Commit `docs(m15): cierre semana 1 suite dominio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
