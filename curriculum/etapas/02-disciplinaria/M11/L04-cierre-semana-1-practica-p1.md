---
id: L04
materia: M11
orden: 4
titulo: Cierre semana 1 — práctica P1
horas: 5.0
semana: 1
lectura: Repaso Silberschatz procesos
evidencia: labs/semana-01-procesos.md consolidado (P1)
---

# L04 — Cierre semana 1 — práctica P1

**~5.0 h · Semana 1**

P1 es bitácora de procesos/señales/permisos. Hoy la dejas revisable.

## Objetivo

Consolidar semana 1 y actualizar el README.

## Pasos

### 1. Inventario (25 min)

```bash
find projects/m11-so -type f | sort
```

### 2. Consolida (90–110 min)

`semana-01-procesos.md` con secciones: dia1, proceso vs hilo, SIGTERM (enlace al código). Incluye 3 comandos “runbook” de diagnóstico.

### 3. README (40 min)

Checklist:

- [x] labs dia1
- [x] notas hilos/event loop
- [x] graceful-server + prueba

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): l04 cierre semana 1 p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Síntesis procesos/hilos/señales; checklist P1 parcial | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-01-procesos.md` unifica L01–L03 con comandos reproducibles.
2. README marca P1 parcial (procesos/señales).
3. Commit `docs(m11): l04 cierre semana 1 p1`.

## Errores comunes

- Labs sin comandos copiables.
- Código graceful sin nota de prueba.
- Checklist vacía.

## Siguiente

[L05 — Memoria virtual y paginación (intuición)](L05-memoria-virtual-y-paginacion-intuicion.md)
