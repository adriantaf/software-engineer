---
id: L12
materia: M13
orden: 12
titulo: Boundaries actualizados y amenazas
horas: 5
semana: 3
lectura: "trust boundaries + STRIDE lite"
evidencia: "trust-boundaries.md v2"
---

# L12 — Boundaries actualizados y amenazas

**~5 h · Semana 3**

## Objetivo

Actualizar boundaries con endpoints y amenazas por zona.

## Por qué importa

P3 requiere límites y notas de amenaza.

## Conceptos

- zona desconfianza.
- amenaza.
- control.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Cada límite: datos, protocolo, control. Al menos 3 amenazas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l12 boundaries-actualizados-y-amenazas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Hilo | seguridad | M10 amenazas |

## Hecho cuando

1. P3 actualizado.
2. Amenazas por zona.
3. Semana 3 cerrada.

## Errores comunes

- Boundary estático sin API.
- Sin control en API.

## Siguiente

[L13 — Plantilla ADR y decisiones de diseño](L13-plantilla-adr-y-decisiones-de-diseno.md)
