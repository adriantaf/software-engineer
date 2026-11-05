---
id: L25
materia: M18
orden: 25
titulo: npm audit y cadena de dependencias
horas: 5
semana: 7
lectura: OWASP A06 Vulnerable Components
evidencia: projects/m18-appsec/docs/npm-audit.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Salida de audit en `projects/m18-appsec/docs/npm-audit.md`
      (+ mirror `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación
      o justificación.


      A06: la cadena de deps es superficie. Hoy mides y remedias al menos un
      high/critical.
  - id: s2
    tipo: ejemplo
    titulo: 1. Corre audit
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      npm audit --omit=dev 2>/dev/null || npm audit

      npm audit --json > /tmp/m18-audit.json || true

      mkdir -p projects/m18-appsec/docs

      cp /tmp/m18-audit.json projects/m18-appsec/docs/npm-audit.json 2>/dev/null
      || true

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "npm audit y cadena de dependencias" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/npm-audit.md
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Salida de audit en `projects/m18-appsec/docs/npm-audit.md` (+ mirror
          `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o
          just…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta + remedia
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/docs/npm-audit.md <<'EOF'
      npm audit — Vitrina
      Fecha:
      High/Critical:
      Acción (update / ignore justificado):
      Commit:
      EOF
      Remedia al menos 1
      npm audit fix --omit=dev || true
      npm ls --depth=0 | head
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/docs/npm-audit.md
      git commit -m "docs(m18): l25 npm audit"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Audit guardado (artefacto: `projects/m18-appsec/docs/npm-audit.md`).'
      - '≥1 acción tomada (artefacto: `projects/m18-appsec/docs/npm-audit.md`).'
      - 'Commit `docs(m18): L25 npm-audit-y-cadena-de-dependencias`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L25 — npm audit y cadena de dependencias

**~5.0 h · Semana 7**

A06: la cadena de deps es superficie. Hoy mides y remedias al menos un high/critical.

## Objetivo

Salida de audit en `projects/m18-appsec/docs/npm-audit.md` (+ mirror `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o justificación.

## Pasos

### 1. Corre audit (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
npm audit --omit=dev 2>/dev/null || npm audit
npm audit --json > /tmp/m18-audit.json || true
mkdir -p projects/m18-appsec/docs
cp /tmp/m18-audit.json projects/m18-appsec/docs/npm-audit.json 2>/dev/null || true
```
### 2. Documenta + remedia (70–90 min)

```bash
cat > projects/m18-appsec/docs/npm-audit.md <<'EOF'
# npm audit — Vitrina
Fecha:
High/Critical:
Acción (update / ignore justificado):
Commit:
EOF
# Remedia al menos 1
npm audit fix --omit=dev || true
npm ls --depth=0 | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/npm-audit.md
git commit -m "docs(m18): l25 npm audit"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A06 Vulnerable Components | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Audit guardado (artefacto: `projects/m18-appsec/docs/npm-audit.md`).
2. ≥1 acción tomada (artefacto: `projects/m18-appsec/docs/npm-audit.md`).
3. Commit `docs(m18): L25 npm-audit-y-cadena-de-dependencias`.

## Errores comunes

- `npm audit fix --force` sin leer.
- Ignorar todo.

## Siguiente

[L26 — Secretos, .env y rotación](L26-secretos-env-y-rotacion.md)
