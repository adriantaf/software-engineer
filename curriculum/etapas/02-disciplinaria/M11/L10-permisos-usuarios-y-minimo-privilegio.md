---
id: L10
materia: M11
orden: 10
titulo: Permisos, usuarios y mínimo privilegio
horas: 5.0
semana: 3
lectura: Silberschatz protección
evidencia: labs/permisos.md
---

# L10 — Permisos, usuarios y mínimo privilegio

**~5.0 h · Semana 3**

Least privilege en host es parte del [hilo de seguridad](../../../hilos/seguridad.md).

## Objetivo

Definir permisos para datos sensibles del piloto.

## Pasos

### 1. Lab (50 min)

```bash
mkdir -p projects/m11-so/samples/permisos-demo
echo 'fake-secret' > projects/m11-so/samples/permisos-demo/secret.env
chmod 600 projects/m11-so/samples/permisos-demo/secret.env
ls -la projects/m11-so/samples/permisos-demo
# secret.env es demo: no pongas secretos reales; añade samples/ al criterio de no-commit si hace falta
```

Asegura que `secret.env` **no** se commitea si contiene algo real — usa placeholder y `.gitignore` si es necesario. Mejor: documenta solo `ls -la` y borra el secreto.

### 2. Política (60 min)

En `labs/permisos.md`: owner del proceso API, grupo, modo de `backups/*.sql`, logs, claves TLS.

### 3. Commit (15 min)

```bash
git add projects/m11-so/labs/permisos.md
git commit -m "docs(m11): l10 permisos least privilege"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | chmod/chown, usuarios/grupos, least privilege en datos y logs | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/permisos.md` con árbol de permisos propuesto para `backups/`, `logs/`, `.env`.
2. Demostración local de archivo 600 vs intento de lectura con otro usuario (o explicación equivalente).
3. Commit `docs(m11): l10 permisos least privilege`.

## Errores comunes

- `chmod 777` otra vez.
- Meter el usuario de la app en grupo docker sin necesidad.
- Secretos con ACL abierta en el repo.

## Siguiente

[L11 — Script de backup automatizado (P2)](L11-script-de-backup-automatizado-p2.md)
