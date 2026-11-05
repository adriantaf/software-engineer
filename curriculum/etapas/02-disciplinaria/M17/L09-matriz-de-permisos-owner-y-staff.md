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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - RBAC

      - owner

      - staff


      **Objetivo de esta lección:** Documentar tabla acción×rol (cancelar
      pedido, ver reportes, gestionar staff).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Redacta matriz owner/staff
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m17-vitrina/docs
      ```

      Crea `projects/m17-vitrina/docs/permisos.md`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Cruza con rutas API
    xp: 10
    cuerpo: >-
      ```bash

      rg -n "router\\.(get|post|patch|delete)|app\\.(get|post)"
      projects/m17-vitrina/src | head -40

      ```


      Marca en la matriz qué ruta aplica cada fila.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Matriz de permisos owner y staff», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Matriz de permisos
          owner y staff
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

      `mkdir -p projects/m17-vitrina/docs`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/docs
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/docs'
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
          Documentar tabla acción×rol (cancelar pedido, ver reportes, gestionar
          staff).
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
