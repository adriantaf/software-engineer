---
id: L10
materia: M14
orden: 10
titulo: Command para acciones admin reversibles
horas: 5
semana: 3
lectura: "Refactoring.Guru Command (selecto)"
evidencia: "projects/m14-patrones/src/admin-command.ts"
---

# L10 — Command para acciones admin reversibles

**~5 h · Semana 3**

## Objetivo

Modelar una acción admin (p. ej. cancelar cita masiva) como Command con `ejecutar`/`deshacer` opcional.

## Por qué importa

Panel owner en Agenda Ops puede necesitar deshacer errores humanos.

## Conceptos

- Command.
- undo.
- invoker.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Un command con undo en memoria. Test ejecutar + deshacer restaura estado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l10 command-para-acciones-admin-reversibles"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Command | — |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. Command con test undo.
2. Sin mezclar con HTTP.
3. Nota límites (no transaccional DB aún).

## Errores comunes

- Command gigante con todo el CRUD.
- Undo sin prueba.

## Siguiente

[L11 — Cierre P1 — Strategy, Observer y Factory](L11-cierre-p1-strategy-observer-y-factory.md)
