---
id: L16
materia: M17
orden: 16
titulo: Formularios pedidos y clientes accesibles
horas: 5.0
semana: 4
lectura: MDN forms a11y básica
evidencia: formularios create
---

# L16 — Formularios pedidos y clientes accesibles

**~5.0 h · Semana 4**

Errores server mapeados a campos.

## Objetivo

Crear/editar pedido y cliente con validación inline alineada a API.

## Conceptos clave

- form
- a11y
- validación

## Pasos (hazlos en orden)

### 1. Forms accesibles (80–100 min)

Labels asociados, `aria-invalid`, mensajes de error ligados al campo. Crear pedido + cliente.

### 2. Verifica teclado (30 min)

```bash
# Tab order completo; Enter envía; error anunciado
# Anota checklist en docs/ui-estados.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L16 formularios pedidos clientes a11y"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN forms a11y básica | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Forms pedido/cliente con labels, errores de campo y orden de tab documentado.
2. Commit `docs(m17): L16 formularios-pedidos-y-clientes-accesibles`.

## Errores comunes

- Inputs sin `<label>` / placeholder como único texto.
- Errores solo en toast no asociado.

## Siguiente

[L17 — Deep links WhatsApp — diseño del mensaje](L17-deep-links-whatsapp-diseno-del-mensaje.md)
