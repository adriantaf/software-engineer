---
id: L04
materia: M23
orden: 4
titulo: Cierre semana 1 métricas — P1 avance
horas: 5
semana: 1
lectura: "Repaso definiciones + privacidad"
evidencia: "projects/m23-ia/metricas/semana-01.md"
---

# L04 — Cierre semana 1 métricas — P1 avance

**~5 h · Semana 1**

## Objetivo

Consolidar semana métricas; revisar que export cumple política futura LLM.

## Por qué importa

Semana 1 cierra base numérica antes de tocar APIs externas.

## Conceptos

- Revisión pares (mentor).
- Checklist P1.
- Documentación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/metricas/semana-01.md`: checklist P1 parcial + preguntas abiertas.

Anticipa `projects/m23-ia/politica-datos-llm.md` con 3 bullets qué **nunca** sale a LLM.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l04 cierre-semana-1-metricas-p1-avance"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M23-ia-datos.md | ../../hilos/seguridad.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. semana-01.md.
2. Checklist P1.
3. Bullets política LLM.

## Errores comunes

- Marcar P1 completo sin pipeline.
- Export sin revisar PII.

## Siguiente

[L05 — Política de datos LLM antes de prompts](L05-politica-de-datos-llm-antes-de-prompts.md)
