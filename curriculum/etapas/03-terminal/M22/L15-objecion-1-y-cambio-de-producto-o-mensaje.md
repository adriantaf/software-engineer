---
id: L15
materia: M22
orden: 15
titulo: Objeción #1 y cambio de producto o mensaje
horas: 5
semana: 4
lectura: "Lean — build-measure-learn en producto"
evidencia: "projects/m22-bektor/objeciones-sintesis.md"
---

# L15 — Objeción #1 y cambio de producto o mensaje

**~5 h · Semana 4**

## Objetivo

Identificar objeción más frecuente y documentar cambio en mensaje **o** issue en backlog Agenda Ops.

## Por qué importa

Criterio dominio: nombrar objeción #1 y qué cambiaste.

## Conceptos

- Objeción.
- Backlog producto.
- Mensaje.
- Trazabilidad M21.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m22-bektor/objeciones-sintesis.md` con ranking top 3 objeciones.

Abre issue en repo producto **o** entrada en `projects/m21-proyectos/roadmap-trimestre.md` si el fix es producto. Enlaza en demo fichas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l15 objecion-1-y-cambio-de-producto-o-mensaj"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M21 | projects/m21-proyectos | ../../../producto-saas.md |

## Hecho cuando

1. Top 3 objeciones.
2. Cambio mensaje/producto enlazado.
3. Issue o roadmap.

## Errores comunes

- Quejarse sin acción.
- Objeción inventada sin demos.

## Siguiente

[L16 — Refinar pricing tras métricas semana 4](L16-refinar-pricing-tras-metricas-semana-4.md)
