---
id: L03
materia: M16
orden: 3
titulo: Estados vacío, carga y error en agenda
horas: 5.0
semana: 1
lectura: Estados UI; mensajes sin filtrar datos ajenos
evidencia: heuristicas/estados-agenda.md (+ mocks en prototipo)
---

# L03 — Estados vacío, carga y error en agenda

**~5.0 h · Semana 1**

La agenda vacía del lunes es el primer contacto real. Hoy diseñas empty/loading/error.

## Objetivo

Especificación (y si puedes, HTML) de los tres estados.

## Pasos (hazlos en orden)

### 1. Inventario de vistas (30 min)

Lista del día, detalle cita, formulario nueva cita.

### 2. Especifica estados (80–100 min)

Copy sugerido, CTA (“Crear primera cita”), error recuperable vs bloqueante.

### 3. Nota de seguridad UX (30 min)

Qué no decir en 403/404.

### 4. Commit

`docs(m16): estados vacio carga error agenda`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Empty/loading/error en agenda; seguridad en mensajes | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Documento de estados vacío/carga/error para agenda y crear cita.
2. Al menos un mensaje de error revisado para no filtrar datos de otros usuarios.
3. Commit `docs(m16): estados vacio carga error agenda`.

## Errores comunes

- Solo mockup del estado feliz con datos densos.
- Spinner eterno sin timeout/mensaje.
- Error “cita #4821 del tenant X” visible.

## Siguiente

[L04 — auditoria-v1 y cierre P1 heurísticas](L04-auditoria-v1-y-cierre-p1-heuristicas.md)
