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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El hilo de seguridad empieza aquí: la app no es dueña del clúster.


      **Objetivo de esta lección:** Aplicar `migrations/003_roles_app.sql`
      (ajustando password local) y completar `roles.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```sql
      DROP TABLE pedidos;          -- debe fallar
      CREATE TABLE hack(x int);  -- debe fallar
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Ajusta y aplica 003
    xp: 10
    cuerpo: |-
      ```bash
      psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina" \
        -c 'SELECT count(*) FROM pedidos;'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Least privilege (P3)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Least privilege (P3)
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina"
      \`
    comandoEsperado:
      - >-
        psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina"
        \
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: psql
      "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/vitrina" \
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Aplicar `migrations/003_roles_app.sql` (ajustando password local) y
          completar `roles.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Prueba positiva
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
