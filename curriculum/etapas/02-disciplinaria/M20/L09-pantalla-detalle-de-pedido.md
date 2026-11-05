---
id: L09
materia: M20
orden: 9
titulo: Pantalla detalle de pedido
horas: 5
semana: 3
lectura: Navigation params
evidencia: commit pantalla detalle
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Navegar a detalle con id; mostrar campos completos de la
      pedido.


      - route args

      - fetch by id
  - id: s2
    tipo: ejemplo
    titulo: 1. Detalle de pedido
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pantalla detalle de pedido" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: commit pantalla detalle
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Navegar a detalle con id; mostrar campos completos de la pedido.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L09 pantalla detalle pedido"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Pantalla detalle de pedido navegable desde la lista (artefacto: `commit
        pantalla detalle`).
      - 'Commit `docs(m20): L09 pantalla-detalle-de-pedido`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
