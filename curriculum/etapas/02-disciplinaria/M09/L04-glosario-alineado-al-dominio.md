---
id: L04
materia: M09
orden: 4
titulo: Glosario alineado al dominio
horas: 5.0
semana: 1
lectura: "Elmasri: diseño conceptual — vocabulario del dominio"
evidencia: glosario.md completo + README enlaza P1 parcial
---

# L04 — Glosario alineado al dominio

**~5.0 h · Semana 1**

Si el equipo dice “cliente” y uno piensa en el tenant SaaS, el esquema se rompe en M17. Hoy cierras vocabulario.

## Objetivo

Dejar `glosario.md` usable por alguien que no leyó Elmasri, alineado a Agenda Ops y a tu ER.

## Pasos

### 1. Lee producto (30 min)

Revisa `curriculum/producto-saas.md` (ICP, citas, tenant). Marca 5 palabras que ya usas distinto.

### 2. Completa el glosario (90 min)

Abre `projects/m09-bases-datos/glosario.md`. Amplía a ≥8 filas. Obligatorio cubrir: Cliente, Servicio, Cita, Tenant, No-show, Migración, Seed, Least privilege.

### 3. Cruza con el ER (45 min)

Cada término de entidad del glosario debe existir en `er-agenda.md`. Si sobra un término huérfano, elimínalo o modela la entidad.

### 4. README de evidencia (30 min)

En `projects/m09-bases-datos/README.md`, sección corta “Semana 1” con enlaces a `er-agenda.md` y `glosario.md`.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): glosario dominio agenda ops"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: diseño conceptual — vocabulario del dominio | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `glosario.md` tiene ≥8 términos con “no confundir con”.
2. El README de m09 enlaza `er-agenda.md` y `glosario.md`.
3. Commit de cierre de semana 1.

## Errores comunes

- Usar “usuario” para todo (staff, cliente, tenant).
- Glosario copiado de Wikipedia sin el producto.
- Términos que no aparecen en el ER.

## Siguiente

[L05 — Primera forma normal y anomalías](L05-primera-forma-normal-y-anomalias.md)
