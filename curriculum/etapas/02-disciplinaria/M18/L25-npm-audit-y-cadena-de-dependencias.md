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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      A06: la cadena de deps es superficie. Hoy mides y remedias al menos un
      high/critical.


      **Objetivo de esta lección:** Salida de audit en
      `projects/m18-appsec/docs/npm-audit.md` (+ mirror
      `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o
      justificación.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Corre audit
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta + remedia
    xp: 10
    cuerpo: |-
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «npm audit y cadena de dependencias», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de npm audit y cadena de
          dependencias
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
      - npm audit --omit=dev 2>/dev/null || npm audit
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
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
        texto: >-
          Salida de audit en `projects/m18-appsec/docs/npm-audit.md` (+ mirror
          `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o
          justificación.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
