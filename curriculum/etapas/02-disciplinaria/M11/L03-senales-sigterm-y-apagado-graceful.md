---
id: L03
materia: M11
orden: 3
titulo: Señales SIGTERM y apagado graceful
horas: 5
semana: 1
lectura: "Silberschatz — señales + Node process signals"
evidencia: "labs/sigterm-node.md"
---

# L03 — Señales SIGTERM y apagado graceful

**~5 h · Semana 1**

## Objetivo

Manejar `SIGTERM` en un script Node para cerrar servidor HTTP sin cortar requests a mitad.

## Por qué importa

En deploy (M19) el orquestador envía SIGTERM; ignorarla corrompe citas a medias.

## Conceptos

- SIGTERM vs SIGKILL.
- Graceful shutdown.
- Timeouts de cierre.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Script mínimo `http.createServer` + handler SIGTERM que cierra con timeout 10s. Prueba con `kill -TERM`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l03 senales-sigterm-y-apagado-graceful"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Señales | Node process.on('SIGTERM') |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Servidor cierra ordenadamente.
2. Log de señal guardado.
3. Diferencia TERM/KILL escrita.

## Errores comunes

- Solo SIGKILL en producción.
- No cerrar pool DB en shutdown.

## Siguiente

[L04 — Cierre semana 1 — práctica P1](L04-cierre-semana-1-practica-p1.md)
