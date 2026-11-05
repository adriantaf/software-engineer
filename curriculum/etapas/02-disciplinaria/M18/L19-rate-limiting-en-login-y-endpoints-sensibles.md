---
id: L19
materia: M18
orden: 19
titulo: Rate limiting en login y endpoints sensibles
horas: 5
semana: 5
lectura: Brute Force + Rate Limiting Cheat Sheets
evidencia: commit middleware + nota en findings
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Límite en login (+1 endpoint costoso); prueba 429
      documentada; nota en findings.


      Sin rate limit, A07 y DoS ligero son triviales.
  - id: s2
    tipo: ejemplo
    titulo: 1. Middleware o proxy
    xp: 10
    cuerpo: |-
      ```ts
      import rateLimit from "express-rate-limit";

      export const loginLimiter = rateLimit({
        windowMs: 15 * 60 * 1000,
        max: 20,
        standardHeaders: true,
        legacyHeaders: false,
        message: { error: "too_many_requests" },
      });

      // app.post("/auth/login", loginLimiter, loginHandler);
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Rate limiting en login y endpoints sensibles" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: commit middleware + nota en findings
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
    pregunta: ¿Es buena práctica en esta lección? “Rate limit solo en front."
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
          Límite en login (+1 endpoint costoso); prueba 429 documentada; nota en
          findings.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prueba de bloqueo
    xp: 10
    cuerpo: >-
      ```bash

      for i in $(seq 1 25); do
        curl -s -o /dev/null -w "$i:%{http_code}\n" -X POST localhost:3000/auth/login \
          -H 'content-type: application/json' \
          -d '{"email":"owner@test.local","password":"wrong"}'
      done | tail -5

      espera ver 429


      printf "\n## Rate limit login\n- window: 15m · max: 20\n- prueba: ver 429
      tras N intentos\n- reset dev: reiniciar proceso / redis FLUSH\n" >>
      projects/m18-appsec/findings-table.md

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add -A && git commit -m "fix(m18): l19 rate limit login"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Rate limit activo (artefacto: `commit middleware`).'
      - 'Prueba documentada (artefacto: `commit middleware`).'
      - 'Commit `docs(m18): L19 rate-limiting-en-login-y-endpoints-sensibles`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Rate limiting en login y endpoints sensibles

**~5.0 h · Semana 5**

Sin rate limit, A07 y DoS ligero son triviales.

## Objetivo

Límite en login (+1 endpoint costoso); prueba 429 documentada; nota en findings.

## Pasos

### 1. Middleware o proxy (60–80 min)

```ts
import rateLimit from "express-rate-limit";

export const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "too_many_requests" },
});

// app.post("/auth/login", loginLimiter, loginHandler);
```
### 2. Prueba de bloqueo (40–50 min)

```bash
for i in $(seq 1 25); do
  curl -s -o /dev/null -w "$i:%{http_code}\n" -X POST localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@test.local","password":"wrong"}'
done | tail -5
# espera ver 429

printf "\n## Rate limit login\n- window: 15m · max: 20\n- prueba: ver 429 tras N intentos\n- reset dev: reiniciar proceso / redis FLUSH\n" >> projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "fix(m18): l19 rate limit login"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Brute Force + Rate Limiting Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Rate limit activo (artefacto: `commit middleware`).
2. Prueba documentada (artefacto: `commit middleware`).
3. Commit `docs(m18): L19 rate-limiting-en-login-y-endpoints-sensibles`.

## Errores comunes

- Rate limit solo en front.
- Bloqueo permanente sin unlock.

## Siguiente

[L20 — Tests automatizados cross-user (P2 avance)](L20-tests-automatizados-cross-user-p2-avance.md)
