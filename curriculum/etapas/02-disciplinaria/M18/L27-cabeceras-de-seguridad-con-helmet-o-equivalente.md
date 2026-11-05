---
id: L27
materia: M18
orden: 27
titulo: Cabeceras de seguridad con Helmet o equivalente
horas: 5
semana: 7
lectura: Security Headers Cheat Sheet
evidencia: commit headers + captura curl
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Headers baratos reducen XSS clickjacking y MIME sniffing.


      **Objetivo de esta lección:** Helmet (o equiv) en la API/front; captura
      `curl -I` en evidencia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Baseline headers
    xp: 10
    cuerpo: >-
      ```bash

      curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-before.txt
      | rg -i 'x-|content-security|strict-transport|referrer|permissions'|| true

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Activa Helmet
    xp: 10
    cuerpo: |-
      ```ts
      import helmet from "helmet";
      app.use(helmet({
        contentSecurityPolicy: false, // CSP en L28
        frameguard: { action: "deny" },
        noSniff: true,
        referrerPolicy: { policy: "no-referrer" },
      }));
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cabeceras de seguridad con Helmet o equivalente», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cabeceras de seguridad
          con Helmet o equ…
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
    pregunta: ¿Es recomendable en esta lección? “HSTS en localhost sin TLS."
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
        texto: Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.
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
      git add projects/m18-appsec/pocs/headers-*.txt
      git commit -m "fix(m18): l27 security headers"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Headers visibles en staging (artefacto: `commit headers`).'
      - 'Login sigue funcionando (artefacto: `commit headers`).'
      - 'Commit `docs(m18): L27 cabeceras-de-seguridad-con-helmet-o-equivalente`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5.0 h · Semana 7**

Headers baratos reducen XSS clickjacking y MIME sniffing.

## Objetivo

Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.

## Pasos

### 1. Baseline headers (20–30 min)

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-before.txt | rg -i 'x-|content-security|strict-transport|referrer|permissions'|| true
```
### 2. Activa Helmet (60–80 min)

```ts
import helmet from "helmet";
app.use(helmet({
  contentSecurityPolicy: false, // CSP en L28
  frameguard: { action: "deny" },
  noSniff: true,
  referrerPolicy: { policy: "no-referrer" },
}));
```

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-after.txt
diff -u projects/m18-appsec/pocs/headers-before.txt projects/m18-appsec/pocs/headers-after.txt || true
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/headers-*.txt
git commit -m "fix(m18): l27 security headers"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security Headers Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers visibles en staging (artefacto: `commit headers`).
2. Login sigue funcionando (artefacto: `commit headers`).
3. Commit `docs(m18): L27 cabeceras-de-seguridad-con-helmet-o-equivalente`.

## Errores comunes

- HSTS en localhost sin TLS.
- CSP rota todo sin reporte.

## Siguiente

[L28 — CSP básica sin romper Vitrina](L28-csp-basica-sin-romper-vitrina.md)
