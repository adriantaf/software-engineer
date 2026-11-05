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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Exponer tres recorridos con tests de snapshot sobre un árbol
      fijo.


      Inorder en un BST es el sorted dump. Preorden y postorden aparecen en
      serialización y borrado de directorios.
  - id: s2
    tipo: ejemplo
    titulo: 1. Repaso teórico
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): bst recorridos"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Recorridos inorder, preorder, postorder" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: Tres recorridos + snapshots en tests
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

      `git commit -am "feat(m07): bst recorridos"`
    comandoEsperado:
      - 'git commit -am "feat(m07): bst recorridos"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): bst recorridos"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Exponer tres recorridos con tests de snapshot sobre un árbol fijo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación recursiva
    xp: 10
    cuerpo: >-
      En `src/bst.ts`: `inorder()`, `preorder()`, `postorder()` → arrays.
      Opcional: versión iterativa bonus.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests snapshot
    xp: 10
    cuerpo: |-
      Árbol 8,3,10,1,6,14,4:

      - inorder: `[1,3,4,8,10,14]` (ajusta si tu set difiere)
      - preorder / postorder según tu dibujo VisuAlgo
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
