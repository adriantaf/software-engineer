---
id: L04
materia: M14
orden: 4
titulo: Cierre semana 1 — creacionales y bitácora
horas: 5.0
semana: 1
lectura: Repaso Factory/Strategy; bitácora
evidencia: bitacora-semana-1.md + README índice parcial
---

# L04 — Cierre semana 1 — creacionales y bitácora

**~5.0 h · Semana 1**

Consolidas vocabulario creacional antes de estructurales.

## Objetivo

Bitácora + índice parcial; suite verde.

## Pasos (hazlos en orden)

### 1. Corre tests (20 min)

```bash
cd projects/m14-patrones && npm test
```

### 2. Bitácora (50–60 min)

Qué patrón aporta flexibilidad real; qué rechazaste.

### 3. README (40 min)

Tabla patrón → archivo → ADR.

### 4. Commit (15 min)

`docs(m14): cierre semana 1 creacionales`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Cierre creacionales: evidencias Strategy + Factory | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Bitácora semana 1 lista Strategy, Factory y rechazo de Singleton.
2. README enlaza `src/pricing`, `src/notify`, ADRs.
3. Commit `docs(m14): cierre semana 1 creacionales`.

## Errores comunes

- Bitácora sin rutas a archivos.
- Tests rotos dejados “para después”.
- ADR sin enlace desde README.

## Siguiente

[L05 — Adapter para API de calendario externo](L05-adapter-para-api-de-calendario-externo.md)
