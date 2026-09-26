---
id: L13
materia: M19
orden: 13
titulo: Backup automático PostgreSQL
horas: 5
semana: 4
lectura: "pg_dump + proveedor backups"
evidencia: "projects/m19-ops/backup.md"
---

# L13 — Backup automático PostgreSQL

**~5 h · Semana 4**

## Objetivo

Automatizar pg_dump o backup gestionado; retención y ubicación segura.

## Por qué importa

P3 sin backup es teatro.

## Conceptos

- pg_dump
- cron
- cifrado opcional

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

backup.md: script o procedimiento, frecuencia, dónde se guarda (sin credenciales).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l13 backup-automatico-postgresql"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| PostgreSQL | backup | Proveedor docs |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Procedimiento escrito.
2. Job programado o gestionado.
3. Tamaño estimado.

## Errores comunes

- Backup manual olvidado
- Dump en repo git

## Siguiente

[L14 — Prueba de restore en entorno aislado](L14-prueba-de-restore-en-entorno-aislado.md)
