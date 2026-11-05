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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - route args

      - fetch by id


      **Objetivo de esta lección:** Navegar a detalle con id; mostrar campos
      completos de la pedido.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Detalle de pedido
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"
      ```

      Pantalla: cliente, servicio, horario, estado. Tap desde lista.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L09 pantalla detalle pedido"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pantalla detalle de pedido», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pantalla detalle de
          pedido
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"
      - git add projects/m20-movil
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS -b /tmp/st.ck "$API_BASE/pedidos/<id>"'
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
        texto: Navegar a detalle con id; mostrar campos completos de la pedido.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git add projects/m20-movil`
    comandoEsperado:
      - git add projects/m20-movil
    explicacionError: 'Esperado: git add projects/m20-movil'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Pantalla detalle de pedido navegable desde la lista (artefacto: `commit
        pantalla detalle`).
      - 'Commit `docs(m20): L09 pantalla-detalle-de-pedido`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
