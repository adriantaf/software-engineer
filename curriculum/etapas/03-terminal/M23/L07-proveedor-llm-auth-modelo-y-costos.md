---
id: L07
materia: M23
orden: 7
titulo: Proveedor LLM — auth, modelo y costos
horas: 5
semana: 2
lectura: "Docs API LLM oficiales"
evidencia: "projects/m23-ia/llm-eval/proveedor.md"
---

# L07 — Proveedor LLM — auth, modelo y costos

**~5 h · Semana 2**

## Objetivo

Elegir proveedor, anotar modelo, límites rate, precio por 1k tokens, variables entorno.

## Por qué importa

Costos ignorados hasta factura es error común del plan.

## Conceptos

- API key.
- Modelo.
- Rate limit.
- Costo estimado.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/llm-eval/proveedor.md`: tabla comparativa si dudaste; decisión final con razón.

Plantilla `.env.example` sin secretos; claves solo en entorno local/staging.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l07 proveedor-llm-auth-modelo-y-costos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Pricing + limits docs | ../../../como-estudiar.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. proveedor.md.
2. .env.example.
3. Sin secretos en git.

## Errores comunes

- Key en repo.
- Modelo sin límite tokens.

## Siguiente

[L08 — Primer script LLM y logs sin PII](L08-primer-script-llm-y-logs-sin-pii.md)
