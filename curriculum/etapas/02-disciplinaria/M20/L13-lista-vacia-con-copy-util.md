---
id: L13
materia: M20
orden: 13
titulo: Lista vacía con copy útil
horas: 5.0
semana: 4
lectura: Empty states UX
evidencia: capturas P2
---

# L13 — Lista vacía con copy útil

**~5.0 h · Semana 4**

P2 pide estados vacío/error.

## Objetivo

UI cuando no hay pedidos semana; CTA coherente con producto.

## Conceptos clave

- empty state
- copy

## Pasos (hazlos en orden)

### 1. Empty state útil (50–60 min)

Copy: “No hay pedidos hoy — crea la primera en la web o aquí”. CTA claro.

### 2. Evidencia P2 (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista vacía
Copy: …  Captura: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L13 lista vacia copy util"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Empty states UX | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Empty state con copy útil documentado en demo-login-lista.md.
2. Commit `docs(m20): L13 lista-vacia-con-copy-util`.

## Errores comunes

- Vacío = pantalla blanca.
- Copy técnico (‘array length 0’).

## Siguiente

[L14 — Sin red: banner y reintento](L14-sin-red-banner-y-reintento.md)
