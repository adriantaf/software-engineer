---
id: L04
materia: M14
orden: 4
titulo: Cierre semana 1 — creacionales y bitácora
horas: 5
semana: 1
lectura: Repaso Factory/Strategy; bitácora
evidencia: bitacora-semana-1.md + README índice parcial
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Consolidas vocabulario creacional antes de estructurales.


      **Objetivo de esta lección:** Bitácora + índice parcial; suite verde.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Corre tests
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m14-patrones && npm test
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Bitácora
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m14-patrones && npm test
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre semana 1 — creacionales y bitácora», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre semana 1 —
          creacionales y bitáco…
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

      `cd projects/m14-patrones && npm test`
    comandoEsperado:
      - cd projects/m14-patrones && npm test
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m14-patrones && npm test'
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
        texto: Bitácora + índice parcial; suite verde.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README
    xp: 10
    cuerpo: Tabla patrón → archivo → ADR.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Bitácora semana 1 lista Strategy, Factory y rechazo de Singleton.'
      - 'README enlaza `src/pricing`, `src/notify`, ADRs.'
      - 'Commit `docs(m14): cierre semana 1 creacionales`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre semana 1 — creacionales y bitácora

**~5.0 h · Semana 1**

Consolidas vocabulario creacional antes de estructurales.

## Objetivo

Bitácora + índice parcial; suite verde.

## Pasos (hazlos en orden)

### 1. Corre tests (20 min)

```bash
cd projects/m14-patrones && npm test
```

### 2. Bitácora (50–60 min)

Qué patrón aporta flexibilidad real; qué rechazaste.

### 3. README (40 min)

Tabla patrón → archivo → ADR.

### 4. Commit (15 min)

`docs(m14): cierre semana 1 creacionales`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Cierre creacionales: evidencias Strategy + Factory | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Bitácora semana 1 lista Strategy, Factory y rechazo de Singleton.
2. README enlaza `src/pricing`, `src/notify`, ADRs.
3. Commit `docs(m14): cierre semana 1 creacionales`.

## Errores comunes

- Bitácora sin rutas a archivos.
- Tests rotos dejados “para después”.
- ADR sin enlace desde README.

## Siguiente

[L05 — Adapter para API de calendario externo](L05-adapter-para-api-de-calendario-externo.md)
