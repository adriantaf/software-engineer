---
id: L13
materia: M25
orden: 13
titulo: Logging sin secretos ni PII innecesaria
horas: 5
semana: 4
lectura: "OWASP Error handling / logging"
evidencia: "projects/m25-ciber/logging/politica-logs.md"
---

# L13 — Logging sin secretos ni PII innecesaria

**~5 h · Semana 4**

## Objetivo

Auditar logs recientes; redactar campos; política breve.

## Por qué importa

Un atacante lee tus logs si exfiltras tokens; un cliente lee tus stack traces.

## Conceptos

- Structured logging
- Correlation id
- Fail closed

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Bitácora semana 4 en `projects/m25-ciber/bitacora/semana-04.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l13 logging-sin-secretos-ni-pii-innecesaria"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Logging cheat sheet | M19 runbook |

## Hecho cuando

1. Política o config documentada.
2. Ejemplo de log seguro vs inseguro.

## Errores comunes

- Loguear Authorization header.
- Alertas imposibles de actuar.

## Siguiente

[L14 — Rate limit login y abuso básico](L14-rate-limit-login-y-abuso-basico.md)
