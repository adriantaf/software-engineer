---
id: L31
materia: M18
orden: 31
titulo: Tests de regresión de seguridad (≥3)
horas: 5
semana: 8
lectura: Security unit tests patterns
evidencia: ≥3 tests en repo producto
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Suite documentada en
      `projects/m18-appsec/docs/security-tests.md`; CI los corre.


      ≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u
      equivalentes).
  - id: s2
    tipo: ejemplo
    titulo: 1. Selecciona 3
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/docs/security-tests.md <<'EOF'
      # Security regression tests
      | # | Archivo | Protege |
      |---|---------|---------|
      | 1 | tests/security/authz-cross-user.test.ts | IDOR pedidos |
      | 2 | tests/security/xss-escape.test.ts | stored XSS notas |
      | 3 | tests/security/rbac-settings.test.ts | staff≠owner |
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests de regresión de seguridad (≥3)" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: ≥3 tests en repo producto
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

      `npm test -- --testPathPattern=security`
    comandoEsperado:
      - npm test -- --testPathPattern=security
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm test -- --testPathPattern=security'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Suite documentada en `projects/m18-appsec/docs/security-tests.md`; CI
          los corre.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementa / verde
    xp: 10
    cuerpo: |-
      Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).

      ```bash
      npm test -- --testPathPattern=security
      Confirma que el workflow L29 incluye este pattern
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add -A && git commit -m "test(m18): l31 regresion seguridad"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '≥3 tests listados (artefacto: `≥3 tests en repo producto`).'
      - 'CI los ejecuta (artefacto: `≥3 tests en repo producto`).'
      - 'Commit `docs(m18): L31 tests-de-regresion-de-seguridad-3`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L31 — Tests de regresión de seguridad (≥3)

**~5.0 h · Semana 8**

≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u equivalentes).

## Objetivo

Suite documentada en `projects/m18-appsec/docs/security-tests.md`; CI los corre.

## Pasos

### 1. Selecciona 3 (20–30 min)

```bash
cat > projects/m18-appsec/docs/security-tests.md <<'EOF'
# Security regression tests
| # | Archivo | Protege |
|---|---------|---------|
| 1 | tests/security/authz-cross-user.test.ts | IDOR pedidos |
| 2 | tests/security/xss-escape.test.ts | stored XSS notas |
| 3 | tests/security/rbac-settings.test.ts | staff≠owner |
EOF
```
### 2. Implementa / verde (100–120 min)

Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).

```bash
npm test -- --testPathPattern=security
# Confirma que el workflow L29 incluye este pattern
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l31 regresion seguridad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security unit tests patterns | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥3 tests listados (artefacto: `≥3 tests en repo producto`).
2. CI los ejecuta (artefacto: `≥3 tests en repo producto`).
3. Commit `docs(m18): L31 tests-de-regresion-de-seguridad-3`.

## Errores comunes

- Tests skipped.
- Solo manual.

## Siguiente

[L32 — Cierre M18 — dominio y riesgo residual](L32-cierre-m18-dominio-y-riesgo-residual.md)
