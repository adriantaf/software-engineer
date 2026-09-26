---
id: L23
materia: M17
orden: 23
titulo: HTTPS y health checks
horas: 5
semana: 6
lectura: "TLS Let's Encrypt / proveedor"
evidencia: "HTTPS + /health"
---

# L23 — HTTPS y health checks

**~5 h · Semana 6**

## Objetivo

Forzar HTTPS en prod/staging y health check para monitor.

## Por qué importa

Design partner no debe ver “no seguro”.

## Conceptos

- TLS.
- HSTS.
- health.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Verificar certificado válido. Health usado en deploy script.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l23 https-y-health-checks"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTPS | — |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. HTTPS activo.
2. Health remoto.
3. Commit.

## Errores comunes

- HTTP prod.
- Health sin DB check documentado.

## Siguiente

[L24 — Smoke test post-deploy](L24-smoke-test-post-deploy.md)
