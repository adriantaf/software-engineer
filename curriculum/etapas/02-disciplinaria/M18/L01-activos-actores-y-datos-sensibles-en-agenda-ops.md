---
id: L01
materia: M18
orden: 1
titulo: Activos, actores y datos sensibles en Agenda Ops
horas: 5.0
semana: 1
lectura: OWASP Threat Modeling (overview) + notas STRIDE
evidencia: projects/m18-appsec/threat-model-v0.md sección Activos
---

# L01 — Activos, actores y datos sensibles en Agenda Ops

**~5.0 h · Semana 1**

Sin lista de activos, el threat model es decoración.

## Objetivo

Tablas de actores y ≥5 activos en `threat-model-v0.md` (PII, credenciales, citas, tokens, Postgres).

## Pasos (hazlos en orden)

### 1. Carpeta evidencia (15 min)

```bash
mkdir -p projects/m18-appsec/{pocs,fixes,tests,ci}
```

### 2. Actores y activos (80–100 min)

Dueño, staff, cliente final, atacante anónimo. Activos con clasificación (confidencialidad). Diagrama: navegador → API → Postgres.

### 3. Superficie JSON (30 min)

Marca qué campos salen en `/api/citas`. `git ls-files | rg -i 'env|secret|pem'`.

### 4. Commit

`docs(m18): l01 activos actores agenda ops`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Threat Modeling (overview) + notas STRIDE | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m18-appsec/threat-model-v0.md` con actores y ≥5 activos.
2. Diagrama ASCII o Mermaid del piloto (artefacto: `projects/m18-appsec/threat-model-v0.md sección Activos`).
3. Comando anti-secretos ejecutado y anotado (artefacto: `projects/m18-appsec/threat-model-v0.md sección Activos`).
4. Commit `docs(m18): L01 activos-actores-y-datos-sensibles-en-agenda-ops`.

## Errores comunes

- Activos genéricos (“la DB”) sin tablas/campos.
- Omitir al cliente final como fuente de datos.

## Siguiente

[L02 — Trust boundaries y flujos de confianza](L02-trust-boundaries-y-flujos-de-confianza.md)
