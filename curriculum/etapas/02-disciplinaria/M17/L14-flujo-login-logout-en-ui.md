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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Form login con labels, errores de credencial, logout que
      limpia sesión.


      - login UI

      - error auth

      - logout
  - id: s2
    tipo: ejemplo
    titulo: 1. Página login
    xp: 10
    cuerpo: >-
      ```bash

      # DevTools → Application → Cookies: tras logout la cookie de sesión
      desaparece

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Flujo login/logout en UI" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: páginas login
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m17-vitrina/apps`
    comandoEsperado:
      - git add projects/m17-vitrina/apps
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m17-vitrina/apps'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Form login con labels, errores de credencial, logout que limpia
          sesión.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Logout limpia sesión
    xp: 10
    cuerpo: >-
      ```bash

      DevTools → Application → Cookies: tras logout la cookie de sesión
      desaparece

      ```


      Botón logout → `POST /auth/logout` + redirect `/login`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
