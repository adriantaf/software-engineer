---
id: L06
materia: M20
orden: 6
titulo: Pull-to-refresh y paginación simple
horas: 5
semana: 2
lectura: Async refresh UX
evidencia: commit UI
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - refresh

      - pagination


      **Objetivo de esta lección:** Refrescar lista; soportar query page/limit
      si la API lo expone.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Pull-to-refresh
    xp: 10
    cuerpo: |-
      ```dart
      // RefreshIndicator onRefresh: () => controller.reload()
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Paginación simple
    xp: 10
    cuerpo: |-
      ```bash
      # API: GET /pedidos?cursor=… o ?page=2 — documenta contrato
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos?limit=20"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pull-to-refresh y paginación simple», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pull-to-refresh y
          paginación simple
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
    pregunta: ¿Es recomendable en esta lección? “Refresh que no vuelve a pedir red."
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
        texto: Refrescar lista; soportar query page/limit si la API lo expone.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Paginación infinita sin fin."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Pull-to-refresh funciona; paginación o `limit` documentada.
      - 'Commit `docs(m20): L06 pull-to-refresh-y-paginacion-simple`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
# API: GET /pedidos?cursor=… o ?page=2 — documenta contrato
curl -sS -b /tmp/st.ck "$API_BASE/pedidos?limit=20"
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
