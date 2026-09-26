---
id: L21
materia: M22
orden: 21
titulo: Pricing final para M26 y trial operativo
horas: 5
semana: 6
lectura: "Stripe docs (preview) + pricing.md"
evidencia: "projects/m22-bektor/pricing.md final"
---

# L21 — Pricing final para M26 y trial operativo

**~5 h · Semana 6**

## Objetivo

Congelar pricing Free/Pro MXN para integración Stripe test en M26; checklist trial operativo.

## Por qué importa

Semana 6 cierra comercial de la materia con números estables.

## Conceptos

- Price freeze.
- Trial 14d.
- Límites.
- Handoff M26.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Marca `projects/m22-bektor/pricing.md` sección **Final M22** con fecha congelación.

Lista checklist trial: alta tenant, credenciales, soporte WhatsApp, activación medida.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l21 pricing-final-para-m26-y-trial-operativo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M26 | ../M26-proyecto-integrador.md | Stripe test mode |
| Catálogo | Entrada M22 | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

1. Pricing congelado fechado.
2. Checklist trial.
3. P3 listo para UI.

## Errores comunes

- Cambiar precio post-cierre sin nota.
- Trial sin proceso.

## Siguiente

[L22 — Síntesis comercial para backlog M21](L22-sintesis-comercial-para-backlog-m21.md)
