---
id: L17
materia: M03
orden: 17
titulo: Grafos — modelo y terminología
horas: 2.5
semana: 5
lectura: "Rosen Cap. 10.1–10.2 — grafos, aristas, grados, caminos, ciclos"
evidencia: "apuntes/grafos.md + grafos/ejemplo.json (5–6 nodos) dibujado a mano"
---

# L17 — Grafos: modelo y terminología

**~2.5 h · Semana 5**

Última semana: grafos unen discretas con redes, rutas y algoritmos. Empiezas con el modelo y un ejemplo concreto.

## Objetivo

Definir grafo `G=(V,E)` (dirigido o no según elijas); grado, camino, ciclo, grafo completo; modelar un problema pequeño como grafo.

## Pasos

### 1. Apuntes (50 min)

`projects/m03-discretas/apuntes/grafos.md`:

- Vértices, aristas, adyacencia.
- Grafo simple vs multigrafo (mención).
- Grado en grafo no dirigido; grado entrante/saliente si es dirigido.
- Camino, ciclo, grafo conexo (definición).

### 2. Dibujo y JSON (50 min)

Elige un grafo de **5–6** nodos (mapa de ciudad ficticia, dependencias de tareas, amistades). Dibuja a mano y escanea/foto opcional en `apuntes/` o describe aristas en texto.

Crea `projects/m03-discretas/grafos/ejemplo.json`:

```json
{
  "dirigido": false,
  "vertices": ["A", "B", "C", "D", "E"],
  "aristas": [
    ["A", "B"],
    ["A", "C"],
    ["B", "D"],
    ["C", "D"],
    ["D", "E"]
  ]
}
```

Ajusta a tu dibujo. Lista grado de cada vértice **a mano** y verifica suma de grados = 2|E| (no dirigido).

### 3. Modelado (30 min)

Segundo mini-ejemplo en el apunte: traduce “prerrequisitos de cursos” a DAG dirigido (3–4 nodos).

### 4. Lectura Rosen (30 min)

Ejercicio de terminología del 10.1 en `grafos.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.1–10.2 |

## Hecho cuando

1. `grafos.md` con definiciones y grados calculados para `ejemplo.json`.
2. Existe `grafos/ejemplo.json` coherente con el dibujo.
3. Distingues camino de ciclo con un ejemplo en tu grafo.

## Errores comunes

- Aristas duplicadas sin documentar multigrafo.
- Confundir grafo dirigido con no dirigido al contar grados.
- JSON sin lista de vértices aislados (inclúyelos si existen).

## Siguiente

[L18 — Representación de grafos en TS](L18-representacion-de-grafos-en-ts.md)
