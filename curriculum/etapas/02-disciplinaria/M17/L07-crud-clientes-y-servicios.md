---
id: L07
materia: M17
orden: 7
titulo: CRUD clientes y servicios
horas: 5
semana: 2
lectura: "SRS RF clientes/servicios"
evidencia: "/clientes /servicios"
---

# L07 — CRUD clientes y servicios

**~5 h · Semana 2**

## Objetivo

CRUD completo clientes y servicios con autorización owner/staff según matriz preliminar.

## Por qué importa

Servicios definen duración y precio base para citas.

## Conceptos

- CRUD.
- servicio.
- cliente.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Endpoints + tests feliz y 404. Seeds opcionales.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l07 crud-clientes-y-servicios"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12-srs | Must | m14 precio opcional |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. CRUD ambos recursos.
2. Tests.
3. Commit.

## Errores comunes

- Mezclar cliente entre negocios.
- Sin validación.

## Siguiente

[L08 — Seeds demo y datos design partner](L08-seeds-demo-y-datos-design-partner.md)
