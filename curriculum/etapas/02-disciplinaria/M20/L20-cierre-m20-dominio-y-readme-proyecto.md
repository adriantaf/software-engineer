---
id: L20
materia: M20
orden: 20
titulo: Cierre M20 — dominio y README proyecto
horas: 5.0
semana: 5
lectura: Repaso M20
evidencia: projects/m20-movil/README.md índice
---

# L20 — Cierre M20 — dominio y README proyecto

**~5.0 h · Semana 5**

Cierras materia móvil antes de emprendimiento M22.

## Objetivo

Verificar P1–P3, criterios dominio, enlaces evidencia.

## Conceptos clave

- README
- dominio

## Pasos (hazlos en orden)

### 1. README índice proyecto (50–60 min)

```bash
ls projects/m20-movil
# README debe enlazar: stack-movil.md, auth-storage.md, demo-login-lista.md,
# build-evidence.md, logging-policy.md, release-notes.md, repo-url.md
rg -n "stack-movil|auth-storage|demo-login|build-evidence" projects/m20-movil/README.md
```

### 2. Commit cierre (15 min)

```bash
git add projects/m20-movil
git commit -m "docs(m20): L20 cierre dominio readme"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Repaso M20 | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/README.md` índice enlaza stack, auth-storage, demo, build, logging, release.
2. Commit `docs(m20): L20 cierre-m20-dominio-y-readme-proyecto`.

## Errores comunes

- README sin enlaces a evidencias.
- Código móvil sin URL/ruta.

## Siguiente

Etapa terminal: [M21 — Admin. proyectos](../../03-terminal/M21-admin-proyectos.md).
