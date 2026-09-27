---
id: L02
materia: M09
orden: 2
titulo: Entidades Categoría, Ítem y Pedido
horas: 5.0
semana: 1
lectura: "Elmasri: modelo ER — entidades y atributos"
evidencia: er-vitrina.md con menú/pedidos y atributos justificados
---

# L02 — Entidades Categoría, Ítem y Pedido

**~5.0 h · Semana 1**

El producto **Vitrina** gira en torno al menú (qué se vende) y al pedido (qué pidieron y en qué estado está).

## Objetivo

Completar el borrador de `er-vitrina.md` con entidades, atributos y un diagrama que puedas defender en voz alta.

## Conceptos

- **Entidad** vs **atributo** vs **relación**.
- Clave primaria estable (`uuid`) vs natural (teléfono — malo como PK).
- `tenant_id` como columna preparatoria (aún single-tenant).

## Pasos

### 1. Lectura dirigida (45–60 min)

En Elmasri, secciones de entidades/atributos/tipos de entidad. Anota 5 términos en `glosario.md` o al final de `er-vitrina.md`.

### 2. Contrasta con el SQL ya aplicado (30 min)

```bash
psql "..." -c '\d menu_categories'
psql "..." -c '\d menu_items'
psql "..." -c '\d orders'
psql "..." -c '\d order_items'
```

Lista en `er-vitrina.md` qué columnas ya existen y si faltan atributos de negocio (ej. `descripcion`, foto URL).

### 3. Escribe atributos con justificación (90 min)

Para cada entidad: atributo → tipo → por qué lo necesitas el día 1. Ejemplo mínimo:

- MenuCategory: `nombre`, `orden`.
- MenuItem: `precio_centavos` (evita floats), `disponible`.
- Order: `canal`, `pago`, `estado`.
- OrderItem: `cantidad`, `precio_unit_centavos`, `nombre_snapshot`.

### 4. Diagrama (45 min)

Actualiza el bloque Mermaid de `er-vitrina.md` (o exporta PNG y enlázalo). Menú y pedidos deben aparecer.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos/er-vitrina.md
git commit -m "docs(m09): entidades menu pedidos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: modelo ER — entidades y atributos | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `er-vitrina.md` describe categorías, ítems, pedidos y líneas con atributos y tipos.
2. El diagrama Mermaid (o equivalente) refleja ese dominio.
3. Commit `docs(m09): entidades menu pedidos`.

## Errores comunes

- Modelar “cita/horario” en lugar de menú + pedido.
- Mezclar “Usuario staff” con “Customer” del local.
- ER bonito sin relación con las tablas de `001_init.sql`.

## Siguiente

[L03 — Cardinalidades y reglas de negocio](L03-cardinalidades-y-reglas-de-negocio.md)
