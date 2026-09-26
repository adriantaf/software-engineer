---
id: L06
materia: M24
orden: 6
titulo: Costo, operación y vendor lock-in
horas: 5
semana: 2
lectura: "Pricing pages + SLA del candidato elegido preliminar"
evidencia: "projects/m24-emergentes/matriz-adopcion.md sección Costo"
---

# L06 — Costo, operación y vendor lock-in

**~5 h · Semana 2**

## Objetivo

Estimar costo mensual a 10 / 100 tenants y documentar dependencia del vendor (migración, export).

## Por qué importa

Agenda Ops es SaaS; un canal de mensajería caro por conversación puede matar margen.

## Conceptos

- Costo marginal por tenant
- Exit strategy
- Fallback manual

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Actualiza la matriz con escenarios de costo (tabla tenants × mensajes/mes).

Para el candidato líder, escribe párrafo **Si el vendor sube precio 2×** en `matriz-adopcion.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l06 costo-operacion-y-vendor-lock-in"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Pricing oficial | Términos de datos |

## Hecho cuando

1. Escenarios de costo documentados.
2. Párrafo exit/lock-in.

## Errores comunes

- Costo ‘gratis’ sin leer tier de producción.
- No considerar tiempo de ingeniería.

## Siguiente

[L07 — Threat sketch del candidato para spike](L07-threat-sketch-del-candidato-para-spike.md)
