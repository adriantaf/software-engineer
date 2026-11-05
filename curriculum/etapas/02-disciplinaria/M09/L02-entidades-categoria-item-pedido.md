---
id: L02
materia: M09
orden: 2
titulo: 'Entidades Categoría, Ítem y Pedido'
horas: 5
semana: 1
lectura: 'Elmasri: modelo ER — entidades y atributos'
evidencia: er-vitrina.md con menú/pedidos y atributos justificados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar el borrador de `er-vitrina.md` con entidades,
      atributos y un diagrama que puedas defender en voz alta.


      - **Entidad** vs **atributo** vs **relación**.

      - Clave primaria estable (`uuid`) vs natural (teléfono — malo como PK).

      - `tenant_id` como columna preparatoria (aún single-tenant).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura dirigida
    xp: 10
    cuerpo: |-
      ```bash
      psql "..." -c '\d menu_categories'
      psql "..." -c '\d menu_items'
      psql "..." -c '\d orders'
      psql "..." -c '\d order_items'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Entidades Categoría, Ítem y Pedido" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: er-vitrina.md con menú/pedidos y atributos justificados
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m09-bases-datos/er-vitrina.md`
    comandoEsperado:
      - git add projects/m09-bases-datos/er-vitrina.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m09-bases-datos/er-vitrina.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar el borrador de `er-vitrina.md` con entidades, atributos y un
          diagrama que puedas defender en voz alta.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Contrasta con el SQL ya aplicado
    xp: 10
    cuerpo: >-
      ```bash

      psql "..." -c '\d menu_categories'

      psql "..." -c '\d menu_items'

      psql "..." -c '\d orders'

      psql "..." -c '\d order_items'

      ```


      Lista en `er-vitrina.md` qué columnas ya existen y si faltan atributos de
      negocio (ej. `descripcion`, foto URL).
  - id: s7
    tipo: explicacion
    titulo: 3. Escribe atributos con justificación
    xp: 10
    cuerpo: >-
      Para cada entidad: atributo → tipo → por qué lo necesitas el día 1.
      Ejemplo mínimo:


      - MenuCategory: `nombre`, `orden`.

      - MenuItem: `precio_centavos` (evita floats), `disponible`.

      - Order: `canal`, `pago`, `estado`.

      - OrderItem: `cantidad`, `precio_unit_centavos`, `nombre_snapshot`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `er-vitrina.md` describe categorías, ítems, pedidos y líneas con
        atributos y tipos.
      - El diagrama Mermaid (o equivalente) refleja ese dominio.
      - 'Commit `docs(m09): entidades menu pedidos`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
