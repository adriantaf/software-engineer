---
id: M23
titulo: Ciencia de datos e IA aplicada
etapa: terminal
orden: 23
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Pipeline de métricas del SaaS (por tenant)
  - id: p2
    titulo: Integración LLM con prompts evaluados
  - id: p3
    titulo: RAG por tenant (sin mezclar datos ni PII innecesaria)
proyecto:
  id: proj
  titulo: Asistente FAQ scoped por tenant (Agenda Ops)
---

# M23 — Ciencia de datos e IA aplicada

## Por qué existe
IA útil = workflow del SaaS + evaluación + costos. **Todo scoped por `tenant_id`**. No mezcles FAQs ni PII entre negocios ([producto-saas](../../producto-saas.md), [hilo](../../hilos/seguridad.md)).

**En cristiano:** métricas del SaaS + LLM con evaluación; RAG **por tenant** sin filtrar datos ajenos.

## Día 1 (2–3 h)
1. Define 3 métricas del SaaS (activación, citas/semana, trials).
2. Exporta CSV **agregado** (sin PII innecesaria).
3. Escribe política: qué datos NUNCA salen a un LLM; cómo filtras por tenant.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Métricas | 6–8 | Por tenant |
| LLM API | 6–8 | Prompts evaluados |
| RAG aislado | 4–6 | Tests cross-tenant |
| Retro | 1 | Costo vs valor |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Temario
Métricas SaaS → LLM API → evaluación → RAG **por tenant** → proyecto FAQ.

## Lecturas

Canon: docs de la API LLM elegida + guía M23 + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Enfoque |
|--------|---------|---------|
| 1 | Métricas SaaS (notas M23 / producto) | Dashboard métricas piloto |
| 2 | Docs API LLM: auth, modelos, límites, costos | Primer script evaluable |
| 3 | Evaluación de respuestas (guía M23) | Rubrica de calidad |
| 4 | RAG concepts (docs del vendor) **con filtro por tenant** | Diseño aislamiento |
| 5 | Implementación FAQ por tenant | Tests cross-tenant |
| 6 | Proyecto FAQ + límites/límites documentados | — |

**Regla:** demo obligatoria de que el tenant A no ve corpus del B.

## Errores comunes
Vender “magia IA”; RAG global que filtra datos de otro tenant; pegar fichas de clientes en prompts.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Pipeline:** Métricas SaaS por tenant.
- **P2 — LLM:** Scripts + rúbrica de calidad.
- **P3 — RAG:** Demo A no ve corpus de B + test.
- **Proyecto — FAQ:** Asistente scoped por tenant.

## Criterios de dominio
- [ ] Demuestras que el tenant A no obtiene respuestas del corpus del B.
- [ ] Mides calidad de respuestas y documentas límites/costos.
