---
id: L12
materia: M22
orden: 12
titulo: Pricing Free/Pro — borrador defendible
horas: 5
semana: 3
lectura: "producto-saas + límites técnicos"
evidencia: "projects/m22-bektor/pricing.md"
---

# L12 — Pricing Free/Pro — borrador defendible

**~5 h · Semana 3**

## Objetivo

Cerrar borrador Free/Pro MXN con límites (calendarios, citas/mes, staff) alineados al código actual.

## Por qué importa

P3 exige coherencia técnica; pricing que rompe el producto es deuda comercial.

## Conceptos

- Free tier.
- Pro tier.
- Límites.
- Upgrade path M26.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa `projects/m22-bektor/pricing.md`: tabla planes, límites, qué pasa al exceder, política trial 14 días.

Párrafo **Por qué estos números** (costo hosting, tiempo ahorrado, comparativa local).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l12 pricing-free-pro-borrador-defendible"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../../producto-saas.md | ../M26-proyecto-integrador.md Stripe |

## Hecho cuando

1. Free/Pro completos.
2. Límites técnicos.
3. Justificación breve.

## Errores comunes

- Pro ‘contactar’ sin cifra.
- Free ilimitado imposible.

## Siguiente

[L13 — Métricas accionables — tablero de trials](L13-metricas-accionables-tablero-de-trials.md)
