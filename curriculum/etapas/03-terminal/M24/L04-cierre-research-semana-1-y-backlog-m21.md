---
id: L04
materia: M24
orden: 4
titulo: Cierre research semana 1 y backlog M21
horas: 5.0
semana: 1
lectura: Repaso research + issues Agenda Ops
evidencia: projects/m24-emergentes/research/README.md + enlace issue M21
---

# L04 — Cierre research semana 1 y backlog M21

**~5 h · Semana 1**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/research/README.md + enlace issue M21`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Cerrar P1 research: índice de notas y al menos un issue o comentario en backlog relacionado (spike futuro o descarte).

## Por qué empieza así

El spike debe resolver duda del producto, no curiosidad técnica aislada.

Conceptos que debes poder explicar al cerrar:

- Definition of spike
- Non-goals
- Evidencia en git

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Repaso research + issues Agenda Ops_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/research`.

`projects/m24-emergentes/research/README.md` enlaza los tres candidatos y resume en 10 líneas cuál parece más prometedor **sin** decidir aún.

### 3. Laboratorio principal (90–120 min)

En el repo del producto o `projects/m21-proyectos/`, abre issue “M24 spike: …” o comenta en roadmap.

### 4. Endurece el entregable (40–60 min)

Cierra `bitacora/semana-01.md` con horas reales vs plan.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l04 cierre-research-semana-1-y-backlog-m21"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Repaso research + issues Agenda Ops | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/research/README.md + enlace issue M21`.
2. README research.
3. Enlace a issue/comentario backlog.
4. Bitácora semana 1 cerrada.
5. Commit `docs(m24): l04 …` en el historial.

## Errores comunes

- Marcar P1 sin tres archivos.
- Prometer feature en M26 sin go/no-go.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Matriz de adopción y pesos](L05-matriz-de-adopcion-y-pesos.md)
