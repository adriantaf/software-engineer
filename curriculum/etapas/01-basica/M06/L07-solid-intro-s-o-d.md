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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Identificar y corregir al menos una violación de S, O y D en
      el código M06 con cambios medibles (menos acoplamiento, extensión sin
      editar clase core).


      SOLID no es culto: son heurísticas. Hoy aplicarás **S** (responsabilidad
      única), **O** (abierto/cerrado) y **D** (inversión de dependencias) a tu
      dominio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      Lee resumen SOLID (libro, artículo mentor o apuntes fiables). Para cada
      letra: definición + ejemplo **no** trivial.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "SOLID intro: S, O y D" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: >-
          Tres mejoras etiquetadas S/O/D en comentarios o ADR corto
          solid-notas.md
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
      ¿Es buena práctica en esta lección? “Una clase por línea (SRP mal
      entendido)."
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
          Identificar y corregir al menos una violación de S, O y D en el código
          M06 con cambios medibles (menos acoplamiento, extensión sin editar c…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `solid-notas.md`
    xp: 10
    cuerpo: 'Por principio: violación encontrada → cambio propuesto → commit previsto.'
  - id: s7
    tipo: explicacion
    titulo: 3. S — Responsabilidad única
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
