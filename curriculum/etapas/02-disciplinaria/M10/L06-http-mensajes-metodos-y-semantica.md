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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar la anatomía de un mensaje HTTP y mapear métodos
      al dominio de pedidos.


      La API de Vitrina será una conversación de mensajes. Hoy fijas métodos e
      idempotencia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Anatomía
    xp: 10
    cuerpo: |-
      ```bash
      curl -v https://httpbin.org/get
      curl -v -X POST https://httpbin.org/post \
        -H 'Content-Type: application/json' \
        -d '{"cliente":"Ana","servicio":"corte"}'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "HTTP mensajes, métodos y semántica" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: labs/http-metodos.md
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

      `curl -v https://httpbin.org/get`
    comandoEsperado:
      - 'curl -v https://httpbin.org/get'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -v https://httpbin.org/get'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar la anatomía de un mensaje HTTP y mapear métodos al dominio
          de pedidos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Labs curl
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
  - id: s7
    tipo: explicacion
    titulo: 3. Mapa Vitrina
    xp: 10
    cuerpo: |-
      | Método | Recurso (borrador) | Idempotente? | Notas |
      |--------|-------------------|--------------|-------|
      | GET | `/api/pedidos?fecha=` | sí | listar |
      | POST | `/api/pedidos` | no | crear |
      | PATCH | `/api/pedidos/:id` | sí* | remarcar |
      | DELETE | `/api/pedidos/:id` | sí | cancelar |

      \*Documenta tu interpretación.
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
