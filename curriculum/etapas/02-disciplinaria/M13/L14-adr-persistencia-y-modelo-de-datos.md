---
id: L14
materia: M13
orden: 14
titulo: ADR persistencia y modelo de datos
horas: 5
semana: 4
lectura: "Elmasri + ADR"
evidencia: "adr/003-persistencia.md"
---

# L14 — ADR persistencia y modelo de datos

**~5 h · Semana 4**

## Objetivo

ADR sobre esquema relacional, migraciones y soft-delete si aplica.

## Por qué importa

M09 y M17 dependen de esta decisión.

## Conceptos

- migración.
- esquema.
- soft delete.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR 003 enlaza clases.md y cardinalidades.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l14 adr-persistencia-y-modelo-de-datos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M09 | ficha | srs |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. ADR 003.
2. Enlace diagrama clases.
3. Migraciones mencionadas.

## Errores comunes

- JSON files en prod.
- Sin plan migraciones.

## Siguiente

[L15 — Extensibilidad tenant_id sin implementar](L15-extensibilidad-tenant-id-sin-implementar.md)
