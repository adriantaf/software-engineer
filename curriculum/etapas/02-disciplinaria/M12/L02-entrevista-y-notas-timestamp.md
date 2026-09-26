---
id: L02
materia: M12
orden: 2
titulo: Entrevista y notas timestamp
horas: 5
semana: 1
lectura: "Técnicas elicitación (plantilla)"
evidencia: "entrevistas/notas-YYYY-MM-DD.md"
---

# L02 — Entrevista y notas timestamp

**~5 h · Semana 1**

## Objetivo

Realizar entrevista (real o simulación seria) y capturar citas, dolores y reglas de negocio.

## Por qué importa

Sin notas crudas no hay trazabilidad al SRS.

## Conceptos

- semiestructurada.
- problema vs solución.
- timestamp.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Sesión ≥30 min. Notas con timestamp cada 10–15 min. Commit notas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l02 entrevista-y-notas-timestamp"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plantilla | secciones contexto | — |

## Hecho cuando

1. Notas con fecha.
2. ≥5 citas o paráfrasis.
3. Problemas sin UI aún.

## Errores comunes

- Inventar respuestas sin marcar simulación.
- Mezclar dos negocios.

## Siguiente

[L03 — Problemas observados y glosario](L03-problemas-observados-y-glosario.md)
