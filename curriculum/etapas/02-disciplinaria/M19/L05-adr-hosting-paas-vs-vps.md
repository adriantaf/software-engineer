---
id: L05
materia: M19
orden: 5
titulo: "ADR hosting: PaaS vs VPS"
horas: 5.0
semana: 2
lectura: Docs Fly/Railway/Render o VPS
evidencia: projects/m19-ops/adr-hosting.md
---

# L05 — ADR hosting: PaaS vs VPS

**~5.0 h · Semana 2**

Elige con criterios: costo, TLS, backups, tiempo.

## Objetivo

`adr-hosting.md` con decisión y consecuencias para Agenda Ops.

## Pasos (hazlos en orden)

### 1. Compara (60 min)

PaaS vs VPS tabla.

### 2. ADR (70–90 min)

Decisión alineada a tu staging M17 si ya existe.

### 3. Commit

`docs(m19): l05 adr hosting`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docs Fly/Railway/Render o VPS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR firmada (artefacto: `projects/m19-ops/adr-hosting.md`).
2. Proveedor elegido (artefacto: `projects/m19-ops/adr-hosting.md`).
3. Riesgos listados (artefacto: `projects/m19-ops/adr-hosting.md`).
4. Commit `docs(m19): L05 adr-hosting-paas-vs-vps`.

## Errores comunes

- Sin ADR.
- Elegir solo por tutorial viejo.

## Siguiente

[L06 — Deploy staging con HTTPS](L06-deploy-staging-con-https.md)
