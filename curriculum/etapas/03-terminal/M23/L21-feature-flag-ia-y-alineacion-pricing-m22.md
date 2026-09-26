---
id: L21
materia: M23
orden: 21
titulo: Feature flag IA y alineación pricing M22
horas: 5
semana: 6
lectura: "Plan Pro limits + cost control"
evidencia: "projects/m23-ia/faq-asistente/plan-pro-ia.md"
---

# L21 — Feature flag IA y alineación pricing M22

**~5 h · Semana 6**

## Objetivo

Documentar flag o límite IA por plan Free/Pro coherente con pricing M22.

## Por qué importa

Vender IA ilimitada en Pro sin costeo tumba margen.

## Conceptos

- Feature flag.
- Cuota mensual.
- Upgrade.
- Free sin RAG.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/faq-asistente/plan-pro-ia.md`: tabla plan → cuotas tokens/preguntas.

Enlaza `projects/m22-bektor/pricing.md` con nota cruzada.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l21 feature-flag-ia-y-alineacion-pricing-m22"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M22 | projects/m22-bektor | ../../../producto-saas.md |

## Hecho cuando

1. plan-pro-ia.md.
2. Enlace pricing.
3. Cuotas numéricas.

## Errores comunes

- IA gratis ilimitada.
- Flag sin default seguro.

## Siguiente

[L22 — Costo mensual estimado por tenant activo](L22-costo-mensual-estimado-por-tenant-activo.md)
