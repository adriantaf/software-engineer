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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Exportar una representación textual/Mermaid del árbol y
      actualizar el README de P2 con la API.


      Cierras P2 parcial dejando el BST inspeccionable y documentado.
  - id: s2
    tipo: ejemplo
    titulo: 1. Formatter
    xp: 10
    cuerpo: >-
      `format(node): string` indentado por profundidad, o generador Mermaid
      `graph TD`. Test: árbol pequeño produce string estable (snapshot).
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Visualización y P2 parcial" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: export traverse a string + README P2
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

      `npm test`
    comandoEsperado:
      - npm test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Exportar una representación textual/Mermaid del árbol y actualizar el
          README de P2 con la API.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. README P2
    xp: 10
    cuerpo: >-
      Sección “P2 — BST”: métodos, política de duplicados, límites del delete,
      ejemplo de uso de 10 líneas.
  - id: s7
    tipo: ejemplo
    titulo: 3. Suite verde
    xp: 10
    cuerpo: |-
      ```bash
      npm test
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`format()` o `toString()` del BST legible (líneas o Mermaid).'
      - README sección P2 con API BST + estado de delete (qué casos cubres).
      - 'Commit `docs(m07): cierre P2 parcial BST`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
