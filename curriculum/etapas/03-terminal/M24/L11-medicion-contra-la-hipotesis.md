---
id: L11
materia: M24
orden: 11
titulo: Medición contra la hipótesis
horas: 5.0
semana: 3
lectura: Notas de experimento / métricas manuales
evidencia: projects/m24-emergentes/spike/resultados.md
---

# L11 — Medición contra la hipótesis

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/resultados.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Registrar qué observaste vs hipótesis (latencia, costo estimado, complejidad, fallos).

## Por qué empieza así

Un spike que ‘más o menos funcionó’ sin números no alimenta go/no-go.

Conceptos que debes poder explicar al cerrar:

- Éxito / fallo honesto
- Deuda si hay go
- Aprendizaje

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Notas de experimento / métricas manuales_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/resultados.md`: tabla **Esperado / Observado / Conclusión**.

### 3. Laboratorio principal (90–120 min)

Si falló, documenta por qué — sigue siendo entrega válida.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l11 medici-n-contra-la-hip-tesis"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Notas de experimento / métricas manuales | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/resultados.md`.
2. resultados.md con ≥3 mediciones.
3. Conclusión explícita.
4. Commit `docs(m24): l11 …` en el historial.

## Errores comunes

- Declarar éxito sin probar hipótesis.
- Ocultar blockers.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L12 — Go/no-go, cierre M24 y handoff](L12-go-no-go-cierre-m24-y-handoff.md)
