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

“IA en el SaaS” sin workflow ni límites es humo. En Agenda Ops la IA útil responde preguntas del **dueño o staff** sobre *su* negocio — horarios, servicios, políticas — usando documentación **de ese tenant**, con evaluación de calidad y costos controlados ([producto-saas](../../producto-saas.md)). Mezclar FAQs de la barbería A con la clínica B es fallo de producto y de seguridad ([hilo seguridad](../../hilos/seguridad.md)).

Esta materia cubre métricas accionables del SaaS (por `tenant_id`), integración LLM con rúbrica, y RAG aislado con prueba de que el tenant A no lee corpus del B.

**En resumen:** métricas del SaaS + LLM con evaluación; RAG **por tenant** sin filtrar datos ajenos.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Definir y calcular métricas SaaS básicas (activación, citas/semana, trials) **agregadas por tenant** sin exportar PII innecesaria.
2. Construir un pipeline reproducible (script o job) que genere CSV o vistas para análisis.
3. Integrar una API LLM con prompts versionados, límites de tokens y registro de costo estimado.
4. Evaluar respuestas con una rúbrica (correcto / parcial / incorrecto / alucinación) sobre un set fijo de preguntas.
5. Implementar RAG donde el retrieval filtra **siempre** por `tenant_id` antes de llamar al modelo.
6. Demostrar con test automatizado o script que preguntas del tenant A no recuperan chunks del tenant B.

## Cómo estudiar esta materia (lecciones)

M23 añade métricas, LLM evaluado y RAG **por tenant** a Agenda Ops: L01–L24 (6 semanas × 4).

