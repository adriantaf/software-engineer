---
id: L07
materia: M24
orden: 7
titulo: Threat sketch del candidato para spike
horas: 5
semana: 2
lectura: "Webhook security + secret management"
evidencia: "projects/m24-emergentes/spike/threat-sketch.md"
---

# L07 — Threat sketch del candidato para spike

**~5 h · Semana 2**

## Objetivo

Una página de amenazas del integración elegida: secretos, replay, PII en payloads, supply chain.

## Por qué importa

Emergente ≠ inseguro por defecto, pero sí suele traer webhooks y tokens nuevos.

## Conceptos

- Firma HMAC webhooks
- PII en mensajes
- Principio mínimo privilegio

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/spike/threat-sketch.md`: actores, datos que cruzan el límite, ≥5 amenazas, mitigaciones previstas en el spike.

Lista secretos nuevos (nombres, no valores) en tabla.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l07 threat-sketch-del-candidato-para-spike"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Webhook / API security notes | hilo seguridad |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. threat-sketch.md ≥1 página.
2. Secretos nombrados sin valores.

## Errores comunes

- Spike sin pensar en replay.
- Loguear payloads con teléfonos reales.

## Siguiente

[L08 — Plan del spike — hipótesis, alcance y éxito](L08-plan-del-spike-hipotesis-alcance-y-exito.md)
