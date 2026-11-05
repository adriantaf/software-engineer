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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - TLS

      - HSTS

      - health


      **Objetivo de esta lección:** Forzar HTTPS en prod/staging y health check
      para monitor.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Fuerza HTTPS
    xp: 10
    cuerpo: |-
      ```bash
      curl -sSI https://TU-STAGING.example/health | head -20
      # sin -k; certificado válido
      curl -sS -o /dev/null -w "%{http_code}\n" http://TU-STAGING.example/health
      # redirect 301/308 a https o rechazo
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Health externo
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS https://TU-STAGING.example/health
      # pega JSON (sin secrets) en docs/deploy.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «HTTPS y health checks», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de HTTPS y health checks
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `curl -sSI https://TU-STAGING.example/health | head -20`
    comandoEsperado:
      - 'curl -sSI https://TU-STAGING.example/health | head -20'
      - >-
        curl -sS -o /dev/null -w "%{http_code}\n"
        http://TU-STAGING.example/health
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sSI https://TU-STAGING.example/health | head -20'
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: Forzar HTTPS en prod/staging y health check para monitor.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
