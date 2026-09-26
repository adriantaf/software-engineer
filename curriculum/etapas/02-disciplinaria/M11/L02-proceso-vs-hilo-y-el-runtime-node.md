---
id: L02
materia: M11
orden: 2
titulo: Proceso vs hilo y el runtime Node
horas: 5
semana: 1
lectura: "Silberschatz — hilos + documentación Node event loop"
evidencia: "labs/semana-01-procesos.md sección hilos"
---

# L02 — Proceso vs hilo y el runtime Node

**~5 h · Semana 1**

## Objetivo

Contrastar proceso OS con el modelo de concurrencia de Node (event loop, workers opcionales).

## Por qué importa

Confundir “Node es single-thread” con “una sola CPU” genera bugs de CPU y bloqueos.

## Conceptos

- Proceso pesado vs hilo ligero.
- Event loop.
- Worker threads (mención).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Diagrama: proceso `node` → un hilo principal → cola de callbacks. ¿Qué pasa con `fs.readFile`?

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l02 proceso-vs-hilo-y-el-runtime-node"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Hilos | Node.js event loop guide |

## Hecho cuando

1. Diagrama en bitácora.
2. Ejemplo I/O no bloqueante explicado.
3. Pregunta abierta para L03.

## Errores comunes

- Usar `while(true)` en handler HTTP.
- Confundir cluster con hilos OS.

## Siguiente

[L03 — Señales SIGTERM y apagado graceful](L03-senales-sigterm-y-apagado-graceful.md)
