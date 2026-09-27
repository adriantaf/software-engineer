---
id: L07
materia: M26
orden: 7
titulo: Panel admin por tenant
horas: 5.0
semana: 2
lectura: Roles dueño/staff
evidencia: projects/m26-capstone/memoria/panel-admin.md
---

# L07 — Panel admin por tenant

**~5 h · Semana 2**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/panel-admin.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Panel admin por tenant con rutas/capturas y nota de authz.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- RBAC
- UI scoped

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Roles dueño/staff_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Inventario de rutas admin (25–35 min)

En `projects/m26-capstone/memoria/panel-admin.md` lista rutas del panel (dashboard, pedidos, clientes, staff, billing).

### 3. Prueba UI scoped (100–120 min)

Login A: captura o anota IDs visibles. Login B: confirma que no ves recursos de A.

Para ≥1 ruta API detrás del panel:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq 'length'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/admin/clientes" | jq 'length'
```

### 4. Nota de authz (25–35 min)

Staff vs owner: qué pantallas cambian. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l07 panel-admin-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Roles dueño/staff | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/panel-admin.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L08 — Demo interna semana 2 — dos tenants](L08-demo-interna-semana-2-dos-tenants.md)
