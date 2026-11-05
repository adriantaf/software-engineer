---
id: L15
materia: M25
orden: 15
titulo: Alertas mínimas operativas
horas: 5
semana: 4
lectura: OWASP Error handling / logging
evidencia: projects/m25-ciber/alertas/minimas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un atacante lee tus logs si exfiltras tokens; un cliente lee tus stack
      traces.


      Conceptos que debes poder explicar al cerrar:


      - Structured logging

      - Correlation id

      - Fail closed


      **Objetivo de esta lección:** Qué te despierta: 5xx, disco, failed logins
      — aunque sea email manual.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo synthetic — adapta a tu provider
      curl -s -X POST "$ALERT_WEBHOOK_URL" \
        -H "Content-Type: application/json" \
        -d '{"text":"m25 synthetic alert — safe to ignore"}'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Elige señales que te despiertan
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l15 alertas-m-nimas-operativas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Alertas mínimas operativas», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Alertas mínimas
          operativas
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

      `curl -s -X POST "$ALERT_WEBHOOK_URL" \`
    comandoEsperado:
      - curl -s -X POST "$ALERT_WEBHOOK_URL" \
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -s -X POST "$ALERT_WEBHOOK_URL" \'
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
        texto: 'Qué te despierta: 5xx, disco, failed logins — aunque sea email manual.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Configura o documenta canal
    xp: 10
    cuerpo: >-
      Deja al menos **un** canal real (email, Slack webhook, provider alert).
      Prueba con un evento falso o synthetic. Pega evidencia (screenshot path o
      mensaje redactado).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/alertas/minimas.md`.'
      - Política o config documentada.
      - Ejemplo de log seguro vs inseguro.
      - 'Commit `docs(m25): l15 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Alertas mínimas operativas

**~5 h · Semana 4**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/alertas/minimas.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Qué te despierta: 5xx, disco, failed logins — aunque sea email manual.

## Por qué empieza así

Un atacante lee tus logs si exfiltras tokens; un cliente lee tus stack traces.

Conceptos que debes poder explicar al cerrar:

- Structured logging
- Correlation id
- Fail closed

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Error handling / logging_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Elige señales que te despiertan (25–35 min)

En `projects/m25-ciber/alertas/minimas.md` tabla:

| Señal | Umbral | Canal | Dueño | Acción |
|-------|--------|-------|-------|--------|

Mínimo: 5xx spike, disco/DB, failed logins, webhook Stripe fallando.

### 3. Configura o documenta canal (90–110 min)

Deja al menos **un** canal real (email, Slack webhook, provider alert). Prueba con un evento falso o synthetic.

```bash
# ejemplo synthetic — adapta a tu provider
curl -s -X POST "$ALERT_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"text":"m25 synthetic alert — safe to ignore"}'
```

Pega evidencia (screenshot path o mensaje redactado).

### 4. Runbook de 5 líneas por alerta (25–35 min)

Por cada señal: qué mirar primero. Bitácora semana-04.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l15 alertas-m-nimas-operativas"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Error handling / logging | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/alertas/minimas.md`.
2. Política o config documentada.
3. Ejemplo de log seguro vs inseguro.
4. Commit `docs(m25): l15 …` en el historial.

## Errores comunes

- Loguear Authorization header.
- Alertas imposibles de actuar.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L16 — Errores HTTP y fugas de stack](L16-errores-http-y-fugas-de-stack.md)
