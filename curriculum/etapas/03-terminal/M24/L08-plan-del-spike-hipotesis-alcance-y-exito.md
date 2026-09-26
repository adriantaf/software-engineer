---
id: L08
materia: M24
orden: 8
titulo: Plan del spike — hipótesis, alcance y éxito
horas: 5
semana: 2
lectura: "Spike-driven development (notas ficha)"
evidencia: "projects/m24-emergentes/spike/hipotesis.md + spike/plan.md"
---

# L08 — Plan del spike — hipótesis, alcance y éxito

**~5 h · Semana 2**

## Objetivo

Elegir **un** candidato para semana 3; definir hipótesis medible, non-goals y criterio de éxito/fallo.

## Por qué importa

Un spike sin timebox se convierte en feature a medias en producción.

## Conceptos

- Hipótesis falsable
- Timebox ≤1 semana
- Demo script

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/spike/hipotesis.md`: “Si integramos X, entonces Y métrica mejora Z%” (aunque midas manualmente).

`projects/m24-emergentes/spike/plan.md`: entradas, salidas, comandos demo, **fuera de alcance** (lista explícita).

Actualiza matriz con candidato **elegido para spike**.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l08 plan-del-spike-hipotesis-alcance-y-exito"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Semana 3 spike | P2 matriz |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. hipotesis.md y plan.md.
2. Non-goals ≥3 ítems.
3. Candidato spike único.

## Errores comunes

- Spike de tres tecnologías a la vez.
- Hipótesis ‘aprender X’ sin métrica.

## Siguiente

[L09 — Scaffold del spike y entorno aislado](L09-scaffold-del-spike-y-entorno-aislado.md)
