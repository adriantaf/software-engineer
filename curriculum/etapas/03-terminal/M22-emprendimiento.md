---
id: M22
titulo: Emprendimiento de negocios de software
etapa: terminal
orden: 22
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Oferta SaaS de UN solo producto (suscripción, no agencia)
  - id: p2
    titulo: 10 demos/trials a negocios reales documentadas
  - id: p3
    titulo: Pricing MXN (Free/Pro) + propuesta escrita
proyecto:
  id: proj
  titulo: Bektor pivoteado a Agenda Ops (SaaS)
---

# M22 — Emprendimiento de negocios de software

## Por qué existe

Bektor como “hacemos de todo digital” no cerró ventas repetibles. El plan pivota a **Agenda Ops**: suscripción mensual a software de citas y clientes para negocios de servicio en Ensenada y alrededores ([producto-saas](../../producto-saas.md)). M22 no es marketing abstracto: es **conversaciones reales** con dueños de barberías, clínicas o talleres, demos sobre el producto que ya desplegaste (M17–M19), aprendizaje documentado y pricing en MXN que puedas defender sin inventar.

El checkout Stripe en producción llega en M26; aquí vendes el **trial** y la propuesta de valor, no promesas de seguridad “nivel banco” sin el trabajo de M18/M25.

**En resumen:** vendes **suscripción SaaS**, no agencia: oferta clara, 10 demos reales y pricing MXN.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Articular en 60 segundos problema → producto → precio → siguiente paso (trial o segunda reunión).
2. Definir un ICP **único** (un sub-vertical) y mantenerlo durante la materia.
3. Ejecutar y documentar **10** demos o intentos de trial con negocios reales (aunque digan que no).
4. Redactar planes Free/Pro en MXN alineados con [producto-saas](../../producto-saas.md) y con lo que viste en el mercado local.
5. Capturar objeciones recurrentes y ajustar mensaje o producto (build-measure-learn).
6. Documentar el pivote Bektor → Agenda Ops como decisión de negocio, no solo rebranding.

## Cómo estudiar esta materia

- Lee *El método Lean Startup* (Eric Ries, ed. ES) según la tabla semanal; cada capítulo debe producir **una acción** (mensaje, lista de contactos, demo).
- Usa el piloto en **staging o prod** de M19; nunca demos con `localhost`.
- Registra cada conversación el mismo día en `projects/m22-bektor/demos/`.
- Pide siempre un siguiente paso concreto: trial de 14 días, segunda visita, introducción a otro dueño.
- Honestidad en bitácora: “no contestó” cuenta si hubo intento documentado; no inflates vanity metrics.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Oferta | 6–8 | Pitch, one-pager, landing borrador |
| Demos | 6–8 | Conversaciones reales |
| Pricing | 4–6 | Free/Pro escrito |
| Retro | 1 | Objeción más frecuente |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. `mkdir -p projects/m22-bektor/demos`.
2. Reescribe la oferta en **un párrafo** en `projects/m22-bektor/oferta-saas.md` (problema del dueño → Agenda Ops → suscripción, no “páginas web”).
3. Borrador de `projects/m22-bektor/pricing.md`: planes Free/Pro en MXN, límites (calendarios, citas/mes), qué incluye cada uno.
4. Lista 20 negocios del ICP en `projects/m22-bektor/outreach-lista.md` (nombre, contacto, por qué encajan).
5. Guion de demo de 5 minutos en `projects/m22-bektor/guion-demo-5min.md`: login → crear cita → WhatsApp link → cierre pidiendo trial.
6. Escribe `projects/m22-bektor/pivote-bektor-agenda-ops.md`: qué dejaste de vender y por qué.

## Ejemplo — estructura de ficha de demo

```markdown
# Demo 03 — Barbería [nombre], 2026-05-12

- **Contacto:** … · **Canal:** visita / WhatsApp / llamada
- **Mostrado:** staging URL, flujo cita, recordatorio manual
- **Objeción principal:** “Ya uso Excel”
- **Respuesta probada:** …
- **Siguiente paso:** trial desde el lunes / rechazó / follow-up 2026-05-19
- **Aprendizaje:** …
```

## Temario semanal

### Semana 1 — Visión y oferta (~20 h)

