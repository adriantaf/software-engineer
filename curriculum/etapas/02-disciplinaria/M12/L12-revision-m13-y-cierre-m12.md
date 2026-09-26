---
id: L12
materia: M12
orden: 12
titulo: Revisión M13 y cierre M12
horas: 5
semana: 3
lectura: "Ficha M12 + handoff diseño"
evidencia: "nota-handoff-m13.md"
---

# L12 — Revisión M13 y cierre M12

**~5 h · Semana 3**

## Objetivo

Auto revisión: coherencia, preguntas abiertas para diseño, criterios dominio.

## Por qué importa

M13 empieza leyendo tu SRS; hoy reduces fricción.

## Conceptos

- handoff.
- preguntas abiertas.
- auditoría.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Lista preguntas para M13 (auth, modelo cita). Bitácora cierre. Commit final M12.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l12 revision-m13-y-cierre-m12"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M12-requerimientos.md | m13-diseno README |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. Handoff escrito.
2. P1–P3 auditados.
3. Cierre M12 commit.

## Errores comunes

- SRS sin fecha.
- Stories sin criterios.
