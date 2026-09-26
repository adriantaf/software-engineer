---
id: L02
materia: M23
orden: 2
titulo: Consulta agregada por tenant_id sin PII
horas: 5
semana: 1
lectura: "SQL agregaciones + minimización datos"
evidencia: "projects/m23-ia/metricas/query-agregada.sql"
---

# L02 — Consulta agregada por tenant_id sin PII

**~5 h · Semana 1**

## Objetivo

Escribir SQL o script que agrupe por `tenant_id` sin columnas de PII en SELECT.

## Por qué importa

El pipeline P1 debe ser reproducible y seguro para compartir export de ejemplo.

## Conceptos

- GROUP BY tenant_id.
- Minimización.
- Vistas.
- Anonimización.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m23-ia/metricas/query-agregada.sql` (o `.ts` script) contra schema Agenda Ops o fixture documentado.

Prohibido SELECT de teléfono, nombre, notas clínicas. Comentario en archivo explica fuente tablas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l02 consulta-agregada-por-tenant-id-sin-pii"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M09 | modelo datos | ../../hilos/seguridad.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. Query/script existe.
2. Sin PII en output.
3. Comentario fuente.

## Errores comunes

- Dump crudo clientes.
- tenant_id del cliente HTTP.

## Siguiente

[L03 — Export de ejemplo y borrador pipeline](L03-export-de-ejemplo-y-borrador-pipeline.md)
