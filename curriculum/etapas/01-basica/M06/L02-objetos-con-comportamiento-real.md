---
id: L02
materia: M06
orden: 2
titulo: Objetos con comportamiento real
horas: 5
semana: 1
lectura: Código limpio cap. 3 (funciones) + cap. 10 intro (clases)
evidencia: 'Métodos de dominio con tests; commit feat(m06): comportamiento en entidades'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Mover reglas de negocio a métodos cohesivos (entidad o
      agregado pequeño); evitar clases contenedor vacías.


      Un objeto combina datos y **comportamiento**. Datos anémicos + servicios
      gigantes es un antipatrón que corregirás hoy.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      CC cap. 3 (funciones pequeñas) + inicio cap. 10. Lista: ¿cuándo una clase
      aporta vs cuándo estorba?
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Objetos con comportamiento real" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          Métodos de dominio con tests; commit feat(m06): comportamiento en
          entidades
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
      ¿Es buena práctica en esta lección? “God class `Biblioteca` de 400
      líneas."
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
          Mover reglas de negocio a métodos cohesivos (entidad o agregado
          pequeño); evitar clases contenedor vacías.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Refactor de anémico → rico
    xp: 10
    cuerpo: >-
      Si tu `Libro` solo expone campos, añade métodos como `marcarPrestado():
      void` con invariantes (no prestar dos veces). La fachada `Biblioteca`
      orquesta, no reimplementa toda la lógica en ifs sueltos.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests de invariantes
    xp: 10
    cuerpo: |-
      - No prestar si ya prestado.
      - Devolver solo si estaba prestado.
      - Mensajes de error legibles (string constantes o pequeño catálogo).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Reglas de negocio viven en métodos nombrados, no dispersos.'
      - Tests cubren invariantes principales.
      - Commit con mensaje que mencione comportamiento en entidades.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Objetos con comportamiento real

**~5 h · Semana 1**

Un objeto combina datos y **comportamiento**. Datos anémicos + servicios gigantes es un antipatrón que corregirás hoy.

## Objetivo

Mover reglas de negocio a métodos cohesivos (entidad o agregado pequeño); evitar clases contenedor vacías.

## Pasos

### 1. Lectura (45 min)

CC cap. 3 (funciones pequeñas) + inicio cap. 10. Lista: ¿cuándo una clase aporta vs cuándo estorba?

### 2. Refactor de anémico → rico (120 min)

Si tu `Libro` solo expone campos, añade métodos como `marcarPrestado(): void` con invariantes (no prestar dos veces). La fachada `Biblioteca` orquesta, no reimplementa toda la lógica en ifs sueltos.

### 3. Tests de invariantes (90 min)

- No prestar si ya prestado.
- Devolver solo si estaba prestado.
- Mensajes de error legibles (string constantes o pequeño catálogo).

### 4. Extracción de funciones (60 min)

Identifica un método >15 líneas; extrae funciones puras con nombres verbales. Commit atómico.

## Hecho cuando

1. Reglas de negocio viven en métodos nombrados, no dispersos.
2. Tests cubren invariantes principales.
3. Commit con mensaje que mencione comportamiento en entidades.

## Errores comunes

- God class `Biblioteca` de 400 líneas.
- Getters/setters sin reglas.

## Siguiente

[L03 — Encapsulación en TypeScript](L03-encapsulacion-en-typescript.md)
