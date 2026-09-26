---
id: L04
materia: M14
orden: 4
titulo: Cierre semana 1 — creacionales y bitácora
horas: 5
semana: 1
lectura: "Repaso creacionales + ficha M14"
evidencia: "projects/m14-patrones/semana-01.md"
---

# L04 — Cierre semana 1 — creacionales y bitácora

**~5 h · Semana 1**

## Objetivo

Cerrar semana 1: índice de patrones creacionales usados/rechazados y retro de un anti-patrón que evitaste.

## Por qué importa

La bitácora evita repetir debates de diseño en M17.

## Conceptos

- bitácora.
- trazabilidad.
- anti-patrón.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`semana-01.md`: patrones tocados, commits (`git log --oneline`), qué integrarás al piloto.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l04 cierre-semana-1-creacionales-y-bitacora"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M14-patrones.md | m13-diseno |

## Hecho cuando

1. semana-01.md existe.
2. Strategy+Factory referenciados.
3. Retro honesta.

## Errores comunes

- Semana sin commits.
- Mezclar patrones sin ADR.

## Siguiente

[L05 — Adapter para API de calendario externo](L05-adapter-para-api-de-calendario-externo.md)
