# M13 — Análisis y diseño de software

Carpeta de **evidencia** de esta materia. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Traduces el SRS de Vitrina a diseño usable: flujos, diagramas y ADRs que el yo-de-M17 pueda seguir.

## Estructura esperada

```text
projects/m13-diseno/
  README.md                 ← este índice
  casos-de-uso.md           ← P1
  arquitectura.md
  endpoints-m17.md
  checklist-scaffold.md
  trazabilidad.md
  diagramas/
    trust-boundaries.md     ← P3
    clases.md               ← P2
    secuencia-auth.md
    secuencia-crear-pedido.md ← P2
    c4-contenedores.md
  adr/
    README.md
    PLANTILLA.md
    001-monolito-modular.md
    002-persistencia.md
    003-auth-sesion.md
    004-extensibilidad-tenant.md
```

## Checklist (Evidencia de hecho)

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Flujos:** `casos-de-uso.md` cubriendo historias Must del SRS.
- **P2 — UML:** `diagramas/clases.md` + `diagramas/secuencia-*.md`.
- **P3 — Boundaries:** `diagramas/trust-boundaries.md` actualizado.
- **Proyecto — Paquete:** este README como índice + ADRs en `adr/`.

## Cómo usarla

1. Abre la ficha **M13** y la lección **L01**.
2. Empieza por trust boundaries + ADR 001.
3. Enlaza el SRS: `projects/m12-srs/srs-v1.md` (o plantilla).
4. Marca prácticas/proyecto en la UI solo cuando exista la evidencia.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M13-analisis-y-diseno.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M13/`
- Bibliografía: `curriculum/bibliografia.md#m13-analisis-y-diseno`
- Plan: `/materia/M13/`
