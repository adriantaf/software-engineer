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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear front con login, layout panel, rutas protegidas
      redirect a login.


      - SPA

      - protected route

      - layout
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold front
    xp: 10
    cuerpo: |-
      ```ts
      // ProtectedRoute: si !session → redirect /login
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Scaffold front y rutas protegidas" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: front app + router
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

      `mkdir -p projects/m17-vitrina/apps/web`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/apps/web
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/apps/web'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Crear front con login, layout panel, rutas protegidas redirect a
          login.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Rutas protegidas
    xp: 10
    cuerpo: |-
      ```ts
      // ProtectedRoute: si !session → redirect /login
      ```

      ```bash
      sin cookie, /pedidos en browser → login
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
