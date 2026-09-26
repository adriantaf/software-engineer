---
id: L22
materia: M23
orden: 22
titulo: Costo mensual estimado por tenant activo
horas: 5
semana: 6
lectura: "Unit economics IA"
evidencia: "projects/m23-ia/llm-eval/costos-mensuales.md"
---

# L22 — Costo mensual estimado por tenant activo

**~5 h · Semana 6**

## Objetivo

Estimar costo API + storage embeddings por tenant/mes con supuestos explícitos.

## Por qué importa

Dueño y tú deben entender bill antes de activar Pro.

## Conceptos

- Costo variable.
- Supuestos.
- Preguntas/mes.
- Margen.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/llm-eval/costos-mensuales.md`: escenario bajo/medio/alto uso; fórmula; en MXN aproximado.

Actualiza `projects/m23-ia/politica-datos-llm.md` sección costos/retención.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l22 costo-mensual-estimado-por-tenant-activo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Pricing calculator | ../../../producto-saas.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. costos-mensuales.md.
2. 3 escenarios.
3. Política actualizada.

## Errores comunes

- Ignorar embedding cost.
- Sin supuestos.

## Siguiente

[L23 — README asistente FAQ y límites producto](L23-readme-asistente-faq-y-limites-producto.md)
