---
id: L06
materia: M23
orden: 6
titulo: Set gold de 10 preguntas FAQ del ICP
horas: 5.0
semana: 2
lectura: FAQ realistas barbería/clínica/taller
evidencia: projects/m23-ia/llm-eval/preguntas-gold.json
---

# L06 — Set gold de 10 preguntas FAQ del ICP

**~5 h · Semana 2**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/preguntas-gold.json`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Listar 10 preguntas con respuesta esperada corta basada en docs ficticios de un tenant demo.

## Por qué empieza así

Evaluación sin gold set es opinión; M22 ICP informa el tono.

Conceptos que debes poder explicar al cerrar:

- Gold set.
- JSON.
- Respuesta esperada.
- Tenant demo.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _FAQ realistas barbería/clínica/taller_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

Crea `projects/m23-ia/llm-eval/preguntas-gold.json` array de {id, pregunta, respuesta_esperada, tenant_id_demo}.

### 3. Laboratorio principal (90–120 min)

Preguntas tipo política cancelación, horario, servicios, pedido abandonado.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l06 set-gold-de-10-preguntas-faq-del-icp"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | FAQ realistas barbería/clínica/taller | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/preguntas-gold.json`.
2. 10 preguntas.
3. JSON válido.
4. Respuesta esperada cada una.
5. Commit `docs(m23): l06 …` en el historial.

## Errores comunes

- Preguntas genéricas Wikipedia.
- Sin tenant_id_demo.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Proveedor LLM — auth, modelo y costos](L07-proveedor-llm-auth-modelo-y-costos.md)
