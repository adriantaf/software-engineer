---
id: L27
materia: M17
orden: 27
titulo: Rate limit en login
horas: 5
semana: 7
lectura: OWASP brute force
evidencia: rate limit middleware
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Limitar intentos login por IP/usuario con respuesta 429
      documentada.


      - rate limit

      - 429

      - login
  - id: s2
    tipo: ejemplo
    titulo: 1. Rate limit login
    xp: 10
    cuerpo: |-
      ```ts
      // p.ej. 5 intentos / 15 min por IP+email en POST /auth/login → 429
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Rate limit en login" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: rate limit middleware
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Rate limit solo en memoria sin doc de
      multi-instancia."
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
        texto: Limitar intentos login por IP/usuario con respuesta 429 documentada.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tests + commit
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- rate-limit
      git add projects/m17-vitrina
      git commit -m "feat(m17): L27 rate limit login"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`POST /auth/login` responde 429 tras ráfaga; test o script lo demuestra.'
      - 'Commit `docs(m17): L27 rate-limit-en-login`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L27 — Rate limit en login

**~5.0 h · Semana 7**

Piloto público en internet necesita mínimo anti-fuerza bruta.

## Objetivo

Limitar intentos login por IP/usuario con respuesta 429 documentada.

## Conceptos clave

- rate limit
- 429
- login

## Pasos (hazlos en orden)

### 1. Rate limit login (70–90 min)

```ts
// p.ej. 5 intentos / 15 min por IP+email en POST /auth/login → 429
```

```bash
for i in $(seq 1 8); do
  curl -sS -o /dev/null -w "%{http_code}\\n" -X POST http://localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@demo.local","password":"wrong"}'
done
# últimos → 429
```

### 2. Tests + commit (40 min)

```bash
npm test -- rate-limit
git add projects/m17-vitrina
git commit -m "feat(m17): L27 rate limit login"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP brute force | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /auth/login` responde 429 tras ráfaga; test o script lo demuestra.
2. Commit `docs(m17): L27 rate-limit-en-login`.

## Errores comunes

- Rate limit solo en memoria sin doc de multi-instancia.
- 429 sin test.

## Siguiente

[L28 — Tests auth en CI o script local reproducible](L28-tests-auth-en-ci-o-script-local-reproducible.md)
