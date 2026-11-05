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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `migrations/` reproducible: 001 + 002 (y notas de 003
      para L19).


      El esquema es código. Si no está en git con orden, no existe.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige convención
    xp: 10
    cuerpo: |-
      ```bash
      docker compose down -v   # ¡borra volumen local de evidencia!
      docker compose up -d
      # aplicar 001, 002, seeds
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Migraciones versionadas" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: migrations/ 001+002 aplicadas y documentadas
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

      `docker compose down -v   # ¡borra volumen local de evidencia!`
    comandoEsperado:
      - 'docker compose down -v   # ¡borra volumen local de evidencia!'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: docker compose down -v   # ¡borra volumen local de evidencia!'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Dejar `migrations/` reproducible: 001 + 002 (y notas de 003 para L19).'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Verifica idempotencia razonable
    xp: 10
    cuerpo: >-
      Reaplicar `001` no debe destruir datos (usamos `IF NOT EXISTS`). Prueba en
      una DB temporal o anota el riesgo.
  - id: s7
    tipo: ejemplo
    titulo: 3. Simula máquina limpia
    xp: 10
    cuerpo: |-
      ```bash
      docker compose down -v   # ¡borra volumen local de evidencia!
      docker compose up -d
      # aplicar 001, 002, seeds
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Al menos dos migraciones numeradas en git.
      - README explica cómo aplicarlas en orden en máquina limpia.
      - Commit si faltaba documentación.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
