---
id: L09
materia: M23
orden: 9
titulo: Rúbrica de evaluación FAQ
horas: 5.0
semana: 3
lectura: Evaluación LLM — correcto/parcial/incorrecto/alucinación
evidencia: projects/m23-ia/llm-eval/rubrica.md
---

# L09 — Rúbrica de evaluación FAQ

**~5 h · Semana 3**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/rubrica.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Definir rúbrica con ejemplos anclados para calificar respuestas del asistente.

## Por qué empieza así

Calidad medible habilita comparar prompt v1 vs v2 objetivamente.

Conceptos que debes poder explicar al cerrar:

- Rúbrica.
- Anclas.
- Alucinación.
- Parcial aceptable.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Evaluación LLM — correcto/parcial/incorrecto/alucinación_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/rubrica.md`: 4 categorías, definición, ejemplo bueno/malo por categoría.

### 3. Laboratorio principal (90–120 min)

Acuerda umbral (ej. ≥80% correcto+parcial aceptable) en el mismo archivo.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l09 r-brica-de-evaluaci-n-faq"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Evaluación LLM — correcto/parcial/incorrecto/alucinación | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/rubrica.md`.
2. Rúbrica 4 niveles.
3. Ejemplos anclados.
4. Umbral numérico.
5. Commit `docs(m23): l09 …` en el historial.

## Errores comunes

- ‘Se ve bien’.
- Sin definir alucinación.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Correr evaluación v1 sobre gold set](L10-correr-evaluacion-v1-sobre-gold-set.md)
