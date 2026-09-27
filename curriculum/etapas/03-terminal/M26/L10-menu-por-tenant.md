---
id: L10
materia: M26
orden: 10
titulo: Menú por tenant
horas: 5.0
semana: 3
lectura: Modelo dominio Vitrina
evidencia: projects/m26-capstone/memoria/menu-por-tenant.md
---

# L10 — Menú por tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/menu-por-tenant.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Categorías e ítems de menú scoped por tenant; perfil público solo muestra el menú del tenant resuelto.

## Por qué empieza así

El menú es el producto principal de Vitrina. Sin aislamiento aquí, el resto del SaaS no importa.

Conceptos que debes poder explicar al cerrar:

- Catálogo por tenant
- Disponibilidad
- Resolución de tenant en URL pública (`/t/:slug` o subdominio)

## Pasos (hazlos en orden)

### 1. Lectura (30 min)

Relee [producto-saas](../../../producto-saas.md) — sección MVP menú.

### 2. Matriz (25 min)

En `memoria/menu-por-tenant.md`: create/update/list ítems × tenant A/B.

### 3. Verifica aislamiento (100–130 min)

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"
# crear ítem en A; intentar leerlo con TOKEN_B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B" "$API/menu/items/$ITEM_A"
```

Perfil público del tenant A no lista ítems de B.

### 4. Commit (15 min)

```bash
git add projects/m26-capstone/memoria/menu-por-tenant.md
git commit -m "docs(m26): l10 menu-por-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas + egreso | Menú aislado | [egreso](../../../egreso.md) |
| Catálogo | M26 | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

1. Menú CRUD por tenant con evidencia HTTP.
2. Perfil público A ≠ menú B.
3. Memoria en git.

## Errores comunes

- Menú global sin `tenant_id`.
- Soft-delete sin filtrar en el perfil público.

## Siguiente

[L11 — Staff y permisos mínimos](L11-staff-y-permisos-minimos.md)
