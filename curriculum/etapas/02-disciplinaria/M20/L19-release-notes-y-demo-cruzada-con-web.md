---
id: L19
materia: M20
orden: 19
titulo: Release notes y demo cruzada con web
horas: 5.0
semana: 5
lectura: Paridad auth web/móvil
evidencia: projects/m20-movil/release-notes.md
---

# L19 — Release notes y demo cruzada con web

**~5.0 h · Semana 5**

Proyecto M20 demuestra canal móvil de Vitrina.

## Objetivo

Notas versión; misma cuenta web y móvil ven mismas pedidos.

## Conceptos clave

- paridad
- demo

## Pasos (hazlos en orden)

### 1. Release notes + demo cruzada (50–60 min)

```bash
cat > projects/m20-movil/release-notes.md << 'EOF'
# Release notes móvil
- Login + lista pedidos (misma API que web)
- Secure storage
- Build: ver build-evidence.md
Demo cruzada: misma pedido visible en web staging y app.
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/release-notes.md
git commit -m "docs(m20): L19 release notes demo cruzada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Paridad auth web/móvil | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/release-notes.md` con demo cruzada web↔app.
2. Commit `docs(m20): L19 release-notes-y-demo-cruzada-con-web`.

## Errores comunes

- Release notes genéricas sin Vitrina.
- Demo web y app con datos distintos sin notarlo.

## Siguiente

[L20 — Cierre M20 — dominio y README proyecto](L20-cierre-m20-dominio-y-readme-proyecto.md)
