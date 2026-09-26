---
id: L16
materia: M07
orden: 16
titulo: Visualización y P2 parcial
horas: 5.0
semana: 4
lectura: Serializar árbol para depuración; cierre P2 parcial
evidencia: export traverse a string + README P2
---

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
