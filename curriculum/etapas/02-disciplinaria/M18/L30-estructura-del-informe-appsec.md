---
id: L30
materia: M18
orden: 30
titulo: Estructura del informe AppSec
horas: 5
semana: 8
lectura: "Reporting + risk rating"
evidencia: "projects/m18-appsec/informe-appsec.md (borrador)"
---

# L30 — Estructura del informe AppSec

**~5 h · Semana 8**

## Objetivo

Redactar informe ejecutivo+técnico: alcance, metodología, hallazgos, mitigaciones, riesgo residual.

## Por qué importa

El proyecto único de M18 es comunicable a un design partner técnico.

## Conceptos

- Alcance staging/prod.
- CVSS lite (opcional).
- Residual risk honesto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Plantilla en `informe-appsec.md`: Resumen, Metodología (OWASP+STRIDE), Tabla hallazgos, Recomendaciones, Anexo tests.

Enlaza `findings-table.md` y threat-model-v1.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l30 estructura-del-informe-appsec"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | proyecto M18 | — |

## Hecho cuando

1. Borrador ≥4 secciones.
2. Enlaces internos.
3. Sin jerga vacía.

## Errores comunes

- Informe sin hallazgos reales.
- Copiar OWASP sin contexto.

## Siguiente

[L31 — Tests de regresión de seguridad (≥3)](L31-tests-de-regresion-de-seguridad-3.md)
