---
id: L12
materia: M07
orden: 12
titulo: Hash vs Map nativo (P1 cierre)
horas: 5
semana: 3
lectura: Contraste implementación propia vs Map/Set nativos
evidencia: 'P1 completa: lista,pila,cola,hash + tabla comparativa nativo'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 cierra aquí: estructuras básicas propias + honestidad frente a `Map`.


      **Objetivo de esta lección:** Verificar evidencia P1 completa y documentar
      cuándo usarías `Map` nativo en producción frente a tu hash de aprendizaje.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist automático
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras
      npm test
      ls src/singly-linked-list.ts src/stack.ts src/queue.ts src/hash-map.ts
      ```

      Arregla cualquier rojo.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Microbench informal
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras
      git commit -m "docs(m07): cierre P1 hash vs Map nativo"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Hash vs Map nativo (P1 cierre)», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Hash vs Map nativo (P1
          cierre)
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

      `cd projects/m07-estructuras`
    comandoEsperado:
      - cd projects/m07-estructuras
      - npm test
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m07-estructuras'
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
          Verificar evidencia P1 completa y documentar cuándo usarías `Map`
          nativo en producción frente a tu hash de aprendizaje.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tabla comparativa
    xp: 10
    cuerpo: >-
      README sección “P1 — Hash vs Map”: API, orden de claves, uso recomendado
      (prod → Map; curso → propio para entender colisiones).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Checklist P1: lista, pila, cola, hash con tests verdes.'
      - >-
        Tabla en README o `COMPLEJIDAD.md`: tu HashMap vs `Map` (ops, cuándo
        usar cada uno).
      - 'Commit `docs(m07): cierre P1 hash vs Map nativo`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Hash vs Map nativo (P1 cierre)

**~5.0 h · Semana 3**

P1 cierra aquí: estructuras básicas propias + honestidad frente a `Map`.

## Objetivo

Verificar evidencia P1 completa y documentar cuándo usarías `Map` nativo en producción frente a tu hash de aprendizaje.

## Pasos

### 1. Checklist automático (40 min)

```bash
cd projects/m07-estructuras
npm test
ls src/singly-linked-list.ts src/stack.ts src/queue.ts src/hash-map.ts
```

Arregla cualquier rojo.

### 2. Microbench informal (70 min)

`bench/hash-vs-map.ts`: N=50_000 set/get en tu HashMap vs `Map`. Imprime ms. **No** concluyas superioridad absoluta; anota que V8 está altamente optimizado.

### 3. Tabla comparativa (50 min)

README sección “P1 — Hash vs Map”: API, orden de claves, uso recomendado (prod → Map; curso → propio para entender colisiones).

### 4. Bitácora semana 3 (30 min)

`bitacora/semana-03.md`: una colisión real que viste y cómo el chaining la resolvió.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre P1 hash vs Map nativo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cuándo usar Map nativo vs hash propio (aprendizaje vs prod) | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist P1: lista, pila, cola, hash con tests verdes.
2. Tabla en README o `COMPLEJIDAD.md`: tu HashMap vs `Map` (ops, cuándo usar cada uno).
3. Commit `docs(m07): cierre P1 hash vs Map nativo`.

## Errores comunes

- Declarar P1 completa sin hash con rehash.
- Tabla que diga “el mío es más rápido” sin medir ni contextualizar aprendizaje.
- Olvidar exportar HashMap en `src/index.ts`.

## Siguiente

[L13 — BST: inserción y búsqueda](L13-bst-insercion-y-busqueda.md)
