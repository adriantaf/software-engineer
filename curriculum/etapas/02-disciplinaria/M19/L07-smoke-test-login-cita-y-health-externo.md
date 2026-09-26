---
id: L07
materia: M19
orden: 7
titulo: Smoke test: login, cita y health externo
horas: 5
semana: 2
lectura: "Runbook borrador"
evidencia: "projects/m19-ops/smoke-staging.md"
---

# L07 — Smoke test: login, cita y health externo

**~5 h · Semana 2**

## Objetivo

Ejecutar checklist smoke desde fuera de tu laptop: login, crear cita, GET /health.

## Por qué importa

‘Contenedor verde’ ≠ producto usable.

## Conceptos

- smoke test
- datos prueba

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Checklist binario en smoke-staging.md con capturas o salidas curl anonimizadas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l07 smoke-test-login-cita-y-health-externo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 | M17 API |

## Hecho cuando

1. Smoke completo.
2. health externo.
3. Fecha registrada.

## Errores comunes

- Solo health sin login
- Smoke nunca repetido

## Siguiente

[L08 — Dominios y deploy-log semana 2](L08-dominios-y-deploy-log-semana-2.md)
