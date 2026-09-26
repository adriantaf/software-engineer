---
id: L22
materia: M17
orden: 22
titulo: Deploy staging en PaaS
horas: 5
semana: 6
lectura: "Docs PaaS elegido"
evidencia: "URL staging"
---

# L22 — Deploy staging en PaaS

**~5 h · Semana 6**

## Objetivo

Desplegar API+front o API primero en staging con build reproducible.

## Por qué importa

Piloto invisible no es piloto.

## Conceptos

- deploy.
- staging.
- build.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

URL en README. Proceso `docs/deploy.md` paso a paso.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l22 deploy-staging-en-paas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| PaaS | docs | m19 preview |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Staging URL.
2. deploy.md.
3. Build CI opcional.

## Errores comunes

- Deploy manual sin doc.
- Solo localhost.

## Siguiente

[L23 — HTTPS y health checks](L23-https-y-health-checks.md)
