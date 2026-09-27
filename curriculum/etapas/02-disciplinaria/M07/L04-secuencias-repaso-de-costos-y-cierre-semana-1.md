---
id: L04
materia: M07
orden: 4
titulo: "Secuencias: repaso de costos y cierre semana 1"
horas: 5.0
semana: 1
lectura: "Repaso arrays vs listas: cuándo cada una"
evidencia: COMPLEJIDAD.md completo semana 1 + bitácora semana
---

# L04 — Secuencias: repaso de costos y cierre semana 1

**~5.0 h · Semana 1**

Cierras la semana de secuencias dejando una tabla defendible y la suite verde.

## Objetivo

Completar `COMPLEJIDAD.md` para array y listas, escribir bitácora de semana 1 y dejar tests verdes.

## Pasos

### 1. Auditoría de código (45 min)

```bash
cd projects/m07-estructuras
find src -name '*.ts' | sort
npm test
```

Anota gaps (métodos sin test, Big-O faltante).

### 2. Tabla unificada (75 min)

En `COMPLEJIDAD.md`, una tabla con columnas: operación | DynamicArray | Singly | Doubly. Filas: acceso, insert head, append, delete por valor, memoria extra por elemento.

### 3. Mini experimento (60 min)

Script `bench/sequences-smoke.ts` (o test de timing informal): 10_000 prepends en lista vs unshift en array nativo. Pega 3 números en la bitácora (no hace falta microbenchmark serio aún).

### 4. Bitácora (40 min)

```bash
mkdir -p bitacora
```

`bitacora/semana-01.md`: qué estructura elegirías para cola de impresión vs buffer de edición, en 2 frases cada una.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 1 secuencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Trade-offs arrays vs listas (tiempo y memoria) | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `COMPLEJIDAD.md` tiene tabla comparativa array / lista simple / lista doble para insert head, append, acceso, delete.
2. Existe `bitacora/semana-01.md` (o sección en README) con 5–8 líneas de lo aprendido.
3. Suite `npm test` verde; commit `docs(m07): cierre semana 1 secuencias`.

## Errores comunes

- Tabla de costos inventada sin mirar tu código.
- Cerrar la semana con tests en rojo.
- Bitácora vacía o solo “terminé las lecciones”.

## Siguiente

[L05 — Pila (Stack) tipada](L05-pila-stack-tipada.md)
