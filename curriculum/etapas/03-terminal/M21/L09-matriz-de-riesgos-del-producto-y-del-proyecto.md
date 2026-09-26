---
id: L09
materia: M21
orden: 9
titulo: Matriz de riesgos del producto y del proyecto
horas: 5
semana: 3
lectura: "Gestión de riesgos (notas propias) + Scrum impediments"
evidencia: "projects/m21-proyectos/riesgos.md borrador"
---

# L09 — Matriz de riesgos del producto y del proyecto

**~5 h · Semana 3**

## Objetivo

Identificar ≥5 riesgos con probabilidad, impacto, mitigación, dueño y fecha de revisión.

## Por qué importa

P3 y criterios de dominio exigen riesgos accionables, no lista genérica de ‘bugs’.

## Conceptos

- Probabilidad × impacto.
- Riesgo vs issue.
- Mitigación verificable.
- Dueño = tú o mentor.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m21-proyectos/riesgos.md` con tabla (≥5 filas): descripción, P, I, mitigación, dueño, revisión.

Incluye riesgos de **producto** (un solo design partner, scope creep) y **técnicos** (dependencia PaaS).

Enlaza issues de mitigación cuando existan.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l09 matriz-de-riesgos-del-producto-y-del-pro"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../hilos/seguridad.md | ../../../producto-saas.md |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. ≥5 riesgos.
2. Mitigación concreta cada uno.
3. Fechas revisión.

## Errores comunes

- Riesgos ‘hackeo’ sin vector.
- Sin dueño.

## Siguiente

[L10 — Riesgos de seguridad, privacidad y multi-tenant](L10-riesgos-de-seguridad-privacidad-y-multi-tenant.md)
