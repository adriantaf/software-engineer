---
id: L15
materia: M17
orden: 15
titulo: Listas con loading, error y vacío
horas: 5
semana: 4
lectura: "m16 estados-ui"
evidencia: "projects/m17-agenda-ops/docs/ui-estados.md"
---

# L15 — Listas con loading, error y vacío

**~5 h · Semana 4**

## Objetivo

Implementar agenda del día y listas con tres estados UX obligatorios.

## Por qué importa

P2 exige documentación de estados.

## Conceptos

- loading.
- empty.
- error boundary.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ui-estados.md con capturas o descripción por pantalla.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l15 listas-con-loading-error-y-vacio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M17-aplicaciones-web.md | P2 |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. ui-estados.md.
2. 3 estados en UI.
3. Commit.

## Errores comunes

- Spinner eterno.
- Lista vacía sin CTA.

## Siguiente

[L16 — Formularios citas y clientes accesibles](L16-formularios-citas-y-clientes-accesibles.md)
