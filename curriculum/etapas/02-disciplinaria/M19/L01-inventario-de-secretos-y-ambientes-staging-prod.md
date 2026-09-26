---
id: L01
materia: M19
orden: 1
titulo: Inventario de secretos y ambientes staging/prod
horas: 5.0
semana: 1
lectura: Docker docs — env vars + 12-factor
evidencia: projects/m19-ops/secrets-inventory.md + ambientes.md
---

# L01 — Inventario de secretos y ambientes staging/prod

**~5.0 h · Semana 1**

Sin mapa de secretos, el Dockerfile los horneará por accidente.

## Objetivo

`ambientes.md` + inventario de secretos **sin valores** (staging vs prod).

## Pasos (hazlos en orden)

### 1. Carpetas (15 min)

```bash
mkdir -p projects/m19-ops/{scripts,logs}
```

### 2. Inventario (80–100 min)

Tabla: nombre var, quién la inyecta, rotación. Separar staging/prod URLs.

### 3. Cruza con M17 `.env.example` (30 min)

### 4. Commit

`docs(m19): l01 inventario secretos ambientes`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docker docs — env vars + 12-factor | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Ambos archivos existen (artefacto: `projects/m19-ops/secrets-inventory.md`).
2. Sin valores secretos (artefacto: `projects/m19-ops/secrets-inventory.md`).
3. URLs objetivo anotadas (artefacto: `projects/m19-ops/secrets-inventory.md`).
4. Commit `docs(m19): L01 inventario-de-secretos-y-ambientes-staging-prod`.

## Errores comunes

- Pegar JWT en markdown.
- Un solo ambiente ‘prod’.

## Siguiente

[L02 — Dockerfile multi-stage para la API](L02-dockerfile-multi-stage-para-la-api.md)
