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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - POST login

      - 401 UX

      - timeout


      **Objetivo de esta lección:** Implementar login email/password contra
      HTTPS M19; errores claros sin stack trace.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Config API URL
    xp: 10
    cuerpo: >-
      ```dart

      // Flutter ejemplo — adapta a RN

      const apiBase = String.fromEnvironment('API_BASE', defaultValue:
      'http://10.0.2.2:3000');

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Pantalla login
    xp: 10
    cuerpo: >-
      ```bash

      # Prueba contra staging:

      curl -sS -X POST "$API_BASE/auth/login" -H 'content-type:
      application/json' \
        -d '{"email":"owner@demo.local","password":"***"}'
      ```


      Email/password → `POST /auth/login`. Muestra error de red/credenciales.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pantalla login contra API staging», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pantalla login contra
          API staging
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
    pregunta: ¿Es recomendable en esta lección? “Mock eterno que nunca pega a staging."
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
        texto: >-
          Implementar login email/password contra HTTPS M19; errores claros sin
          stack trace.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
