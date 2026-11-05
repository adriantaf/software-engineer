---
id: L24
materia: M02
orden: 24
titulo: Cierre M02 y evidencias
horas: 2.5
semana: 6
lectura: Ficha M02 + checklist projects/m02-programacion
evidencia: bitácora cierre + progress.json + P1–P3 y proyecto verificados
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Marcar sin evidencia rompe el contrato del plan. Hoy auditas con
      honestidad.


      **Objetivo de esta lección:** Confirmar P1–P3 y proyecto CLI, bitácora de
      cierre, y marcar en la UI solo lo que existe en git.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist evidencias
    xp: 10
    cuerpo: >-
      | Ítem | Evidencia | |------|-----------| | **P1** | `projects/m02-katas/`
      ≥20 soluciones TS + README | | **P2** | Script JSON + error archivo
      faltante | | **P3** | `npm test` ≥10 tests | | **Proyecto** | CLI
      add/list/done/stats/export; JSON local; README | Pega `git log --oneline`
      relevante en la bitácora.
  - id: s3
    tipo: ejemplo
    titulo: Bitácora cierre
    xp: 10
    cuerpo: >-
      `projects/m01-diario/semana-XXXX-m02-cierre.md` (o nota en
      m02-programacion): ```markdown # Cierre M02
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M02 y evidencias», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Checklist P1–P3 y proyecto verificada con comandos reales.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Cierre M02 y evidencias
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
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
          Confirmar P1–P3 y proyecto CLI, bitácora de cierre, y marcar en la UI
          solo lo que existe en git.
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
    pregunta: ¿Debes hacer esto? “Katas copiadas sin poder explicarlas."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M02
    xp: 25
    enunciado: >-
      Cierra **Programación I (TypeScript)** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: 20 katas de fundamentos (variables, control, funciones)'
      - 'P2: Módulos + manejo de errores en un script real'
      - 'P3: Primera suite de tests con Vitest (10+ casos)'
      - 'Proyecto: CLI de hábitos y tareas con export CSV'
      - bitácora cierre + progress.json + P1–P3 y proyecto verificados
    rubrica:
      - id: r1
        criterio: Checklist P1–P3 y proyecto verificada con comandos reales.
      - id: r2
        criterio: Bitácora de cierre escrita.
      - id: r3
        criterio: Sabes qué checkboxes puedes marcar hoy.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Checklist P1–P3 y proyecto verificada con comandos reales.
      - Bitácora de cierre escrita.
      - Sabes qué checkboxes puedes marcar hoy.
    siguiente: Materia M02 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M02 y evidencias

**~2.5 h · Semana 6**

Cierras la materia como en M01: revisas evidencias, autoevalúas criterios de dominio y preparas el salto a la siguiente materia.

## Objetivo

Confirmar P1–P3 y proyecto CLI, bitácora de cierre, y marcar en la UI solo lo que existe en git.

## Por qué importa

Marcar sin evidencia rompe el contrato del plan. Hoy auditas con honestidad.

## Pasos

### 1. Checklist evidencias (50 min)

| Ítem | Evidencia |
|------|-----------|
| **P1** | `projects/m02-katas/` ≥20 soluciones TS + README |
| **P2** | Script JSON + error archivo faltante |
| **P3** | `npm test` ≥10 tests |
| **Proyecto** | CLI add/list/done/stats/export; JSON local; README |

Pega `git log --oneline` relevante en la bitácora.

### 2. Bitácora cierre (40 min)

`projects/m01-diario/semana-XXXX-m02-cierre.md` (o nota en m02-programacion):

```markdown
# Cierre M02

## Lecciones L01–L24
- Completadas con evidencia:
- Repetiría:

## Sync vs async (en mis palabras)

## Qué rompió un test cuando lo intenté

## Siguiente materia
```

### 3. Criterios de dominio (30 min)

En la bitácora, sí/no + frase:

- [ ] Programa ~200 líneas sin tutorial paso a paso.
- [ ] Explicas sync vs async.
- [ ] Tests fallan al romper lógica a propósito.
- [ ] CLI la usarías tú una semana real.

### 4. progress.json (20 min)

Actualiza progreso; commit si es ritual del plan.

### 5. Marca UI (20 min)

Lecciones L01–L24 solo con “Hecho cuando” cumplido. Prácticas/proyecto con evidencia. Materia completada si todo cuadra.

## Lectura de esta lección

Vuelve a la [ficha M02](../M02-programacion-i.md) y repasa errores comunes.

## Hecho cuando

1. Checklist P1–P3 y proyecto verificada con comandos reales.
2. Bitácora de cierre escrita.
3. Sabes qué checkboxes puedes marcar hoy.

## Errores comunes

- Marcar M02 completa con CLI sin `export`.
- Katas copiadas sin poder explicarlas.
- Tests verdes pero triviales (revisar P3).

## Siguiente

Vuelve a la [ficha M02](../M02-programacion-i.md), cierra checkboxes con evidencia, y continúa con la siguiente materia del plan.
