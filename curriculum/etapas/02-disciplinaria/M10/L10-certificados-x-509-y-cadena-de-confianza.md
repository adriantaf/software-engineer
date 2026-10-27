---
id: L10
materia: M10
orden: 10
titulo: Certificados X.509 y cadena de confianza
horas: 5.0
semana: 3
lectura: Tanenbaum PKI intro + MDN certificados
evidencia: labs/certificados.md
---

# L10 — Certificados X.509 y cadena de confianza

**~5.0 h · Semana 3**

El navegador no “confía en example.com”: confía en una CA que firmó un leaf con SAN correcto.

## Objetivo

Inspeccionar un certificado real y explicar la cadena.

## Pasos

### 1. openssl s_client (60–75 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

Pega resultado anotado en `labs/certificados.md`.

### 2. Cadena (45 min)

```bash
echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null | head -80
```

Diagrama: leaf → intermediate → root del almacén local.

### 3. Fallos (30 min)

Escribe: cert expirado, hostname mismatch, CA desconocida — síntoma en el cliente y qué harías en staging de Vitrina.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/certificados.md
git commit -m "docs(m10): l10 certificados x509"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | X.509, CA intermedia, leaf, validez y CN/SAN | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/certificados.md` con cadena leaf→intermedia→root explicada para un sitio real.
2. Salida `openssl s_client` o `curl -v` anotando fechas y SAN.
3. Commit `docs(m10): l10 certificados x509`.

## Errores comunes

- Confiar en un cert autofirmado en prod “porque es mío”.
- Ignorar SAN y mirar solo CN legacy.
- Subir claves privadas al repo.

## Siguiente

[L11 — Lab openssl y pinning conceptual](L11-lab-openssl-y-pinning-conceptual.md)
