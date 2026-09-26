---
id: L20
materia: M23
orden: 20
titulo: Test automatizado cross-tenant en CI
horas: 5
semana: 5
lectura: "Vitest/Jest en repo producto"
evidencia: "projects/m23-ia/rag/ci-evidencia.md"
---

# L20 — Test automatizado cross-tenant en CI

**~5 h · Semana 5**

## Objetivo

Automatizar al menos un test que falle si retrieval devuelve chunk de otro tenant.

## Por qué importa

Manual no escala; CI evita regresión antes de M26.

## Conceptos

- Test auto.
- Fixture dos tenants.
- CI verde.
- Regression.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/rag/ci-evidencia.md`: enlace workflow o comando local, commit SHA, salida test PASS.

Si aún no hay CI, script `npm test -- rag-isolation` documentado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l20 test-automatizado-cross-tenant-en-ci"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M15 | ../M15-vv-calidad.md | GitHub Actions |

## Hecho cuando

1. Test automatizado.
2. ci-evidencia.md.
3. Enlace commit.

## Errores comunes

- Solo test manual.
- Skip en CI.

## Siguiente

[L21 — Feature flag IA y alineación pricing M22](L21-feature-flag-ia-y-alineacion-pricing-m22.md)
