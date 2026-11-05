---
id: L28
materia: M18
orden: 28
titulo: CSP básica sin romper Vitrina
horas: 5
semana: 7
lectura: Content Security Policy Cheat Sheet
evidencia: projects/m18-appsec/docs/csp.md + commit opcional
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Política en `projects/m18-appsec/docs/csp.md`; report-only
      en staging; anota violaciones.


      CSP report-only primero: observas violaciones sin romper el panel.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventaria fuentes
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'cdn\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g
      '*.jsx' | head -30

      cat > projects/m18-appsec/docs/csp.md <<'EOF'

      CSP — Vitrina
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "CSP básica sin romper Vitrina" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/csp.md + commit opcional
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
    pregunta: ¿Es buena práctica en esta lección? “`unsafe-inline` everywhere."
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
        texto: >-
          Política en `projects/m18-appsec/docs/csp.md`; report-only en staging;
          anota violaciones.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Política escrita (artefacto: `projects/m18-appsec/docs/csp.md`).'
      - >-
        Prueba report-only o estricta (artefacto:
        `projects/m18-appsec/docs/csp.md`).
      - 'Commit `docs(m18): L28 csp-basica-sin-romper-vitrina`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L28 — CSP básica sin romper Vitrina

**~5.0 h · Semana 7**

CSP report-only primero: observas violaciones sin romper el panel.

## Objetivo

Política en `projects/m18-appsec/docs/csp.md`; report-only en staging; anota violaciones.

## Pasos

### 1. Inventaria fuentes (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'cdn\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g '*.jsx' | head -30
cat > projects/m18-appsec/docs/csp.md <<'EOF'
# CSP — Vitrina
## Fuentes externas
- …

## Política propuesta (report-only)
default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none';

## Violaciones observadas
- …
EOF
```
### 2. Report-Only (60–80 min)

```ts
app.use((_req, res, next) => {
  res.setHeader(
    "Content-Security-Policy-Report-Only",
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'",
  );
  next();
});
```

```bash
curl -sI localhost:3000/ | rg -i content-security-policy
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/csp.md
git commit -m "docs(m18): l28 csp report-only"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Content Security Policy Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita (artefacto: `projects/m18-appsec/docs/csp.md`).
2. Prueba report-only o estricta (artefacto: `projects/m18-appsec/docs/csp.md`).
3. Commit `docs(m18): L28 csp-basica-sin-romper-vitrina`.

## Errores comunes

- `unsafe-inline` everywhere.
- CSP en meta sin HTTPS.

## Siguiente

[L29 — Pipeline CI: lint, test, audit, anti-secretos](L29-pipeline-ci-lint-test-audit-anti-secretos.md)
