---
id: L15
materia: M04
orden: 15
titulo: Informe para negocio (informe.md)
horas: 5
semana: 4
lectura: "Relee objetivos M04 y M22 (emprendimiento) en el plan"
evidencia: "projects/m04-stats/informe.md completo"
---

# L15 — Informe para negocio (`informe.md`)

**~5 h · Semana 4**

Integras simulaciones, descriptivos, gráfico e inferencia en un informe de una página que un dueño de negocio pueda leer — **proyecto** de la materia.

## Objetivo

Redactar `informe.md` con pregunta, datos, método, resultado, limitaciones y recomendación accionable.

## Estructura obligatoria

Crea `projects/m04-stats/informe.md`:

```markdown
# Informe — [título corto]

## Pregunta de negocio
-

## Datos
- Fuente:
- Periodo:
- n / columnas clave:

## Método
- Descriptivos:
- Visualización:
- Inferencia (IC / hipótesis):

## Resultados
(bullets con números, sin jerga innecesaria)

## Limitaciones
-

## Recomendación
(una acción concreta; qué medir después)

## Anexo técnico (opcional)
Enlaces a scripts en src/
```

## Pasos

### 1. Borrador (60 min)

Copia cifras desde `salida/` y notas L09–L14. No inventes números.

### 2. Edición para audiencia (50 min)

Lee en voz alta. Elimina “rechazamos H0” sin traducción. Añade una frase sobre correlación ≠ causalidad si usaste correlación.

### 3. Revisión cruzada (30 min)

Pide a alguien (o simula con checklist): ¿entendió la recomendación sin ver el código?

### 4. Commit

```bash
git add projects/m04-stats/informe.md
git commit -m "docs(m04): informe de negocio L15"
```

## Hecho cuando

1. `informe.md` tiene todas las secciones obligatorias.
2. Recomendación accionable presente.
3. Commit.

## Siguiente

[L16 — Cierre M04: evidencias y dominio](L16-cierre-m04-evidencias.md)
