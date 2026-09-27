---
id: L05
materia: M17
orden: 5
titulo: Modelo de dominio pedidos, clientes y servicios
horas: 5.0
semana: 2
lectura: m13 diagrama clases + srs-v1
evidencia: migraciones / entidades
---

# L05 — Modelo de dominio pedidos, clientes y servicios

**~5.0 h · Semana 2**

CRUD sin modelo coherente genera IDOR y datos huérfanos.

## Objetivo

Alinear tablas y entidades con diseño M13: pedidos, clientes, servicios, relaciones y reglas en código dominio.

## Conceptos clave

- entidad
- migración
- dominio

## Pasos (hazlos en orden)

### 1. Cruza M13 + M09 (25–35 min)

```bash
ls projects/m13-diseno/diagramas projects/m09-bases-datos/migrations
rg -n "pedido|cliente|servicio" projects/m13-diseno projects/m12-srs 2>/dev/null | head
```

### 2. Migraciones dominio (70–90 min)

Asegura tablas `clientes`, `servicios`, `orders` con FKs (negocio/usuario según diseño).

```bash
npm run migrate
# o psql "$DATABASE_URL" -c '\dt'
```

Evidencia: listado de tablas en nota breve en `docs/` o salida en README (sin datos reales).

### 3. Reglas en domain/ (50–60 min)

```ts
// src/domain/pedido-rules.ts — puro, sin ORM
export function assertHorario(inicio: Date, fin: Date) {
  if (!(fin > inicio)) throw new Error("fin_debe_ser_despues_de_inicio");
}
```

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L05 modelo dominio pedidos clientes servicios"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m13 diagrama clases + srs-v1 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Migraciones aplicadas: tablas `clientes`, `servicios`, `orders` visibles.
2. Reglas puras en `projects/m17-vitrina/src/domain/` (o equivalente).
3. Commit `docs(m17): L05 modelo-de-dominio-pedidos-clientes-y-servicios`.

## Errores comunes

- Lógica de horario solo en controllers.
- Tablas sin FK a cliente/servicio.

## Siguiente

[L06 — API pedidos — crear y listar con reglas](L06-api-pedidos-crear-y-listar-con-reglas.md)
