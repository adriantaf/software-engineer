---
id: L07
materia: M06
orden: 7
titulo: 'SOLID intro: S, O y D'
horas: 5
semana: 2
lectura: 'Resumen SOLID (S, O, D) + CC cap. 6 y 10'
evidencia: Tres mejoras etiquetadas S/O/D en comentarios o ADR corto solid-notas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      SOLID no es culto: son heurísticas. Hoy aplicarás **S** (responsabilidad
      única), **O** (abierto/cerrado) y **D** (inversión de dependencias) a tu
      dominio.


      **Objetivo de esta lección:** Identificar y corregir al menos una
      violación de S, O y D en el código M06 con cambios medibles (menos
      acoplamiento, extensión sin editar clase core).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      Lee resumen SOLID (libro, artículo mentor o apuntes fiables). Para cada
      letra: definición + ejemplo **no** trivial.
  - id: s3
    tipo: ejemplo
    titulo: '`solid-notas.md`'
    xp: 10
    cuerpo: 'Por principio: violación encontrada → cambio propuesto → commit previsto.'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «SOLID intro: S, O y D», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`solid-notas.md` enlaza commits reales.'
      - id: b
        texto: 'Instalar herramientas al azar sin evidencia de SOLID intro: S, O y D'
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Una clase por línea (SRP mal
      entendido)."
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
        texto: >-
          Identificar y corregir al menos una violación de S, O y D en el código
          M06 con cambios medibles (menos acoplamiento, extensión sin editar
          clase core).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: S — Responsabilidad única
    xp: 10
    cuerpo: Divide clase que mezcla persistencia + reglas + formato de informe.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`solid-notas.md` enlaza commits reales.'
      - >-
        Extensión demostrada (nueva política) sin modificar código prohibido
        (documenta qué tocaste).
      - Tests verdes.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — SOLID intro: S, O y D

**~5 h · Semana 2**

SOLID no es culto: son heurísticas. Hoy aplicarás **S** (responsabilidad única), **O** (abierto/cerrado) y **D** (inversión de dependencias) a tu dominio.

## Objetivo

Identificar y corregir al menos una violación de S, O y D en el código M06 con cambios medibles (menos acoplamiento, extensión sin editar clase core).

## Pasos

### 1. Lectura (60 min)

Lee resumen SOLID (libro, artículo mentor o apuntes fiables). Para cada letra: definición + ejemplo **no** trivial.

### 2. `solid-notas.md` (45 min)

Por principio: violación encontrada → cambio propuesto → commit previsto.

### 3. S — Responsabilidad única (75 min)

Divide clase que mezcla persistencia + reglas + formato de informe.

### 4. O — Abierto/cerrado (75 min)

Ejemplo: nueva regla de préstamo vía estrategia/política sin editar `ServicioPrestamo` entero.

### 5. D — Dependencias (60 min)

Servicio depende de interfaces; wiring en `crearApp()` o factory de tests.

### 6. Commits (15 min)

Hasta tres commits: `refactor(m06): SRP ...`, etc.

## Hecho cuando

1. `solid-notas.md` enlaza commits reales.
2. Extensión demostrada (nueva política) sin modificar código prohibido (documenta qué tocaste).
3. Tests verdes.

## Errores comunes

- Una clase por línea (SRP mal entendido).
- Interfaces duplicadas sin implementaciones.

## Siguiente

[L08 — Refactor documentado (P2)](L08-refactor-documentado-p2.md)
