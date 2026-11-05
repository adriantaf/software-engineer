---
id: L10
materia: M20
orden: 10
titulo: 'Navegación: tabs o drawer mínimo'
horas: 5
semana: 3
lectura: Navigation container
evidencia: commit nav
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - tabs

      - drawer

      - logout


      **Objetivo de esta lección:** Estructura Pedidos / Perfil / logout
      accesible.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tabs o drawer
    xp: 10
    cuerpo: |-
      ```dart
      // BottomNavigation: Pedidos | Clientes | Cuenta
      // o Drawer equivalente en RN
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L10 navegacion tabs drawer"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Navegación: tabs o drawer mínimo», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Navegación: tabs o
          drawer mínimo
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
    pregunta: ¿Es recomendable en esta lección? “Nav sin destino Cuenta/Logout."
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
        texto: Estructura Pedidos / Perfil / logout accesible.
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
    pregunta: ¿Debes hacer esto? “Tres navegadores distintos."
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
      - 'Tabs o drawer mínimo con ≥2 destinos (artefacto: `commit nav`).'
      - 'Commit `docs(m20): L10 navegacion-tabs-o-drawer-minimo`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Navegación: tabs o drawer mínimo

**~5.0 h · Semana 3**

App usable sin laberinto de pantallas.

## Objetivo

Estructura Pedidos / Perfil / logout accesible.

## Conceptos clave

- tabs
- drawer
- logout

## Pasos (hazlos en orden)

### 1. Tabs o drawer (60–80 min)

```dart
// BottomNavigation: Pedidos | Clientes | Cuenta
// o Drawer equivalente en RN
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L10 navegacion tabs drawer"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Navigation container | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabs o drawer mínimo con ≥2 destinos (artefacto: `commit nav`).
2. Commit `docs(m20): L10 navegacion-tabs-o-drawer-minimo`.

## Errores comunes

- Nav sin destino Cuenta/Logout.
- Tres navegadores distintos.

## Siguiente

[L11 — Acciones permitidas: cancelar / atendida](L11-acciones-permitidas-cancelar-atendida.md)
