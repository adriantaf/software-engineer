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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - **Hit/miss** de caché; línea de caché y bloque.

      - **Localidad temporal** (reusar) y **espacial** (vecinos).

      - **Working set** intuitivo.

      - Por qué un loop compacto suele ir más rápido que acceso aleatorio.


      **Objetivo de esta lección:** Describir la pirámide de memoria (registros
      → cachés → RAM → disco) y los principios de localidad temporal y espacial.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      Stallings: jerarquía y caché. Dibuja la pirámide con **latencia relativa**
      (no memorices nanosegundos; usa órdenes 1 : 10 : 100 : 1000).
  - id: s3
    tipo: ejemplo
    titulo: '`cache-localidad.md`'
    xp: 10
    cuerpo: >-
      Incluye: - Pirámide anotada. - Dos fragmentos pseudocódigo: recorrido
      row-major vs column-major en matriz; predice cuál cachea mejor y **por
      qué** (sin benchmark aún).
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Jerarquía de memoria y caché», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Archivo con pirámide, localidad explicada y predicción row/column
          major.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Jerarquía de memoria y
          caché
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
      ¿Es recomendable en esta lección? “Tratar caché como “RAM extra” sin
      política de reemplazo (idea)."
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
          Describir la pirámide de memoria (registros → cachés → RAM → disco) y
          los principios de localidad temporal y espacial.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Mini experimento
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
