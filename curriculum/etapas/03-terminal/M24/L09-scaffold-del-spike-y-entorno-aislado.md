---
id: L09
materia: M24
orden: 9
titulo: Scaffold del spike y entorno aislado
horas: 5.0
semana: 3
lectura: Quickstart oficial de la tecnología elegida
evidencia: projects/m24-emergentes/spike/README.md
---

# L09 — Scaffold del spike y entorno aislado

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/README.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Bootstrap del PoC en rama/carpeta aislada sin tocar prod de Vitrina.

## Por qué empieza así

M24 prohíbe merge experimental a prod sin go explícito.

Conceptos que debes poder explicar al cerrar:

- Rama spike/*
- Secrets locales
- Staging vs prod

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Quickstart oficial de la tecnología elegida_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/README.md`: prerequisitos, variables de entorno (nombres), comando para arrancar.

### 3. Laboratorio principal (90–120 min)

Código mínimo o script en `spike/`; `.env.example` sin valores reales.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l09 scaffold-del-spike-y-entorno-aislado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Quickstart oficial de la tecnología elegida | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/README.md`.
2. README con comando reproducible.
3. .env.example sin secretos.
4. Commit `docs(m24): l09 …` en el historial.

## Errores comunes

- Commit de tokens.
- PoC directo en rama main del SaaS.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Flujo mínimo demostrable](L10-flujo-minimo-demostrable.md)
