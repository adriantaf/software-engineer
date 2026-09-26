---
id: L29
materia: M17
orden: 29
titulo: ADR tenant_id y modelo multi-negocio
horas: 5
semana: 8
lectura: "producto-saas multi-tenant"
evidencia: "projects/m17-agenda-ops/docs/adr-tenant-id.md"
---

# L29 — ADR tenant_id y modelo multi-negocio

**~5 h · Semana 8**

## Objetivo

ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries siempre filtradas.

## Por qué importa

M26 depende de esta decisión; M17 la prepara.

## Conceptos

- tenant_id.
- ADR.
- single-tenant piloto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR con contexto M09/M13. Lista tablas afectadas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l29 adr-tenant-id-y-modelo-multi-negocio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| producto-saas.md | fases | m13 L15 |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. adr-tenant-id.md.
2. Tablas listadas.
3. Commit.

## Errores comunes

- Multi-tenant completo día 1.
- Sin filtro en queries.

## Siguiente

[L30 — Checklist camino a SaaS](L30-checklist-camino-a-saas.md)
