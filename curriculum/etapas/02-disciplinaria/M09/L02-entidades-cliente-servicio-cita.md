---
id: L02
materia: M09
orden: 2
titulo: Entidades Cliente, Servicio, Cita
horas: 5.0
semana: 1
lectura: "Elmasri: modelo ER — entidades y atributos"
evidencia: er-agenda.md con 3 entidades y atributos justificados
---

# L02 — Entidades Cliente, Servicio, Cita

**~5.0 h · Semana 1**

El producto Agenda Ops gira en torno a tres hechos: quién reserva, qué se ofrece y cuándo ocurre.

## Objetivo

Completar el borrador de `er-agenda.md` con entidades, atributos y un diagrama que puedas defender en voz alta.

## Conceptos

- **Entidad** vs **atributo** vs **relación**.
- Clave primaria estable (`uuid`) vs natural (teléfono — malo como PK).
- `tenant_id` como columna preparatoria (aún single-tenant).

## Pasos

### 1. Lectura dirigida (45–60 min)

En Elmasri, secciones de entidades/atributos/tipos de entidad. Anota 5 términos en `glosario.md` o al final de `er-agenda.md`.

### 2. Contrasta con el SQL ya aplicado (30 min)

```bash
psql "..." -c '\d clientes'
psql "..." -c '\d servicios'
psql "..." -c '\d citas'
```

Lista en `er-agenda.md` qué columnas ya existen y si faltan atributos de negocio (ej. `notas`).

### 3. Escribe atributos con justificación (90 min)

Para cada entidad: atributo → tipo → por qué lo necesitas el día 1. Ejemplo mínimo:

- Cliente: `nombre`, `telefono` (WhatsApp), `email` opcional.
- Servicio: `duracion_min`, `precio_centavos` (evita floats).
- Cita: `inicia_en`, `termina_en`, `estado`.

### 4. Diagrama (45 min)

Actualiza el bloque Mermaid de `er-agenda.md` (o exporta PNG y enlázalo). Las tres entidades deben aparecer.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos/er-agenda.md
git commit -m "docs(m09): entidades cliente servicio cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: modelo ER — entidades y atributos | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `er-agenda.md` describe Cliente, Servicio y Cita con atributos y tipos.
2. El diagrama Mermaid (o equivalente) refleja esas tres entidades.
3. Commit `docs(m09): entidades cliente servicio cita`.

## Errores comunes

- Mezclar “Usuario staff” con “Cliente” del salón.
- Poner precio solo en la cita y olvidar el catálogo de servicios.
- ER bonito sin relación con las tablas de `001_init.sql`.

## Siguiente

[L03 — Cardinalidades y reglas de negocio](L03-cardinalidades-y-reglas-de-negocio.md)
