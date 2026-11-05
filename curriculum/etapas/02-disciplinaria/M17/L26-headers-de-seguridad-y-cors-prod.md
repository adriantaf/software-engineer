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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - helmet

      - CORS

      - CSP intro


      **Objetivo de esta lección:** Configurar headers básicos y CORS
      restrictivo a dominio front.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Headers seguridad
    xp: 10
    cuerpo: |-
      ```ts
      // helmet() o equivalentes: CSP básica, nosniff, frameguard
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: CORS prod
    xp: 10
    cuerpo: >-
      ```bash

      git add projects/m17-vitrina

      git commit -m "feat(m17): L26 headers seguridad cors"

      ```


      Allowlist `CORS_ORIGIN` de staging/prod — no `*`. Documenta en
      `docs/deploy.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Headers de seguridad y CORS prod», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Headers de seguridad y
          CORS prod
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “`Access-Control-Allow-Origin: *` en
      prod."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Configurar headers básicos y CORS restrictivo a dominio front.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Sin `helmet`/equivalente y sin nota."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Headers de seguridad visibles en `curl -sSI`; CORS allowlist (no `*`).
      - 'Commit `docs(m17): L26 headers-de-seguridad-y-cors-prod`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
