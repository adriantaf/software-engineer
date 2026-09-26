---
id: L24
materia: M08
orden: 24
titulo: Cierre M08 y evidencias
horas: 5.0
semana: 6
lectura: Checklist P1–P3 + proyecto; índice ≥15
evidencia: checklist + indice ≥15
---

# L24 — Cierre M08 y evidencias

**~5.0 h · Semana 6**

Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y autocomplete.

## Objetivo

Completar índice ≥15, checklist de dominio y dejar el README raíz como mapa de evidencias.

## Pasos

### 1. Contar problemas (40 min)

```bash
find problems -name 'enunciado.md' | wc -l
```

Si <15, añade los faltantes hoy (plantilla corta) o recupera de semanas previas mal indexados.

### 2. Checklist (60 min)

`bitacora/cierre-m08.md` con rutas:

- P1 índice ≥15
- P2 `sorts/README.md`
- P3 `dp/` ×3
- Proyecto `autocomplete/` + DISENO + CLI

### 3. Dominio oral (40 min)

Outline escrito: resuelve two-sum / ventana en voz alta con complejidad.

### 4. Regresión (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Autoevaluación: explicar un medio de arrays/hash en voz alta | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `indice-patrones.md` con **≥15** entradas; checklist en `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
2. `npm test` verde; autocomplete documentado enlazado desde README raíz.
3. Commit `docs(m08): cierre materia y evidencias`.

## Errores comunes

- Índice inflado con filas vacías.
- Marcar P3 sin tres DP.
- Autocomplete sin complejidad de query.

## Siguiente

M08 cerrado — siguiente materia: [M09 · Bases de datos](../M09-bases-de-datos.md)
