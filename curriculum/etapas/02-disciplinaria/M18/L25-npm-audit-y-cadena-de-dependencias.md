---
id: L25
materia: M18
orden: 25
titulo: npm audit y cadena de dependencias
horas: 5.0
semana: 7
lectura: OWASP A06 Vulnerable Components
evidencia: projects/m18-appsec/deps-audit.md
---

# L25 — npm audit y cadena de dependencias

**~5.0 h · Semana 7**

A06: componentes vulnerables.

## Objetivo

`npm audit` (o equivalente) corrido; severidades altas tratadas o aceptadas con justificación.

## Pasos (hazlos en orden)

### 1. Audit (40 min)

```bash
npm audit --json > projects/m18-appsec/docs/npm-audit.json || true
```

### 2. Triage (70–90 min)

Tabla: CVE, impacto en Agenda Ops, acción.

### 3. Commit

`docs(m18): l25 npm audit triage`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A06 Vulnerable Components | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Audit guardado (artefacto: `projects/m18-appsec/deps-audit.md`).
2. ≥1 acción tomada (artefacto: `projects/m18-appsec/deps-audit.md`).
3. Fecha en doc (artefacto: `projects/m18-appsec/deps-audit.md`).
4. Commit `docs(m18): L25 npm-audit-y-cadena-de-dependencias`.

## Errores comunes

- `npm audit fix --force` sin leer.
- Ignorar todo.

## Siguiente

[L26 — Secretos, .env y rotación](L26-secretos-env-y-rotacion.md)
