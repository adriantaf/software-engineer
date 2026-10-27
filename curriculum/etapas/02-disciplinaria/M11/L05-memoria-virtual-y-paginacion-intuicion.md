---
id: L05
materia: M11
orden: 5
titulo: Memoria virtual y paginación (intuición)
horas: 5.0
semana: 2
lectura: Silberschatz — memoria virtual
evidencia: labs/semana-02-memoria.md
---

# L05 — Memoria virtual y paginación (intuición)

**~5.0 h · Semana 2**

OOM y lentitud empiezan cuando no entiendes qué es RSS. Hoy el modelo mental.

## Objetivo

Documentar memoria virtual/paginación a nivel operador.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/semana-02-memoria.md`: página, page fault (suave/duro), por qué un proceso “pide” más de la RAM física.

### 2. Host (40 min)

```bash
free -h
head -20 /proc/meminfo
```

Define MemAvailable vs swap used en tus palabras.

### 3. Producto (30 min)

Escenario: VPS 1 GB con API + Postgres. Qué síntomas verías antes del OOM killer.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-02-memoria.md
git commit -m "docs(m11): l05 memoria virtual"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Espacio virtual vs físico; páginas; swap/thrashing intuición | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-02-memoria.md` explica virtual vs RSS vs swap en lenguaje propio.
2. Comandos `free -h` / `/proc/meminfo` (o equivalente) anotados.
3. Commit `docs(m11): l05 memoria virtual`.

## Errores comunes

- Equivaler “memoria virtual” con “archivo swap” solamente.
- Diagramas copiados sin explicación.
- Ignorar qué pasa cuando el VPS de Vitrina thrashing-ea.

## Siguiente

[L06 — Observar RSS y CPU de Node](L06-observar-rss-y-cpu-de-node.md)
