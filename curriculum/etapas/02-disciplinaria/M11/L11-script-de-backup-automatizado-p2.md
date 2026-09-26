---
id: L11
materia: M11
orden: 11
titulo: Script de backup automatizado (P2)
horas: 5
semana: 3
lectura: "Silberschatz I/O + bash strict"
evidencia: "projects/m11-so/scripts/backup.sh"
---

# L11 — Script de backup automatizado (P2)

**~5 h · Semana 3**

## Objetivo

Escribir backup con `set -euo pipefail` y variables de entorno (sin secretos en repo).

## Por qué importa

Sin backup probado, el piloto no es serio.

## Conceptos

- pipefail.
- RETENTION.
- pg_dump o equivalente simulado.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa `scripts/backup.sh` y doc de variables. Simula dump a archivo si no hay DB.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l11 script-de-backup-automatizado-p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | I/O | bash manual |

## Hecho cuando

1. Script versionado.
2. Ejecución exitosa logueada.
3. Secretos fuera del repo.

## Errores comunes

- Hardcode DATABASE_URL.
- Backup en mismo disco sin copia offsite (anótalo).

## Siguiente

[L12 — Rotación de logs y restore de prueba](L12-rotacion-de-logs-y-restore-de-prueba.md)
