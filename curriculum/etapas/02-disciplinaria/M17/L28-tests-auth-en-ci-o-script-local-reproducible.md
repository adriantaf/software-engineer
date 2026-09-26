---
id: L28
materia: M17
orden: 28
titulo: Tests auth en CI o script local reproducible
horas: 5
semana: 7
lectura: "m15 pipeline"
evidencia: ".github/workflows en m17"
---

# L28 — Tests auth en CI o script local reproducible

**~5 h · Semana 7**

## Objetivo

Asegurar que suite auth+roles corre en CI o script documentado `npm run test:ci`.

## Por qué importa

Deploy sin tests es regresión garantizada.

## Conceptos

- CI.
- regresión.
- auth tests.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Enlaza workflow desde README m17. Verde en main.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l28 tests-auth-en-ci-o-script-local-reproduc"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m15 | nota cierre | — |

## Hecho cuando

1. CI verde.
2. Auth en pipeline.
3. Cierre semana 7.

## Errores comunes

- Tests skipped en CI.
- Solo local.

## Siguiente

[L29 — ADR tenant_id y modelo multi-negocio](L29-adr-tenant-id-y-modelo-multi-negocio.md)
