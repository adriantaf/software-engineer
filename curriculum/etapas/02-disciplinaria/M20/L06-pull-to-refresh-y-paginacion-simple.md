---
id: L06
materia: M20
orden: 6
titulo: Pull-to-refresh y paginación simple
horas: 5.0
semana: 2
lectura: Async refresh UX
evidencia: commit UI
---

# L06 — Pull-to-refresh y paginación simple

**~5.0 h · Semana 2**

Dueño espera gesto natural en móvil.

## Objetivo

Refrescar lista; soportar query page/limit si la API lo expone.

## Conceptos clave

- refresh
- pagination

## Pasos (hazlos en orden)

### 1. Pull-to-refresh (50–60 min)

```dart
// RefreshIndicator onRefresh: () => controller.reload()
```

### 2. Paginación simple (50–60 min)

```bash
# API: GET /citas?cursor=… o ?page=2 — documenta contrato
curl -sS -b /tmp/st.ck "$API_BASE/citas?limit=20"
```

```bash
git add projects/m20-movil
git commit -m "feat(m20): L06 pull-to-refresh paginacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Async refresh UX | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Pull-to-refresh funciona; paginación o `limit` documentada.
2. Commit `docs(m20): L06 pull-to-refresh-y-paginacion-simple`.

## Errores comunes

- Refresh que no vuelve a pedir red.
- Paginación infinita sin fin.

## Siguiente

[L07 — Estados de carga en lista](L07-estados-de-carga-en-lista.md)
