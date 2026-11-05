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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Las interfaces fijan **contratos**; las clases son reemplazables. Así
      pruebas y diseño ganan independencia.


      **Objetivo de esta lección:** Definir interfaces de repositorio/servicio;
      implementar versión en memoria y fake/stub para tests de integración
      ligeros.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      Handbook: interfaces vs type aliases (cuándo usar cada uno). CC cap. 6
      (objetos y estructuras de datos).
  - id: s3
    tipo: ejemplo
    titulo: Diseño de contratos
    xp: 10
    cuerpo: >-
      Separa: - `RepositorioLibros` (persistencia) - `ServicioPrestamo` (casos
      de uso) El servicio depende del repositorio por interfaz, no por clase
      concreta.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Interfaces y contratos de dominio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Servicio desacoplado de implementación concreta.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Interfaces y contratos
          de dominio
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
      ¿Es recomendable en esta lección? “Interfaz con 20 métodos “por si
      acaso”."
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
          Definir interfaces de repositorio/servicio; implementar versión en
          memoria y fake/stub para tests de integración ligeros.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Implementación fake
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
