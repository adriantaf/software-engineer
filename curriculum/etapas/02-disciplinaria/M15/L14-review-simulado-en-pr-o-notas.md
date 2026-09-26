---
id: L14
materia: M15
orden: 14
titulo: Review simulado en PR o notas
horas: 5
semana: 4
lectura: "Ejemplo review"
evidencia: "projects/m15-calidad/review-ejemplo.md"
---

# L14 — Review simulado en PR o notas

**~5 h · Semana 4**

## Objetivo

Aplicar checklist a un diff (PR propio o parche ficticio) con comentarios línea a línea.

## Por qué importa

Practicar review enseña a escribir código revisable.

## Conceptos

- PR.
- comentarios.
- severidad.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`review-ejemplo.md` con ≥10 comentarios categorizados (blocker/nit).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l14 review-simulado-en-pr-o-notas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M15-vv-calidad.md | P3 |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. review-ejemplo.md.
2. Checklist referenciado.
3. Al menos 1 blocker encontrado.

## Errores comunes

- Review de 2 líneas.
- Sin categoría.

## Siguiente

[L15 — Política bug → test el mismo día](L15-politica-bug-test-el-mismo-dia.md)
