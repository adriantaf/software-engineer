---
id: L01
materia: M23
orden: 1
titulo: Tres métricas SaaS por tenant — definiciones
horas: 5.0
semana: 1
lectura: producto-saas + notas métricas M23
evidencia: projects/m23-ia/metricas/definiciones.md
---

# L01 — Tres métricas SaaS por tenant — definiciones

**~5 h · Semana 1**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/metricas/definiciones.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Definir activación 7d, citas creadas/semana y trials activos con fórmula y fuente de datos.

## Por qué empieza así

M23 y M22 comparten métricas accionables; sin definición clara los CSV mienten.

Conceptos que debes poder explicar al cerrar:

- Activación.
- tenant_id.
- Vanity vs accionable.
- Ventana temporal.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _producto-saas + notas métricas M23_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
```

### 3. Laboratorio principal (90–120 min)

En `projects/m23-ia/metricas/definiciones.md` documenta ≥3 métricas con fórmula, numerador/denominador, frecuencia, anti-PII.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l01 tres-m-tricas-saas-por-tenant-definicion"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | producto-saas + notas métricas M23 | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/metricas/definiciones.md`.
2. definiciones.md ≥3 métricas.
3. Fórmulas explícitas.
4. Anti-PII.
5. Commit `docs(m23): l01 …` en el historial.

## Errores comunes

- Métrica sin fórmula.
- Mezclar tenants en definición.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Consulta agregada por tenant_id sin PII](L02-consulta-agregada-por-tenant-id-sin-pii.md)
