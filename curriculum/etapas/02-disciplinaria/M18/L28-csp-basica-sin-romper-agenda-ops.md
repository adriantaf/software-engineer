---
id: L28
materia: M18
orden: 28
titulo: CSP básica sin romper Agenda Ops
horas: 5
semana: 7
lectura: "Content Security Policy Cheat Sheet"
evidencia: "projects/m18-appsec/csp.md + commit opcional"
---

# L28 — CSP básica sin romper Agenda Ops

**~5 h · Semana 7**

## Objetivo

Diseñar política CSP mínima (default-src, script-src) y desplegar en report-only o estricta según tolerancia.

## Por qué importa

CSP es red de seguridad ante XSS residual.

## Conceptos

- nonce vs hash.
- report-uri / report-to.
- inline scripts legacy.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m18-appsec/csp.md`: política propuesta, fuentes externas que usa tu front (CDN, analytics futuro).

Implementa CSP report-only primero; anota violaciones en consola.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l28 csp-basica-sin-romper-agenda-ops"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | CSP | MDN CSP |

## Hecho cuando

1. Política escrita.
2. Prueba report-only o estricta.
3. Sin romper build.

## Errores comunes

- `unsafe-inline` everywhere.
- CSP en meta sin HTTPS.

## Siguiente

[L29 — Pipeline CI: lint, test, audit, anti-secretos](L29-pipeline-ci-lint-test-audit-anti-secretos.md)
