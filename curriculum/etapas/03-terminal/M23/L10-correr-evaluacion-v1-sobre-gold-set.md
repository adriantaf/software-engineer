---
id: L10
materia: M23
orden: 10
titulo: Correr evaluación v1 sobre gold set
horas: 5
semana: 3
lectura: "Batch eval reproducible"
evidencia: "projects/m23-ia/llm-eval/resultados-v1.csv"
---

# L10 — Correr evaluación v1 sobre gold set

**~5 h · Semana 3**

## Objetivo

Ejecutar evaluación completa v1; tabular pregunta, respuesta modelo, score rúbrica.

## Por qué importa

Resultados versionados permiten auditoría y mejora.

## Conceptos

- Batch.
- CSV resultados.
- Reproducibilidad.
- Version tag.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Genera `projects/m23-ia/llm-eval/resultados-v1.csv`. Documenta comando exacto en `projects/m23-ia/llm-eval/README.md`.

No pegues API key en README.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l10 correr-evaluacion-v1-sobre-gold-set"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M23-ia-datos.md semana 3 | preguntas-gold.json |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. resultados-v1.csv 10 filas.
2. README comando.
3. prompt-v1 referenciado.

## Errores comunes

- Eval parcial sin commit.
- Editar gold para ‘pasar’.

## Siguiente

[L11 — Prompt v2 — iteración medida](L11-prompt-v2-iteracion-medida.md)
