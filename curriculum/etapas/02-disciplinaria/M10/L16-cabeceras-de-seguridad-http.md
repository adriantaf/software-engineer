---
id: L16
materia: M10
orden: 16
titulo: Cabeceras de seguridad HTTP
horas: 5.0
semana: 4
lectura: MDN CSP, HSTS, X-Frame-Options / frame-ancestors
evidencia: labs/security-headers.md
---

# L16 — Cabeceras de seguridad HTTP

**~5.0 h · Semana 4**

Capa barata y visible. Hoy inventarias headers y dejas una checklist para M17/M18.

## Objetivo

Escribir la política inicial de security headers del producto.

## Pasos

### 1. Escaneo (40 min)

```bash
curl -sI https://example.com | sed -n '1,40p'
```

Busca: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.

### 2. Checklist Vitrina (75 min)

En `labs/security-headers.md`, para cada header: valor propuesto + riesgo si falta. CSP en modo report-only primero está bien — documéntalo.

### 3. Cierre semana 4 (30 min)

README: L13–L16 hechos; enlace a cookies/CORS/headers.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l16 security headers"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | HSTS, CSP, X-Content-Type-Options, Referrer-Policy, frame-ancestors | [MDN · Strict-Transport-Security](https://developer.mozilla.org/es/docs/Web/HTTP/Headers/Strict-Transport-Security) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/security-headers.md` con checklist de headers y valores iniciales para Vitrina.
2. `curl -sI` contra un sitio real anotando cuáles faltan.
3. Commit `docs(m10): l16 security headers`.

## Errores comunes

- CSP `unsafe-inline` eterno “para que cargue”.
- HSTS en localhost de desarrollo sin saber cómo deshacerlo.
- Creer que headers reemplazan authz.

## Siguiente

[L17 — Superficie de ataque: endpoints y datos](L17-superficie-de-ataque-endpoints-y-datos.md)
