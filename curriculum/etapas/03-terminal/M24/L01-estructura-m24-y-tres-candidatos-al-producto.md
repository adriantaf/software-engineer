---
id: L01
materia: M24
orden: 1
titulo: Estructura M24 y tres candidatos al producto
horas: 5.0
semana: 1
lectura: Ficha M24 + producto-saas (recordatorios / realtime)
evidencia: projects/m24-emergentes/candidatos.md + bitácora semana-01.md
---

# L01 — Estructura M24 y tres candidatos al producto

**~5 h · Semana 1**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/candidatos.md + bitácora semana-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Crear carpetas de evidencia y registrar tres tecnologías candidatas alineadas a Vitrina (ej. WhatsApp Cloud API, SSE/WebSockets, cola managed).

## Por qué empieza así

M24 separa hype de utilidad; sin candidatos escritos terminas en tutorial random sin decisión.

Conceptos que debes poder explicar al cerrar:

- Spike vs producción
- Fuentes primarias obligatorias
- Hipótesis de producto

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Ficha M24 + producto-saas (recordatorios / realtime)_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m24-emergentes/research projects/m24-emergentes/spike
```

### 3. Laboratorio principal (90–120 min)

En `projects/m24-emergentes/candidatos.md` lista **tres** candidatos con una línea de valor para el ICP (barberías, clínicas dentales, etc.).

### 4. Endurece el entregable (40–60 min)

Abre `projects/m24-emergentes/bitacora/semana-01.md` (crea la carpeta) con objetivo de la semana: research completo antes del spike.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l01 estructura-m24-y-tres-candidatos-al-prod"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Ficha M24 + producto-saas (recordatorios / realtime) | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/candidatos.md + bitácora semana-01.md`.
2. Tres candidatos nombrados con valor ICP.
3. Carpetas research/ y spike/ existen.
4. Bitácora semana 1 iniciada.
5. Commit `docs(m24): l01 …` en el historial.

## Errores comunes

- Elegir blockchain sin caso de uso en pedidos.
- Copiar stack de un tutorial sin leer límites.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Research candidato 1 — fuentes primarias](L02-research-candidato-1-fuentes-primarias.md)
