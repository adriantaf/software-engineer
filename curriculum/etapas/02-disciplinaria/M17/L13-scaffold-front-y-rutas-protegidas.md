---
id: L13
materia: M17
orden: 13
titulo: Scaffold front y rutas protegidas
horas: 5
semana: 4
lectura: React Router / framework docs
evidencia: front app + router
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - SPA

      - protected route

      - layout


      **Objetivo de esta lección:** Crear front con login, layout panel, rutas
      protegidas redirect a login.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold front
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m17-vitrina/apps/web

      # Vite/Next según stack.md — TypeScript

      cd projects/m17-vitrina/apps/web && npm create vite@latest . -- --template
      react-ts

      ```


      Documenta el comando real en `stack.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Rutas protegidas
    xp: 10
    cuerpo: |-
      ```ts
      // ProtectedRoute: si !session → redirect /login
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Scaffold front y rutas protegidas», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Scaffold front y rutas
          protegidas
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

      `mkdir -p projects/m17-vitrina/apps/web`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/apps/web
      - >-
        cd projects/m17-vitrina/apps/web && npm create vite@latest . --
        --template react-ts
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/apps/web'
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
          Crear front con login, layout panel, rutas protegidas redirect a
          login.
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
      git add projects/m17-vitrina/apps projects/m17-vitrina/stack.md
      git commit -m "feat(m17): L13 scaffold front rutas protegidas"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Front scaffold en `apps/web` (o ruta en stack.md) con rutas protegidas.
      - 'Commit `docs(m17): L13 scaffold-front-y-rutas-protegidas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Scaffold front y rutas protegidas

**~5.0 h · Semana 4**

Vitrina se usa desde navegador diario.

## Objetivo

Crear front con login, layout panel, rutas protegidas redirect a login.

## Conceptos clave

- SPA
- protected route
- layout

## Pasos (hazlos en orden)

### 1. Scaffold front (60–80 min)

```bash
mkdir -p projects/m17-vitrina/apps/web
# Vite/Next según stack.md — TypeScript
cd projects/m17-vitrina/apps/web && npm create vite@latest . -- --template react-ts
```

Documenta el comando real en `stack.md`.

### 2. Rutas protegidas (60–80 min)

```ts
// ProtectedRoute: si !session → redirect /login
```

```bash
# sin cookie, /pedidos en browser → login
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/apps projects/m17-vitrina/stack.md
git commit -m "feat(m17): L13 scaffold front rutas protegidas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | React Router / framework docs | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Front scaffold en `apps/web` (o ruta en stack.md) con rutas protegidas.
2. Commit `docs(m17): L13 scaffold-front-y-rutas-protegidas`.

## Errores comunes

- Rutas ‘protegidas’ solo ocultando links.
- Front sin TypeScript / fuera de stack.md.

## Siguiente

[L14 — Flujo login/logout en UI](L14-flujo-login-logout-en-ui.md)
