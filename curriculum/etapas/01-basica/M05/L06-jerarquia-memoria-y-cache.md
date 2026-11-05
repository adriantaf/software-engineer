---
id: L06
materia: M05
orden: 6
titulo: Jerarquía de memoria y caché
horas: 5
semana: 2
lectura: 'Stallings — jerarquía, caché, localidad temporal/espacial'
evidencia: projects/m05-como-corre/cache-localidad.md + sketch de jerarquía
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Describir la pirámide de memoria (registros → cachés → RAM →
      disco) y los principios de localidad temporal y espacial.


      - **Hit/miss** de caché; línea de caché y bloque.

      - **Localidad temporal** (reusar) y **espacial** (vecinos).

      - **Working set** intuitivo.

      - Por qué un loop compacto suele ir más rápido que acceso aleatorio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      Stallings: jerarquía y caché. Dibuja la pirámide con **latencia relativa**
      (no memorices nanosegundos; usa órdenes 1 : 10 : 100 : 1000).
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Jerarquía de memoria y caché" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/cache-localidad.md + sketch de jerarquía
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
      ¿Es buena práctica en esta lección? “Tratar caché como “RAM extra” sin
      política de reemplazo (idea)."
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
          Describir la pirámide de memoria (registros → cachés → RAM → disco) y
          los principios de localidad temporal y espacial.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `cache-localidad.md`
    xp: 10
    cuerpo: >-
      Incluye:


      - Pirámide anotada.

      - Dos fragmentos pseudocódigo: recorrido row-major vs column-major en
      matriz; predice cuál cachea mejor y **por qué** (sin benchmark aún).
  - id: s7
    tipo: explicacion
    titulo: 3. Mini experimento
    xp: 10
    cuerpo: >-
      Si tienes Node, compara suma en arreglo lineal vs saltos grandes
      (`stride`). Documenta tiempos con `console.time` (≥3 repeticiones).
      Relaciona con localidad.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Archivo con pirámide, localidad explicada y predicción row/column major.'
      - 'Si corriste benchmark, ≥3 repeticiones y conclusión honesta.'
      - Respondiste la pregunta sobre hilos y caché.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Jerarquía de memoria y caché

**~5 h · Semana 2**

No toda la RAM es igual de “cerca” de la CPU. La jerarquía explica órdenes de magnitud en rendimiento.

## Objetivo

Describir la pirámide de memoria (registros → cachés → RAM → disco) y los principios de localidad temporal y espacial.

## Conceptos

- **Hit/miss** de caché; línea de caché y bloque.
- **Localidad temporal** (reusar) y **espacial** (vecinos).
- **Working set** intuitivo.
- Por qué un loop compacto suele ir más rápido que acceso aleatorio.

## Pasos

### 1. Lectura (75–90 min)

Stallings: jerarquía y caché. Dibuja la pirámide con **latencia relativa** (no memorices nanosegundos; usa órdenes 1 : 10 : 100 : 1000).

### 2. `cache-localidad.md` (90 min)

Incluye:

- Pirámide anotada.
- Dos fragmentos pseudocódigo: recorrido row-major vs column-major en matriz; predice cuál cachea mejor y **por qué** (sin benchmark aún).

### 3. Mini experimento (opcional, 60 min)

Si tienes Node, compara suma en arreglo lineal vs saltos grandes (`stride`). Documenta tiempos con `console.time` (≥3 repeticiones). Relaciona con localidad.

### 4. Conexión con hilos (30 min)

Párrafo: ¿por qué “más hilos” no siempre acelera si compiten por caché/bus?

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Jerarquía, caché, localidad |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Archivo con pirámide, localidad explicada y predicción row/column major.
2. Si corriste benchmark, ≥3 repeticiones y conclusión honesta.
3. Respondiste la pregunta sobre hilos y caché.

## Errores comunes

- Tratar caché como “RAM extra” sin política de reemplazo (idea).
- Benchmark una sola vez.

## Siguiente

[L07 — Disco vs RAM y persistencia](L07-disco-vs-ram-y-persistencia.md)
