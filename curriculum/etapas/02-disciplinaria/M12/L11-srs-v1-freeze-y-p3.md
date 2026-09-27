---
id: L11
materia: M12
orden: 11
titulo: SRS v1, freeze y P3
horas: 5.0
semana: 3
lectura: plantilla completa
evidencia: projects/m12-srs/srs-v1.md
---

# L11 — SRS v1, freeze y P3

**~5.0 h · Semana 3**

P3 y proyecto: el documento que M13/M17 consumen.

## Objetivo

Publicar `srs-v1.md` congelado.

## Pasos

### 1. Copiar y pulir (90–120 min)

```bash
cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
```

Completa huecos: referencias, supuestos, dependencias (Node, Postgres), RNF ≥3, glosario, MoSCoW resumido.

### 2. Freeze banner (20 min)

Al inicio:

```markdown
> **Freeze v1 — YYYY-MM-DD**  
> Cambios post-freeze → ADR o srs-v1.1 con diff explícito.
```

### 3. Checklist P3 (30 min)

README: P1 entrevistas, P2 stories≥8, P3 srs-v1 con RNF.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l11 srs-v1 freeze p3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Freeze: copiar borrador → srs-v1.md; RNF seguridad ≥3 | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `srs-v1.md` completo (intro, contexto, RF, RNF≥3 seguridad/privacidad, fuera de alcance, glosario).
2. Fecha de freeze y versión v1 anotadas.
3. Commit `docs(m12): l11 srs-v1 freeze p3`.

## Errores comunes

- Seguir editando “borrador eterno” sin v1.
- RNF de seguridad ausentes.
- Glosario desalineado con M09/M17.

## Siguiente

[L12 — Revisión M13 y cierre M12](L12-revision-m13-y-cierre-m12.md)
