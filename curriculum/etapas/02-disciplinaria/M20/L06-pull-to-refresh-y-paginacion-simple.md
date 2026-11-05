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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Refrescar lista; soportar query page/limit si la API lo
      expone.


      - refresh

      - pagination
  - id: s2
    tipo: ejemplo
    titulo: 1. Pull-to-refresh
    xp: 10
    cuerpo: |-
      ```dart
      // RefreshIndicator onRefresh: () => controller.reload()
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pull-to-refresh y paginación simple" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: commit UI
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
    pregunta: ¿Es buena práctica en esta lección? “Refresh que no vuelve a pedir red."
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
        texto: Refrescar lista; soportar query page/limit si la API lo expone.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Paginación simple
    xp: 10
    cuerpo: |-
      ```bash
      API: GET /pedidos?cursor=… o ?page=2 — documenta contrato
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos?limit=20"
      ```

      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L06 pull-to-refresh paginacion"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Pull-to-refresh funciona; paginación o `limit` documentada.
      - 'Commit `docs(m20): L06 pull-to-refresh-y-paginacion-simple`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
