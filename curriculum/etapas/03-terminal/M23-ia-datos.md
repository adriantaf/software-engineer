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

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) y la sección AI de [producto-saas](../../producto-saas.md).
- Política primero: escribe `projects/m23-ia/politica-datos-llm.md` antes de pegar datos en prompts.
- No envíes a APIs externas: fichas completas de clientes, CURP, notas clínicas, contraseñas, ni dumps crudos de BD.
- Cada mejora de prompt lleva versión (`prompt-v2.txt`) y resultado en la rúbrica.
- La demo obligatoria de aislamiento cross-tenant es requisito de egreso, no opcional.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Métricas | 6–8 | Pipeline por tenant |
| LLM API | 6–8 | Prompts evaluados |
| RAG aislado | 4–6 | Tests cross-tenant |
| Retro | 1 | Costo vs valor |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. `mkdir -p projects/m23-ia/{metricas,llm-eval,rag}`.
2. Define 3 métricas en `projects/m23-ia/metricas/definiciones.md` (ej. activación 7d, citas creadas/semana, trials activos).
3. Escribe consulta SQL o script que agrupe por `tenant_id` sin columnas de PII; exporta muestra a `projects/m23-ia/metricas/export-ejemplo.csv` (datos ficticios o anonimizados si hace falta).
4. Redacta `projects/m23-ia/politica-datos-llm.md`: qué **nunca** sale a un LLM; retención de logs; cómo se filtra por tenant.
5. Elige proveedor LLM (API oficial); anota modelo, límites y precio aproximado por 1k tokens.
6. Lista 10 preguntas FAQ realistas del ICP para evaluación posterior en `projects/m23-ia/llm-eval/preguntas-gold.json`.

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

## Temario semanal

### Semana 1 — Métricas del SaaS (~20 h)

- Métricas de activación y uso vs vanity (páginas vistas sin citas).
- Pipeline: extracción → agregación → export o dashboard mínimo.
- Privacidad: minimización de datos en exports.
- Entregable: `metricas/pipeline.md` + script ejecutable.

### Semana 2 — LLM API y primeros prompts (~20 h)

- Auth, rate limits, manejo de errores y timeouts.
- Prompt sistema + usuario; temperatura y cuándo bajarla para FAQ.
- Script CLI o endpoint interno `POST /admin/faq-preview` (protegido).
- Registro de latencia y tokens en `llm-eval/logs/` (sin PII).

### Semana 3 — Evaluación (~20 h)

- Rúbrica en `projects/m23-ia/llm-eval/rubrica.md`.
- Correr evaluación sobre `preguntas-gold.json`; tabla resultados por versión de prompt.
- Iterar prompt hasta umbral acordado (ej. ≥80% correcto o parcial aceptable).

### Semana 4 — Diseño RAG por tenant (~20 h)

- Ingesta de docs por tenant (markdown, PDF de políticas del negocio).
- Chunking, embeddings, almacén (pgvector, sqlite-vss, servicio managed — documenta elección).
- Amenazas: prompt injection en docs del tenant, fuga por metadatos mal filtrados.

### Semana 5 — Implementación FAQ (~20 h)

- Endpoint o UI: asistente solo para usuarios autenticados del tenant.
- Citas de fuente (opcional pero recomendado) para confianza del dueño.
- Tests: tenant A pregunta por política de B → sin chunks de B en contexto.

### Semana 6 — Integración producto y límites (~20 h)

- Feature flag o plan Pro si limitas IA por pricing M22.
- Documentar costo mensual estimado por tenant activo.
- README del asistente para soporte: qué hace y qué **no** hace (no agenda citas sola si no está implementado).

## Lecturas

Canon: docs de la API LLM elegida + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Enfoque |
|--------|---------|---------|
| 1 | Métricas SaaS (notas M23 / producto) | `metricas/definiciones.md` |
| 2 | Docs API LLM: auth, modelos, límites, costos | Primer script en `llm-eval/` |
| 3 | Evaluación de respuestas (rúbrica propia + guías del vendor) | `llm-eval/rubrica.md` |
| 4 | RAG (docs del vendor) **con filtro por tenant** | Diseño en `rag/diseno.md` |
| 5 | Implementación + tests cross-tenant | `rag/tests-cross-tenant.md` |
| 6 | Límites legales/éticos + costos | `politica-datos-llm.md` actualizada |

**Regla:** demo obligatoria de que el tenant A no ve corpus del B.

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
