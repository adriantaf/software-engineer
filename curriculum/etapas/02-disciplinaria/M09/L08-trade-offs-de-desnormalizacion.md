---
id: L08
materia: M09
orden: 8
titulo: Trade-offs de desnormalización
horas: 5.0
semana: 2
lectura: "Elmasri: desnormalización / diseño físico intro"
evidencia: "Nota en er-agenda.md: qué desnormalizarías y por qué"
---

# L08 — Trade-offs de desnormalización

**~5.0 h · Semana 2**

3FN no es religión: a veces el reporte del dueño necesita un snapshot. Hoy decides con criterio.

## Objetivo

Documentar **una** desnormalización consciente (implementada o aplazada) en `er-agenda.md`.

## Pasos

### 1. Lectura corta (30 min)

Secciones de diseño físico / desnormalización. Alternativa: notas PG sobre costos de JOIN vs almacenamiento.

### 2. Caso Agenda Ops (60 min)

Si el precio del “Corte” sube mañana, las citas completadas ayer ¿deben mostrar $150 o $180?

- Opción A: siempre JOIN a `servicios` (precio actual).
- Opción B: `citas.precio_centavos_snapshot` al crear la cita.

Elige y justifica en la sección L08 de `er-agenda.md`.

### 3. (Opcional) Migración (60–90 min)

Si eliges B:

```sql
ALTER TABLE citas
  ADD COLUMN IF NOT EXISTS precio_centavos_snapshot integer;
```

Versiona en `migrations/002_…` o un archivo nuevo numerado. Rellena snapshot en seeds después.

### 4. Regla de equipo (30 min)

Una frase en README: “Desnormalizamos X; la fuente de verdad de Y sigue siendo Z”.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): trade-off desnormalizacion precio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: desnormalización / diseño físico intro | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Escribes un trade-off concreto (ej. `precio_centavos_snapshot` en `citas`).
2. Listas costo (consistencia) vs beneficio (historial / reportes).
3. Decides para M09: ¿lo implementas en una migración o lo dejas documentado?

## Errores comunes

- Desnormalizar “por si acaso” sin query que lo pida.
- Copiar `nombre_cliente` a la cita sin decir cómo se actualiza.
- Confundir caché de lectura con modelo canónico.

## Siguiente

[L09 — Joins inner y left](L09-joins-inner-y-left.md)
