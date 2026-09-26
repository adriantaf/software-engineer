---
id: L11
materia: M24
orden: 11
titulo: Medición contra la hipótesis
horas: 5
semana: 3
lectura: "Notas de experimento / métricas manuales"
evidencia: "projects/m24-emergentes/spike/resultados.md"
---

# L11 — Medición contra la hipótesis

**~5 h · Semana 3**

## Objetivo

Registrar qué observaste vs hipótesis (latencia, costo estimado, complejidad, fallos).

## Por qué importa

Un spike que ‘más o menos funcionó’ sin números no alimenta go/no-go.

## Conceptos

- Éxito / fallo honesto
- Deuda si hay go
- Aprendizaje

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/spike/resultados.md`: tabla **Esperado / Observado / Conclusión**.

Si falló, documenta por qué — sigue siendo entrega válida.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l11 medicion-contra-la-hipotesis"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Hipótesis L08 | Matriz costo |

## Hecho cuando

1. resultados.md con ≥3 mediciones.
2. Conclusión explícita.

## Errores comunes

- Declarar éxito sin probar hipótesis.
- Ocultar blockers.

## Siguiente

[L12 — Go/no-go, cierre M24 y handoff](L12-go-no-go-cierre-m24-y-handoff.md)