1. Orden **L01 → L24**; escribe `politica-datos-llm.md` **antes** de pegar datos en APIs.
2. No envíes PII, dumps crudos ni secretos a proveedores LLM.
3. Cada prompt: versión en archivo + resultado en rúbrica.
4. Demo obligatoria: tenant A no lee corpus de B (test automatizado preferido).
5. [producto-saas](../../producto-saas.md), [hilo seguridad](../../hilos/seguridad.md), [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Métricas / LLM / RAG | 10–12 | 4 lecciones (~5 h) |
| Evaluación + tests | 4–6 | CSV, rúbrica, CI |
| Producto FAQ | 4–6 | staging, README asistente |
| Retro | 1 | Costo vs valor |

Si un día solo tienes 2 h: **una lección** con evidencia en `projects/m23-ia/`.

## Lecciones

### Semana 1 — Métricas del SaaS (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Tres métricas SaaS por tenant — definiciones](M23/L01-tres-metricas-saas-por-tenant-definiciones.md) | 5 |
| L02 | [Consulta agregada por tenant_id sin PII](M23/L02-consulta-agregada-por-tenant-id-sin-pii.md) | 5 |
| L03 | [Export de ejemplo y borrador pipeline](M23/L03-export-de-ejemplo-y-borrador-pipeline.md) | 5 |
| L04 | [Cierre semana 1 métricas — P1 avance](M23/L04-cierre-semana-1-metricas-p1-avance.md) | 5 |

### Semana 2 — LLM API y primeros prompts (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Política de datos LLM antes de prompts](M23/L05-politica-de-datos-llm-antes-de-prompts.md) | 5 |
| L06 | [Set gold de 10 preguntas FAQ del ICP](M23/L06-set-gold-de-10-preguntas-faq-del-icp.md) | 5 |
| L07 | [Proveedor LLM — auth, modelo y costos](M23/L07-proveedor-llm-auth-modelo-y-costos.md) | 5 |
| L08 | [Primer script LLM y logs sin PII](M23/L08-primer-script-llm-y-logs-sin-pii.md) | 5 |

### Semana 3 — Evaluación (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Rúbrica de evaluación FAQ](M23/L09-rubrica-de-evaluacion-faq.md) | 5 |
| L10 | [Correr evaluación v1 sobre gold set](M23/L10-correr-evaluacion-v1-sobre-gold-set.md) | 5 |
| L11 | [Prompt v2 — iteración medida](M23/L11-prompt-v2-iteracion-medida.md) | 5 |
| L12 | [Umbral de calidad y cierre P2 parcial](M23/L12-umbral-de-calidad-y-cierre-p2-parcial.md) | 5 |

### Semana 4 — Diseño RAG por tenant (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Diseño RAG por tenant — chunking y almacén](M23/L13-diseno-rag-por-tenant-chunking-y-almacen.md) | 5 |
| L14 | [Ingesta corpus tenant A (demo)](M23/L14-ingesta-corpus-tenant-a-demo.md) | 5 |
| L15 | [Ingesta corpus tenant B y contraste](M23/L15-ingesta-corpus-tenant-b-y-contraste.md) | 5 |
| L16 | [Implementación retrieval con WHERE tenant_id](M23/L16-implementacion-retrieval-con-where-tenant-id.md) | 5 |

### Semana 5 — Implementación FAQ (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Endpoint faq-preview protegido](M23/L17-endpoint-faq-preview-protegido.md) | 5 |
| L18 | [UI o CLI asistente para owner](M23/L18-ui-o-cli-asistente-para-owner.md) | 5 |
| L19 | [Casos tests-cross-tenant manuales](M23/L19-casos-tests-cross-tenant-manuales.md) | 5 |
| L20 | [Test automatizado cross-tenant en CI](M23/L20-test-automatizado-cross-tenant-en-ci.md) | 5 |

### Semana 6 — Integración producto y límites (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L21 | [Feature flag IA y alineación pricing M22](M23/L21-feature-flag-ia-y-alineacion-pricing-m22.md) | 5 |
| L22 | [Costo mensual estimado por tenant activo](M23/L22-costo-mensual-estimado-por-tenant-activo.md) | 5 |
| L23 | [README asistente FAQ y límites producto](M23/L23-readme-asistente-faq-y-limites-producto.md) | 5 |
| L24 | [Cierre M23 — P1–P3, dominio y handoff M26](M23/L24-cierre-m23-p1-p3-dominio-y-handoff-m26.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: docs API LLM elegida + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Enfoque |
|--------|-----------|---------|---------|
| 1 | L01–L04 | Métricas SaaS (plan + M23) | `metricas/` pipeline |
| 2 | L05–L08 | API LLM: auth, modelos, costos | `llm-eval/` + política |
| 3 | L09–L12 | Evaluación + rúbrica | resultados v1/v2 |
| 4 | L13–L16 | RAG vendor docs + filtro tenant | `rag/diseno.md`, corpus A/B |
| 5 | L17–L20 | Implementación + tests cross-tenant | FAQ staging |
| 6 | L21–L24 | Costos, planes Pro, cierre | política actualizada |

**Regla:** demo obligatoria de que el tenant A no ve corpus del B.



## Ejemplo — retrieval con filtro de tenant (idea)

```sql
-- Pseudológica: NUNCA buscar vectores sin tenant_id en el WHERE
SELECT chunk_text, embedding <-> $query_vec AS dist
FROM faq_chunks
WHERE tenant_id = $authenticated_tenant_id
ORDER BY dist
LIMIT 5;
```

En aplicación: el `tenant_id` viene de la sesión autenticada, no de un parámetro que el cliente pueda falsificar.



## Prácticas

1. **P1 — Pipeline métricas:** `projects/m23-ia/metricas/pipeline.md` + script y `export-ejemplo.csv` (o enlace a job en repo producto).
2. **P2 — LLM evaluado:** `projects/m23-ia/llm-eval/` con prompts versionados, rúbrica y resultados tabulados.
3. **P3 — RAG aislado:** implementación referenciada + `projects/m23-ia/rag/tests-cross-tenant.md` y test automatizado en repo si aplica.

## Proyecto útil

**Asistente FAQ por tenant** integrado en Agenda Ops (staging mínimo): el owner pregunta “¿cuál es la política de cancelación?” y recibe respuesta basada solo en docs de su negocio. Documentación en `projects/m23-ia/faq-asistente/README.md`.

## Errores comunes

- RAG global con filtro “después” en el prompt (el modelo ya vio texto del otro tenant).
- Pegar export de clientes en ChatGPT “solo para probar”.
- Vender “IA que agenda sola” sin workflow ni permisos.
- Ignorar costos hasta la factura del mes.
- Métricas sin `tenant_id` que mezclan negocios en un solo gráfico.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Pipeline:** `projects/m23-ia/metricas/pipeline.md` + script + export de ejemplo.
- **P2 — LLM:** `projects/m23-ia/llm-eval/rubrica.md` + resultados de evaluación.
- **P3 — RAG:** `projects/m23-ia/rag/tests-cross-tenant.md` + evidencia de test (log o CI).
- **Proyecto — FAQ:** `projects/m23-ia/faq-asistente/README.md` + enlace a código/endpoint.

## Criterios de dominio

- [ ] Demuestras que el tenant A no obtiene respuestas del corpus del B (test o script reproducible).
- [ ] Mides calidad de respuestas con rúbrica y documentas límites/costos.
- [ ] Política de datos LLM escrita y respetada en los scripts.
- [ ] Métricas definidas con fórmula clara y agregación por tenant.
- [ ] El asistente no sustituye controles de acceso de la API.
