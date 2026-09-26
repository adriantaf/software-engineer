---
id: L08
materia: M23
orden: 8
titulo: Primer script LLM y logs sin PII
horas: 5
semana: 2
lectura: "Prompt sistema + usuario"
evidencia: "projects/m23-ia/llm-eval/prompt-v1.txt + logs/"
---

# L08 — Primer script LLM y logs sin PII

**~5 h · Semana 2**

## Objetivo

Implementar CLI o script que llame API con prompt v1 y registre latencia/tokens sin PII.

## Por qué importa

P2 empieza con versión explícita de prompt, no ‘el que funcionó ayer’.

## Conceptos

- Prompt versionado.
- Tokens.
- Latencia.
- Redacción logs.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Guarda `projects/m23-ia/llm-eval/prompt-v1.txt`. Script en `projects/m23-ia/llm-eval/run-eval.ts` o `.py` (documenta comando).

Log en `projects/m23-ia/llm-eval/logs/` con timestamp, tokens, modelo — **sin** texto de cliente.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l08 primer-script-llm-y-logs-sin-pii"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Quickstart API | ../M23-ia-datos.md semana 2 |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. prompt-v1.txt.
2. Script ejecutable.
3. Log sin PII.

## Errores comunes

- Log con teléfonos.
- Prompt en código sin archivo.

## Siguiente

[L09 — Rúbrica de evaluación FAQ](L09-rubrica-de-evaluacion-faq.md)
