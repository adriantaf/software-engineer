---
id: L04
materia: M24
orden: 4
titulo: Cierre research semana 1 y backlog M21
horas: 5
semana: 1
lectura: "Repaso research + issues Agenda Ops"
evidencia: "projects/m24-emergentes/research/README.md + enlace issue M21"
---

# L04 — Cierre research semana 1 y backlog M21

**~5 h · Semana 1**

## Objetivo

Cerrar P1 research: índice de notas y al menos un issue o comentario en backlog relacionado (spike futuro o descarte).

## Por qué importa

El spike debe resolver duda del producto, no curiosidad técnica aislada.

## Conceptos

- Definition of spike
- Non-goals
- Evidencia en git

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/research/README.md` enlaza los tres candidatos y resume en 10 líneas cuál parece más prometedor **sin** decidir aún.

En el repo del producto o `projects/m21-proyectos/`, abre issue “M24 spike: …” o comenta en roadmap.

Cierra `bitacora/semana-01.md` con horas reales vs plan.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l04 cierre-research-semana-1-y-backlog-m21"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Práctica P1 M24 | M21 roadmap |

## Hecho cuando

1. README research.
2. Enlace a issue/comentario backlog.
3. Bitácora semana 1 cerrada.

## Errores comunes

- Marcar P1 sin tres archivos.
- Prometer feature en M26 sin go/no-go.

## Siguiente

[L05 — Matriz de adopción y pesos](L05-matriz-de-adopcion-y-pesos.md)
