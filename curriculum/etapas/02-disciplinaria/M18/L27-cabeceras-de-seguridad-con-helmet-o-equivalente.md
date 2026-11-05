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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Helmet (o equiv) en la API/front; captura `curl -I` en
      evidencia.


      Headers baratos reducen XSS clickjacking y MIME sniffing.
  - id: s2
    tipo: ejemplo
    titulo: 1. Baseline headers
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cabeceras de seguridad con Helmet o equivalente" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: commit headers + captura curl
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
    pregunta: ¿Es buena práctica en esta lección? “HSTS en localhost sin TLS."
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
        texto: Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Activa Helmet
    xp: 10
    cuerpo: >-
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

      diff -u projects/m18-appsec/pocs/headers-before.txt
      projects/m18-appsec/pocs/headers-after.txt || true

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
