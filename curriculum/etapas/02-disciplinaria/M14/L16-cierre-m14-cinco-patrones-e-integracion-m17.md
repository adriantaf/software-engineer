---
id: L16
materia: M14
orden: 16
titulo: Cierre M14 — cinco patrones e integración M17
horas: 5
semana: 4
lectura: "Ficha M14 proyecto + M17 ficha"
evidencia: "projects/m14-patrones/README.md proyecto + adr resumen"
---

# L16 — Cierre M14 — cinco patrones e integración M17

**~5 h · Semana 4**

## Objetivo

Entregar índice ≥5 patrones justificados y plan de migración a `projects/m17-agenda-ops/`.

## Por qué importa

El piloto hereda decisiones; hoy las dejas trazables.

## Conceptos

- handoff M17.
- ADR resumen.
- criterios dominio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

README final: 5+ patrones, ADRs, comando test. `nota-handoff-m17.md` con rutas a copiar.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l16 cierre-m14-cinco-patrones-e-integracion-"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M14-patrones.md | ../M17-aplicaciones-web.md |

## Hecho cuando

1. ≥5 patrones en índice.
2. Handoff M17.
3. Cierre M14 commit.

## Errores comunes

- Patrones sin justificación.
- Olvidar tests.
