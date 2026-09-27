---
id: L05
materia: M24
orden: 5
titulo: Matriz de adopción y pesos
horas: 5.0
semana: 2
lectura: Criterios M24 + threat modeling ligero
evidencia: projects/m24-emergentes/matriz-adopcion.md
---

# L05 — Matriz de adopción y pesos

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/matriz-adopcion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Crear matriz con criterios ponderados: valor ICP, costo, riesgo ops, seguridad, fit M26.

## Por qué empieza así

P2 obliga a explicitar trade-offs antes de escribir código del spike.

Conceptos que debes poder explicar al cerrar:

- Peso ≥ hype
- Columna seguridad
- Score transparente

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Criterios M24 + threat modeling ligero_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

En `projects/m24-emergentes/matriz-adopcion.md` define pesos (suma 100%). Filas = candidatos; columnas = criterios.

### 3. Laboratorio principal (90–120 min)

Documenta **cómo** puntuas (1–5) con ejemplos por celda del candidato más fuerte.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l05 matriz-de-adopci-n-y-pesos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Criterios M24 + threat modeling ligero | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md`.
2. Matriz con pesos y ≥3 candidatos.
3. Columna seguridad no vacía.
4. Commit `docs(m24): l05 …` en el historial.

## Errores comunes

- Todos 5/5 sin justificación.
- Olvidar costo mensual estimado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Costo, operación y vendor lock-in](L06-costo-operacion-y-vendor-lock-in.md)
