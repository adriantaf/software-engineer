---
id: L08
materia: M24
orden: 8
titulo: Plan del spike — hipótesis, alcance y éxito
horas: 5.0
semana: 2
lectura: Spike-driven development (notas ficha)
evidencia: projects/m24-emergentes/spike/hipotesis.md + spike/plan.md
---

# L08 — Plan del spike — hipótesis, alcance y éxito

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/hipotesis.md + spike/plan.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Elegir **un** candidato para semana 3; definir hipótesis medible, non-goals y criterio de éxito/fallo.

## Por qué empieza así

Un spike sin timebox se convierte en feature a medias en producción.

Conceptos que debes poder explicar al cerrar:

- Hipótesis falsable
- Timebox ≤1 semana
- Demo script

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Spike-driven development (notas ficha)_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/hipotesis.md`: “Si integramos X, entonces Y métrica mejora Z%” (aunque midas manualmente).

### 3. Laboratorio principal (90–120 min)

`projects/m24-emergentes/spike/plan.md`: entradas, salidas, comandos demo, **fuera de alcance** (lista explícita).

### 4. Endurece el entregable (40–60 min)

Actualiza matriz con candidato **elegido para spike**.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l08 plan-del-spike-hip-tesis-alcance-y-xito"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Spike-driven development (notas ficha) | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/hipotesis.md + spike/plan.md`.
2. hipotesis.md y plan.md.
3. Non-goals ≥3 ítems.
4. Candidato spike único.
5. Commit `docs(m24): l08 …` en el historial.

## Errores comunes

- Spike de tres tecnologías a la vez.
- Hipótesis ‘aprender X’ sin métrica.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — Scaffold del spike y entorno aislado](L09-scaffold-del-spike-y-entorno-aislado.md)
