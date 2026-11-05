---
id: L03
materia: M09
orden: 3
titulo: Cardinalidades y reglas de negocio
horas: 5
semana: 1
lectura: 'Elmasri: relaciones, cardinalidad, participación'
evidencia: er-vitrina.md con cardinalidades + CHECK/estado documentados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar en `er-vitrina.md` las cardinalidades 1:N y un bloque
      de reglas verificables (algunas ya están en `001_init.sql`).


      Una FK sin regla de negocio es decoración. Hoy fijas cardinalidades y
      constraints que el dueño del salón entendería.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```sql

      -- Debe fallar:

      INSERT INTO pedidos (cliente_id, servicio_id, inicia_en, termina_en,
      estado)

      SELECT id, (SELECT id FROM servicios LIMIT 1), now(), now() - interval '1
      hour', 'programada'

      FROM clientes LIMIT 1;

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cardinalidades y reglas de negocio" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: er-vitrina.md con cardinalidades + CHECK/estado documentados
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
      ¿Es buena práctica en esta lección? “Dibujar N:M Cliente–Servicio sin
      tabla puente cuando el MVP es pedido con un servicio."
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
          Dejar en `er-vitrina.md` las cardinalidades 1:N y un bloque de reglas
          verificables (algunas ya están en `001_init.sql`).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe cardinalidades
    xp: 10
    cuerpo: >-
      En `er-vitrina.md`:


      - Cliente **1** — **0..N** Pedidos

      - Servicio **1** — **0..N** Pedidos

      - Una Pedido **exactamente 1** Cliente y **exactamente 1** Servicio (MVP)


      Si más adelante quieres varios servicios por pedido, documenta la tabla
      puente como *cambio futuro*, no lo inventes ya.
  - id: s7
    tipo: ejemplo
    titulo: 3. Reglas de negocio
    xp: 10
    cuerpo: >-
      ```sql

      -- Debe fallar:

      INSERT INTO pedidos (cliente_id, servicio_id, inicia_en, termina_en,
      estado)

      SELECT id, (SELECT id FROM servicios LIMIT 1), now(), now() - interval '1
      hour', 'programada'

      FROM clientes LIMIT 1;

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Cardinalidades Cliente–Pedido y Servicio–Pedido escritas (1:N).'
      - >-
        Al menos 3 reglas de negocio (estados, `termina_en > inicia_en`, una más
        tuya).
      - Commit descriptivo.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Cardinalidades y reglas de negocio

**~5.0 h · Semana 1**

Una FK sin regla de negocio es decoración. Hoy fijas cardinalidades y constraints que el dueño del salón entendería.

## Objetivo

Dejar en `er-vitrina.md` las cardinalidades 1:N y un bloque de reglas verificables (algunas ya están en `001_init.sql`).

## Pasos

### 1. Lectura (45 min)

Cardinalidad mínima/máxima y participación total/parcial en Elmasri.

### 2. Escribe cardinalidades (40 min)

En `er-vitrina.md`:

- Cliente **1** — **0..N** Pedidos
- Servicio **1** — **0..N** Pedidos
- Una Pedido **exactamente 1** Cliente y **exactamente 1** Servicio (MVP)

Si más adelante quieres varios servicios por pedido, documenta la tabla puente como *cambio futuro*, no lo inventes ya.

### 3. Reglas de negocio (90 min)

Completa una lista numerada. Mínimo:

1. `termina_en > inicia_en` (ya hay `CHECK`).
2. `estado ∈ {programada, confirmada, completada, cancelada, no_show}`.
3. Una regla tuya (ej. no solapar dos pedidos del mismo staff — si aún no hay staff, anótala como pendiente M17).

Verifica en SQL:

```sql
-- Debe fallar:
INSERT INTO pedidos (cliente_id, servicio_id, inicia_en, termina_en, estado)
SELECT id, (SELECT id FROM servicios LIMIT 1), now(), now() - interval '1 hour', 'programada'
FROM clientes LIMIT 1;
```

### 4. Participación (30 min)

¿Puede existir un cliente sin pedidos? (sí — parcial). ¿Una pedido sin cliente? (no — total hacia cliente). Anótalo.

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

1. Cardinalidades Cliente–Pedido y Servicio–Pedido escritas (1:N).
2. Al menos 3 reglas de negocio (estados, `termina_en > inicia_en`, una más tuya).
3. Commit descriptivo.

## Errores comunes

- Dibujar N:M Cliente–Servicio sin tabla puente cuando el MVP es pedido con un servicio.
- Reglas solo en la cabeza / en el front, nunca en ER ni en CHECK.
- Olvidar pedido abandonado como estado distinto de cancelada.

## Siguiente

[L04 — Glosario alineado al dominio](L04-glosario-alineado-al-dominio.md)
