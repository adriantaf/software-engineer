---
id: L15
materia: M17
orden: 15
titulo: Listas con loading, error y vacío
horas: 5.0
semana: 4
lectura: m16 estados-ui
evidencia: projects/m17-vitrina/docs/ui-estados.md
---

# L15 — Listas con loading, error y vacío

**~5.0 h · Semana 4**

P2 exige documentación de estados.

## Objetivo

Implementar agenda del día y listas con tres estados UX obligatorios.

## Conceptos clave

- loading
- empty
- error boundary

## Pasos (hazlos en orden)

### 1. Estados de lista (70–90 min)

Loading skeleton/spinner; error con reintento; vacío con CTA “Crear pedido”.

### 2. Documenta ui-estados.md (30–40 min)

```bash
cat > projects/m17-vitrina/docs/ui-estados.md << 'EOF'
# UI estados (P2)
| Vista | loading | error | vacío |
|-------|---------|-------|-------|
| /pedidos | … | … | … |
EOF
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/ui-estados.md projects/m17-vitrina/apps
git commit -m "feat(m17): L15 listas loading error vacio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m16 estados-ui | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/ui-estados.md` con loading/error/vacío para listas.
2. Commit `docs(m17): L15 listas-con-loading-error-y-vacio`.

## Errores comunes

- Spinner eterno sin timeout/error.
- Vacío idéntico a error.

## Siguiente

[L16 — Formularios pedidos y clientes accesibles](L16-formularios-pedidos-y-clientes-accesibles.md)
