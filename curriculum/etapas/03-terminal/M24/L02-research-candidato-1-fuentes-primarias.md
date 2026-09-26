---
id: L02
materia: M24
orden: 2
titulo: Research candidato 1 — fuentes primarias
horas: 5
semana: 1
lectura: "Documentación oficial del candidato 1 (pricing + límites)"
evidencia: "projects/m24-emergentes/research/candidato-1.md"
---

# L02 — Research candidato 1 — fuentes primarias

**~5 h · Semana 1**

## Objetivo

Documentar candidato 1 con enlaces oficiales, pricing, regiones, rate limits y al menos una limitación crítica.

## Por qué importa

Sin docs del vendor no puedes puntuar seguridad ni costo en la matriz.

## Conceptos

- Rate limits
- Webhook security
- Vendor lock-in

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa `projects/m24-emergentes/research/candidato-1.md` con secciones: **Problema**, **Docs**, **Precio**, **Límites**, **Seguridad (secretos/webhooks)**, **Crítica**.

Incluye ≥5 bullets accionables y ≥2 URLs oficiales (no blogs).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l02 research-candidato-1-fuentes-primarias"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Docs oficiales candidato 1 | Changelog seguridad |

## Hecho cuando

1. candidato-1.md completo.
2. ≥1 limitación honesta citada.
3. Sin pegar API keys.

## Errores comunes

- Solo marketing del vendor.
- Omitir costo por conversación/mensaje.

## Siguiente

[L03 — Research candidatos 2 y 3](L03-research-candidatos-2-y-3.md)
