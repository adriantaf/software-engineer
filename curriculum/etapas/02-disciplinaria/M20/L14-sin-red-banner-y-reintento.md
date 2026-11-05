---
id: L14
materia: M20
orden: 14
titulo: 'Sin red: banner y reintento'
horas: 5
semana: 4
lectura: Connectivity plugins
evidencia: captura offline
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Detectar offline o fallo DNS; banner y botón reintentar.

      - offline
      - retry
  - id: s2
    tipo: ejemplo
    titulo: 1. Banner offline
    xp: 10
    cuerpo: |-
      ```dart
      // connectivity_plus / NetInfo → banner "Sin red" + botón Reintentar
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sin red: banner y reintento" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: captura offline
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
    pregunta: ¿Es buena práctica en esta lección? “Crash sin red."
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
        texto: Detectar offline o fallo DNS; banner y botón reintentar.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prueba avión
    xp: 10
    cuerpo: |-
      ```bash
      Activa modo avión → banner visible → reintento al volver
      echo "Offline OK $(date -I)" >> projects/m20-movil/demo-login-lista.md
      git add projects/m20-movil
      git commit -m "feat(m20): L14 banner sin red reintento"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Banner offline + reintento demostrado (modo avión) (artefacto: `captura
        offline`).
      - 'Commit `docs(m20): L14 sin-red-banner-y-reintento`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L14 — Sin red: banner y reintento

**~5.0 h · Semana 4**

Dueño en campo pierde señal a menudo.

## Objetivo

Detectar offline o fallo DNS; banner y botón reintentar.

## Conceptos clave

- offline
- retry

## Pasos (hazlos en orden)

### 1. Banner offline (60–80 min)

```dart
// connectivity_plus / NetInfo → banner "Sin red" + botón Reintentar
```

### 2. Prueba avión (30 min)

```bash
# Activa modo avión → banner visible → reintento al volver
echo "Offline OK $(date -I)" >> projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L14 banner sin red reintento"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Connectivity plugins | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Banner offline + reintento demostrado (modo avión) (artefacto: `captura offline`).
2. Commit `docs(m20): L14 sin-red-banner-y-reintento`.

## Errores comunes

- Crash sin red.
- Sin botón reintentar.

## Siguiente

[L15 — Timeout, 5xx y mensajes humanos](L15-timeout-5xx-y-mensajes-humanos.md)
