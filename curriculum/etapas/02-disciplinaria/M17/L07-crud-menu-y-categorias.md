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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** CRUD completo de categorías e ítems de menú con autorización
      owner/staff.


      - CRUD

      - disponibilidad

      - precio_centavos
  - id: s2
    tipo: ejemplo
    titulo: 1. CRUD categorías
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \
        -H 'content-type: application/json' \
        -d '{"nombre":"Bebidas","orden":1}'
      curl -sS -b /tmp/ao.ck http://localhost:3000/menu/categories
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "CRUD menú y categorías" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: /menu/categories /menu/items
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

      `curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \`
    comandoEsperado:
      - 'curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/menu/categories \'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/ao.ck -X POST
      http://localhost:3000/menu/categories \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          CRUD completo de categorías e ítems de menú con autorización
          owner/staff.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. CRUD ítems
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
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
