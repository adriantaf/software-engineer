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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Reemplazar (o evitar) jerarquías `extends` innecesarias por
      composición de comportamientos/interfaces.


      Herencia profunda acopla; la composición suele escalar mejor en dominios
      reales.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      CC cap. 10 + notas del plan M06. Escribe regla personal: “Heredo solo si
      hay relación **es-un** verdadera y estable”.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Composición frente a herencia" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          Eliminación o reducción de jerarquías; composición documentada en
          DOMINIO.md
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
    pregunta: ¿Es buena práctica en esta lección? “Mixin caótico sin interfaces claras."
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
          Reemplazar (o evitar) jerarquías `extends` innecesarias por
          composición de comportamientos/interfaces.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Auditoría
    xp: 10
    cuerpo: >-
      Busca `extends` en el proyecto. Por cada uno: ¿justificado? Si no, plan de
      composición.
  - id: s7
    tipo: explicacion
    titulo: 3. Refactor
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
