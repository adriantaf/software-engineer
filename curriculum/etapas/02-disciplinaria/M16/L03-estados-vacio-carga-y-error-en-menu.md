---
id: L03
materia: M16
orden: 3
titulo: 'Estados vacío, carga y error en agenda'
horas: 5
semana: 1
lectura: Estados UI; mensajes sin filtrar datos ajenos
evidencia: heuristicas/estados-agenda.md (+ mocks en prototipo)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Especificación (y si puedes, HTML) de los tres estados.


      La agenda vacía del lunes es el primer contacto real. Hoy diseñas
      empty/loading/error.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario de vistas
    xp: 10
    cuerpo: 'Lista del día, detalle pedido, formulario nueva pedido.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Estados vacío, carga y error en agenda" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: heuristicas/estados-agenda.md (+ mocks en prototipo)
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Solo mockup del estado feliz con
      datos densos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Especificación (y si puedes, HTML) de los tres estados.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Especifica estados
    xp: 10
    cuerpo: >-
      Copy sugerido, CTA (“Crear primera pedido”), error recuperable vs
      bloqueante.
  - id: s7
    tipo: explicacion
    titulo: 3. Nota de seguridad UX
    xp: 10
    cuerpo: Qué no decir en 403/404.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Documento de estados vacío/carga/error para agenda y crear pedido.
      - >-
        Al menos un mensaje de error revisado para no filtrar datos de otros
        usuarios.
      - 'Commit `docs(m16): estados vacio carga error agenda`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Estados vacío, carga y error en agenda

**~5.0 h · Semana 1**

La agenda vacía del lunes es el primer contacto real. Hoy diseñas empty/loading/error.

## Objetivo

Especificación (y si puedes, HTML) de los tres estados.

## Pasos (hazlos en orden)

### 1. Inventario de vistas (30 min)

Lista del día, detalle pedido, formulario nueva pedido.

### 2. Especifica estados (80–100 min)

Copy sugerido, CTA (“Crear primera pedido”), error recuperable vs bloqueante.

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

1. Documento de estados vacío/carga/error para agenda y crear pedido.
2. Al menos un mensaje de error revisado para no filtrar datos de otros usuarios.
3. Commit `docs(m16): estados vacio carga error agenda`.

## Errores comunes

- Solo mockup del estado feliz con datos densos.
- Spinner eterno sin timeout/mensaje.
- Error “pedido #4821 del tenant X” visible.

## Siguiente

[L04 — auditoria-v1 y cierre P1 heurísticas](L04-auditoria-v1-y-cierre-p1-heuristicas.md)
