---
id: L12
materia: M25
orden: 12
titulo: Backup y restore probado
horas: 5
semana: 3
lectura: "OWASP Configuration + Stripe webhooks docs"
evidencia: "projects/m25-ciber/hardening/restore-test.md"
---

# L12 — Backup y restore probado

**~5 h · Semana 3**

## Objetivo

Restore en entorno aislado; anotar tiempo y pasos.

## Por qué importa

Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

## Conceptos

- Stripe signature
- Secrets manager / env
- Restore ≠ backup

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Ejecuta checks reales (`curl -I`, `pg_restore`, etc.) y pega **salida redactada** en el archivo de evidencia.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l12 backup-y-restore-probado"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Stripe | Webhooks signing | M19 backup |
| Catálogo | Entrada M25 | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

1. Checklist ítem demostrado.
2. Sin valores de API keys.

## Errores comunes

- Solo checklist teórico.
- Restore nunca probado.

## Siguiente

[L13 — Logging sin secretos ni PII innecesaria](L13-logging-sin-secretos-ni-pii-innecesaria.md)
