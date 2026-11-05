---
id: L04
materia: M20
orden: 4
titulo: Errores de validación y flujo 401
horas: 5
semana: 1
lectura: Interceptors HTTP
evidencia: commit + nota en auth-storage.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Manejar 401 global (logout), validación formulario, estados
      loading/error en login.


      - interceptor

      - navigator login
  - id: s2
    tipo: ejemplo
    titulo: 1. Interceptor 401
    xp: 10
    cuerpo: |-
      ```ts
      // si response.status === 401 → clearSecureStorage(); navigate('Login');
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Errores de validación y flujo 401" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: commit + nota en auth-storage.md
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
    pregunta: ¿Es buena práctica en esta lección? “401 deja la sesión zombie."
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
          Manejar 401 global (logout), validación formulario, estados
          loading/error en login.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prueba manual
    xp: 10
    cuerpo: |-
      ```bash
      1) Login OK  2) Invalida token en storage  3) Pull lista → vuelve a Login
      Anota en auth-storage.md
      git add projects/m20-movil/auth-storage.md
      git commit -m "feat(m20): L04 flujo 401 y validacion"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 401 limpia storage y vuelve a Login; nota en auth-storage.md.
      - 'Commit `docs(m20): L04 errores-de-validacion-y-flujo-401`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Errores de validación y flujo 401

**~5.0 h · Semana 1**

Auth móvil real no termina en login exitoso una vez.

## Objetivo

Manejar 401 global (logout), validación formulario, estados loading/error en login.

## Conceptos clave

- interceptor
- navigator login

## Pasos (hazlos en orden)

### 1. Interceptor 401 (70–90 min)

```ts
// si response.status === 401 → clearSecureStorage(); navigate('Login');
```

Mensajes de validación 400 legibles (campo email/password).

### 2. Prueba manual (30 min)

```bash
# 1) Login OK  2) Invalida token en storage  3) Pull lista → vuelve a Login
# Anota en auth-storage.md
git add projects/m20-movil/auth-storage.md
git commit -m "feat(m20): L04 flujo 401 y validacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Interceptors HTTP | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. 401 limpia storage y vuelve a Login; nota en auth-storage.md.
2. Commit `docs(m20): L04 errores-de-validacion-y-flujo-401`.

## Errores comunes

- 401 deja la sesión zombie.
- Mensajes de error opacos (‘Error’).

## Siguiente

[L05 — Lista de pedidos autenticada](L05-lista-de-pedidos-autenticada.md)
