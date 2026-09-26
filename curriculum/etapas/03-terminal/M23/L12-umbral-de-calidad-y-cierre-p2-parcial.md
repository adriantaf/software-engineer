---
id: L12
materia: M23
orden: 12
titulo: Umbral de calidad y cierre P2 parcial
horas: 5
semana: 3
lectura: "Quality gate FAQ"
evidencia: "projects/m23-ia/llm-eval/resumen-evaluacion.md"
---

# L12 — Umbral de calidad y cierre P2 parcial

**~5 h · Semana 3**

## Objetivo

Comparar v1 vs v2; decidir si cumples umbral o documentas deuda para semana 5–6.

## Por qué importa

P2 exige rúbrica + resultados tabulados; hoy cierras el gate numérico.

## Conceptos

- Umbral.
- Deuda.
- Costo por eval.
- Go/no-go RAG.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/llm-eval/resumen-evaluacion.md`: tabla versiones, % correcto, costo tokens estimado, decisión.

Si no alcanzas umbral, lista 3 acciones (más docs tenant, RAG, bajar temperatura).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l12 umbral-de-calidad-y-cierre-p2-parcial"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M23-ia-datos.md P2 | ../../../producto-saas.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. Resumen v1/v2.
2. Umbral evaluado.
3. Decisión documentada.

## Errores comunes

- Declarar éxito sin CSV.
- Ignorar costos.

## Siguiente

[L13 — Diseño RAG por tenant — chunking y almacén](L13-diseno-rag-por-tenant-chunking-y-almacen.md)
