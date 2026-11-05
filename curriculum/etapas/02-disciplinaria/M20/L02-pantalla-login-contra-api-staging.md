---
id: L02
materia: M20
orden: 2
titulo: Pantalla login contra API staging
horas: 5
semana: 1
lectura: HTTP client + auth API
evidencia: projects/m20-movil/demo-login-lista.md (inicio)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar login email/password contra HTTPS M19; errores
      claros sin stack trace.


      - POST login

      - 401 UX

      - timeout
  - id: s2
    tipo: ejemplo
    titulo: 1. Config API URL
    xp: 10
    cuerpo: >-
      ```dart

      // Flutter ejemplo — adapta a RN

      const apiBase = String.fromEnvironment('API_BASE', defaultValue:
      'http://10.0.2.2:3000');

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pantalla login contra API staging" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/demo-login-lista.md (inicio)
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
      ¿Es buena práctica en esta lección? “Mock eterno que nunca pega a
      staging."
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
        texto: >-
          Implementar login email/password contra HTTPS M19; errores claros sin
          stack trace.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Pantalla login
    xp: 10
    cuerpo: >-
      Email/password → `POST /auth/login`. Muestra error de red/credenciales.


      ```bash

      Prueba contra staging:

      curl -sS -X POST "$API_BASE/auth/login" -H 'content-type:
      application/json' \
        -d '{"email":"owner@demo.local","password":"***"}'
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      echo "## Login" > projects/m20-movil/demo-login-lista.md
      git add projects/m20-movil
      git commit -m "feat(m20): L02 login contra api staging"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Login UI contra API documentada en
        `projects/m20-movil/demo-login-lista.md`.
      - >-
        Errores de red/credenciales visibles (artefacto:
        `projects/m20-movil/demo-login-lista.md (inicio)`).
      - 'Commit `docs(m20): L02 pantalla-login-contra-api-staging`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Pantalla login contra API staging

**~5.0 h · Semana 1**

Misma API que web M17.

## Objetivo

Implementar login email/password contra HTTPS M19; errores claros sin stack trace.

## Conceptos clave

- POST login
- 401 UX
- timeout

## Pasos (hazlos en orden)

### 1. Config API URL (30–40 min)

```dart
// Flutter ejemplo — adapta a RN
const apiBase = String.fromEnvironment('API_BASE', defaultValue: 'http://10.0.2.2:3000');
```

```bash
# Dev: apunta a staging M19 o local documentado en demo-login-lista.md
```

### 2. Pantalla login (90–110 min)

Email/password → `POST /auth/login`. Muestra error de red/credenciales.

```bash
# Prueba contra staging:
curl -sS -X POST "$API_BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
```

### 3. Commit (15 min)

```bash
echo "## Login" > projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L02 login contra api staging"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | HTTP client + auth API | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Login UI contra API documentada en `projects/m20-movil/demo-login-lista.md`.
2. Errores de red/credenciales visibles (artefacto: `projects/m20-movil/demo-login-lista.md (inicio)`).
3. Commit `docs(m20): L02 pantalla-login-contra-api-staging`.

## Errores comunes

- Mock eterno que nunca pega a staging.
- Hardcodear secrets de prod.

## Siguiente

[L03 — Secure storage de token o sesión](L03-secure-storage-de-token-o-sesion.md)
