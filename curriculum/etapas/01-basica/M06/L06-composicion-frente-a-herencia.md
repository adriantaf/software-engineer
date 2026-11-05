---
id: L06
materia: M06
orden: 6
titulo: Composición frente a herencia
horas: 5
semana: 2
lectura: CC cap. 10 (clases) + artículo corto composición vs herencia
evidencia: Eliminación o reducción de jerarquías; composición documentada en DOMINIO.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Herencia profunda acopla; la composición suele escalar mejor en dominios
      reales.


      **Objetivo de esta lección:** Reemplazar (o evitar) jerarquías `extends`
      innecesarias por composición de comportamientos/interfaces.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      CC cap. 10 + notas del plan M06. Escribe regla personal: “Heredo solo si
      hay relación **es-un** verdadera y estable”.
  - id: s3
    tipo: ejemplo
    titulo: Auditoría
    xp: 10
    cuerpo: >-
      Busca `extends` en el proyecto. Por cada uno: ¿justificado? Si no, plan de
      composición.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Composición frente a herencia», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Cero jerarquías de profundidad >2, o justificación escrita.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Composición frente a
          herencia
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
    pregunta: ¿Es recomendable en esta lección? “Mixin caótico sin interfaces claras."
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
          Reemplazar (o evitar) jerarquías `extends` innecesarias por
          composición de comportamientos/interfaces.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Refactor
    xp: 10
    cuerpo: >-
      Ejemplo: en lugar de `LibroEspecial extends Libro`, composición con
      `PoliticaPrestamo` inyectada.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Cero jerarquías de profundidad >2, o justificación escrita.'
      - Tests verdes.
      - Puedes explicar un caso donde no usaste herencia.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Composición frente a herencia

**~5 h · Semana 2**

Herencia profunda acopla; la composición suele escalar mejor en dominios reales.

## Objetivo

Reemplazar (o evitar) jerarquías `extends` innecesarias por composición de comportamientos/interfaces.

## Pasos

### 1. Lectura (45 min)

CC cap. 10 + notas del plan M06. Escribe regla personal: “Heredo solo si hay relación **es-un** verdadera y estable”.

### 2. Auditoría (60 min)

Busca `extends` en el proyecto. Por cada uno: ¿justificado? Si no, plan de composición.

### 3. Refactor (150 min)

Ejemplo: en lugar de `LibroEspecial extends Libro`, composición con `PoliticaPrestamo` inyectada.

### 4. Tests (60 min)

Asegura paridad de comportamiento tras refactor.

### 5. Documento (30 min)

En `DOMINIO.md`, tabla: antes (herencia) → después (composición).

## Hecho cuando

1. Cero jerarquías de profundidad >2, o justificación escrita.
2. Tests verdes.
3. Puedes explicar un caso donde **no** usaste herencia.

## Errores comunes

- Mixin caótico sin interfaces claras.
- Herencia solo para reutilizar código (usa funciones).

## Siguiente

[L07 — SOLID intro: S, O y D](L07-solid-intro-s-o-d.md)
