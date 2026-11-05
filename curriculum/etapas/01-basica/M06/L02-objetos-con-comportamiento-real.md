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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un objeto combina datos y **comportamiento**. Datos anémicos + servicios
      gigantes es un antipatrón que corregirás hoy.


      **Objetivo de esta lección:** Mover reglas de negocio a métodos cohesivos
      (entidad o agregado pequeño); evitar clases contenedor vacías.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      CC cap. 3 (funciones pequeñas) + inicio cap. 10. Lista: ¿cuándo una clase
      aporta vs cuándo estorba?
  - id: s3
    tipo: ejemplo
    titulo: Refactor de anémico → rico
    xp: 10
    cuerpo: >-
      Si tu `Libro` solo expone campos, añade métodos como `marcarPrestado():
      void` con invariantes (no prestar dos veces). La fachada `Biblioteca`
      orquesta, no reimplementa toda la lógica en ifs sueltos.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Objetos con comportamiento real», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Reglas de negocio viven en métodos nombrados, no dispersos.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Objetos con
          comportamiento real
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
    pregunta: ¿Es recomendable en esta lección? “God class `Biblioteca` de 400 líneas."
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
          Mover reglas de negocio a métodos cohesivos (entidad o agregado
          pequeño); evitar clases contenedor vacías.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests de invariantes
    xp: 10
    cuerpo: >-
      - No prestar si ya prestado. - Devolver solo si estaba prestado. -
      Mensajes de error legibles (string constantes o pequeño catálogo).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Reglas de negocio viven en métodos nombrados, no dispersos.'
      - Tests cubren invariantes principales.
      - Commit con mensaje que mencione comportamiento en entidades.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
