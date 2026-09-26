---
id: L15
materia: M13
orden: 15
titulo: Extensibilidad tenant_id sin implementar
horas: 5.0
semana: 4
lectura: producto-saas.md multi-tenant; nota de extensibilidad
evidencia: adr/004-extensibilidad-tenant.md o seccion en arquitectura.md
---

# L15 — Extensibilidad tenant_id sin implementar

**~5.0 h · Semana 4**

El camino a SaaS pide `tenant_id` después. Hoy dejas el gancho **sin** construir el edificio.

## Objetivo

Nota de extensibilidad legible por el yo-de-M17/M19.

## Pasos (hazlos en orden)

### 1. Lee producto-saas (25 min)

Sección evolución técnica: piloto single-tenant → tenants.

### 2. Escribe la nota (80–100 min)

`adr/004-extensibilidad-tenant.md`:

```markdown
# Nota — Extensibilidad multi-tenant

## Ahora (piloto)
Un negocio design partner. `negocioId` implícito o constante de config.

## Después
Columna `tenant_id` en clientes, servicios, citas, usuarios.
Queries siempre filtran por tenant. Tests IDOR cross-tenant en M15/M18.

## Qué no hacemos hoy
Stripe, onboarding self-serve, N esquemas Postgres.
```

### 3. Marca en clases.md (30 min)

Comentario: “candidato a tenant_id” en entidades de negocio.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): nota extensibilidad tenant_id"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Single-tenant ahora; dónde encajará tenant_id después | [Producto SaaS — evolución técnica](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Documento que explica single-tenant del piloto y *dónde* se añadirá `tenant_id` (tablas/capas).
2. Lista explícita de lo que NO implementas aún (billing, onboarding multi-negocio).
3. Commit `docs(m13): nota extensibilidad tenant_id`.

## Errores comunes

- Implementar multi-tenant completo en diseño día 1.
- Ignorar tenant y luego reescribir todo el esquema.
- Poner tenant_id solo en el front.

## Siguiente

[L16 — ADR auth y sesión](L16-adr-auth-y-sesion.md)
