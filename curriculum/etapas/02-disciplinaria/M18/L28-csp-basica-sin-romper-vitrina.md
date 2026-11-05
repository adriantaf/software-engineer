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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      CSP report-only primero: observas violaciones sin romper el panel.


      **Objetivo de esta lección:** Política en
      `projects/m18-appsec/docs/csp.md`; report-only en staging; anota
      violaciones.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventaria fuentes
    xp: 10
    cuerpo: >-
      ```bash cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops> rg -n
      'cdn\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g '*.jsx'
      | head -30 cat > projects/m18-appsec/docs/csp.md <<'EOF' # CSP — Vitrina
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «CSP básica sin romper Vitrina», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de CSP básica sin romper
          Vitrina
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “`unsafe-inline` everywhere."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Política en `projects/m18-appsec/docs/csp.md`; report-only en staging;
          anota violaciones.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “CSP en meta sin HTTPS."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
