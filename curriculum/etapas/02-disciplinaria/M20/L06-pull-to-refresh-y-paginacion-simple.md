---
id: L06
materia: M20
orden: 6
titulo: Pull-to-refresh y paginación simple
horas: 5.0
semana: 2
lectura: Async refresh UX
evidencia: commit UI
---

# L06 — Pull-to-refresh y paginación simple

**~5.0 h · Semana 2**

El dueño tira hacia abajo para ver el día actualizado.

## Objetivo

Refresh gestual + paginación o “cargar más” si la API lo soporta.

## Pasos (hazlos en orden)

### 1. Refresh (50–60 min)

### 2. Paginación (60–80 min)

Si no hay cursor API: documenta límite y TODO.

### 3. Commit

`feat(m20): l06 refresh paginacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Async refresh UX | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Refresh funciona (artefacto: `commit UI`).
2. Sin crash lista vacía loading (artefacto: `commit UI`).
3. Commit `docs(m20): L06 pull-to-refresh-y-paginacion-simple`.

## Errores comunes

- Refresh sin indicador.
- Duplicar fetch infinito.

## Siguiente

[L07 — Estados de carga en lista](L07-estados-de-carga-en-lista.md)
