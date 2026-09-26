---
id: L06
materia: M20
orden: 6
titulo: Pull-to-refresh y paginación simple
horas: 5
semana: 2
lectura: "Async refresh UX"
evidencia: "commit UI"
---

# L06 — Pull-to-refresh y paginación simple

**~5 h · Semana 2**

## Objetivo

Refrescar lista; soportar query page/limit si la API lo expone.

## Por qué importa

Dueño espera gesto natural en móvil.

## Conceptos

- refresh
- pagination

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Documenta comportamiento si API sin paginación (corte client-side temporal).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l06 pull-to-refresh-y-paginacion-simple"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docs | list refresh | — |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Refresh funciona
2. Sin crash lista vacía loading

## Errores comunes

- Refresh sin indicador
- Duplicar fetch infinito

## Siguiente

[L07 — Estados de carga en lista](L07-estados-de-carga-en-lista.md)
