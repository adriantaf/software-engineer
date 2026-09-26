---
id: L22
materia: M22
orden: 22
titulo: Síntesis comercial para backlog M21
horas: 5
semana: 6
lectura: "Lean — aprendizaje → producto"
evidencia: "projects/m22-bektor/handoff-producto.md"
---

# L22 — Síntesis comercial para backlog M21

**~5 h · Semana 6**

## Objetivo

Traducir aprendizajes comerciales en ≥5 issues priorizados para Agenda Ops (M21 backlog).

## Por qué importa

El hilo Ops/SaaS cierra loop gestión ↔ mercado.

## Conceptos

- Backlog.
- Prioridad.
- Issue template.
- Demo feedback.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m22-bektor/handoff-producto.md`: tabla aprendizaje → issue sugerido → prioridad.

Crea o enlaza issues reales en repo producto. Notifica en `projects/m21-proyectos/board.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l22 sintesis-comercial-para-backlog-m21"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M21 | projects/m21-proyectos | ../../../producto-saas.md |

## Hecho cuando

1. ≥5 issues sugeridos.
2. Enlaces GitHub.
3. board.md actualizado.

## Errores comunes

- Lista deseos sin issues.
- Features sin origen demo.

## Siguiente

[L23 — Pitch final 60s y práctica grabada](L23-pitch-final-60s-y-practica-grabada.md)
