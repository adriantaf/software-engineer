---
id: L17
materia: M09
orden: 17
titulo: Transacciones ACID
horas: 5.0
semana: 5
lectura: "Elmasri: transacciones ACID; PG BEGIN/COMMIT/ROLLBACK"
evidencia: sql/transaccion-pedido.sql
---

# L17 — Transacciones ACID

**~5.0 h · Semana 5**

Crear pedido sin auditoría (o al revés) es un bug de integridad. ACID lo evita.

## Objetivo

Entregar `sql/transaccion-pedido.sql` que inserta pedido + `cita_auditoria` atómicamente.

## Pasos

### 1. Lectura (45 min)

Propiedades ACID en Elmasri. Traduce cada letra con un ejemplo de pedidos.

### 2. Asegura tabla auditoría (30 min)

Aplica `migrations/002_auditoria_y_indices.sql` si no lo hiciste.

### 3. Script feliz (75 min)

```sql
BEGIN;
WITH nueva AS (
  INSERT INTO pedidos (cliente_id, servicio_id, inicia_en, termina_en, estado)
  VALUES (…, …, now() + interval '3 days', now() + interval '3 days 30 min', 'programada')
  RETURNING id
)
INSERT INTO cita_auditoria (cita_id, accion, detalle)
SELECT id, 'crear', jsonb_build_object('via', 'm09-l17') FROM nueva;
COMMIT;
```

### 4. Script de fallo (45 min)

Fuerza un error (FK inválida) dentro de `BEGIN` y verifica que no quedó basura (`ROLLBACK` implícito/ explícito).

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos/sql/transaccion-pedido.sql
git commit -m "feat(m09): transaccion pedido + auditoria"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: transacciones ACID; PG BEGIN/COMMIT/ROLLBACK | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Script con `BEGIN` que inserta pedido + fila de auditoría y `COMMIT`.
2. Demuestras un `ROLLBACK` (error forzado) dejando la BD consistente.
3. Commit del SQL.

## Errores comunes

- Dos statements sueltos sin transacción cuando deben ser atómicos.
- Auditar en la app “más tarde” y perder el enlace.
- Dejar transacciones abiertas en `psql`.

## Siguiente

[L18 — Migraciones versionadas](L18-migraciones-versionadas.md)
