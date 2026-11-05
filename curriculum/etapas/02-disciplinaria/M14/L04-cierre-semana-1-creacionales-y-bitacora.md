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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Bitácora + índice parcial; suite verde.

      Consolidas vocabulario creacional antes de estructurales.
  - id: s2
    tipo: ejemplo
    titulo: 1. Corre tests
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m14-patrones && npm test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre semana 1 — creacionales y bitácora" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: bitacora-semana-1.md + README índice parcial
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

      `cd projects/m14-patrones && npm test`
    comandoEsperado:
      - cd projects/m14-patrones && npm test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m14-patrones && npm test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Bitácora + índice parcial; suite verde.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Bitácora
    xp: 10
    cuerpo: Qué patrón aporta flexibilidad real; qué rechazaste.
  - id: s7
    tipo: explicacion
    titulo: 3. README
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
