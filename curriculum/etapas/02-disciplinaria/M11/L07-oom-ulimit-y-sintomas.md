---
id: L07
materia: M11
orden: 7
titulo: OOM, ulimit y síntomas
horas: 5.0
semana: 2
lectura: Silberschatz OOM + ulimit man
evidencia: labs/oom-ulimit.md
---

# L07 — OOM, ulimit y síntomas

**~5.0 h · Semana 2**

Cuando el kernel mata tu API, el síntoma parece “se reinició solo”. Hoy lo reconoces.

## Objetivo

Documentar límites (`ulimit`) y la firma de un OOM.

## Pasos

### 1. ulimit (30 min)

```bash
ulimit -a
ulimit -n
```

Anota open files y qué pasaría si la API abre demasiados sockets.

### 2. Señales OOM (60 min)

En `labs/oom-ulimit.md` documenta (sin tumbar el host):

- exit code 137 (128+9 SIGKILL) en contenedores
- `dmesg | grep -i oom` (si tienes permiso)
- restart loops en compose

### 3. Runbook corto (40 min)

Pasos si Agenda Ops cae por memoria: mirar RSS, logs PG, bajar concurrency, subir RAM o limitar cgroup.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/oom-ulimit.md
git commit -m "docs(m11): l07 oom ulimit"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | OOM killer; ulimit -n/-v; síntomas en logs | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/oom-ulimit.md` con `ulimit -a` anotado y escenarios OOM.
2. Lista de síntomas (exit 137, dmesg OOM, contenedor reiniciando).
3. Commit `docs(m11): l07 oom ulimit`.

## Errores comunes

- Forzar OOM en máquina compartida sin cuidado.
- Ignorar file descriptors (`ulimit -n`) en APIs con muchas conexiones.
- Culpar “Node lento” cuando es thrashing.

## Siguiente

[L08 — cgroups y memoria en contenedores](L08-cgroups-y-memoria-en-contenedores.md)
