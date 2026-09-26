---
id: L01
materia: M22
orden: 1
titulo: Lean Startup aplicado a Agenda Ops — carpeta y visión
horas: 5
semana: 1
lectura: "El método Lean Startup — visión, start, build-measure-learn"
evidencia: "projects/m22-bektor/demos + bitacora-m22.md"
---

# L01 — Lean Startup aplicado a Agenda Ops — carpeta y visión

**~5 h · Semana 1**

## Objetivo

Crear estructura comercial, leer visión/start/BML y escribir hipótesis de negocio SaaS (no agencia).

## Por qué importa

M22 vende **suscripción** al producto que construiste; Bektor como agencia no es el modelo del plan.

## Conceptos

- Visión vs estrategia.
- Build-measure-learn.
- SaaS vertical.
- Anti-patrón agencia.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m22-bektor/demos
```

Lee capítulos iniciales de *El método Lean Startup* (ed. ES). En `projects/m22-bektor/bitacora-m22.md`: visión en 5 líneas + ciclo BML aplicado a trials de Agenda Ops.

Lista 3 supuestos que **matarían** el negocio si fueran falsos.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l01 lean-startup-aplicado-a-agenda-ops-carpe"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ries | Lean Startup inicio | ../../../producto-saas.md |
| Ficha | ../M22-emprendimiento.md | ../../../como-estudiar.md |

## Hecho cuando

1. demos/ existe.
2. bitacora con BML.
3. 3 supuestos críticos.

## Errores comunes

- Volver a vender ‘páginas web’.
- Leer sin escribir acción.

## Siguiente

[L02 — ICP único — sub-vertical fijado por escrito](L02-icp-unico-sub-vertical-fijado-por-escrito.md)
