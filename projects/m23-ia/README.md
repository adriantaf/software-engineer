# M23 — Ciencia de datos e IA aplicada

Evidencia de métricas SaaS, LLM evaluado y RAG **por tenant** para Agenda Ops.

## En resumen

Métricas del SaaS + LLM con evaluación; RAG por tenant sin filtrar datos ajenos.

## Estructura esperada

```text
projects/m23-ia/
  README.md
  bitacora-m23.md
  politica-datos-llm.md
  cierre-m23.md
  metricas/
    definiciones.md
    query-agregada.sql
    export-ejemplo.csv
    pipeline.md
    semana-01.md
  llm-eval/
    preguntas-gold.json
    proveedor.md
    prompt-v1.txt
    prompt-v2.txt
    rubrica.md
    resultados-v1.csv
    resumen-evaluacion.md
    costos-mensuales.md
    logs/
  rag/
    diseno.md
    implementacion.md
    tests-cross-tenant.md
    ci-evidencia.md
    corpus/tenant-a/
    corpus/tenant-b/
  faq-asistente/
    endpoint.md
    README.md
    plan-pro-ia.md
```

## Checklist

- **P1 — Pipeline:** métricas por `tenant_id` sin PII innecesaria.
- **P2 — LLM:** prompts versionados + rúbrica sobre gold set.
- **P3 — RAG:** demo A no ve corpus de B + test (preferible en CI).
- **Proyecto — FAQ:** asistente scoped por tenant documentado.

## Reglas

1. Escribe `politica-datos-llm.md` **antes** de pegar datos en APIs.
2. No envíes dumps, secretos ni PII a proveedores LLM.
3. Cada prompt: versión en archivo + resultado en rúbrica.

## Enlaces

- Ficha: `curriculum/etapas/03-terminal/M23-ia-datos.md`
- Bibliografía: `curriculum/bibliografia.md#m23-ia-datos`
