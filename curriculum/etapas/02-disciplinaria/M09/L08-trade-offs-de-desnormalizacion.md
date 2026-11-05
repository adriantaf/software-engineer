---
id: L08
materia: M09
orden: 8
titulo: Trade-offs de desnormalización
horas: 5
semana: 2
lectura: 'Elmasri: desnormalización / diseño físico intro'
evidencia: 'Nota en er-vitrina.md: qué desnormalizarías y por qué'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar **una** desnormalización consciente (implementada
      o aplazada) en `er-vitrina.md`.


      3FN no es religión: a veces el reporte del dueño necesita un snapshot. Hoy
      decides con criterio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura corta
    xp: 10
    cuerpo: |-
      ```sql
      ALTER TABLE pedidos
        ADD COLUMN IF NOT EXISTS precio_centavos_snapshot integer;
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Trade-offs de desnormalización" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: 'Nota en er-vitrina.md: qué desnormalizarías y por qué'
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Desnormalizar “por si acaso” sin
      query que lo pida."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar **una** desnormalización consciente (implementada o
          aplazada) en `er-vitrina.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Caso Vitrina
    xp: 10
    cuerpo: >-
      Si el precio del “Corte” sube mañana, las pedidos completadas ayer ¿deben
      mostrar $150 o $180?


      - Opción A: siempre JOIN a `servicios` (precio actual).

      - Opción B: `pedidos.precio_centavos_snapshot` al crear la pedido.


      Elige y justifica en la sección L08 de `er-vitrina.md`.
  - id: s7
    tipo: ejemplo
    titulo: 3. (Opcional) Migración
    xp: 10
    cuerpo: |-
      ```sql
      ALTER TABLE pedidos
        ADD COLUMN IF NOT EXISTS precio_centavos_snapshot integer;
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Escribes un trade-off concreto (ej. `precio_centavos_snapshot` en
        `orders`).
      - Listas costo (consistencia) vs beneficio (historial / reportes).
      - >-
        Decides para M09: ¿lo implementas en una migración o lo dejas
        documentado?
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Trade-offs de desnormalización

**~5.0 h · Semana 2**

3FN no es religión: a veces el reporte del dueño necesita un snapshot. Hoy decides con criterio.

## Objetivo

Documentar **una** desnormalización consciente (implementada o aplazada) en `er-vitrina.md`.

## Pasos

### 1. Lectura corta (30 min)

Secciones de diseño físico / desnormalización. Alternativa: notas PG sobre costos de JOIN vs almacenamiento.

### 2. Caso Vitrina (60 min)

Si el precio del “Corte” sube mañana, las pedidos completadas ayer ¿deben mostrar $150 o $180?

- Opción A: siempre JOIN a `servicios` (precio actual).
- Opción B: `pedidos.precio_centavos_snapshot` al crear la pedido.

Elige y justifica en la sección L08 de `er-vitrina.md`.

### 3. (Opcional) Migración (60–90 min)

Si eliges B:

```sql
ALTER TABLE pedidos
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

1. Escribes un trade-off concreto (ej. `precio_centavos_snapshot` en `orders`).
2. Listas costo (consistencia) vs beneficio (historial / reportes).
3. Decides para M09: ¿lo implementas en una migración o lo dejas documentado?

## Errores comunes

- Desnormalizar “por si acaso” sin query que lo pida.
- Copiar `nombre_cliente` a la pedido sin decir cómo se actualiza.
- Confundir caché de lectura con modelo canónico.

## Siguiente

[L09 — Joins inner y left](L09-joins-inner-y-left.md)
