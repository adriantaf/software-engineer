---
id: L08
materia: M11
orden: 8
titulo: cgroups y memoria en contenedores
horas: 5.0
semana: 2
lectura: Docker docs memory + Silberschatz resumen
evidencia: labs/cgroups-nota.md
---

# L08 — cgroups y memoria en contenedores

**~5.0 h · Semana 2**

Docker no “aisla magia”: usa cgroups. Hoy lo conectas con OOM de contenedor.

## Objetivo

Explicar límites de memoria en contenedores con un experimento o procedimiento escrito.

## Pasos

### 1. Lectura (40 min)

Docker memory constraints + idea de cgroup v1/v2 (alto nivel). Notas en `labs/cgroups-nota.md`.

### 2. Experimento (60–75 min)

Si tienes Docker:

```bash
docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0 || true
```

Documenta el fallo. Si no hay Docker: deja el comando y describe el resultado esperado + plan de verificación en L13.

### 3. Diseño piloto (30 min)

Propón límites tentativos API vs Postgres en un VPS 2 GB.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/cgroups-nota.md
git commit -m "docs(m11): l08 cgroups memoria"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | cgroups memoria/CPU; docker run -m; por qué el límite no es “RAM del host” | [Docker · Memory constraints](https://docs.docker.com/config/containers/resource_constraints/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cgroups-nota.md` explica límite `-m`/`mem_limit` y qué ve el proceso.
2. Experimento documentado con `docker run --memory` (o nota si Docker no está disponible + comandos listos).
3. Commit `docs(m11): l08 cgroups memoria`.

## Errores comunes

- Contenedor sin límite en un VPS pequeño compartiendo con Postgres.
- Confundir límite soft/hard.
- Pensar que cgroup “arregla leaks”.

## Siguiente

[L09 — Sistema de archivos: inodos y espacio](L09-sistema-de-archivos-inodos-y-espacio.md)
