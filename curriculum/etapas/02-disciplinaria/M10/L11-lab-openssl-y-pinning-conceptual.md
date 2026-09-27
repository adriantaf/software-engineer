---
id: L11
materia: M10
orden: 11
titulo: Lab openssl y pinning conceptual
horas: 5.0
semana: 3
lectura: MDN certificate pinning (advertencias) + hilo seguridad
evidencia: labs/openssl-lab.md
---

# L11 — Lab openssl y pinning conceptual

**~5.0 h · Semana 3**

Huella y pinning son herramientas de **confianza extra**, no magia. Hoy las documentas con cuidado.

## Objetivo

Calcular fingerprint y escribir cuándo el pinning tiene sentido (y cuándo no) para Agenda Ops.

## Pasos

### 1. Fingerprint (45 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -fingerprint -sha256 -noout
```

Guarda en `labs/openssl-lab.md`.

### 2. Exportar PEM de estudio (30 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -out projects/m10-redes/samples/example-leaf.pem
openssl x509 -in projects/m10-redes/samples/example-leaf.pem -noout -text | head -40
```

Solo cert público — **nunca** claves privadas de tu producto en git.

### 3. Pinning conceptual (60 min)

Escribe: (a) mobile/API crítica con pin + backup pin; (b) por qué rotar leaf sin backup rompe clientes; (c) alternativa: Certificate Transparency + buena validación de cadena + HSTS.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/openssl-lab.md projects/m10-redes/samples
git commit -m "docs(m10): l11 openssl pinning"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Huella del cert; pinning: cuándo ayuda y cómo duele en rotación | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/openssl-lab.md` con fingerprint SHA256 del leaf de un sitio + comandos reproducibles.
2. Nota de pinning: beneficio vs riesgo operacional (rotación CA/leaf).
3. Commit `docs(m10): l11 openssl pinning`.

## Errores comunes

- Recomendar pinning ciego en una app web típica sin plan de rotación.
- Tratar pinning como sustituto de validación de cadena.
- Publicar material de “cómo hacer MITM” ofensivo — aquí solo defensa conceptual.

## Siguiente

[L12 — MITM conceptual y amenazas de enlace](L12-mitm-conceptual-y-amenazas-de-enlace.md)
