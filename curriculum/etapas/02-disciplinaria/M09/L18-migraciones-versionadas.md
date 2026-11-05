---
id: L18
materia: M09
orden: 18
titulo: Migraciones versionadas
horas: 5
semana: 5
lectura: 'Práctica: migraciones en git; opcional herramienta (dbmate/flyway/prisma)'
evidencia: migrations/ 001+002 aplicadas y documentadas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El esquema es código. Si no está en git con orden, no existe.


      **Objetivo de esta lección:** Dejar `migrations/` reproducible: 001 + 002
      (y notas de 003 para L19).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige convención
    xp: 10
    cuerpo: |-
      ```bash
      docker compose down -v   # ¡borra volumen local de evidencia!
      docker compose up -d
      # aplicar 001, 002, seeds
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Verifica idempotencia razonable
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): migraciones versionadas reproducibles"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Migraciones versionadas», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Migraciones versionadas
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `docker compose down -v   # ¡borra volumen local de evidencia!`
    comandoEsperado:
      - 'docker compose down -v   # ¡borra volumen local de evidencia!'
      - docker compose up -d
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: docker compose down -v   # ¡borra volumen local de evidencia!'
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
        texto: 'Dejar `migrations/` reproducible: 001 + 002 (y notas de 003 para L19).'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Simula máquina limpia
    xp: 10
    cuerpo: >-
      Solo si puedes recrear seeds después. Si no quieres borrar, usa otro
      `POSTGRES_DB` / compose project name.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Al menos dos migraciones numeradas en git.
      - README explica cómo aplicarlas en orden en máquina limpia.
      - Commit si faltaba documentación.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Migraciones versionadas

**~5.0 h · Semana 5**

El esquema es código. Si no está en git con orden, no existe.

## Objetivo

Dejar `migrations/` reproducible: 001 + 002 (y notas de 003 para L19).

## Pasos

### 1. Elige convención (30 min)

Ya tienes numeración `001_`, `002_`. Documenta en `migrations/README.md` si más adelante usarás dbmate/flyway/prisma — **no hace falta migrar la herramienta hoy**.

### 2. Verifica idempotencia razonable (60 min)

Reaplicar `001` no debe destruir datos (usamos `IF NOT EXISTS`). Prueba en una DB temporal o anota el riesgo.

### 3. Simula máquina limpia (90 min)

```bash
docker compose down -v   # ¡borra volumen local de evidencia!
docker compose up -d
# aplicar 001, 002, seeds
```

Solo si puedes recrear seeds después. Si no quieres borrar, usa otro `POSTGRES_DB` / compose project name.

### 4. README “desde cero” (45 min)

Lista ordenada de comandos en el README principal.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): migraciones versionadas reproducibles"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Práctica: migraciones en git; opcional herramienta (dbmate/flyway/prisma) | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Al menos dos migraciones numeradas en git.
2. README explica cómo aplicarlas en orden en máquina limpia.
3. Commit si faltaba documentación.

## Errores comunes

- Cambiar `001_init.sql` ya aplicado en prod/compañero sin nueva migración.
- Migraciones solo en la cabeza / en un GUI.
- Orden no determinista de archivos.

## Siguiente

[L19 — Least privilege (P3)](L19-least-privilege-p3.md)