- Lean: visión, start, build-measure-learn aplicado a SaaS vertical.
- Pitch 60 s y one-pager (no folleto de agencia).
- ICP fijado por escrito; anti-patterns (marketplace, “hacemos apps a medida”).
- Alineación con MVP de [producto-saas](../../producto-saas.md).

### Semana 2 — Validated learning y guion (~20 h)

- Hipótesis: dolor (no-shows, doble reserva), solución mínima, métrica de éxito del trial.
- Guion demo + manejo de “no tengo tiempo”.
- Primeras 2–3 conversaciones (aunque sean exploratorias).
- Actualizar oferta según feedback.

### Semana 3 — Experimentos de pricing e ICP (~20 h)

- Tres hipótesis de precio o sub-vertical; cómo las invalidarías.
- Comparar con alternativas (libreta, Calendly genérico, WhatsApp solo).
- 2–3 demos adicionales documentadas.

### Semana 4 — Métricas accionables (~20 h)

- Trials iniciados, activación (≥1 cita en 7 días), no MRR ficticio sin pagos.
- Tablero simple en `projects/m22-bektor/metricas-trials.md`.
- 2–3 demos más; refinar pricing draft.

### Semana 5 — Acelerar outreach (~20 h)

- Lotes pequeños: 5 contactos por semana con seguimiento.
- Landing con precios (puede ser estática en el repo del producto); enlace en evidencia.
- Demos 6–9 documentadas.

### Semana 6 — Cierre comercial de la materia (~20 h)

- Demo 10 completada.
- Pricing Free/Pro final para M26 (Stripe test).
- Síntesis de objeciones y decisiones de producto para backlog M21.
- README de carpeta actualizado.

## Lecturas

Canon: *El método Lean Startup* — Eric Ries (ed. ES). Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos (por tema de tu ed.) | Práctica |
|--------|-------------------------------|----------|
| 1 | Visión / start / build-measure-learn | `oferta-saas.md` + pitch 60s |
| 2 | Validated learning | `guion-demo-5min.md` + ≥2 demos |
| 3 | Experimentación / pivote | 3 hipótesis en `pricing.md` o anexo |
| 4 | Medir (métricas accionables vs vanity) | `metricas-trials.md` |
| 5 | Acelerar / lotes pequeños | Demos 5–9 en `demos/` |
| 6 | Cierre: síntesis + pricing draft | 10 demos totales + pricing final |

**Regla:** cada capítulo → una conversación o demo real, no solo subrayado.

## Prácticas

1. **P1 — Oferta:** `projects/m22-bektor/oferta-saas.md` (un producto, suscripción; sin lista de “también hacemos logos”).
2. **P2 — 10 demos:** `projects/m22-bektor/demos/demo-01.md` … `demo-10.md` (o índice en `demos/README.md`).
3. **P3 — Pricing:** `projects/m22-bektor/pricing.md` con Free/Pro MXN, límites y justificación breve.

## Proyecto útil

**Bektor → Agenda Ops** documentado en `projects/m22-bektor/pivote-bektor-agenda-ops.md` más artefactos comerciales (oferta, pricing, métricas, demos). Enlaza la landing de precios del repo del producto cuando exista.

## Errores comunes

- Volver a vender proyectos a medida o “mantenimiento web”.
- Demos sin pedir trial o fecha de seguimiento.
- Prometer seguridad o disponibilidad sin runbook ni M18.
- Cambiar de ICP cada semana porque un contacto dijo otra cosa.
- Contar “envié WhatsApp” como demo sin conversación sobre el producto.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Oferta:** `projects/m22-bektor/oferta-saas.md`.
- **P2 — 10 demos:** `projects/m22-bektor/demos/` con 10 fichas o índice equivalente.
- **P3 — Pricing:** `projects/m22-bektor/pricing.md`.
- **Proyecto — Pivote:** `projects/m22-bektor/pivote-bektor-agenda-ops.md` + `projects/m22-bektor/README.md` actualizado.

## Criterios de dominio

- [ ] Pitch de 60 segundos de **SaaS** + pedir trial o siguiente reunión sin tartamudear el precio.
- [ ] 10 demos documentadas con aprendizaje distinto o objeción registrada (no copy-paste).
- [ ] Pricing MXN coherente con límites técnicos del producto actual.
- [ ] Puedes nombrar la objeción #1 y qué cambiaste (mensaje o producto) por ella.
- [ ] ICP único mantenido durante las 6 semanas.
