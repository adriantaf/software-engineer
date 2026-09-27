---
id: L12
materia: M24
orden: 12
titulo: Go/no-go, cierre M24 y handoff
horas: 5.0
semana: 3
lectura: Repaso ficha M24 criterios dominio
evidencia: projects/m24-emergentes/go-no-go.md + bitácora semana-03.md
---

# L12 — Go/no-go, cierre M24 y handoff

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/go-no-go.md + bitácora semana-03.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Redactar decisión go/no-go argumentada; actualizar backlog; cerrar prácticas P2–P3 y criterios dominio.

## Por qué empieza así

Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo > valor.

Conceptos que debes poder explicar al cerrar:

- Go / no-go / defer
- Issue derivado
- Archivar spike

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Repaso ficha M24 criterios dominio_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

`projects/m24-emergentes/go-no-go.md`: decisión, criterios, próximos pasos si go, qué archivar si no.

### 3. Laboratorio principal (90–120 min)

Cierra bitácora semana 3. README del proyecto enlaza toda la evidencia P1–P3.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Repaso ficha M24 criterios dominio | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/go-no-go.md + bitácora semana-03.md`.
2. go-no-go.md publicado.
3. README proyecto actualizado.
4. Backlog M21 tocado.
5. Commit `docs(m24): l12 …` en el historial.

## Errores comunes

- Go sin plan de seguridad.
- No-go sin spike ejecutado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
