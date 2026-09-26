---
id: L10
materia: M24
orden: 10
titulo: Flujo mínimo demostrable
horas: 5
semana: 3
lectura: "API reference secciones usadas en el spike"
evidencia: "projects/m24-emergentes/spike/ + demo-log.md"
---

# L10 — Flujo mínimo demostrable

**~5 h · Semana 3**

## Objetivo

Implementar un flujo que un mentor pueda ver en ≤10 min (webhook, evento UI, mensaje test, etc.).

## Por qué importa

P3 exige PoC, no repositorio vacío con intenciones.

## Conceptos

- Happy path
- Idempotencia básica
- Logs sin PII

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa el happy path del plan. Registra en `spike/demo-log.md` pasos + capturas o salida terminal.

Si usas webhooks: verifica firma o documenta TODO explícito.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l10 flujo-minimo-demostrable"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | API usada en spike | threat-sketch |

## Hecho cuando

1. Flujo demo reproducible.
2. demo-log.md con pasos.

## Errores comunes

- Demo solo en tu máquina sin instrucciones.
- PII real en prueba.

## Siguiente

[L11 — Medición contra la hipótesis](L11-medicion-contra-la-hipotesis.md)
