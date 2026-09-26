---
id: L07
materia: M25
orden: 7
titulo: Automatizar test cross-tenant en CI
horas: 5
semana: 2
lectura: "OWASP — Identity / Authorization testing"
evidencia: "test en repo producto + nota en projects/m25-ciber/aislamiento/tests.md"
---

# L07 — Automatizar test cross-tenant en CI

**~5 h · Semana 2**

## Objetivo

Al menos un test que falle si A lee cita de B.

## Por qué importa

Cosmética CSS no salva un leak entre barberías.

## Conceptos

- Authn vs authz
- tenant_id en sesión
- Tests de regresión

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Trabaja en **tu** Agenda Ops desplegado. Registra comandos `curl` o Vitest/Jest con tokens de A y B.

Actualiza `projects/m25-ciber/bitacora/semana-02.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l07 automatizar-test-cross-tenant-en-ci"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Access control testing | M18 IDOR |

## Hecho cuando

1. Evidencia en ruta indicada.
2. Si es test: corre en CI o documenta por qué no aún.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.

## Siguiente

[L08 — Cerrar ≥1 hallazgo crítico de aislamiento](L08-cerrar-1-hallazgo-critico-de-aislamiento.md)
