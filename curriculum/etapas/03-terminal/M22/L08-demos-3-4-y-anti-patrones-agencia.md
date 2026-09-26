---
id: L08
materia: M22
orden: 8
titulo: Demos 3–4 y anti-patrones agencia
horas: 5
semana: 2
lectura: "Lean — perseverancia vs pivot"
evidencia: "projects/m22-bektor/demos/demo-03.md + demo-04.md"
---

# L08 — Demos 3–4 y anti-patrones agencia

**~5 h · Semana 2**

## Objetivo

Completar dos demos más; registrar tentación de vender ‘proyecto a medida’ y rechazarla por escrito.

## Por qué importa

El pivote Bektor→Agenda Ops es decisión de negocio; documentar qué **no** vendes.

## Conceptos

- Perseverancia.
- Pivot.
- Scope comercial.
- Trial vs proyecto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea demo-03 y demo-04. Escribe `projects/m22-bektor/pivote-bektor-agenda-ops.md` borrador: qué dejaste de vender (lista) y por qué SaaS gana.

Actualiza `projects/m22-bektor/README.md` con contador demos (4/10).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l08 demos-3-4-y-anti-patrones-agencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M22-emprendimiento.md proyecto | ../../../producto-saas.md |
| Catálogo | Entrada M22 | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

1. 2 demos.
2. pivote borrador.
3. README contador.

## Errores comunes

- Aceptar proyecto custom sin ADR comercial.
- Demos sin fecha.

## Siguiente

[L09 — Tres hipótesis de precio o sub-vertical](L09-tres-hipotesis-de-precio-o-sub-vertical.md)
