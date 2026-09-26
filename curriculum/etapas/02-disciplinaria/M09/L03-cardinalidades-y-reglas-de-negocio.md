---
id: L03
materia: M09
orden: 3
titulo: Cardinalidades y reglas de negocio
horas: 5.0
semana: 1
lectura: "Elmasri: relaciones, cardinalidad, participación"
evidencia: er-agenda.md con cardinalidades + CHECK/estado documentados
---

# L03 — Cardinalidades y reglas de negocio

**~5.0 h · Semana 1**

Una FK sin regla de negocio es decoración. Hoy fijas cardinalidades y constraints que el dueño del salón entendería.

## Objetivo

Dejar en `er-agenda.md` las cardinalidades 1:N y un bloque de reglas verificables (algunas ya están en `001_init.sql`).

## Pasos

### 1. Lectura (45 min)

Cardinalidad mínima/máxima y participación total/parcial en Elmasri.

### 2. Escribe cardinalidades (40 min)

En `er-agenda.md`:

- Cliente **1** — **0..N** Citas
- Servicio **1** — **0..N** Citas
- Una Cita **exactamente 1** Cliente y **exactamente 1** Servicio (MVP)

Si más adelante quieres varios servicios por cita, documenta la tabla puente como *cambio futuro*, no lo inventes ya.

### 3. Reglas de negocio (90 min)

Completa una lista numerada. Mínimo:

1. `termina_en > inicia_en` (ya hay `CHECK`).
2. `estado ∈ {programada, confirmada, completada, cancelada, no_show}`.
3. Una regla tuya (ej. no solapar dos citas del mismo staff — si aún no hay staff, anótala como pendiente M17).

Verifica en SQL:

```sql
-- Debe fallar:
INSERT INTO citas (cliente_id, servicio_id, inicia_en, termina_en, estado)
SELECT id, (SELECT id FROM servicios LIMIT 1), now(), now() - interval '1 hour', 'programada'
FROM clientes LIMIT 1;
```

### 4. Participación (30 min)

¿Puede existir un cliente sin citas? (sí — parcial). ¿Una cita sin cliente? (no — total hacia cliente). Anótalo.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): cardinalidades y reglas de negocio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: relaciones, cardinalidad, participación | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Cardinalidades Cliente–Cita y Servicio–Cita escritas (1:N).
2. Al menos 3 reglas de negocio (estados, `termina_en > inicia_en`, una más tuya).
3. Commit descriptivo.

## Errores comunes

- Dibujar N:M Cliente–Servicio sin tabla puente cuando el MVP es cita con un servicio.
- Reglas solo en la cabeza / en el front, nunca en ER ni en CHECK.
- Olvidar no-show como estado distinto de cancelada.

## Siguiente

[L04 — Glosario alineado al dominio](L04-glosario-alineado-al-dominio.md)
