---
id: L15
materia: M07
orden: 15
titulo: 'BST: mínimo, máximo y sucesor'
horas: 5
semana: 4
lectura: Extremos y sucesor en BST; borrado de hoja intro
evidencia: min/max/delete leaf intro
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Min/max son caminatas a izquierda/derecha. El borrado completo puede
      esperar; hoy hojas y un hijo.


      **Objetivo de esta lección:** Añadir `min`/`max`, opcional `successor`, y
      `delete` al menos para hojas (ideal: también un solo hijo).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Min/max
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst min max delete hoja"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Sucesor
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst min max delete hoja"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «BST: mínimo, máximo y sucesor», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de BST: mínimo, máximo y
          sucesor
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

      `git commit -am "feat(m07): bst min max delete hoja"`
    comandoEsperado:
      - 'git commit -am "feat(m07): bst min max delete hoja"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): bst min max delete hoja"'
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
          Añadir `min`/`max`, opcional `successor`, y `delete` al menos para
          hojas (ideal: también un solo hijo).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Delete hoja / un hijo
    xp: 10
    cuerpo: >-
      Implementa casos 0 y 1 hijo. Caso 2 hijos puede quedar como TODO
      documentado si te falta tiempo — dilo en README P2.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `min()`, `max()` y al menos borrado de hoja (y preferible nodo con un
        hijo).
      - >-
        Tests para min/max en árbol no vacío y delete que mantiene invariante
        (inorder coherente).
      - 'Commit `feat(m07): bst min max delete hoja`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — BST: mínimo, máximo y sucesor

**~5.0 h · Semana 4**

Min/max son caminatas a izquierda/derecha. El borrado completo puede esperar; hoy hojas y un hijo.

## Objetivo

Añadir `min`/`max`, opcional `successor`, y `delete` al menos para hojas (ideal: también un solo hijo).

## Pasos

### 1. Min/max (40 min)

Implementa y testa árbol vacío (throw o undefined) y árbol con varios nodos.

### 2. Sucesor (50 min)

Documenta algoritmo: si hay derecho, min del subárbol; si no, sube por padres (si guardas `parent`) o re-busca desde root. Test con claves conocidas.

### 3. Delete hoja / un hijo (90 min)

Implementa casos 0 y 1 hijo. Caso 2 hijos puede quedar como TODO documentado si te falta tiempo — dilo en README P2.

### 4. Tests de invariante (40 min)

Tras deletes, `inorder()` sigue ordenado y `contains` del borrado es false.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst min max delete hoja"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Min/max por rama; sucesor; borrar hoja y un hijo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `min()`, `max()` y al menos borrado de hoja (y preferible nodo con un hijo).
2. Tests para min/max en árbol no vacío y delete que mantiene invariante (inorder coherente).
3. Commit `feat(m07): bst min max delete hoja`.

## Errores comunes

- Borrar sin reenlazar padres.
- Sucesor mal calculado (olvidar el subárbol derecho).
- Dejar tests sin verificar inorder tras delete.

## Siguiente

[L16 — Visualización y P2 parcial](L16-visualizacion-y-p2-parcial.md)
