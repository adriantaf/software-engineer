---
id: L09
materia: M20
orden: 9
titulo: Pantalla detalle de pedido
horas: 5.0
semana: 3
lectura: Navigation params
evidencia: commit pantalla detalle
---

# L09 — Pantalla detalle de pedido

**~5.0 h · Semana 3**

Lista sin detalle no sirve al dueño en campo.

## Objetivo

Navegar a detalle con id; mostrar campos completos de la pedido.

## Conceptos clave

- route args
- fetch by id

## Pasos (hazlos en orden)

### 1. Detalle de pedido (70–90 min)

```bash
curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"
```

Pantalla: cliente, servicio, horario, estado. Tap desde lista.

### 2. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L09 pantalla detalle pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Navigation params | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Pantalla detalle de pedido navegable desde la lista (artefacto: `commit pantalla detalle`).
2. Commit `docs(m20): L09 pantalla-detalle-de-pedido`.

## Errores comunes

- Detalle sin id real (solo mock).
- PII extra en la pantalla.

## Siguiente

[L10 — Navegación: tabs o drawer mínimo](L10-navegacion-tabs-o-drawer-minimo.md)
