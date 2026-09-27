---
id: L19
materia: M13
orden: 19
titulo: Checklist listo para scaffold
horas: 5.0
semana: 5
lectura: Checklist de salida hacia M17
evidencia: checklist-scaffold.md marcado con evidencia enlazada
---

# L19 — Checklist listo para scaffold

**~5.0 h · Semana 5**

Definition of Ready: si falta algo Must, hoy se arregla o se documenta el riesgo.

## Objetivo

`checklist-scaffold.md` que un yo futuro use el día 1 de M17.

## Pasos (hazlos en orden)

### 1. Escribe el checklist (60–70 min)

```markdown
# Checklist — listo para scaffold M17

- [ ] SRS enlazado
- [ ] casos-de-uso.md (P1)
- [ ] clases + secuencia (P2)
- [ ] trust-boundaries (P3)
- [ ] arquitectura.md + DTOs
- [ ] ADR 001–003
- [ ] endpoints-m17.md
- [ ] nota tenant_id
```

### 2. Marca con enlaces (50–60 min)

Cada ítem: ruta relativa al archivo.

### 3. Deuda consciente (30 min)

Sección “Aceptamos no tener X porque…”.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/checklist-scaffold.md
git commit -m "docs(m13): checklist listo para scaffold"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Definition of Ready del paquete de diseño | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `checklist-scaffold.md` con ítems marcados y enlaces a archivos del paquete.
2. Cero ítems Must en “TBD” sin justificación.
3. Commit `docs(m13): checklist listo para scaffold`.

## Errores comunes

- Checklist todo ✓ sin enlaces.
- Dejar P2/P3 incompletos y seguir igual.
- Incluir nice-to-have como bloqueantes.

## Siguiente

[L20 — Cierre M13 — trazabilidad y dominio](L20-cierre-m13-trazabilidad-y-dominio.md)
