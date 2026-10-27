---
id: L12
materia: M10
orden: 12
titulo: MITM conceptual y amenazas de enlace
horas: 5.0
semana: 3
lectura: Tanenbaum ataques en red (selecto) + hilo seguridad
evidencia: amenazas-enlace.md en m10-redes
---

# L12 — MITM conceptual y amenazas de enlace

**~5.0 h · Semana 3**

Cierras la semana TLS con un documento de amenazas **defensivo**: qué temes y qué mitigación aplica.

## Objetivo

Redactar `amenazas-enlace.md` usable como input de M18.

## Pasos

### 1. Modelo (45 min)

Actores: usuario del panel, red del café, ISP, DNS resolver, tu API. Dibuja trust boundaries.

### 2. Catálogo (75 min)

Para cada amenaza (eavesdropping HTTP, MITM con cert falso si el cliente no valida, DNS spoofing, session theft en tránsito):

- Impacto en pedidos/PII
- Mitigación (TLS bien validado, HSTS, no mixed content, DNS provider serio…)
- Residual risk

### 3. Checklist P1 (40 min)

README: labs semana 1–3 listos. Enlace a `amenazas-enlace.md`.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l12 amenazas enlace"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Amenazas en tránsito: eavesdropping, MITM, DNS spoofing (alto nivel) | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m10-redes/amenazas-enlace.md` con ≥4 amenazas y mitigaciones (TLS, HSTS, DNS confiable…).
2. Semana 3 enlazada en README; P1 labs TLS cerrados.
3. Commit `docs(m10): l12 amenazas enlace`.

## Errores comunes

- Tutorial ofensivo de MITM — aquí solo modelo de amenaza y defensa.
- Pensar que HTTP “solo en la LAN” es inocuo.
- Olvidar captive portals / Wi‑Fi públicas en el modelo.

## Siguiente

[L13 — Cookies: atributos y modelo de almacenamiento](L13-cookies-atributos-y-modelo-de-almacenamiento.md)
