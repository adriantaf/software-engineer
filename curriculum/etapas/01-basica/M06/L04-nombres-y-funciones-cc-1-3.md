---
id: L04
materia: M06
orden: 4
titulo: Nombres y funciones pequeñas (CC 1–3)
horas: 5
semana: 1
lectura: "Código limpio caps. 1–3 completos"
evidencia: "Refactor de nombres + funciones ≤15 líneas; semana-0001 bitácora opcional"
---

# L04 — Nombres y funciones pequeñas (CC 1–3)

**~5 h · Semana 1**

Cierras la semana 1 puliendo legibilidad: nombres que revelan intención y funciones que caben en una pantalla.

## Objetivo

Aplicar CC 1–3 al código del dominio; registrar antes/después en notas para **P2** (refactor formal en L08).

## Pasos

### 1. Lectura CC 1–3 (60 min)

Subraya 10 reglas accionables. No decorativas.

### 2. Inventario de olores (45 min)

Lista: nombres ambiguos (`data`, `handle`, `process`), funciones largas, números mágicos.

### 3. Refactor mecánico (150 min)

- Renombra con IDE (tests verdes tras cada paso).
- Extrae funciones; sustituye magic numbers por constantes nombradas.
- Guarda `git diff` o captura en `refactor-notas.md` (**antes** snapshot: tag o commit `pre-refactor-semana1`).

### 4. Revisión entre pares (opcional, 30 min)

Si estudias solo, lee en voz alta el módulo principal; corrige lo que tropezó.

### 5. Commit (15 min)

```bash
git commit -am "refactor(m06): nombres y funciones pequeñas CC 1-3"
```

## Hecho cuando

1. No quedan funciones públicas >~20 líneas sin justificación documentada.
2. `refactor-notas.md` lista cambios principales.
3. Tests verdes.

## Errores comunes

- Renombrar sin correr tests.
- Abstracciones de una sola línea inútiles.

## Siguiente

[L05 — Interfaces y contratos de dominio](L05-interfaces-y-contratos.md)
