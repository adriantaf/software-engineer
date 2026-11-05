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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - interceptor

      - navigator login


      **Objetivo de esta lección:** Manejar 401 global (logout), validación
      formulario, estados loading/error en login.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Interceptor 401
    xp: 10
    cuerpo: |-
      ```ts
      // si response.status === 401 → clearSecureStorage(); navigate('Login');
      ```

      Mensajes de validación 400 legibles (campo email/password).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Prueba manual
    xp: 10
    cuerpo: >-
      ```bash

      # 1) Login OK  2) Invalida token en storage  3) Pull lista → vuelve a
      Login

      # Anota en auth-storage.md

      git add projects/m20-movil/auth-storage.md

      git commit -m "feat(m20): L04 flujo 401 y validacion"

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Errores de validación y flujo 401», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Errores de validación y
          flujo 401
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
    pregunta: ¿Es recomendable en esta lección? “401 deja la sesión zombie."
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
          Manejar 401 global (logout), validación formulario, estados
          loading/error en login.
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
    pregunta: ¿Debes hacer esto? “Mensajes de error opacos (‘Error’)."
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
      - 401 limpia storage y vuelve a Login; nota en auth-storage.md.
      - 'Commit `docs(m20): L04 errores-de-validacion-y-flujo-401`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
