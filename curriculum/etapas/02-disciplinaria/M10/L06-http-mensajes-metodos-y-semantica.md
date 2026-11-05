---
id: L06
materia: M10
orden: 6
titulo: 'HTTP mensajes, métodos y semántica'
horas: 5
semana: 2
lectura: MDN HTTP methods + Tanenbaum capa aplicación
evidencia: labs/http-metodos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La API de Vitrina será una conversación de mensajes. Hoy fijas métodos e
      idempotencia.


      **Objetivo de esta lección:** Documentar la anatomía de un mensaje HTTP y
      mapear métodos al dominio de pedidos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Anatomía
    xp: 10
    cuerpo: |-
      ```bash
      curl -v https://httpbin.org/get
      curl -v -X POST https://httpbin.org/post \
        -H 'Content-Type: application/json' \
        -d '{"cliente":"Ana","servicio":"corte"}'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Labs curl
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://httpbin.org/get

      curl -v -X POST https://httpbin.org/post \
        -H 'Content-Type: application/json' \
        -d '{"cliente":"Ana","servicio":"corte"}'
      ```


      Guarda fragmentos en `samples/` (sin tokens). Anota `Host`, `User-Agent`,
      `Content-Type`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «HTTP mensajes, métodos y semántica», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de HTTP mensajes, métodos
          y semántica
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

      `curl -v https://httpbin.org/get`
    comandoEsperado:
      - 'curl -v https://httpbin.org/get'
      - 'curl -v -X POST https://httpbin.org/post \'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -v https://httpbin.org/get'
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
          Documentar la anatomía de un mensaje HTTP y mapear métodos al dominio
          de pedidos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Mapa Vitrina
    xp: 10
    cuerpo: >-
      | Método | Recurso (borrador) | Idempotente? | Notas |
      |--------|-------------------|--------------|-------| | GET |
      `/api/pedidos?fecha=` | sí | listar | | POST | `/api/pedidos` | no | crear
      | | PATCH | `/api/pedidos/:id` | sí* | remarcar | | DELETE |
      `/api/pedidos/:id` | sí | cancelar | \*Documenta tu interpretación.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/http-metodos.md` con tabla método → semántica → ejemplo Vitrina
        (`/pedidos`, `/clientes`).
      - >-
        Al menos dos capturas `curl -v` (GET y POST de ejemplo a httpbin o
        similar).
      - 'Commit `docs(m10): l06 http metodos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — HTTP mensajes, métodos y semántica

**~5.0 h · Semana 2**

La API de Vitrina será una conversación de mensajes. Hoy fijas métodos e idempotencia.

## Objetivo

Documentar la anatomía de un mensaje HTTP y mapear métodos al dominio de pedidos.

## Pasos

### 1. Anatomía (40 min)

En `labs/http-metodos.md` dibuja request y response: start-line, headers, body vacío vs JSON.

### 2. Labs curl (75 min)

```bash
curl -v https://httpbin.org/get
curl -v -X POST https://httpbin.org/post \
  -H 'Content-Type: application/json' \
  -d '{"cliente":"Ana","servicio":"corte"}'
```

Guarda fragmentos en `samples/` (sin tokens). Anota `Host`, `User-Agent`, `Content-Type`.

### 3. Mapa Vitrina (60 min)

| Método | Recurso (borrador) | Idempotente? | Notas |
|--------|-------------------|--------------|-------|
| GET | `/api/pedidos?fecha=` | sí | listar |
| POST | `/api/pedidos` | no | crear |
| PATCH | `/api/pedidos/:id` | sí* | remarcar |
| DELETE | `/api/pedidos/:id` | sí | cancelar |

\*Documenta tu interpretación.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/http-metodos.md projects/m10-redes/samples
git commit -m "docs(m10): l06 http metodos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Request-line, headers, body; GET/POST/PUT/PATCH/DELETE e idempotencia | [MDN · Métodos HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Methods) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/http-metodos.md` con tabla método → semántica → ejemplo Vitrina (`/pedidos`, `/clientes`).
2. Al menos dos capturas `curl -v` (GET y POST de ejemplo a httpbin o similar).
3. Commit `docs(m10): l06 http metodos`.

## Errores comunes

- Usar GET con body para “crear pedido”.
- Confundir PUT y PATCH.
- Llamar “REST” a cualquier JSON sin mirar semántica del método.

## Siguiente

[L07 — Status codes y cabeceras de respuesta](L07-status-codes-y-cabeceras-de-respuesta.md)
