---
id: L18
materia: M09
orden: 18
titulo: Migraciones versionadas
horas: 5.0
semana: 5
lectura: "Práctica: migraciones en git; opcional herramienta (dbmate/flyway/prisma)"
evidencia: migrations/ 001+002 aplicadas y documentadas
---

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
