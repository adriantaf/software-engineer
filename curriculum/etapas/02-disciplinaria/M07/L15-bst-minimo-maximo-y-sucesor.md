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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Añadir `min`/`max`, opcional `successor`, y `delete` al
      menos para hojas (ideal: también un solo hijo).


      Min/max son caminatas a izquierda/derecha. El borrado completo puede
      esperar; hoy hojas y un hijo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Min/max
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst min max delete hoja"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "BST: mínimo, máximo y sucesor" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: min/max/delete leaf intro
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m07): bst min max delete hoja"`
    comandoEsperado:
      - 'git commit -am "feat(m07): bst min max delete hoja"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): bst min max delete hoja"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Añadir `min`/`max`, opcional `successor`, y `delete` al menos para
          hojas (ideal: también un solo hijo).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Sucesor
    xp: 10
    cuerpo: >-
      Documenta algoritmo: si hay derecho, min del subárbol; si no, sube por
      padres (si guardas `parent`) o re-busca desde root. Test con claves
      conocidas.
  - id: s7
    tipo: explicacion
    titulo: 3. Delete hoja / un hijo
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
