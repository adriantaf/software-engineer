---
id: L20
materia: M09
orden: 20
titulo: Reportes, seeds y cierre M09
horas: 5.0
semana: 5
lectura: "Cierre: seeds + reportes de negocio"
evidencia: seeds + reportes.md + README — cierra proyecto M09
---

# L20 — Reportes, seeds y cierre M09

**~5.0 h · Semana 5**

Cierras el **proyecto** de la materia: esquema reproducible, seeds y reportes útiles.

## Objetivo

Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta esto”.

## Pasos

### 1. Seeds realistas (75 min)

Amplía `seeds/001_demo.sql`: ≥5 clientes, ≥3 servicios, citas en varios estados (`programada`, `completada`, `no_show`, `cancelada`). Reaplica en DB limpia o tras truncate controlado.

### 2. Dos reportes (75 min)

Completa `reportes.md`. Ideas:

1. No-shows de los últimos 30 días por cliente.
2. Ingresos estimados (centavos) por servicio en citas `completada`.

Cada uno: pregunta → archivo SQL → salida → uso para el dueño.

### 3. Checklist total (45 min)

P1 `er-agenda.md` · P2 `sql/` + `explain-notas.md` · P3 `migrations/` + `roles.md` · Proyecto seeds + reportes.

### 4. Simulación máquina limpia (45 min)

Sigue solo tu README (sin mirar las lecciones). Anota fricciones y arréglalas.

### 5. Commit de cierre (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): cierre materia seeds y reportes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Cierre: seeds + reportes de negocio | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `seeds/001_demo.sql` (o ampliado) aplica limpio.
2. `reportes.md` tiene ≥2 reportes con SQL + salida.
3. Otro dev podría recrear la BD solo con tu README (lo simulas tú).

## Errores comunes

- Reportes sin pregunta de negocio.
- Seeds con datos personales reales.
- Marcar el proyecto en la UI sin `reportes.md`.

## Siguiente

Cierra la [ficha M09](../M09-bases-de-datos.md). Siguiente materia disciplinaria según tu plan.
