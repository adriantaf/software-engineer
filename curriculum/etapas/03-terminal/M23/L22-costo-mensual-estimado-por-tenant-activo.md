---
id: L22
materia: M23
orden: 22
titulo: Costo mensual estimado por tenant activo
horas: 5.0
semana: 6
lectura: Unit economics IA
evidencia: projects/m23-ia/llm-eval/costos-mensuales.md
---

# L22 — Costo mensual estimado por tenant activo

**~5 h · Semana 6**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/costos-mensuales.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Estimar costo API + storage embeddings por tenant/mes con supuestos explícitos.

## Por qué empieza así

Dueño y tú deben entender bill antes de activar Pro.

Conceptos que debes poder explicar al cerrar:

- Costo variable.
- Supuestos.
- Preguntas/mes.
- Margen.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Unit economics IA_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/costos-mensuales.md`: escenario bajo/medio/alto uso; fórmula; en MXN aproximado.

### 3. Laboratorio principal (90–120 min)

Actualiza `projects/m23-ia/politica-datos-llm.md` sección costos/retención.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l22 costo-mensual-estimado-por-tenant-activo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Unit economics IA | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/costos-mensuales.md`.
2. costos-mensuales.md.
3. 3 escenarios.
4. Política actualizada.
5. Commit `docs(m23): l22 …` en el historial.

## Errores comunes

- Ignorar embedding cost.
- Sin supuestos.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L23 — README asistente FAQ y límites producto](L23-readme-asistente-faq-y-limites-producto.md)
