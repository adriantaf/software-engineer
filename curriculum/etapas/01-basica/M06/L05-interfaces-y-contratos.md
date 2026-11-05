---
id: L05
materia: M06
orden: 5
titulo: Interfaces y contratos de dominio
horas: 5
semana: 2
lectura: 'Handbook TS — Object Types, Interfaces; CC cap. 6'
evidencia: Interfaces Repositorio/Servicio + segunda implementación fake para tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir interfaces de repositorio/servicio; implementar
      versión en memoria y fake/stub para tests de integración ligeros.


      Las interfaces fijan **contratos**; las clases son reemplazables. Así
      pruebas y diseño ganan independencia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      Handbook: interfaces vs type aliases (cuándo usar cada uno). CC cap. 6
      (objetos y estructuras de datos).
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Interfaces y contratos de dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          Interfaces Repositorio/Servicio + segunda implementación fake para
          tests
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
      ¿Es buena práctica en esta lección? “Interfaz con 20 métodos “por si
      acaso”."
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
          Definir interfaces de repositorio/servicio; implementar versión en
          memoria y fake/stub para tests de integración ligeros.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Diseño de contratos
    xp: 10
    cuerpo: |-
      Separa:

      - `RepositorioLibros` (persistencia)
      - `ServicioPrestamo` (casos de uso)

      El servicio depende del repositorio por interfaz, no por clase concreta.
  - id: s7
    tipo: explicacion
    titulo: 3. Implementación fake
    xp: 10
    cuerpo: '`RepositorioLibrosFake` con contador de llamadas (útil para tests).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Servicio desacoplado de implementación concreta.
      - ≥2 implementaciones de repositorio (memoria + fake).
      - Tests del servicio sin tocar disco/red.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Interfaces y contratos de dominio

**~5 h · Semana 2**

Las interfaces fijan **contratos**; las clases son reemplazables. Así pruebas y diseño ganan independencia.

## Objetivo

Definir interfaces de repositorio/servicio; implementar versión en memoria y fake/stub para tests de integración ligeros.

## Pasos

### 1. Lectura (60 min)

Handbook: interfaces vs type aliases (cuándo usar cada uno). CC cap. 6 (objetos y estructuras de datos).

### 2. Diseño de contratos (90 min)

Separa:

- `RepositorioLibros` (persistencia)
- `ServicioPrestamo` (casos de uso)

El servicio depende del repositorio por interfaz, no por clase concreta.

### 3. Implementación fake (90 min)

`RepositorioLibrosFake` con contador de llamadas (útil para tests).

### 4. Tests de servicio (60 min)

Mock/fake: verifica que `prestar` llama `guardar` o equivalente.

## Hecho cuando

1. Servicio desacoplado de implementación concreta.
2. ≥2 implementaciones de repositorio (memoria + fake).
3. Tests del servicio sin tocar disco/red.

## Errores comunes

- Interfaz con 20 métodos “por si acaso”.
- `implements` en cadena sin necesidad.

## Siguiente

[L06 — Composición frente a herencia](L06-composicion-frente-a-herencia.md)
