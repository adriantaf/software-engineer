---
id: L15
materia: M06
orden: 15
titulo: "Tests de borde: null, vacío, duplicados (P3)"
horas: 5
semana: 4
lectura: "Código limpio cap. 9 intro (pruebas); Vitest docs"
evidencia: "≥10 tests incluyendo null/undefined/vacío/duplicados; evidencia P3"
---

# L15 — Tests de borde: null, vacío, duplicados (P3)

**~5 h · Semana 4**

La práctica **P3** exige bordes: donde el software real falla en producción.

## Objetivo

Ampliar suite Vitest con casos null/undefined, colecciones vacías, IDs duplicados, strings vacíos; documentar matriz de bordes.

## Pasos

### 1. Matriz de bordes (45 min)

`tests/bordes.md`: filas = operación, columnas = null, vacío, duplicado, límite.

### 2. Implementación tests (150 min)

Mínimo **10 tests** nuevos o reforzados. Usa `it.each` si conviene.

### 3. Endurecer tipos (60 min)

Entrada inválida: rechazo temprano con Result err claro.

### 4. Regresión (30 min)

Corre suite completa ≥3 veces; flaky zero tolerance (investiga si falla intermitente).

### 5. Evidencia P3 (15 min)

Commit `test(m06): bordes P3 null vacio duplicados`.

Marca **P3** cuando la matriz y tests existan.

## Hecho cuando

1. Matriz cubierta por tests reales.
2. ≥10 casos de borde explícitos.
3. Suite verde estable.

## Errores comunes

- Solo happy path.
- Tests que no assertan mensaje/código de error.

## Siguiente

[L16 — Logging, diagnóstico y contratos de error](L16-logging-y-diagnostico.md)
