---
id: L06
materia: M17
orden: 6
titulo: API pedidos — crear y listar con reglas
horas: 5
semana: 2
lectura: REST + validación de líneas/estados
evidencia: POST/GET /orders
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - REST

      - snapshot de precio

      - estados: recibido → preparando → listo → entregado


      **Objetivo de esta lección:** Endpoints crear/listar pedidos con auth, ≥1
      línea, precios desde servidor (snapshot), estados válidos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: POST /orders autenticado
    xp: 10
    cuerpo: >-
      ```bash

      curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
        -H 'content-type: application/json' \
        -d '{"customerName":"Ana","customerPhone":"5255...","canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"...","cantidad":2}]}'
      # 201

      curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
        -H 'content-type: application/json' \
        -d '{"items":[]}'
      # 400 pedido_sin_lineas

      ```


      El servidor resuelve precio/nombre desde `menu_items` y guarda snapshot en
      `order_items`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: GET /orders + reglas
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/ao.ck "http://localhost:3000/orders?estado=recibido"
      curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/orders
      # 401
      ```

      Listar con filtro estado; 401 sin auth.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «API pedidos — crear y listar con reglas», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de API pedidos — crear y
          listar con reglas
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

      `curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \`
    comandoEsperado:
      - 'curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \'
      - 'curl -sS -b /tmp/ao.ck "http://localhost:3000/orders?estado=recibido"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \'
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
          Endpoints crear/listar pedidos con auth, ≥1 línea, precios desde
          servidor (snapshot), estados válidos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests + commit
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- orders
      git add projects/m17-vitrina
      git commit -m "feat(m17): L06 api orders crear y listar"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`POST /orders` y `GET /orders` con auth; 401 sin sesión.'
      - 'Tests 201, 400 sin líneas; total recalculado en servidor.'
      - 'Commit `feat(m17): L06 api orders crear y listar`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — API pedidos — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto Vitrina: crear un pedido con ítems del menú.

## Objetivo

Endpoints crear/listar pedidos con auth, ≥1 línea, precios desde servidor (snapshot), estados válidos.

## Conceptos clave

- REST
- snapshot de precio
- estados: recibido → preparando → listo → entregado

## Pasos (hazlos en orden)

### 1. POST /orders autenticado (70–90 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
  -H 'content-type: application/json' \
  -d '{"customerName":"Ana","customerPhone":"5255...","canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"...","cantidad":2}]}'
# 201
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/orders \
  -H 'content-type: application/json' \
  -d '{"items":[]}'
# 400 pedido_sin_lineas
```

El servidor resuelve precio/nombre desde `menu_items` y guarda snapshot en `order_items`.

### 2. GET /orders + reglas (50–60 min)

Listar con filtro estado; 401 sin auth.

```bash
curl -sS -b /tmp/ao.ck "http://localhost:3000/orders?estado=recibido"
curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/orders
# 401
```

### 3. Tests + commit (40 min)

```bash
npm test -- orders
git add projects/m17-vitrina
git commit -m "feat(m17): L06 api orders crear y listar"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | REST + validación | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /orders` y `GET /orders` con auth; 401 sin sesión.
2. Tests 201, 400 sin líneas; total recalculado en servidor.
3. Commit `feat(m17): L06 api orders crear y listar`.

## Errores comunes

- Confiar en el precio que manda el cliente.
- Listar pedidos sin autenticación.

## Siguiente

[L07 — CRUD menú y categorías](L07-crud-menu-y-categorias.md)
