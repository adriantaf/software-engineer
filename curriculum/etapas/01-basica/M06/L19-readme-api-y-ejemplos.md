---
id: L19
materia: M06
orden: 19
titulo: 'README, API pública y ejemplos'
horas: 5
semana: 5
lectura: READMEs de librerías OSS pequeñas (2 ejemplos)
evidencia: 'README con instalación, uso, API, desarrollo; examples/basic.mjs'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un paquete sin README es código cerrado disfrazado.


      **Objetivo de esta lección:** Redactar README profesional: instalación,
      ejemplo mínimo, API resumida, cómo contribuir/testear.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Benchmark READMEs
    xp: 10
    cuerpo: Lee dos librerías pequeñas en npm. Anota estructura.
  - id: s3
    tipo: ejemplo
    titulo: Redacción
    xp: 10
    cuerpo: >-
      Secciones: Title, Install, Quick start, API, Errors/Result, Development,
      License.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «README, API pública y ejemplos», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: README permite usar la lib sin leer todo el src.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de README, API pública y
          ejemplos
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
    pregunta: ¿Es recomendable en esta lección? “Solo badges decorativos."
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
          Redactar README profesional: instalación, ejemplo mínimo, API
          resumida, cómo contribuir/testear.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Ejemplo ejecutable
    xp: 10
    cuerpo: >-
      `examples/basic.mjs` importa desde `dist` o usa `tsx` en dev; copiable por
      usuario.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - README permite usar la lib sin leer todo el src.
      - Ejemplo corre en máquina limpia tras `npm run build`.
      - Checklist proyecto casi completa.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — README, API pública y ejemplos

**~5 h · Semana 5**

Un paquete sin README es código cerrado disfrazado.

## Objetivo

Redactar README profesional: instalación, ejemplo mínimo, API resumida, cómo contribuir/testear.

## Pasos

### 1. Benchmark READMEs (45 min)

Lee dos librerías pequeñas en npm. Anota estructura.

### 2. Redacción (120 min)

Secciones: Title, Install, Quick start, API, Errors/Result, Development, License.

### 3. Ejemplo ejecutable (90 min)

`examples/basic.mjs` importa desde `dist` o usa `tsx` en dev; copiable por usuario.

### 4. API reference (60 min)

Tabla métodos + tipos exportados (puede generarse a mano).

### 5. Enlace evidencia plan (15 min)

Actualiza `projects/m06-programacion-ii/README.md` checklist proyecto.

## Hecho cuando

1. README permite usar la lib sin leer todo el src.
2. Ejemplo corre en máquina limpia tras `npm run build`.
3. Checklist proyecto casi completa.

## Errores comunes

- Solo badges decorativos.
- API undocumented breaking en 0.1.0.

## Siguiente

[L20 — Librería final y cierre de etapa básica](L20-libreria-final-y-cierre.md)
