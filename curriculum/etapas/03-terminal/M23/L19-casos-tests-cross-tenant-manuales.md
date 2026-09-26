---
id: L19
materia: M23
orden: 19
titulo: Casos tests-cross-tenant manuales
horas: 5
semana: 5
lectura: "QA seguridad producto"
evidencia: "projects/m23-ia/rag/tests-cross-tenant.md"
---

# L19 — Casos tests-cross-tenant manuales

**~5 h · Semana 5**

## Objetivo

Documentar casos: tenant A pregunta política B → no chunks B en contexto/respuesta.

## Por qué importa

P3 y criterio egreso: evidencia reproducible de aislamiento.

## Conceptos

- Cross-tenant.
- Context dump.
- Assertion.
- Evidencia log.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/rag/tests-cross-tenant.md`: ≥4 casos, pasos, resultado esperado, evidencia (log CI o captura redacted).

Pregunta A sobre ‘política cancelación’ debe citar solo A.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l19 casos-tests-cross-tenant-manuales"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| SEC | ../../hilos/seguridad.md | ../M18-seguridad.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. ≥4 casos.
2. Evidencia adjunta/enlace.
3. Pasos reproducibles.

## Errores comunes

- Solo ‘parece ok’.
- Test sin tenant B ingestado.

## Siguiente

[L20 — Test automatizado cross-tenant en CI](L20-test-automatizado-cross-tenant-en-ci.md)
