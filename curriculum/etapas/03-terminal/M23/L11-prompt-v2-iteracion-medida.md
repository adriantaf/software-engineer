---
id: L11
materia: M23
orden: 11
titulo: Prompt v2 — iteración medida
horas: 5
semana: 3
lectura: "Error analysis sobre v1"
evidencia: "projects/m23-ia/llm-eval/prompt-v2.txt + notas"
---

# L11 — Prompt v2 — iteración medida

**~5 h · Semana 3**

## Objetivo

Analizar fallos v1, ajustar prompt v2, documentar hipótesis de mejora.

## Por qué importa

Iteración sin análisis es adivinar; registra **por qué** cambiaste cada frase.

## Conceptos

- Error analysis.
- Changelog prompt.
- Temperatura.
- Grounding.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/llm-eval/prompt-v2-changelog.md`: fallos v1 → cambio v2.

Archivo `prompt-v2.txt`. Re-ejecuta eval → `resultados-v2.csv`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l11 prompt-v2-iteracion-medida"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Prompt engineering tips | ../../hilos/seguridad.md |

## Hecho cuando

1. prompt-v2 + changelog.
2. resultados-v2.csv.
3. Hipótesis por cambio.

## Errores comunes

- v2 sin comparar v1.
- Subir temperatura sin razón.

## Siguiente

[L12 — Umbral de calidad y cierre P2 parcial](L12-umbral-de-calidad-y-cierre-p2-parcial.md)
