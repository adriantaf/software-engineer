---
id: L14
materia: M26
orden: 14
titulo: App móvil M20 conectada o plan cierre
horas: 5
semana: 4
lectura: "m20-movil README"
evidencia: "projects/m26-capstone/mobile-gap.md"
---

# L14 — App móvil M20 conectada o plan cierre

**~5 h · Semana 4**

## Objetivo

Entregar evidencia de: App móvil M20 conectada o plan cierre para el capstone Agenda Ops en producción.

## Por qué importa

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

## Conceptos

- Misma API
- Staging HTTPS

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m26-capstone/memoria projects/m26-capstone/demos projects/m26-capstone/bitacora
```

Estado conexión móvil; APK contra staging o plan con fecha.

Registra horas y bloqueos en `projects/m26-capstone/bitacora/semana-04.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m26): l14 app-movil-m20-conectada-o-plan-cierre"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | [producto-saas.md](../../producto-saas.md) | [egreso.md](../../egreso.md) |
| Ficha | M26-proyecto-integrador.md | M25 security-review |
| Catálogo | Entrada M26 | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

1. Artefacto indicado existe: projects/m26-capstone/mobile-gap.md.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L15 — Métricas M22 en producto](L15-metricas-m22-en-producto.md)
