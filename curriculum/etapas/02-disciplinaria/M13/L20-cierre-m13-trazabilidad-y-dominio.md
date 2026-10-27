---
id: L20
materia: M13
orden: 20
titulo: Cierre M13 — trazabilidad y dominio
horas: 5.0
semana: 5
lectura: Criterios de dominio ficha M13; trazabilidad SRS↔diagramas
evidencia: trazabilidad.md + README final; criterios de dominio autoevaluados
---

# L20 — Cierre M13 — trazabilidad y dominio

**~5.0 h · Semana 5**

Cierras la materia demostrando que cada diagrama sirve a un requisito — y que puedes defender el monolito modular.

## Objetivo

Matriz de trazabilidad + autoevaluación de criterios de dominio de la ficha.

## Pasos (hazlos en orden)

### 1. Matriz (70–90 min)

`trazabilidad.md`:

| Historia SRS | UC | Diagrama / ADR |
|--------------|----|----------------|
| H-pedido-01 | UC-03 | secuencia-crear-pedido, ADR 002 |

Borra artefactos huérfanos o enlázalos.

### 2. Criterios de dominio (40–50 min)

De la ficha M13 — responde en `bitacora-cierre.md`:

- ¿Defiendes monolito modular con trade-offs?
- ¿Sabes dónde se valida el rol?
- ¿Un compañero puede empezar M17 con SRS + este paquete?

### 3. Pulido README (30 min)

Estado: “Paquete listo para M17” + fecha.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Trazabilidad requisito→diseño; autoevaluación criterios de dominio | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.
2. Autoevaluación de criterios de dominio en bitácora o README (honesta).
3. Commit `docs(m13): cierre trazabilidad y criterios de dominio`.

## Errores comunes

- Diagramas sin fila en la matriz de trazabilidad.
- Autoevaluación todo ✓ sin evidencia.
- Microservicios reintroducidos en el cierre.

## Siguiente

Materia siguiente: [M14 — Patrones](../M14-patrones.md) · L01 en `../M14/`.
