---
id: L16
materia: M15
orden: 16
titulo: Cierre M15 — pipeline, coverage dominio, dominio
horas: 5
semana: 4
lectura: "Ficha M15 criterios"
evidencia: "projects/m15-calidad/nota-cierre-m15.md"
---

# L16 — Cierre M15 — pipeline, coverage dominio, dominio

**~5 h · Semana 4**

## Objetivo

Auditar P1–P3, coverage en dominio, CI verde, criterios dominio respondidos.

## Por qué importa

M17 debe mantener este pipeline; hoy lo dejas listo.

## Conceptos

- handoff M17.
- P1–P3.
- dominio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`nota-cierre-m15.md` + checklist ficha. Enlaza workflow y coverage report.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l16 cierre-m15-pipeline-coverage-dominio-dom"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M15-vv-calidad.md | ../M17-aplicaciones-web.md |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. P1–P3 verificados.
2. 401/403 en tests.
3. Cierre commit.

## Errores comunes

- Marcar sin CI.
- Coverage solo en UI.
