---
id: L31
materia: M18
orden: 31
titulo: Tests de regresión de seguridad (≥3)
horas: 5
semana: 8
lectura: "Security unit tests patterns"
evidencia: "≥3 tests en repo producto"
---

# L31 — Tests de regresión de seguridad (≥3)

**~5 h · Semana 8**

## Objetivo

Consolidar tests: authz cross-user, input malicioso, headers o rate limit — al menos tres automatizados.

## Por qué importa

Sin tests, el hardening se erosiona en el próximo feature.

## Conceptos

- Regression suite.
- CI los ejecuta.
- Nombres claros.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Lista tests en `projects/m18-appsec/security-tests.md` con archivo y qué protege.

Verifica que CI los corre. Añade uno si faltan.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l31 tests-de-regresion-de-seguridad-3"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18 proyecto | P2/P3 |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. ≥3 tests listados.
2. CI los ejecuta.
3. Todos verdes.

## Errores comunes

- Tests skipped.
- Solo manual.

## Siguiente

[L32 — Cierre M18 — dominio y riesgo residual](L32-cierre-m18-dominio-y-riesgo-residual.md)
