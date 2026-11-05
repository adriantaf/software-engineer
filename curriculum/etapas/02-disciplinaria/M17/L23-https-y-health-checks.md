---
id: L23
materia: M17
orden: 23
titulo: HTTPS y health checks
horas: 5
semana: 6
lectura: TLS Let's Encrypt / proveedor
evidencia: HTTPS + /health
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Forzar HTTPS en prod/staging y health check para monitor.

      - TLS
      - HSTS
      - health
  - id: s2
    tipo: ejemplo
    titulo: 1. Fuerza HTTPS
    xp: 10
    cuerpo: |-
      ```bash
      curl -sSI https://TU-STAGING.example/health | head -20
      # sin -k; certificado válido
      curl -sS -o /dev/null -w "%{http_code}\n" http://TU-STAGING.example/health
      # redirect 301/308 a https o rechazo
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "HTTPS y health checks" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: HTTPS + /health
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `curl -sSI https://TU-STAGING.example/health | head -20`
    comandoEsperado:
      - 'curl -sSI https://TU-STAGING.example/health | head -20'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sSI https://TU-STAGING.example/health | head -20'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Forzar HTTPS en prod/staging y health check para monitor.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Health externo
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS https://TU-STAGING.example/health
      pega JSON (sin secrets) en docs/deploy.md
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/deploy.md
      git commit -m "docs(m17): L23 https y health checks"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        HTTPS válido en staging; `GET /health` externo 200 documentado en
        deploy.md.
      - 'Commit `docs(m17): L23 https-y-health-checks`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L23 — HTTPS y health checks

**~5.0 h · Semana 6**

Design partner no debe ver “no seguro”.

## Objetivo

Forzar HTTPS en prod/staging y health check para monitor.

## Conceptos clave

- TLS
- HSTS
- health

## Pasos (hazlos en orden)

### 1. Fuerza HTTPS (40–50 min)

```bash
curl -sSI https://TU-STAGING.example/health | head -20
# sin -k; certificado válido
curl -sS -o /dev/null -w "%{http_code}\n" http://TU-STAGING.example/health
# redirect 301/308 a https o rechazo
```

### 2. Health externo (40 min)

```bash
curl -sS https://TU-STAGING.example/health
# pega JSON (sin secrets) en docs/deploy.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/deploy.md
git commit -m "docs(m17): L23 https y health checks"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | TLS Let's Encrypt / proveedor | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. HTTPS válido en staging; `GET /health` externo 200 documentado en deploy.md.
2. Commit `docs(m17): L23 https-y-health-checks`.

## Errores comunes

- Usar `curl -k` como ‘HTTPS OK’.
- Health solo en localhost.

## Siguiente

[L24 — Smoke test post-deploy](L24-smoke-test-post-deploy.md)
