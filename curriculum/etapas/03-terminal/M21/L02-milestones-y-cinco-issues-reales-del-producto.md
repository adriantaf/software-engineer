---
id: L02
materia: M21
orden: 2
titulo: Milestones y cinco issues reales del producto
horas: 5
semana: 1
lectura: "Scrum Guide — artefactos y compromiso del backlog"
evidencia: "projects/m21-proyectos/board.md borrador"
---

# L02 — Milestones y cinco issues reales del producto

**~5 h · Semana 1**

## Objetivo

Crear milestones de cuatro semanas de M21 y mover cinco issues **reales** del repo Agenda Ops al backlog priorizado.

## Por qué importa

El tablero ficticio no prepara trials (M22) ni FAQ (M23); hoy enlazas gestión al código que ya desplegaste.

## Conceptos

- Milestone.
- Issue vs épica.
- Etiquetas feature/security/ops.
- Prioridad vs urgencia.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

En GitHub Projects (o Linear): milestones `M21-S1` … `M21-S4` con fechas orientativas.

Mueve **5 issues** del repo producto al backlog ordenado. **Al menos uno** debe ser seguridad o `tenant_id` (cross-tenant, secretos, backup).

Escribe `projects/m21-proyectos/board.md` con URL del board + fecha de captura. Lista los 5 issues con enlace `#`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l02 milestones-y-cinco-issues-reales-del-pro"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Scrum Guide | Artefactos | GitHub Projects docs |

## Hecho cuando

1. 5 issues enlazados.
2. ≥1 issue security/tenant.
3. board.md con URL.

## Errores comunes

- Issues de tutorial sin repo producto.
- Milestone sin fechas.

## Siguiente

[L03 — Roadmap trimestral alineado a producto-saas](L03-roadmap-trimestral-alineado-a-producto-saas.md)
