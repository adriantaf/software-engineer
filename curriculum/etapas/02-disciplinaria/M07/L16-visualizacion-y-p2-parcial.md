---
id: L16
materia: M07
orden: 16
titulo: Visualización y P2 parcial
horas: 5
semana: 4
lectura: Serializar árbol para depuración; cierre P2 parcial
evidencia: export traverse a string + README P2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras P2 parcial dejando el BST inspeccionable y documentado.


      **Objetivo de esta lección:** Exportar una representación textual/Mermaid
      del árbol y actualizar el README de P2 con la API.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Formatter
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras
      git commit -m "docs(m07): cierre P2 parcial BST"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: README P2
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras
      git commit -m "docs(m07): cierre P2 parcial BST"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Visualización y P2 parcial», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Visualización y P2
          parcial
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

      `npm test`
    comandoEsperado:
      - npm test
      - git add projects/m07-estructuras
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm test'
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
          Exportar una representación textual/Mermaid del árbol y actualizar el
          README de P2 con la API.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Suite verde
    xp: 10
    cuerpo: Añade test de regresión si encontraste un bug al formatear.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`format()` o `toString()` del BST legible (líneas o Mermaid).'
      - README sección P2 con API BST + estado de delete (qué casos cubres).
      - 'Commit `docs(m07): cierre P2 parcial BST`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Visualización y P2 parcial

**~5.0 h · Semana 4**

Cierras P2 parcial dejando el BST inspeccionable y documentado.

## Objetivo

Exportar una representación textual/Mermaid del árbol y actualizar el README de P2 con la API.

## Pasos

### 1. Formatter (70 min)

`format(node): string` indentado por profundidad, o generador Mermaid `graph TD`. Test: árbol pequeño produce string estable (snapshot).

### 2. README P2 (60 min)

Sección “P2 — BST”: métodos, política de duplicados, límites del delete, ejemplo de uso de 10 líneas.

### 3. Suite verde (40 min)

```bash
npm test
```

Añade test de regresión si encontraste un bug al formatear.

### 4. Bitácora semana 4 (30 min)

`bitacora/semana-04.md`: peor caso del BST (datos ordenados) y qué estructura usarías en su lugar (AVL/hash) — una frase.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre P2 parcial BST"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Debug visual de BST; checklist P2 | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `format()` o `toString()` del BST legible (líneas o Mermaid).
2. README sección P2 con API BST + estado de delete (qué casos cubres).
3. Commit `docs(m07): cierre P2 parcial BST`.

## Errores comunes

- Visualización que no corresponde al árbol real.
- Marcar P2 “hecho” sin recorridos.
- README sin enlazar `src/bst.ts`.

## Siguiente

[L17 — Modelo de heap binario](L17-modelo-de-heap-binario.md)
