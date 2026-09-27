---
id: L11
materia: M04
orden: 11
titulo: Visualización e histogramas para no técnicos
horas: 5
semana: 3
lectura: "OpenStax gráficos · Walpole gráficos descriptivos"
evidencia: "projects/m04-stats/salida/histograma-pedidos.md (+ png/svg opcional) + notas/explicar-histograma.md"
---

# L11 — Visualización e histogramas para no técnicos

**~5 h · Semana 3**

Construyes un histograma de pedidos (script, Python, Excel o herramienta que prefieras) y escribes la explicación que darías en una reunión con stakeholders.

## Objetivo

Cumplir el criterio de dominio “explicas un histograma a un no técnico” con evidencia escrita.

## Pasos

### 1. Histograma (70 min)

Genera bins sobre `pedidos` (ej. 10 bins). Guarda:

- Imagen en `salida/histograma-pedidos.png` **o**
- Histograma ASCII/tabla en `salida/histograma-pedidos.md`

### 2. Guion de 2 minutos (40 min)

`notas/explicar-histograma.md`:

```markdown
# Cómo explico este histograma

## Qué muestra (sin jerga)
-

## Qué NO muestra
-

## Pregunta que abre al negocio
-
```

### 3. Lectura (60 min)

Buenas prácticas de gráficos (eje Y, bins, no truncar ejes sin decirlo).

### 4. Commit

```bash
git commit -am "docs(m04): histograma y guion L11"
```

## Hecho cuando

1. Histograma guardado en `salida/`.
2. Guion de explicación completo.
3. Commit.

## Siguiente

[L12 — Correlación, muestreo y sesgo](L12-correlacion-muestreo-y-sesgo.md)
