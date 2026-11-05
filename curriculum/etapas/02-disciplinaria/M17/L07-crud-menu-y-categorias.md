---
id: L07
materia: M17
orden: 7
titulo: CRUD menú y categorías
horas: 5
semana: 2
lectura: SRS RF menú
evidencia: /menu/categories /menu/items
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - CRUD

      - disponibilidad

      - precio_centavos


      **Objetivo de esta lección:** CRUD completo de categorías e ítems de menú
      con autorización owner/staff.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: CRUD categorías
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \
        -H 'content-type: application/json' \
        -d '{"nombre":"Bebidas","orden":1}'
      curl -sS -b /tmp/ao.ck http://localhost:3000/menu/categories
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: CRUD ítems
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/items \
        -H 'content-type: application/json' \
        -d '{"categoryId":"...","nombre":"Matcha latte","precioCentavos":6500,"disponible":true}'
      curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/menu/items/ID \
        -H 'content-type: application/json' \
        -d '{"disponible":false}'
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «CRUD menú y categorías», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de CRUD menú y categorías
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

      `curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \`
    comandoEsperado:
      - 'curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \'
      - 'curl -sS -b /tmp/ao.ck http://localhost:3000/menu/categories'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/ao.ck -X POST
      http://localhost:3000/menu/categories \
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
          CRUD completo de categorías e ítems de menú con autorización
          owner/staff.
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
      git add projects/m17-vitrina
      git commit -m "feat(m17): L07 crud menu categorias items"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - CRUD categorías e ítems con auth; ítem puede marcarse no disponible.
      - Precios en centavos (enteros).
      - 'Commit `feat(m17): L07 crud menu categorias items`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — CRUD menú y categorías

**~5.0 h · Semana 2**

El menú es el producto principal de Vitrina. Sin categorías e ítems no hay perfil público útil.

## Objetivo

CRUD completo de categorías e ítems de menú con autorización owner/staff.

## Conceptos clave

- CRUD
- disponibilidad
- precio_centavos

## Pasos (hazlos en orden)

### 1. CRUD categorías (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \
  -H 'content-type: application/json' \
  -d '{"nombre":"Bebidas","orden":1}'
curl -sS -b /tmp/ao.ck http://localhost:3000/menu/categories
```

### 2. CRUD ítems (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/items \
  -H 'content-type: application/json' \
  -d '{"categoryId":"...","nombre":"Matcha latte","precioCentavos":6500,"disponible":true}'
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/menu/items/ID \
  -H 'content-type: application/json' \
  -d '{"disponible":false}'
```

### 3. Commit (20 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L07 crud menu categorias items"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas | MVP menú | [producto-saas](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. CRUD categorías e ítems con auth; ítem puede marcarse no disponible.
2. Precios en centavos (enteros).
3. Commit `feat(m17): L07 crud menu categorias items`.

## Errores comunes

- Precio en float.
- Borrar categoría con ítems sin regla clara (restringe o cascada documentada).

## Siguiente

[L08 — Seeds demo y datos design partner](L08-seeds-demo-y-datos-design-partner.md)
