---
id: L09
materia: M11
orden: 9
titulo: "Sistema de archivos: inodos y espacio"
horas: 5.0
semana: 3
lectura: Silberschatz sistema de archivos
evidencia: labs/semana-03-fs.md
---

# L09 — Sistema de archivos: inodos y espacio

**~5.0 h · Semana 3**

Backups y logs viven en disco. Hoy mides espacio e inodos.

## Objetivo

Diagnosticar uso de disco como operador del piloto.

## Pasos

### 1. Medición (45 min)

```bash
df -h
df -i
du -sh projects/* 2>/dev/null | sort -h
```

### 2. Conceptos (45 min)

Inodo vs nombre de archivo; hardlink vs symlink (una tabla). Qué pasa con muchas fotos/tmp de pedidos.

### 3. Política (30 min)

Dónde vivirían backups y logs de Vitrina; cuota mínima libre antes de alerta.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-03-fs.md
git commit -m "docs(m11): l09 filesystem inodos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Inodos, enlaces, df/du; quedarse sin inodos vs sin bloques | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-03-fs.md` con `df -h`, `df -i`, `du -sh` anotados.
2. Explicas diferencia “disco lleno” vs “sin inodos”.
3. Commit `docs(m11): l09 filesystem inodos`.

## Errores comunes

- Borrar logs a ciegas en prod.
- Llenar disco con dumps de BD sin rotación.
- Ignorar tamaño de `node_modules`/imágenes Docker.

## Siguiente

[L10 — Permisos, usuarios y mínimo privilegio](L10-permisos-usuarios-y-minimo-privilegio.md)
