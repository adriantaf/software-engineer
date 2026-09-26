---
id: L12
materia: M11
orden: 12
titulo: Rotación de logs y restore de prueba
horas: 5.0
semana: 3
lectura: logrotate concept + tu script de backup
evidencia: restore-prueba.md + script rotación
---

# L12 — Rotación de logs y restore de prueba

**~5.0 h · Semana 3**

Un backup no probado es un cuento. Hoy rotas y restauras.

## Objetivo

Cerrar P2 con rotación + `restore-prueba.md`.

## Pasos

### 1. Rotación (60 min)

`scripts/rotate-logs.sh`: mueve `logs/app.log` a `logs/app-$(date +%F).log` si supera N bytes; comprime; borra >RETENTION.

### 2. Restore de prueba (75–90 min)

```bash
# idea; ajusta a tu motor
# createdb agenda_restore_test
# gunzip -c backups/db-….sql.gz | psql agenda_restore_test
```

Documenta en `restore-prueba.md`: fecha, origen, destino, verificación (`SELECT count(*)` o equivalente en fixture).

### 3. README P2 (20 min)

Marca P2 listo con enlaces a scripts + restore.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "feat(m11): l12 rotacion y restore"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Rotación por tamaño/fecha; restore de backup a destino de prueba | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. Script de rotación de logs (o backups) en `scripts/`.
2. `restore-prueba.md` con fecha, comandos y resultado (aunque sea fixture).
3. Commit `feat(m11): l12 rotacion y restore`.

## Errores comunes

- Backup sin restore de prueba.
- Rotar borrando el único backup bueno.
- Restore sobre prod sin decirlo.

## Siguiente

[L13 — Imágenes, contenedores y volúmenes](L13-imagenes-contenedores-y-volumenes.md)
