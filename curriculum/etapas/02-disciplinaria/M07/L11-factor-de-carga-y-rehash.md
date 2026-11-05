---
id: L11
materia: M07
orden: 11
titulo: Factor de carga y rehash
horas: 5
semana: 3
lectura: 'Load factor, umbral y rehashing'
evidencia: Rehash al superar umbral; tests que fuerzan resize
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin rehash, el encadenamiento degenera a listas largas y pierdes el O(1)
      promedio.


      **Objetivo de esta lección:** Hacer que tu `HashMap` redimensione al
      cruzar un umbral de load factor y probarlo con un test que fuerce el
      resize.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Define umbral
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): hashmap rehash por load factor"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`_rehash(newCap)`'
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): hashmap rehash por load factor"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Factor de carga y rehash», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Factor de carga y
          rehash
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "feat(m07): hashmap rehash por load factor"`
    comandoEsperado:
      - 'git commit -am "feat(m07): hashmap rehash por load factor"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): hashmap rehash por load factor"'
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
          Hacer que tu `HashMap` redimensione al cruzar un umbral de load factor
          y probarlo con un test que fuerce el resize.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Test de resize
    xp: 10
    cuerpo: >-
      Capacidad inicial pequeña (4). Inserta 10 claves distintas; assert
      capacity ≥ 8 (o la esperada); todos los `get` siguen correctos; loadFactor
      ≤ MAX_LOAD tras rehash.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Rehash automático al superar umbral (p. ej. α > 0.75) duplicando
        capacidad.
      - Test que inserta hasta forzar ≥1 resize y verifica gets posteriores.
      - 'Commit `feat(m07): hashmap rehash por load factor`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Factor de carga y rehash

**~5.0 h · Semana 3**

Sin rehash, el encadenamiento degenera a listas largas y pierdes el O(1) promedio.

## Objetivo

Hacer que tu `HashMap` redimensione al cruzar un umbral de load factor y probarlo con un test que fuerce el resize.

## Pasos

### 1. Define umbral (20 min)

Constante `MAX_LOAD = 0.75` (o la de tu texto). Documéntala en JSDoc y `COMPLEJIDAD.md`.

### 2. `_rehash(newCap)` (90 min)

Nuevo array de buckets; reinserta **todas** las entradas con el nuevo módulo; actualiza capacity/size. Llámalo desde `set` cuando `size/capacity > MAX_LOAD`.

### 3. Test de resize (60 min)

Capacidad inicial pequeña (4). Inserta 10 claves distintas; assert capacity ≥ 8 (o la esperada); todos los `get` siguen correctos; loadFactor ≤ MAX_LOAD tras rehash.

### 4. Nota amortizada (40 min)

Párrafo en `COMPLEJIDAD.md`: costo de rehash O(n) puntual, O(1) amortizado por insert si creces ×2.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): hashmap rehash por load factor"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Load factor α; cuándo rehash; costo amortizado | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Rehash automático al superar umbral (p. ej. α > 0.75) duplicando capacidad.
2. Test que inserta hasta forzar ≥1 resize y verifica gets posteriores.
3. Commit `feat(m07): hashmap rehash por load factor`.

## Errores comunes

- Rehash que no re-inserta (solo crece el array vacío).
- Umbral nunca documentado.
- Tests que no provocan resize.

## Siguiente

[L12 — Hash vs Map nativo (P1 cierre)](L12-hash-vs-map-nativo-p1-cierre.md)
