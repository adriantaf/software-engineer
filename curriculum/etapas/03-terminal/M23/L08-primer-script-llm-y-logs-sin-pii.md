---
id: L08
materia: M23
orden: 8
titulo: Primer script LLM y logs sin PII
horas: 5.0
semana: 2
lectura: Prompt sistema + usuario
evidencia: projects/m23-ia/llm-eval/prompt-v1.txt + logs/
---

# L08 — Primer script LLM y logs sin PII

**~5 h · Semana 2**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/prompt-v1.txt + logs/`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Implementar CLI o script que llame API con prompt v1 y registre latencia/tokens sin PII.

## Por qué empieza así

P2 empieza con versión explícita de prompt, no ‘el que funcionó ayer’.

Conceptos que debes poder explicar al cerrar:

- Prompt versionado.
- Tokens.
- Latencia.
- Redacción logs.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Prompt sistema + usuario_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

Guarda `projects/m23-ia/llm-eval/prompt-v1.txt`. Script en `projects/m23-ia/llm-eval/run-eval.ts` o `.py` (documenta comando).

### 3. Laboratorio principal (90–120 min)

Log en `projects/m23-ia/llm-eval/logs/` con timestamp, tokens, modelo — **sin** texto de cliente.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l08 primer-script-llm-y-logs-sin-pii"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Prompt sistema + usuario | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/prompt-v1.txt + logs/`.
2. prompt-v1.txt.
3. Script ejecutable.
4. Log sin PII.
5. Commit `docs(m23): l08 …` en el historial.

## Errores comunes

- Log con teléfonos.
- Prompt en código sin archivo.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — Rúbrica de evaluación FAQ](L09-rubrica-de-evaluacion-faq.md)
