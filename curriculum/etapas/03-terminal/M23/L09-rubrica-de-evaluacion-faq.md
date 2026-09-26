---
id: L09
materia: M23
orden: 9
titulo: Rúbrica de evaluación FAQ
horas: 5
semana: 3
lectura: "Evaluación LLM — correcto/parcial/incorrecto/alucinación"
evidencia: "projects/m23-ia/llm-eval/rubrica.md"
---

# L09 — Rúbrica de evaluación FAQ

**~5 h · Semana 3**

## Objetivo

Definir rúbrica con ejemplos anclados para calificar respuestas del asistente.

## Por qué importa

Calidad medible habilita comparar prompt v1 vs v2 objetivamente.

## Conceptos

- Rúbrica.
- Anclas.
- Alucinación.
- Parcial aceptable.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/llm-eval/rubrica.md`: 4 categorías, definición, ejemplo bueno/malo por categoría.

Acuerda umbral (ej. ≥80% correcto+parcial aceptable) en el mismo archivo.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l09 rubrica-de-evaluacion-faq"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Eval guides | ../../../como-estudiar.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. Rúbrica 4 niveles.
2. Ejemplos anclados.
3. Umbral numérico.

## Errores comunes

- ‘Se ve bien’.
- Sin definir alucinación.

## Siguiente

[L10 — Correr evaluación v1 sobre gold set](L10-correr-evaluacion-v1-sobre-gold-set.md)
