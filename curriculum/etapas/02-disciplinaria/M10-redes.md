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


## Objetivos

1. Explicar capas (modelo simplificado) y el viaje DNS → TCP → TLS → HTTP.
2. Usar `curl`, leer headers y status codes con criterio.
3. Entender certificados TLS a nivel ingeniero (no crypto avanzada).
4. Dibujar la superficie de ataque de tu propio servicio.

## Cómo estudiar esta materia

- Cada concepto → un lab en terminal el mismo día.
- Relaciona siempre con **tu** futuro CRM (M17).
- No memorices números de puerto: entiende *por qué* 443 importa.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura redes | 6–8 | Caps. Tanenbaum / MDN |
| Labs curl/TLS | 6–8 | Bitácora de labs |
| Doc amenazas | 4–6 | Superficie de tu API |
| Retro | 1 | Qué protege TLS y qué no |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Ejecuta y anota:
   ```bash
   curl -v https://example.com -o /dev/null
   ```
2. Identifica en la salida: DNS (si aparece), TLS handshake, status HTTP, headers.
3. Compara `http://` vs `https://` (redirigidos).
4. Escribe en `projects/m10-redes/dia1.md`: “qué protege TLS y qué no protege”.
5. Lee el capítulo de Tanenbaum (ES) sobre capa de aplicación / HTTP (selecto).

## Ejemplo — inspeccionar headers de seguridad

```bash
curl -sI https://tu-dominio.ejemplo | sed -n '1,30p'
```

Busca (cuando tengas producto): `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`. Si faltan, anótalo para M18.

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Modelo de capas, IP, TCP vs UDP, puertos |
| 2 | DNS, HTTP/1.1–2 intuición, status codes |
| 3 | TLS, certificados, MITM conceptual |
| 4 | Cookies, sesiones, CORS intro |
| 5 | Superficie de ataque + proyecto doc |

## Lecturas

Canon: *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) + MDN HTTP (ES). Ver [bibliografía](../../bibliografia.md) y [hilo de seguridad](../../hilos/seguridad.md).

| Semana | Capítulos / recursos | Alternativa |
|--------|---------------------|-------------|
| 1 | Tanenbaum: **intro + capa de red/transporte** (IP, TCP vs UDP, puertos) | Labs `curl`/ping/`ss` |
| 2 | Tanenbaum: **capa de aplicación** + HTTP; MDN *HTTP overview* + status codes | MDN ES HTTP |
| 3 | Tanenbaum: **seguridad en la red / TLS** (selecto) + lab certificados | Docs MDN *Transport Layer Security* |
| 4 | MDN **Cookies** + sesiones; CORS intro (MDN) | Misma MDN ES |
| 5 | Sintetiza superficie de ataque (puertos, headers, cookies) → doc proyecto | [Hilo seguridad](../../hilos/seguridad.md) |

**Regla:** cada capítulo → un lab en terminal el mismo día.

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
