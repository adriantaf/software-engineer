---
id: L32
materia: M17
orden: 32
titulo: Cierre M17 — evidencias, dominio y handoff M19
horas: 5.0
semana: 8
lectura: Ficha M17 criterios dominio
evidencia: projects/m17-agenda-ops/docs/nota-cierre-m17.md
---

# L32 — Cierre M17 — evidencias, dominio y handoff M19

**~5.0 h · Semana 8**

Cierras la materia más densa del plan disciplinario.

## Objetivo

Auditar P1–P3, proyecto piloto, criterios dominio, README final y handoff deploy M19.

## Conceptos clave

- cierre
- handoff M19
- dominio

## Pasos (hazlos en orden)

### 1. Índice de evidencias (50–60 min)

```bash
cat > projects/m17-agenda-ops/docs/nota-cierre-m17.md << 'EOF'
# Cierre M17
## Artefactos
- stack.md, docs/auth.md, permisos.md, ui-estados.md
- integracion-whatsapp.md, deploy.md, smoke-test.md
- owasp-mapa.md, adr-tenant-id.md, checklist-saas.md
## Handoff M19
Dockerfile pendiente / Compose / secrets → projects/m19-ops/
EOF
ls projects/m17-agenda-ops/docs
```

### 2. README proyecto + commit (40 min)

Actualiza checklist P1–P3 del README. Enlace a M19.

```bash
git add projects/m17-agenda-ops
git commit -m "docs(m17): L32 cierre evidencias handoff m19"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 criterios dominio | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/docs/nota-cierre-m17.md` con índice de artefactos y handoff M19.
2. README P1–P3 coherente con evidencias (artefacto: `projects/m17-agenda-ops/docs/nota-cierre-m17.md`).
3. Commit `docs(m17): L32 cierre-m17-evidencias-dominio-y-handoff-m19`.

## Errores comunes

- Cerrar M17 sin listar gaps.
- No mencionar handoff Docker/secrets a M19.

## Siguiente

Materia siguiente: [M18 — Seguridad AppSec](../M18-seguridad.md) (en paralelo práctico con deploy M19).
