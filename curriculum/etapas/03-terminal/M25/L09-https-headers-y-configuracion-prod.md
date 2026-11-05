---
id: L09
materia: M25
orden: 9
titulo: 'HTTPS, headers y configuración prod'
horas: 5
semana: 3
lectura: OWASP Configuration + Stripe webhooks docs
evidencia: projects/m25-ciber/hardening/headers.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Verificar TLS, HSTS, headers seguridad en URL prod/staging.

      Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

      Conceptos que debes poder explicar al cerrar:

      - Stripe signature
      - Secrets manager / env
      - Restore ≠ backup
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "HTTPS, headers y configuración prod" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/hardening/headers.md
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

      `curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt`
    comandoEsperado:
      - 'curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Verificar TLS, HSTS, headers seguridad en URL prod/staging.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Mide headers en staging/prod
    xp: 10
    cuerpo: >-
      En `projects/m25-ciber/hardening/headers.md` pega salida redactada:


      ```bash

      curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt

      ```


      Tabla: HSTS | CSP | X-Content-Type-Options | X-Frame-Options |
      Referrer-Policy | Permissions-Policy.
  - id: s7
    tipo: explicacion
    titulo: 3. TLS y redirects
    xp: 10
    cuerpo: >-
      Verifica HTTPS obligatorio (http→https), certificado válido, no mixed
      content en panel.


      Documenta URL exacta + fecha del check. Si falta header: issue + plan de
      fix (no solo “poner nginx”).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/hardening/headers.md`.'
      - Checklist ítem demostrado.
      - Sin valores de API keys.
      - 'Commit `docs(m25): l09 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — HTTPS, headers y configuración prod

**~5 h · Semana 3**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hardening/headers.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Verificar TLS, HSTS, headers seguridad en URL prod/staging.

## Por qué empieza así

Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

Conceptos que debes poder explicar al cerrar:

- Stripe signature
- Secrets manager / env
- Restore ≠ backup

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Configuration + Stripe webhooks docs_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Mide headers en staging/prod (30–40 min)

En `projects/m25-ciber/hardening/headers.md` pega salida redactada:

```bash
curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt
```

Tabla: HSTS | CSP | X-Content-Type-Options | X-Frame-Options | Referrer-Policy | Permissions-Policy.

### 3. TLS y redirects (80–100 min)

Verifica HTTPS obligatorio (http→https), certificado válido, no mixed content en panel.

Documenta URL exacta + fecha del check. Si falta header: issue + plan de fix (no solo “poner nginx”).

### 4. Prioriza remediación (25–35 min)

Top 3 gaps con dueño=tú y evidencia esperada. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l09 https-headers-y-configuraci-n-prod"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Configuration + Stripe webhooks docs | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hardening/headers.md`.
2. Checklist ítem demostrado.
3. Sin valores de API keys.
4. Commit `docs(m25): l09 …` en el historial.

## Errores comunes

- Solo checklist teórico.
- Restore nunca probado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Secretos Stripe y rotación](L10-secretos-stripe-y-rotacion.md)
