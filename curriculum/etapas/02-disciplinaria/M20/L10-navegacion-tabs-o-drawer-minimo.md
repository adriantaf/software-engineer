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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Estructura Pedidos / Perfil / logout accesible.

      - tabs
      - drawer
      - logout
  - id: s2
    tipo: ejemplo
    titulo: 1. Tabs o drawer
    xp: 10
    cuerpo: |-
      ```dart
      // BottomNavigation: Pedidos | Clientes | Cuenta
      // o Drawer equivalente en RN
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Navegación: tabs o drawer mínimo" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: commit nav
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
    pregunta: ¿Es buena práctica en esta lección? “Nav sin destino Cuenta/Logout."
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
        texto: Estructura Pedidos / Perfil / logout accesible.
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
      git commit -m "feat(m20): L10 navegacion tabs drawer"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Tabs o drawer mínimo con ≥2 destinos (artefacto: `commit nav`).'
      - 'Commit `docs(m20): L10 navegacion-tabs-o-drawer-minimo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
