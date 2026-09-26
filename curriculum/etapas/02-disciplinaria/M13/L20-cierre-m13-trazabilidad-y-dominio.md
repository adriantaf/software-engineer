---
id: L20
materia: M13
orden: 20
titulo: Cierre M13 — trazabilidad y dominio
horas: 5
semana: 5
lectura: "Auditoría completa"
evidencia: "nota-cierre-m13.md"
---

# L20 — Cierre M13 — trazabilidad y dominio

**~5 h · Semana 5**

## Objetivo

Auditar P1–P3, criterios dominio, eliminar diagramas huérfanos.

## Por qué importa

Cierras diseño antes de implementación.

## Conceptos

- trazabilidad.
- limpieza.
- handoff M17.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Matriz requisito→artefacto. Borra o enlaza diagramas sin uso. Commit cierre.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l20 cierre-m13-trazabilidad-y-dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M13-analisis-y-diseno.md | — |

## Hecho cuando

1. P1–P3 verificados.
2. Sin huérfanos.
3. Handoff M17 escrito.

## Errores comunes

- Microservicios en doc.
- SRS no enlazado.
