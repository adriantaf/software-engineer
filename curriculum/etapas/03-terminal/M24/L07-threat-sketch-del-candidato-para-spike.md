---
id: L07
materia: M24
orden: 7
titulo: Threat sketch del candidato para spike
horas: 5.0
semana: 2
lectura: Webhook security + secret management
evidencia: projects/m24-emergentes/spike/threat-sketch.md
---

# L07 — Threat sketch del candidato para spike

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/threat-sketch.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Una página de amenazas del integración elegida: secretos, replay, PII en payloads, supply chain.

## Por qué empieza así

Emergente ≠ inseguro por defecto, pero sí suele traer webhooks y tokens nuevos.

Conceptos que debes poder explicar al cerrar:

- Firma HMAC webhooks
- PII en mensajes
- Principio mínimo privilegio

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Webhook security + secret management_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/threat-sketch.md`: actores, datos que cruzan el límite, ≥5 amenazas, mitigaciones previstas en el spike.

### 3. Laboratorio principal (90–120 min)

Lista secretos nuevos (nombres, no valores) en tabla.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l07 threat-sketch-del-candidato-para-spike"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Webhook security + secret management | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/threat-sketch.md`.
2. threat-sketch.md ≥1 página.
3. Secretos nombrados sin valores.
4. Commit `docs(m24): l07 …` en el historial.

## Errores comunes

- Spike sin pensar en replay.
- Loguear payloads con teléfonos reales.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Plan del spike — hipótesis, alcance y éxito](L08-plan-del-spike-hipotesis-alcance-y-exito.md)
