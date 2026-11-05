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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La agenda vacía del lunes es el primer contacto real. Hoy diseñas
      empty/loading/error.


      **Objetivo de esta lección:** Especificación (y si puedes, HTML) de los
      tres estados.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario de vistas
    xp: 10
    cuerpo: 'Lista del día, detalle pedido, formulario nueva pedido.'
  - id: s3
    tipo: ejemplo
    titulo: Especifica estados
    xp: 10
    cuerpo: >-
      Copy sugerido, CTA (“Crear primera pedido”), error recuperable vs
      bloqueante.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Estados vacío, carga y error en agenda», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Estados vacío, carga y
          error en agenda
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Solo mockup del estado feliz con datos
      densos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: 'Especificación (y si puedes, HTML) de los tres estados.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota de seguridad UX
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
