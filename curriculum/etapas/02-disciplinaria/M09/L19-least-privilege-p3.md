---
id: L19
materia: M09
orden: 19
titulo: Least privilege (P3)
horas: 5
semana: 5
lectura: 'PG: roles / GRANT; Elmasri seguridad intro'
evidencia: roles.md + 003_roles_app.sql — cierra P3
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aplicar `migrations/003_roles_app.sql` (ajustando password
      local) y completar `roles.md`.


      El hilo de seguridad empieza aquí: la app no es dueña del clúster.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```bash
      psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina" \
        -c 'SELECT count(*) FROM pedidos;'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Least privilege (P3)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: roles.md + 003_roles_app.sql — cierra P3
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
      ¿Es buena práctica en esta lección? “App y migraciones con el mismo
      superuser."
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
          Aplicar `migrations/003_roles_app.sql` (ajustando password local) y
          completar `roles.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ajusta y aplica 003
    xp: 10
    cuerpo: >-
      Edita la password del `CREATE ROLE` con tu `APP_DB_PASSWORD` **local**.
      Aplica el SQL.
  - id: s7
    tipo: ejemplo
    titulo: 3. Prueba positiva
    xp: 10
    cuerpo: |-
      ```bash
      psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina" \
        -c 'SELECT count(*) FROM pedidos;'
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe rol `agenda_app` (o equivalente) sin superuser.
      - Demuestras SELECT/INSERT OK y DDL denegado (error pegado en `roles.md`).
      - README marca P3 listo.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Least privilege (P3)

**~5.0 h · Semana 5**

El hilo de seguridad empieza aquí: la app no es dueña del clúster.

## Objetivo

Aplicar `migrations/003_roles_app.sql` (ajustando password local) y completar `roles.md`.

## Pasos

### 1. Lectura (40 min)

[PG privileges](https://www.postgresql.org/docs/current/ddl-priv.html) — GRANT/REVOKE básicos.

### 2. Ajusta y aplica 003 (45 min)

Edita la password del `CREATE ROLE` con tu `APP_DB_PASSWORD` **local**. Aplica el SQL.

### 3. Prueba positiva (40 min)

```bash
psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina" \
  -c 'SELECT count(*) FROM pedidos;'
```

### 4. Prueba negativa (40 min)

```sql
DROP TABLE pedidos;          -- debe fallar
CREATE TABLE hack(x int);  -- debe fallar
```

Pega el error en `roles.md`.

### 5. Commit (20 min) — sin secretos

```bash
git add projects/m09-bases-datos/roles.md projects/m09-bases-datos/migrations/003_roles_app.sql
git commit -m "feat(m09): rol agenda_app least privilege"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | PG: roles / GRANT; Elmasri seguridad intro | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe rol `agenda_app` (o equivalente) sin superuser.
2. Demuestras SELECT/INSERT OK y DDL denegado (error pegado en `roles.md`).
3. README marca P3 listo.

## Errores comunes

- App y migraciones con el mismo superuser.
- GRANT ALL TABLES TO PUBLIC.
- Password del rol app en el README.

## Siguiente

[L20 — Reportes, seeds y cierre M09](L20-reportes-seeds-y-cierre-m09.md)
