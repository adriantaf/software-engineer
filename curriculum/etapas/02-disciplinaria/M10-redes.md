---
id: M10
titulo: Redes de computadoras
etapa: disciplinaria
orden: 10
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Labs HTTP/DNS/TLS con curl e inspección de certificados
  - id: p2
    titulo: Cliente/servidor TCP simple + diagrama de una request
  - id: p3
    titulo: Mapa de superficie de ataque de tu API (puertos, headers, cookies)
proyecto:
  id: proj
  titulo: Documentación de red + amenazas del producto web
---

# M10 — Redes de computadoras (con mirada de seguridad)

## Por qué existe

Sin redes no hay web. Sin entender TLS, cookies y la ruta de una request, la “seguridad” es teatro. Esta materia es la **capa A** de la pista de ciberseguridad ([hilo](../../hilos/seguridad.md)).

**En resumen:** sigues el viaje de una petición (DNS → TCP → TLS → HTTP) y anotas qué puede fallar en **tu** producto.


## Objetivos de aprendizaje

1. Explicar capas (modelo simplificado) y el viaje DNS → TCP → TLS → HTTP.
2. Usar `curl`, leer headers y status codes con criterio.
3. Entender certificados TLS a nivel ingeniero (no crypto avanzada).
4. Dibujar la superficie de ataque de tu propio servicio.

## Cómo estudiar esta materia (lecciones)

M10 sigue el formato de lecciones completas (como M01): marcas una a una en la UI.

1. Abre las lecciones **en orden** (L01 → L20).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección solo si cumple ese criterio.
4. Las **prácticas / proyecto** exigen evidencia en `projects/m10-redes/`.
5. Relaciona labs con el piloto **Agenda Ops** (M12+) y la API de M17.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + labs | 10–12 | Lecciones de la semana (4× ~5 h) |
| Bitácora P1 | 4–6 | `projects/m10-redes/labs/` |
| Proyecto / P2–P3 | 4–6 | TCP echo, superficie, amenazas |
| Retro | 1 | Qué protege TLS y qué no |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Capas, IP, TCP/UDP y puertos (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Modelo de capas y primer curl](M10/L01-modelo-de-capas-y-primer-curl.md) | 5 |
| L02 | [IP, direccionamiento y enrutamiento intro](M10/L02-ip-direccionamiento-y-enrutamiento-intro.md) | 5 |
| L03 | [TCP vs UDP y puertos bien usados](M10/L03-tcp-vs-udp-y-puertos-bien-usados.md) | 5 |
| L04 | [Cierre semana 1 — bitácora P1](M10/L04-cierre-semana-1-bitacora-p1.md) | 5 |

### Semana 2 — DNS y HTTP (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [DNS: resolución, registros y fallos](M10/L05-dns-resolucion-registros-y-fallos.md) | 5 |
| L06 | [HTTP mensajes, métodos y semántica](M10/L06-http-mensajes-metodos-y-semantica.md) | 5 |
| L07 | [Status codes y cabeceras de respuesta](M10/L07-status-codes-y-cabeceras-de-respuesta.md) | 5 |
| L08 | [HTTP/2 intuición y curl avanzado](M10/L08-http-2-intuicion-y-curl-avanzado.md) | 5 |

### Semana 3 — TLS y certificados (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [TLS: handshake y qué protege en tránsito](M10/L09-tls-handshake-y-que-protege-en-transito.md) | 5 |
| L10 | [Certificados X.509 y cadena de confianza](M10/L10-certificados-x-509-y-cadena-de-confianza.md) | 5 |
| L11 | [Lab openssl y pinning conceptual](M10/L11-lab-openssl-y-pinning-conceptual.md) | 5 |
| L12 | [MITM conceptual y amenazas de enlace](M10/L12-mitm-conceptual-y-amenazas-de-enlace.md) | 5 |

### Semana 4 — Cookies, sesiones y CORS (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Cookies: atributos y modelo de almacenamiento](M10/L13-cookies-atributos-y-modelo-de-almacenamiento.md) | 5 |
| L14 | [Sesiones, tokens y estado en APIs](M10/L14-sesiones-tokens-y-estado-en-apis.md) | 5 |
| L15 | [CORS, preflight y errores típicos](M10/L15-cors-preflight-y-errores-tipicos.md) | 5 |
| L16 | [Cabeceras de seguridad HTTP](M10/L16-cabeceras-de-seguridad-http.md) | 5 |

### Semana 5 — Superficie de ataque y proyecto (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Superficie de ataque: endpoints y datos](M10/L17-superficie-de-ataque-endpoints-y-datos.md) | 5 |
| L18 | [Cliente y servidor TCP mínimo (P2)](M10/L18-cliente-y-servidor-tcp-minimo-p2.md) | 5 |
| L19 | [Documento de amenazas de red del producto](M10/L19-documento-de-amenazas-de-red-del-producto.md) | 5 |
| L20 | [Cierre M10 — evidencias y dominio](M10/L20-cierre-m10-evidencias-y-dominio.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) + MDN HTTP (ES). Ver [bibliografía](../../bibliografia.md#m10-redes) y [hilo de seguridad](../../hilos/seguridad.md).

| Semana | Lecciones | Capítulos / recursos | Alternativa |
|--------|-----------|---------------------|-------------|
| 1 | L01–L04 | Tanenbaum: **intro + red/transporte** (IP, TCP/UDP, puertos) | `curl`, `ping`, `ss` |
| 2 | L05–L08 | **Capa de aplicación** + HTTP; MDN overview + status codes | MDN ES HTTP |
| 3 | L09–L12 | **Seguridad / TLS** (selecto) + labs certificados | MDN TLS |
| 4 | L13–L16 | MDN **Cookies**, sesiones, CORS, security headers | Hilo seguridad |
| 5 | L17–L20 | Superficie de ataque → doc proyecto + cierre | [Hilo seguridad](../../hilos/seguridad.md) |

**Regla:** cada capítulo → un lab en terminal el mismo día.



## Ejemplo — inspeccionar headers de seguridad

```bash
curl -sI https://tu-dominio.ejemplo | sed -n '1,30p'
```

Busca (cuando tengas producto): `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`. Si faltan, anótalo para M18.



## Prácticas

1. **P1:** Bitácora de labs curl/TLS con capturas o logs.
2. **P2:** Echo TCP mínimo en Node/TS + diagrama.
3. **P3:** Inventario: endpoints, auth, datos sensibles, trust boundaries.

## Proyecto útil

Doc `projects/m10-redes/README.md`: cómo viaja una request a tu API + lista de amenazas de red (eavesdropping, session theft, DNS spoofing a alto nivel) y mitigaciones que aplicarás en M18/M19.

## Errores comunes

- Pensar que “HTTPS = ya estoy seguro” (XSS/IDOR siguen vivos).
- Exponer APIs en HTTP “solo en local” y luego olvidarlo en prod.
- Ignorar cookies `Secure` / `HttpOnly`.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Labs:** `projects/m10-redes/` con logs curl/TLS.
- **P2 — TCP:** Echo TCP mínimo + diagrama de una request.
- **P3 — Superficie:** Mapa puertos/headers/cookies de tu servicio.
- **Proyecto — Doc:** Amenazas de red del producto web enlazadas a M18.

## Criterios de dominio

- [ ] Depuras un timeout con hipótesis red vs app.
- [ ] Explicas TLS a un compañero sin decir “es magia”.
- [ ] Tu mapa de superficie existe y es honesto.
