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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Confirmar P1–P3 y proyecto CLI, bitácora de cierre, y marcar
      en la UI solo lo que existe en git.


      Marcar sin evidencia rompe el contrato del plan. Hoy auditas con
      honestidad.
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist evidencias
    xp: 10
    cuerpo: |-
      | Ítem | Evidencia |
      |------|-----------|
      | **P1** | `projects/m02-katas/` ≥20 soluciones TS + README |
      | **P2** | Script JSON + error archivo faltante |
      | **P3** | `npm test` ≥10 tests |
      | **Proyecto** | CLI add/list/done/stats/export; JSON local; README |

      Pega `git log --oneline` relevante en la bitácora.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Cierre M02 y evidencias" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: bitácora cierre + progress.json + P1–P3 y proyecto verificados
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Marcar M02 completa con CLI sin
      `export`."
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
        texto: >-
          Confirmar P1–P3 y proyecto CLI, bitácora de cierre, y marcar en la UI
          solo lo que existe en git.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Bitácora cierre
    xp: 10
    cuerpo: >-
      `projects/m01-diario/semana-XXXX-m02-cierre.md` (o nota en
      m02-programacion):


      ```markdown

      Cierre M02
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Checklist P1–P3 y proyecto verificada con comandos reales.
      - Bitácora de cierre escrita.
      - Sabes qué checkboxes puedes marcar hoy.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
