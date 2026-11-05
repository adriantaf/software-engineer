---
id: L14
materia: M17
orden: 14
titulo: Flujo login/logout en UI
horas: 5
semana: 4
lectura: Forms accesibles
evidencia: páginas login
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - login UI

      - error auth

      - logout


      **Objetivo de esta lección:** Form login con labels, errores de
      credencial, logout que limpia sesión.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Página login
    xp: 10
    cuerpo: >-
      ```bash

      # DevTools → Application → Cookies: tras logout la cookie de sesión
      desaparece

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Logout limpia sesión
    xp: 10
    cuerpo: >-
      ```bash

      # DevTools → Application → Cookies: tras logout la cookie de sesión
      desaparece

      ```


      Botón logout → `POST /auth/logout` + redirect `/login`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Flujo login/logout en UI», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Flujo login/logout en
          UI
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

      `git add projects/m17-vitrina/apps`
    comandoEsperado:
      - git add projects/m17-vitrina/apps
      - 'git commit -m "feat(m17): L14 login logout UI"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m17-vitrina/apps'
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
          Form login con labels, errores de credencial, logout que limpia
          sesión.
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
      git add projects/m17-vitrina/apps
      git commit -m "feat(m17): L14 login logout UI"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - UI login/logout funcional; cookie de sesión desaparece tras logout.
      - 'Commit `docs(m17): L14 flujo-login-logout-en-ui`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Flujo login/logout en UI

**~5.0 h · Semana 4**

Primera impresión del piloto.

## Objetivo

Form login con labels, errores de credencial, logout que limpia sesión.

## Conceptos clave

- login UI
- error auth
- logout

## Pasos (hazlos en orden)

### 1. Página login (60–80 min)

Form email/password → `POST /auth/login` (credentials include). Maneja error 401 visible.

### 2. Logout limpia sesión (40–50 min)

```bash
# DevTools → Application → Cookies: tras logout la cookie de sesión desaparece
```

Botón logout → `POST /auth/logout` + redirect `/login`.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/apps
git commit -m "feat(m17): L14 login logout UI"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Forms accesibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. UI login/logout funcional; cookie de sesión desaparece tras logout.
2. Commit `docs(m17): L14 flujo-login-logout-en-ui`.

## Errores comunes

- Logout solo limpia estado React y deja cookie.
- Form sin mensaje de 401.

## Siguiente

[L15 — Listas con loading, error y vacío](L15-listas-con-loading-error-y-vacio.md)
