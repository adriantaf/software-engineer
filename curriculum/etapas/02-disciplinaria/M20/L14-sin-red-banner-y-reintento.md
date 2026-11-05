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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - offline

      - retry


      **Objetivo de esta lección:** Detectar offline o fallo DNS; banner y botón
      reintentar.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Banner offline
    xp: 10
    cuerpo: |-
      ```dart
      // connectivity_plus / NetInfo → banner "Sin red" + botón Reintentar
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Prueba avión
    xp: 10
    cuerpo: |-
      ```bash
      # Activa modo avión → banner visible → reintento al volver
      echo "Offline OK $(date -I)" >> projects/m20-movil/demo-login-lista.md
      git add projects/m20-movil
      git commit -m "feat(m20): L14 banner sin red reintento"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sin red: banner y reintento», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Sin red: banner y
          reintento
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
    pregunta: ¿Es recomendable en esta lección? “Crash sin red."
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
        texto: Detectar offline o fallo DNS; banner y botón reintentar.
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
    pregunta: ¿Debes hacer esto? “Sin botón reintentar."
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
      - >-
        Banner offline + reintento demostrado (modo avión) (artefacto: `captura
        offline`).
      - 'Commit `docs(m20): L14 sin-red-banner-y-reintento`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
