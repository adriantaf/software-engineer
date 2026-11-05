---
id: L14
materia: M25
orden: 14
titulo: Rate limit login y abuso básico
horas: 5
semana: 4
lectura: OWASP Error handling / logging
evidencia: projects/m25-ciber/abuso/rate-limit.md
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


      **Objetivo de esta lección:** Confirmar o implementar límite; documentar
      umbrales.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      for i in $(seq 1 30); do
        curl -s -o /dev/null -w "%{http_code}\n" -X POST "$API/auth/login" \
          -H "Content-Type: application/json" \
          -d '{"email":"nope@test","password":"x"}'
      done | sort | uniq -c
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Define umbrales
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l14 rate-limit-login-y-abuso-b-sico"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Rate limit login y abuso básico», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Rate limit login y
          abuso básico
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

      `curl -s -o /dev/null -w "%{http_code}\n" -X POST "$API/auth/login" \`
    comandoEsperado:
      - 'curl -s -o /dev/null -w "%{http_code}\n" -X POST "$API/auth/login" \'
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -o /dev/null -w "%{http_code}\n" -X POST
      "$API/auth/login" \
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
        texto: Confirmar o implementar límite; documentar umbrales.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Prueba o implementa límite
    xp: 10
    cuerpo: >-
      Dispara ráfaga controlada contra staging: Documenta códigos observados. Si
      no hay 429: implementa o configura WAF/middleware y re-prueba.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/abuso/rate-limit.md`.'
      - Política o config documentada.
      - Ejemplo de log seguro vs inseguro.
      - 'Commit `docs(m25): l14 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Rate limit login y abuso básico

**~5 h · Semana 4**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/abuso/rate-limit.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Confirmar o implementar límite; documentar umbrales.

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

### 2. Define umbrales (20–30 min)

En `projects/m25-ciber/abuso/rate-limit.md`: endpoint login (y opcional signup/webhook) → req/min → respuesta (429).

### 3. Prueba o implementa límite (100–120 min)

Dispara ráfaga controlada contra staging:

```bash
for i in $(seq 1 30); do
  curl -s -o /dev/null -w "%{http_code}\n" -X POST "$API/auth/login" \
    -H "Content-Type: application/json" \
    -d '{"email":"nope@test","password":"x"}'
done | sort | uniq -c
```

Documenta códigos observados. Si no hay 429: implementa o configura WAF/middleware y re-prueba.

### 4. Abuso adyacente (25–35 min)

Nota 3 vectores (credential stuffing, brute invite, webhook flood) + estado. Bitácora semana-04.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l14 rate-limit-login-y-abuso-b-sico"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Error handling / logging | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/abuso/rate-limit.md`.
2. Política o config documentada.
3. Ejemplo de log seguro vs inseguro.
4. Commit `docs(m25): l14 …` en el historial.

## Errores comunes

- Loguear Authorization header.
- Alertas imposibles de actuar.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L15 — Alertas mínimas operativas](L15-alertas-minimas-operativas.md)
