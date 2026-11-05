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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar README profesional: instalación, ejemplo mínimo,
      API resumida, cómo contribuir/testear.


      Un paquete sin README es código cerrado disfrazado.
  - id: s2
    tipo: ejemplo
    titulo: 1. Benchmark READMEs
    xp: 10
    cuerpo: Lee dos librerías pequeñas en npm. Anota estructura.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "README, API pública y ejemplos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: 'README con instalación, uso, API, desarrollo; examples/basic.mjs'
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
    pregunta: ¿Es buena práctica en esta lección? “Solo badges decorativos."
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
          Redactar README profesional: instalación, ejemplo mínimo, API
          resumida, cómo contribuir/testear.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Redacción
    xp: 10
    cuerpo: >-
      Secciones: Title, Install, Quick start, API, Errors/Result, Development,
      License.
  - id: s7
    tipo: explicacion
    titulo: 3. Ejemplo ejecutable
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
