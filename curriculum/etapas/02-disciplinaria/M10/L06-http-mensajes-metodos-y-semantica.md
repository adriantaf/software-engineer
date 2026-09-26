---
id: L06
materia: M10
orden: 6
titulo: HTTP mensajes, métodos y semántica
horas: 5.0
semana: 2
lectura: MDN HTTP methods + Tanenbaum capa aplicación
evidencia: labs/http-metodos.md
---

# L06 — HTTP mensajes, métodos y semántica

**~5.0 h · Semana 2**

La API de Agenda Ops será una conversación de mensajes. Hoy fijas métodos e idempotencia.

## Objetivo

Documentar la anatomía de un mensaje HTTP y mapear métodos al dominio de citas.

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

### 3. Mapa Agenda Ops (60 min)

| Método | Recurso (borrador) | Idempotente? | Notas |
|--------|-------------------|--------------|-------|
| GET | `/api/citas?fecha=` | sí | listar |
| POST | `/api/citas` | no | crear |
| PATCH | `/api/citas/:id` | sí* | remarcar |
| DELETE | `/api/citas/:id` | sí | cancelar |

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

1. `labs/http-metodos.md` con tabla método → semántica → ejemplo Agenda Ops (`/citas`, `/clientes`).
2. Al menos dos capturas `curl -v` (GET y POST de ejemplo a httpbin o similar).
3. Commit `docs(m10): l06 http metodos`.

## Errores comunes

- Usar GET con body para “crear cita”.
- Confundir PUT y PATCH.
- Llamar “REST” a cualquier JSON sin mirar semántica del método.

## Siguiente

[L07 — Status codes y cabeceras de respuesta](L07-status-codes-y-cabeceras-de-respuesta.md)
