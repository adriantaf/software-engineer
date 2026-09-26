---
id: L04
materia: M12
orden: 4
titulo: Stakeholders y contexto Agenda Ops
horas: 5
semana: 1
lectura: "SRS plantilla stakeholders"
evidencia: "srs-borrador.md sección contexto"
---

# L04 — Stakeholders y contexto Agenda Ops

**~5 h · Semana 1**

## Objetivo

Documentar actores owner/staff/cliente final y objetivos del piloto single-tenant.

## Por qué importa

M13 y M17 heredan actores; cambiarlos tarde cuesta caro.

## Conceptos

- stakeholder.
- single-tenant.
- MVP 4 semanas.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa contexto y alcance preliminar en borrador. MoSCoW preview.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l04 stakeholders-y-contexto-agenda-ops"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plantilla | introducción | hilo seguridad |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. Actores definidos.
2. Objetivo piloto escrito.
3. Cierre semana 1 P1.

## Errores comunes

- Omitir cliente final indirecto.
- Multi-tenant en MVP.

## Siguiente

[L05 — Formato user story y trazabilidad](L05-formato-user-story-y-trazabilidad.md)
