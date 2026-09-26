---
id: L10
materia: M24
orden: 10
titulo: Flujo mínimo demostrable
horas: 5.0
semana: 3
lectura: API reference secciones usadas en el spike
evidencia: projects/m24-emergentes/spike/ + demo-log.md
---

# L10 — Flujo mínimo demostrable

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/ + demo-log.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Implementar un flujo que un mentor pueda ver en ≤10 min (webhook, evento UI, mensaje test, etc.).

## Por qué empieza así

P3 exige PoC, no repositorio vacío con intenciones.

Conceptos que debes poder explicar al cerrar:

- Happy path
- Idempotencia básica
- Logs sin PII

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _API reference secciones usadas en el spike_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

Completa el happy path del plan. Registra en `spike/demo-log.md` pasos + capturas o salida terminal.

### 3. Laboratorio principal (90–120 min)

Si usas webhooks: verifica firma o documenta TODO explícito.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l10 flujo-m-nimo-demostrable"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | API reference secciones usadas en el spike | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/ + demo-log.md`.
2. Flujo demo reproducible.
3. demo-log.md con pasos.
4. Commit `docs(m24): l10 …` en el historial.

## Errores comunes

- Demo solo en tu máquina sin instrucciones.
- PII real en prueba.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Medición contra la hipótesis](L11-medicion-contra-la-hipotesis.md)
