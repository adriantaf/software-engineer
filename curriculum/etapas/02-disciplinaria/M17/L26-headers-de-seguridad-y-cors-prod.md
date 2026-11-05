---
id: L26
materia: M17
orden: 26
titulo: Headers de seguridad y CORS prod
horas: 5
semana: 7
lectura: MDN security headers
evidencia: helmet o equivalente
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Configurar headers básicos y CORS restrictivo a dominio
      front.


      - helmet

      - CORS

      - CSP intro
  - id: s2
    tipo: ejemplo
    titulo: 1. Headers seguridad
    xp: 10
    cuerpo: |-
      ```ts
      // helmet() o equivalentes: CSP básica, nosniff, frameguard
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Headers de seguridad y CORS prod" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: helmet o equivalente
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “`Access-Control-Allow-Origin: *` en
      prod."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Configurar headers básicos y CORS restrictivo a dominio front.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. CORS prod
    xp: 10
    cuerpo: >-
      Allowlist `CORS_ORIGIN` de staging/prod — no `*`. Documenta en
      `docs/deploy.md`.


      ```bash

      git add projects/m17-vitrina

      git commit -m "feat(m17): L26 headers seguridad cors"

      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Headers de seguridad visibles en `curl -sSI`; CORS allowlist (no `*`).
      - 'Commit `docs(m17): L26 headers-de-seguridad-y-cors-prod`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L26 — Headers de seguridad y CORS prod

**~5.0 h · Semana 7**

Reduce superficie antes de abrir al partner.

## Objetivo

Configurar headers básicos y CORS restrictivo a dominio front.

## Conceptos clave

- helmet
- CORS
- CSP intro

## Pasos (hazlos en orden)

### 1. Headers seguridad (60–80 min)

```ts
// helmet() o equivalentes: CSP básica, nosniff, frameguard
```

```bash
curl -sSI https://TU-STAGING.example/health | rg -i 'content-security|x-frame|x-content-type|strict-transport'
```

### 2. CORS prod (40 min)

Allowlist `CORS_ORIGIN` de staging/prod — no `*`. Documenta en `docs/deploy.md`.

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L26 headers seguridad cors"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN security headers | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers de seguridad visibles en `curl -sSI`; CORS allowlist (no `*`).
2. Commit `docs(m17): L26 headers-de-seguridad-y-cors-prod`.

## Errores comunes

- `Access-Control-Allow-Origin: *` en prod.
- Sin `helmet`/equivalente y sin nota.

## Siguiente

[L27 — Rate limit en login](L27-rate-limit-en-login.md)
