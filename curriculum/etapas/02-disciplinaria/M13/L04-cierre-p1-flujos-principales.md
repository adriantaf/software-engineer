---
id: L04
materia: M13
orden: 4
titulo: Cierre P1 flujos principales
horas: 5.0
semana: 1
lectura: Repaso casos de uso Must; evidencia P1 ficha M13
evidencia: casos-de-uso.md consolidado (P1) + bitácora semana 1
---

# L04 — Cierre P1 flujos principales

**~5.0 h · Semana 1**

P1 de M13 es evidencia: flujos principales del Agenda en un solo archivo legible.

## Objetivo

Consolidar `casos-de-uso.md` y dejar bitácora de semana 1 lista para marcar P1.

## Pasos (hazlos en orden)

### 1. Auditoría Must (50–60 min)

Compara `casos-de-uso.md` vs SRS:

```bash
# anota a mano o con grep mental
# ¿Cada historia Must tiene UC-xx?
```

Tabla de cobertura al inicio del archivo:

| Historia SRS | UC | ¿Errores? |
|--------------|----|-----------|
| … | UC-0x | sí/no |

### 2. Limpieza (40–50 min)

- Elimina UC duplicados o “nice to have” sin traza.
- Unifica nombres (Cliente vs Customer).
- Asegura que login y crear cita tienen alternos.

### 3. Bitácora semana 1 (40–50 min)

`projects/m13-diseno/bitacora-semana-1.md`:

```markdown
# Bitácora M13 — Semana 1

## Hecho
- Trust boundaries + ADR 001
- Casos de uso Must + errores

## Fuera de alcance (consciente)
- …

## Decisión que sostengo
Monolito modular porque …
```

### 4. Checklist P1 (20 min)

Según ficha: P1 = `casos-de-uso.md` cubriendo Must. Léelo en voz alta 5 minutos: ¿un compañero entiende el piloto?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre P1 flujos principales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Cierre de flujos Must; checklist P1 de la ficha M13 | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `casos-de-uso.md` cubre historias Must del SRS con actores, UC y errores 401/403/409 donde aplica.
2. Existe `projects/m13-diseno/bitacora-semana-1.md` (qué quedó fuera + 1 decisión).
3. Commit `docs(m13): cierre P1 flujos principales`.

## Errores comunes

- Marcar P1 en la UI sin el archivo consolidado en git.
- Dejar UC “TBD” en Must.
- Bitácora vacía o solo “avancé”.

## Siguiente

[L05 — Diagrama de clases del dominio](L05-diagrama-de-clases-del-dominio.md)
