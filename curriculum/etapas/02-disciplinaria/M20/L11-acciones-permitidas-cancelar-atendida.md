---
id: L11
materia: M20
orden: 11
titulo: "Acciones permitidas: cancelar / atendida"
horas: 5.0
semana: 3
lectura: Mutations HTTP
evidencia: commit si API expone
---

# L11 — Acciones permitidas: cancelar / atendida

**~5.0 h · Semana 3**

Solo acciones que el backend autoriza.

## Objetivo

Llamar PATCH/POST que la API expone; deshabilitar si 403.

## Conceptos clave

- mutation
- optimistic UI opcional

## Pasos (hazlos en orden)

### 1. Acciones cancelar/atendida (70–90 min)

```bash
curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
  -H 'content-type: application/json' \
  -d '{"estado":"cancelada"}'
```

Botones solo si el rol/API lo permiten; maneja 403.

### 2. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L11 acciones cancelar atendida"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Mutations HTTP | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Acciones cancelar/atendida llaman API; 403 manejado (artefacto: `commit si API expone`).
2. Commit `docs(m20): L11 acciones-permitidas-cancelar-atendida`.

## Errores comunes

- Cambiar estado solo en memoria local.
- No manejar 403.

## Siguiente

[L12 — Deep link opcional a una pedido](L12-deep-link-opcional-a-una-pedido.md)
