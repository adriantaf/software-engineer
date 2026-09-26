---
id: L21
materia: M17
orden: 21
titulo: Variables de entorno y secrets
horas: 5.0
semana: 6
lectura: 12-factor config
evidencia: projects/m17-agenda-ops/.env.example
---

# L21 — Variables de entorno y secrets

**~5.0 h · Semana 6**

Deploy seguro empieza por no commitear secretos.

## Objetivo

`.env.example` completo; validación de arranque si falta `DATABASE_URL`/`SESSION_SECRET`.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

Lista vars: DB, session, CORS origin, WhatsApp phone opcional.

### 2. Example + validación (70–90 min)

Fail-fast al boot con mensaje claro. Confirma `.gitignore` cubre `.env`.

### 3. Grep anti-secretos (20 min)

```bash
git ls-files | rg -i 'env|pem|secret' || true
```

### 4. Commit

`chore(m17): l21 env example y validacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | 12-factor config | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. .env.example (artefacto: `projects/m17-agenda-ops/.env.example`).
2. Validación arranque (artefacto: `projects/m17-agenda-ops/.env.example`).
3. Commit (artefacto: `projects/m17-agenda-ops/.env.example`).

## Errores comunes

- .env en git.
- Secrets en front.

## Siguiente

[L22 — Deploy staging en PaaS](L22-deploy-staging-en-paas.md)
