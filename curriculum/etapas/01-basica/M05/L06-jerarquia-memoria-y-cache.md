---
id: L06
materia: M05
orden: 6
titulo: Jerarquía de memoria y caché
horas: 5
semana: 2
lectura: "Stallings — jerarquía, caché, localidad temporal/espacial"
evidencia: "projects/m05-como-corre/cache-localidad.md + sketch de jerarquía"
---

# L06 — Jerarquía de memoria y caché

**~5 h · Semana 2**

No toda la RAM es igual de “cerca” de la CPU. La jerarquía explica órdenes de magnitud en rendimiento.

## Objetivo

Describir la pirámide de memoria (registros → cachés → RAM → disco) y los principios de localidad temporal y espacial.

## Conceptos

- **Hit/miss** de caché; línea de caché y bloque.
- **Localidad temporal** (reusar) y **espacial** (vecinos).
- **Working set** intuitivo.
- Por qué un loop compacto suele ir más rápido que acceso aleatorio.

## Pasos

### 1. Lectura (75–90 min)

Stallings: jerarquía y caché. Dibuja la pirámide con **latencia relativa** (no memorices nanosegundos; usa órdenes 1 : 10 : 100 : 1000).

### 2. `cache-localidad.md` (90 min)

Incluye:

- Pirámide anotada.
- Dos fragmentos pseudocódigo: recorrido row-major vs column-major en matriz; predice cuál cachea mejor y **por qué** (sin benchmark aún).

### 3. Mini experimento (opcional, 60 min)

Si tienes Node, compara suma en arreglo lineal vs saltos grandes (`stride`). Documenta tiempos con `console.time` (≥3 repeticiones). Relaciona con localidad.

### 4. Conexión con hilos (30 min)

Párrafo: ¿por qué “más hilos” no siempre acelera si compiten por caché/bus?

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Jerarquía, caché, localidad |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Archivo con pirámide, localidad explicada y predicción row/column major.
2. Si corriste benchmark, ≥3 repeticiones y conclusión honesta.
3. Respondiste la pregunta sobre hilos y caché.

## Errores comunes

- Tratar caché como “RAM extra” sin política de reemplazo (idea).
- Benchmark una sola vez.

## Siguiente

[L07 — Disco vs RAM y persistencia](L07-disco-vs-ram-y-persistencia.md)
