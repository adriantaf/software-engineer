---
id: L09
materia: M12
orden: 9
titulo: Alcance MVP y MoSCoW
horas: 5.0
semana: 3
lectura: producto-saas fases + priorización
evidencia: srs-borrador alcance MoSCoW
---

# L09 — Alcance MVP y MoSCoW

**~5.0 h · Semana 3**

Decir “no” es un entregable. Hoy priorizas.

## Objetivo

Congelar alcance MVP con MoSCoW en el borrador SRS.

## Pasos

### 1. Inventario (30 min)

Lista US-xx existentes.

### 2. MoSCoW (75 min)

| US | MoSCoW | Justificación 1 línea |
|----|--------|----------------------|

Must típicos: auth owner, clientes, pedidos CRUD básico, agenda del día. Won't: multi-tenant, Stripe, IA, app móvil nativa.

### 3. Capacidad (40 min)

Escribe supuestos de velocidad (1 dev) y qué cae si algo Must se atrasa.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
git commit -m "docs(m12): l09 moscow mvp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | MVP 4 semanas build; Must/Should/Could/Won't | [producto-saas.md](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla MoSCoW de todas las US + lista explícita Won't (multi-tenant, billing, IA…).
2. Párrafo: por qué el Must cabe en ~4 semanas de build hacia M17.
3. Commit `docs(m12): l09 moscow mvp`.

## Errores comunes

- Todo es Must.
- Won't vacío.
- MVP que incluye pagos + IA + multi-sucursal.

## Siguiente

[L10 — Requisitos funcionales en SRS](L10-requisitos-funcionales-en-srs.md)
