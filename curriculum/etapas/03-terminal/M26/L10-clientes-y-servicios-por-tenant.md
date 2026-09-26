---
id: L10
materia: M26
orden: 10
titulo: Clientes y servicios por tenant
horas: 5.0
semana: 3
lectura: Modelo dominio Agenda Ops
evidencia: projects/m26-capstone/memoria/clientes-servicios.md
---

# L10 — Clientes y servicios por tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/clientes-servicios.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Clientes y servicios scoped por tenant con evidencia en repo + memoria.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Catálogo servicios
- Duración

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Modelo dominio Agenda Ops_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Modelo dominio en memoria (25–35 min)

En `projects/m26-capstone/memoria/clientes-servicios.md`: entidades Cliente y Servicio (campos, `tenant_id`, duración, precio).

### 3. CRUD scoped + prueba cross-tenant (100–130 min)

Crea cliente y servicio en A y en B. Verifica listados:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/clientes" | jq '[.[]|.id]'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/clientes" | jq '[.[]|.id]'
# sets disjuntos
```

Documenta endpoints y status de un GET cruzado.

### 4. Captura o nota UI (25–35 min)

Enlace a ruta UI o screenshot path en repo. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l10 clientes-y-servicios-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Modelo dominio Agenda Ops | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/clientes-servicios.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L11 — Staff y permisos mínimos](L11-staff-y-permisos-minimos.md)
