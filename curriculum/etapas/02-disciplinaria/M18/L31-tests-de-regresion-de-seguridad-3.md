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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      ≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u
      equivalentes).


      **Objetivo de esta lección:** Suite documentada en
      `projects/m18-appsec/docs/security-tests.md`; CI los corre.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Selecciona 3
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Implementa / verde
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- --testPathPattern=security
      # Confirma que el workflow L29 incluye este pattern
      ```

      Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests de regresión de seguridad (≥3)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests de regresión de
          seguridad (≥3)
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

      `npm test -- --testPathPattern=security`
    comandoEsperado:
      - npm test -- --testPathPattern=security
      - 'git add -A && git commit -m "test(m18): l31 regresion seguridad"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm test -- --testPathPattern=security'
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
          Suite documentada en `projects/m18-appsec/docs/security-tests.md`; CI
          los corre.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
