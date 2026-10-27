---
id: L07
materia: M10
orden: 7
titulo: Status codes y cabeceras de respuesta
horas: 5.0
semana: 2
lectura: MDN HTTP response status + cabeceras selectas
evidencia: labs/status-codes.md
---

# L07 — Status codes y cabeceras de respuesta

**~5.0 h · Semana 2**

El cliente (y tú en soporte) leen el status antes que el JSON. Hoy eliges códigos con criterio.

## Objetivo

Tabla de status para Vitrina + inspección de cabeceras con `curl -sI`.

## Pasos

### 1. Inventario de códigos (60 min)

En `labs/status-codes.md` documenta al menos: 200, 201, 204, 301/302, 400, 401, 403, 404, 409, 422, 429, 500, 502/503. Una frase de cuándo aplica a pedidos/clientes.

### 2. Labs cabeceras (60 min)

```bash
curl -sI https://example.com | tee projects/m10-redes/samples/headers-example.txt
curl -sI https://httpbin.org/status/404
curl -sI https://httpbin.org/status/301
```

Marca `Content-Type`, `Location`, `Cache-Control` / `Age` si aparecen.

### 3. Matriz producto (45 min)

Escenarios: pedido duplicada en mismo slot → ¿409?; token ausente → 401; staff sin permiso a notas privadas → 403; validación de horario → 422.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/status-codes.md projects/m10-redes/samples
git commit -m "docs(m10): l07 status codes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Clases 2xx/3xx/4xx/5xx; Cache-Control, Content-Type, Location | [MDN · Códigos de estado](https://developer.mozilla.org/es/docs/Web/HTTP/Status) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/status-codes.md` con ≥8 códigos y cuándo los usaría Vitrina (401/403/404/409/422/429…).
2. Labs `curl -sI` anotando status + 3 cabeceras relevantes.
3. Commit `docs(m10): l07 status codes`.

## Errores comunes

- Devolver 200 con `{error:…}` en el body y llamarlo API.
- Confundir 401 (no autenticado) con 403 (no autorizado).
- Usar 500 para validación de input del cliente.

## Siguiente

[L08 — HTTP/2 intuición y curl avanzado](L08-http-2-intuicion-y-curl-avanzado.md)
