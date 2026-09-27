---
id: L09
materia: M10
orden: 9
titulo: "TLS: handshake y qué protege en tránsito"
horas: 5.0
semana: 3
lectura: Tanenbaum seguridad/TLS selecto + MDN TLS
evidencia: labs/tls-handshake.md
---

# L09 — TLS: handshake y qué protege en tránsito

**~5.0 h · Semana 3**

Sin TLS, cookies de sesión de Vitrina viajan en claro. Con TLS mal entendido, crees que ya terminaste AppSec.

## Objetivo

Describir el handshake y delimitar el alcance de protección en tránsito.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/tls-handshake.md`: ClientHello → ServerHello/cert → claves → Application Data. Una figura ASCII basta.

### 2. Ver en curl (45 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/samples/tls-curl.txt
```

Resalta: ALPN, versión TLS, “SSL certificate verify ok” (o error).

### 3. Alcance (45 min)

Tabla “protege / no protege” con ejemplos del producto (eavesdropping en café Wi‑Fi vs XSS en el panel).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/tls-handshake.md projects/m10-redes/samples
git commit -m "docs(m10): l09 tls handshake"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Handshake TLS; confidencialidad e integridad en tránsito; qué NO cubre | [MDN · TLS](https://developer.mozilla.org/es/docs/Glossary/TLS) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/tls-handshake.md` explica handshake en lenguaje ingeniero + captura `curl -v` con líneas TLS.
2. Lista explícita: 3 cosas que TLS protege y 3 que **no** (XSS, IDOR, BD robada…).
3. Commit `docs(m10): l09 tls handshake`.

## Errores comunes

- “HTTPS = seguro contra todo”.
- Pensar que el body JSON ya no necesita authz.
- Confundir certificado inválido con “firewall”.

## Siguiente

[L10 — Certificados X.509 y cadena de confianza](L10-certificados-x-509-y-cadena-de-confianza.md)
