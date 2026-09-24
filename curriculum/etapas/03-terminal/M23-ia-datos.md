---
id: M23
titulo: Ciencia de datos e IA aplicada
etapa: terminal
orden: 23
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Pipeline de métricas del producto
  - id: p2
    titulo: Integración LLM con prompts evaluados
  - id: p3
    titulo: RAG básico (sin filtrar PII innecesaria)
proyecto:
  id: proj
  titulo: Asistente FAQ para el cliente del CRM
---

# M23 — Ciencia de datos e IA aplicada

## Por qué existe
IA útil = producto + evaluación + costos. **No envíes PII a APIs** sin política ([hilo](../../hilos/seguridad.md)).

## Día 1 (2–3 h)
Define 3 métricas del CRM. Exporta CSV. Escribe qué datos NUNCA salen a un LLM.

## Temario
Métricas → LLM API → evaluación de respuestas → RAG → proyecto FAQ.

## Recursos
Material ES + APIs; libros EN cuando B1.

## Errores comunes
Vender “magia IA”; no medir alucinaciones; pegar datos de clientes en prompts.

## Criterios de dominio
- [ ] Mides calidad de respuestas y documentas límites.
