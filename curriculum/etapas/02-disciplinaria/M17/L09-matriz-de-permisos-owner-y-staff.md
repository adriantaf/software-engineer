---
id: L09
materia: M17
orden: 9
titulo: Matriz de permisos owner y staff
horas: 5
semana: 3
lectura: m13 casos de uso admin
evidencia: projects/m17-vitrina/docs/permisos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar tabla acción×rol (cancelar pedido, ver reportes,
      gestionar staff).


      - RBAC

      - owner

      - staff
  - id: s2
    tipo: ejemplo
    titulo: 1. Redacta matriz owner/staff
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m17-vitrina/docs
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Matriz de permisos owner y staff" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/permisos.md
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

      `mkdir -p projects/m17-vitrina/docs`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/docs
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/docs'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar tabla acción×rol (cancelar pedido, ver reportes, gestionar
          staff).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Cruza con rutas API
    xp: 10
    cuerpo: >-
      ```bash

      rg -n "router\\.(get|post|patch|delete)|app\\.(get|post)"
      projects/m17-vitrina/src | head -40

      ```


      Marca en la matriz qué ruta aplica cada fila.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/permisos.md
      git commit -m "docs(m17): L09 matriz permisos owner staff"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/permisos.md` con matriz owner/staff y
        rutas.
      - 'Commit `docs(m17): L09 matriz-de-permisos-owner-y-staff`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Matriz de permisos owner y staff

**~5.0 h · Semana 3**

Roles sin matriz escrita se implementan inconsistente.

## Objetivo

Documentar tabla acción×rol (cancelar pedido, ver reportes, gestionar staff).

## Conceptos clave

- RBAC
- owner
- staff

## Pasos (hazlos en orden)

### 1. Redacta matriz owner/staff (60–80 min)

```bash
mkdir -p projects/m17-vitrina/docs
```

Crea `projects/m17-vitrina/docs/permisos.md`:

```md
| Acción | owner | staff |
|--------|-------|-------|
| CRUD pedidos propias negocio | sí | sí |
| Borrar servicio | sí | no |
| Invitar staff | sí | no |
| Ver panel /admin | sí | no |
```

### 2. Cruza con rutas API (40 min)

```bash
rg -n "router\\.(get|post|patch|delete)|app\\.(get|post)" projects/m17-vitrina/src | head -40
```

Marca en la matriz qué ruta aplica cada fila.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/permisos.md
git commit -m "docs(m17): L09 matriz permisos owner staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m13 casos de uso admin | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/permisos.md` con matriz owner/staff y rutas.
2. Commit `docs(m17): L09 matriz-de-permisos-owner-y-staff`.

## Errores comunes

- Matriz genérica sin rutas del piloto.
- Permisos solo ‘en la cabeza’.

## Siguiente

[L10 — Middleware de autorización en API](L10-middleware-de-autorizacion-en-api.md)
