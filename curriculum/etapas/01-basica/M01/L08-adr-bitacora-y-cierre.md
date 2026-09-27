---
id: L08
materia: M01
orden: 8
titulo: ADR, bitácora y cierre
horas: 3
semana: 2
lectura: "Plantilla ADR de la materia; bitácora semana 0002"
evidencia: "adr-001-*.md + semana-0002.md + progress.json actualizable"
---

# L08 — ADR, bitácora y cierre

**~3 h · Semana 2**

Cierras M01 como ingeniero en formación: documentas una decisión (ADR), cierras la bitácora y revisas evidencias antes de marcar prácticas/proyecto.

## Objetivo

Escribir un ADR de una página, completar la bitácora de la semana 2 y autoevaluar criterios de dominio con honestidad.

## Qué es un ADR

**Architecture Decision Record**: contexto → decisión → consecuencias. Corto. Sin teatro.

## Pasos

### 1. Escribe el ADR (P3) — 50–70 min

Crea `projects/m01-diario/adr-001-typescript.md` (o el tema que elijas, pero el plan recomienda TypeScript como lenguaje principal):

```markdown
# ADR 001 — TypeScript como lenguaje principal

## Contexto
Necesito un lenguaje profundo para web, APIs e IA tooling.

## Decisión
Usar TypeScript en modo strict para el plan.

## Consecuencias
+ Tipos y mejor tooling
+ Escala a React/Node
− Curva inicial vs JS puro
```

Amplía el contexto con *tu* situación (carrera, trabajo, inglés). Commit:

```bash
git add projects/m01-diario/adr-001-typescript.md
git commit -m "docs(m01): ADR 001 TypeScript como lenguaje principal"
```

### 2. Bitácora semana 0002 (40–50 min)

Crea `projects/m01-diario/semana-0002.md`:

```markdown
# Semana 0002 — M01

## Qué estudié
- Lecciones:
- Capítulos Pro Git:

## Evidencia
- Commits relevantes (`git log --oneline` pegado):
- Archivos en projects/m01-diario/:

## Qué bloqueó
-

## Qué sigue (M02)
-
```

### 3. Checklist de evidencias (30–40 min)

Antes de marcar nada en la UI, verifica:

| Ítem | Evidencia |
|------|-----------|
| **P1** | `entorno.md` con SO/Git/Node (+ aliases si aplica) |
| **P2** | ≥7 commits atómicos en 7 días (o documenta si aún estás a mitad de racha: **no marques** hasta cumplir) |
| **P3** | `adr-001-*.md` con contexto / decisión / consecuencias |
| **Proyecto** | ≥2 notas `semana-NNNN.md` + intención de actualizar `progress.json` |

### 4. Criterios de dominio (20 min)

Sin mirar tutoriales, responde en la bitácora (sí/no + una frase):

- [ ] Explicas branching sin Stack Overflow.
- [ ] Resuelves un conflicto de merge simple.
- [ ] Tu bitácora de la semana 2 existe y es honesta.
- [ ] No dependes de la GUI de Git para lo básico.

Si algún “no”, anota qué lección repetirás 1 h.

### 5. Marca progreso (10 min)

1. Marca las **lecciones** L01–L08 completadas (solo las que cumplen “Hecho cuando”).
2. Marca **prácticas / proyecto** en la ficha M01 solo con evidencia.
3. Si todo cuadra, marca la materia **Completada**.
4. Exporta JSON desde Progreso y haz commit de `progress.json` cuando toque el ritual semanal.

## Lectura

No hay capítulo nuevo obligatorio. Si te faltó profundidad en ramas, vuelve al cap. 3 de *Pro Git*.

## Hecho cuando

1. Existe el ADR commiteado.
2. Existe `semana-0002.md` con retro honesta.
3. Sabes qué checkboxes de la ficha puedes marcar hoy y cuáles aún no.

## Errores comunes

- Marcar la materia completa porque “ya leí las lecciones”.
- ADR de 10 líneas vacías de consecuencias.
- Olvidar el commit del ADR.

## Siguiente

Vuelve a la [ficha M01](../M01-metodo-y-herramientas.md), cierra checkboxes con evidencia, y pasa a **M02 — Programación I (TypeScript)**.
