---
id: L14
materia: M07
orden: 14
titulo: 'Recorridos inorder, preorder, postorder'
horas: 5
semana: 4
lectura: 'Recorridos de árbol: inorden, preorden, postorden'
evidencia: Tres recorridos + snapshots en tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Inorder en un BST es el sorted dump. Preorden y postorden aparecen en
      serialización y borrado de directorios.


      **Objetivo de esta lección:** Exponer tres recorridos con tests de
      snapshot sobre un árbol fijo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Repaso teórico
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst recorridos"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación recursiva
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst recorridos"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Recorridos inorder, preorder, postorder», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Recorridos inorder,
          preorder, postorder
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

      `git commit -am "feat(m07): bst recorridos"`
    comandoEsperado:
      - 'git commit -am "feat(m07): bst recorridos"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): bst recorridos"'
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
        texto: Exponer tres recorridos con tests de snapshot sobre un árbol fijo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests snapshot
    xp: 10
    cuerpo: >-
      Árbol 8,3,10,1,6,14,4: - inorder: `[1,3,4,8,10,14]` (ajusta si tu set
      difiere) - preorder / postorder según tu dibujo VisuAlgo
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Métodos `inorder`, `preorder`, `postorder` que devuelven `number[]` (o
        visitor).
      - 'Tests con snapshot de la secuencia 8,3,10,1,6 (inorder = ordenado).'
      - 'Commit `feat(m07): bst recorridos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Recorridos inorder, preorder, postorder

**~5.0 h · Semana 4**

Inorder en un BST es el sorted dump. Preorden y postorden aparecen en serialización y borrado de directorios.

## Objetivo

Exponer tres recorridos con tests de snapshot sobre un árbol fijo.

## Pasos

### 1. Repaso teórico (25 min)

Escribe en `docs/bst-semana4.md` una línea por recorrido: orden de visita.

### 2. Implementación recursiva (70 min)

En `src/bst.ts`: `inorder()`, `preorder()`, `postorder()` → arrays. Opcional: versión iterativa bonus.

### 3. Tests snapshot (60 min)

Árbol 8,3,10,1,6,14,4:

- inorder: `[1,3,4,8,10,14]` (ajusta si tu set difiere)
- preorder / postorder según tu dibujo VisuAlgo

### 4. Uso didáctico (40 min)

Función `toSortedArray()` = inorder. Test de propiedad: insertar permutación y sorted es el mismo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst recorridos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Inorder ordena claves BST; pre/post usos | [VisuAlgo · BST](https://visualgo.net/en/bst) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Métodos `inorder`, `preorder`, `postorder` que devuelven `number[]` (o visitor).
2. Tests con snapshot de la secuencia 8,3,10,1,6 (inorder = ordenado).
3. Commit `feat(m07): bst recorridos`.

## Errores comunes

- Inorder que no queda ordenado → invariante roto en insert.
- Recorridos mutando el árbol.
- Solo implementar inorder y fingir los otros.

## Siguiente

[L15 — BST: mínimo, máximo y sucesor](L15-bst-minimo-maximo-y-sucesor.md)
