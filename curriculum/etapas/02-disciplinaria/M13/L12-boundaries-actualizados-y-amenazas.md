---
id: L12
materia: M13
orden: 12
titulo: Boundaries actualizados y amenazas
horas: 5.0
semana: 3
lectura: Trust boundaries + amenazas alto nivel; cierre P3
evidencia: trust-boundaries.md actualizado (P3) + notas de amenaza
---

# L12 — Boundaries actualizados y amenazas

**~5.0 h · Semana 3**

Cierras P3: el diagrama de L01 ahora refleja capas, DTOs y contenedores reales.

## Objetivo

Actualizar `diagramas/trust-boundaries.md` y dejar P3 evidenciable.

## Pasos (hazlos en orden)

### 1. Relee L01 + arquitectura (30 min)

Marca desactualizaciones (¿apareció el mail? ¿sesión?).

### 2. Tabla de amenazas (70–90 min)

| Amenaza | Límite | Mitigación de diseño |
|---------|--------|----------------------|
| IDOR pedido | API→DB | filtro por dueño/negocio en queries |
| Session hijack | Browser→API | Cookie Secure/HttpOnly; logout |
| Mass assignment | Browser→API | DTO allowlist |
| SQLi | API→DB | parametrized queries / ORM |

### 3. Checklist P3 (20 min)

Ficha: `trust-boundaries.md` con límites y notas de amenaza.

### 4. Bitácora semana 3 (30 min)

`bitacora-semana-3.md`: capas + amenaza que más te preocupa.

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): boundaries actualizados y amenazas P3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Amenazas en límites; IDOR, sesión, validación | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `trust-boundaries.md` actualizado con capas/C4 y ≥3 amenazas con mitigación de diseño.
2. P3 cumplido: boundaries con límites y notas de amenaza.
3. Commit `docs(m13): boundaries actualizados y amenazas P3`.

## Errores comunes

- Lista OWASP Top 10 pegada sin relación a tus cajas.
- Mitigaciones solo “usaremos HTTPS” sin authz en API.
- P3 marcado con el archivo de L01 sin actualizar.

## Siguiente

[L13 — Plantilla ADR y decisiones de diseño](L13-plantilla-adr-y-decisiones-de-diseno.md)
