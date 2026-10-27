---
id: L29
materia: M17
orden: 29
titulo: ADR tenant_id y modelo multi-negocio
horas: 5.0
semana: 8
lectura: producto-saas multi-tenant
evidencia: projects/m17-vitrina/docs/adr-tenant-id.md
---

# L29 — ADR tenant_id y modelo multi-negocio

**~5.0 h · Semana 8**

M26 depende de esta decisión; M17 la prepara.

## Objetivo

ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries siempre filtradas.

## Conceptos clave

- tenant_id
- ADR
- single-tenant piloto

## Pasos (hazlos en orden)

### 1. ADR tenant_id (70–90 min)

```bash
cat > projects/m17-vitrina/docs/adr-tenant-id.md << 'EOF'
# ADR: tenant_id / multi-negocio
## Contexto
Piloto single-tenant hoy; camino a SaaS.
## Decisión
Columna/negocio_id nullable ahora; queries siempre filtradas cuando presente.
## Consecuencias
...
EOF
```

### 2. Marca código futuro (30 min)

```ts
// TODO(tenant): filtrar por negocio_id en listados
```

```bash
git add projects/m17-vitrina/docs/adr-tenant-id.md
git commit -m "docs(m17): L29 adr tenant_id multi-negocio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas multi-tenant | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/adr-tenant-id.md` con contexto/decisión/consecuencias.
2. Commit `docs(m17): L29 adr-tenant-id-y-modelo-multi-negocio`.

## Errores comunes

- ADR genérico sin Vitrina.
- Implementar multi-tenant completo sin necesidad.

## Siguiente

[L30 — Checklist camino a SaaS](L30-checklist-camino-a-saas.md)
