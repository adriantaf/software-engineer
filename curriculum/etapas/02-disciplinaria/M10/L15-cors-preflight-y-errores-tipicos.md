---
id: L15
materia: M10
orden: 15
titulo: CORS, preflight y errores típicos
horas: 5.0
semana: 4
lectura: MDN CORS
evidencia: labs/cors.md
---

# L15 — CORS, preflight y errores típicos

**~5.0 h · Semana 4**

CORS no autentica usuarios: solo relaja same-origin en el browser. Hoy lo configuras sin abrirlo todo.

## Objetivo

Documentar preflight y una política CORS para panel+API de Vitrina.

## Pasos

### 1. Lectura MDN (45 min)

Same-origin; simple request vs preflight; `Access-Control-Allow-Credentials`.

### 2. Simula preflight (45 min)

```bash
curl -v -X OPTIONS https://httpbin.org/anything \
  -H 'Origin: https://app.agenda.local' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type,authorization'
```

Anota qué respondería **tu** API (orígenes permitidos, métodos, headers).

### 3. Política producto (45 min)

En `labs/cors.md`: allowlist de orígenes staging/prod; nunca `*` con credentials; cómo fallar cerrado.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cors.md
git commit -m "docs(m10): l15 cors"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Same-origin policy; ACAO; preflight OPTIONS; credenciales | [MDN · CORS](https://developer.mozilla.org/es/docs/Web/HTTP/CORS) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cors.md` explica preflight y configuración segura (sin `*` + credentials).
2. Ejemplo de error de consola típico y cómo lo depurarías con curl OPTIONS.
3. Commit `docs(m10): l15 cors`.

## Errores comunes

- `Access-Control-Allow-Origin: *` con cookies.
- Desactivar CORS en el navegador “para desarrollar”.
- Confundir CORS con authz de negocio.

## Siguiente

[L16 — Cabeceras de seguridad HTTP](L16-cabeceras-de-seguridad-http.md)
