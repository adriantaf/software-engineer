---
id: L05
materia: M22
orden: 5
titulo: Validated learning — hipótesis de dolor y métrica de trial
horas: 5
semana: 2
lectura: "Lean — validated learning"
evidencia: "projects/m22-bektor/hipotesis-trial.md"
---

# L05 — Validated learning — hipótesis de dolor y métrica de trial

**~5 h · Semana 2**

## Objetivo

Formular hipótesis: dolor, solución mínima, métrica de éxito del trial (≥1 cita en 7 días).

## Por qué importa

M22 mide aprendizaje, no vanity; esta métrica alinea con M23.

## Conceptos

- Hipótesis falsable.
- Métrica activación.
- Baseline.
- Criterio de pivot.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m22-bektor/hipotesis-trial.md` con plantilla: Creemos que… Mediremos… Éxito si… Fracaso si…

Enlaza a `projects/m22-bektor/metricas-trials.md` (crear encabezados de columnas: negocio, trial iniciado, activación 7d, notas).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l05 validated-learning-hipotesis-de-dolor-y-"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ries | Validated learning | ../../../producto-saas.md |
| Catálogo | Entrada M22 | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

1. hipotesis-trial.md.
2. metricas-trials.md esqueleto.
3. Métrica activación definida.

## Errores comunes

- Métrica ‘likes’.
- Hipótesis no falsable.

## Siguiente

[L06 — Demo 1 — conversación real documentada](L06-demo-1-conversacion-real-documentada.md)
