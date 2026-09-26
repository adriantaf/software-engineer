---
id: L10
materia: M12
orden: 10
titulo: Requisitos funcionales en SRS
horas: 5
semana: 3
lectura: "plantilla.md funcionales"
evidencia: "srs-borrador.md funcionales"
---

# L10 — Requisitos funcionales en SRS

**~5 h · Semana 3**

## Objetivo

Completar sección funcional numerada alineada a stories Must.

## Por qué importa

El SRS es contrato para M13/M17.

## Conceptos

- RF numerado.
- consistencia.
- dependencias.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Cada Must tiene RF. Revisa duplicados y conflictos.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l10 requisitos-funcionales-en-srs"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plantilla | funcionales | stories.md |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. RF cubren Must.
2. Sin contradicciones.
3. Referencias US-XX.

## Errores comunes

- RF vagos.
- Desalineación con stories.

## Siguiente

[L11 — SRS v1, freeze y P3](L11-srs-v1-freeze-y-p3.md)
