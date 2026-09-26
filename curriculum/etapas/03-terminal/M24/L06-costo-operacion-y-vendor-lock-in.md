---
id: L06
materia: M24
orden: 6
titulo: Costo, operación y vendor lock-in
horas: 5.0
semana: 2
lectura: Pricing pages + SLA del candidato elegido preliminar
evidencia: projects/m24-emergentes/matriz-adopcion.md sección Costo
---

# L06 — Costo, operación y vendor lock-in

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/matriz-adopcion.md sección Costo`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Estimar costo mensual a 10 / 100 tenants y documentar dependencia del vendor (migración, export).

## Por qué empieza así

Agenda Ops es SaaS; un canal de mensajería caro por conversación puede matar margen.

Conceptos que debes poder explicar al cerrar:

- Costo marginal por tenant
- Exit strategy
- Fallback manual

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Pricing pages + SLA del candidato elegido preliminar_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

Actualiza la matriz con escenarios de costo (tabla tenants × mensajes/mes).

### 3. Laboratorio principal (90–120 min)

Para el candidato líder, escribe párrafo **Si el vendor sube precio 2×** en `matriz-adopcion.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l06 costo-operaci-n-y-vendor-lock-in"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Pricing pages + SLA del candidato elegido preliminar | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md sección Costo`.
2. Escenarios de costo documentados.
3. Párrafo exit/lock-in.
4. Commit `docs(m24): l06 …` en el historial.

## Errores comunes

- Costo ‘gratis’ sin leer tier de producción.
- No considerar tiempo de ingeniería.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Threat sketch del candidato para spike](L07-threat-sketch-del-candidato-para-spike.md)
