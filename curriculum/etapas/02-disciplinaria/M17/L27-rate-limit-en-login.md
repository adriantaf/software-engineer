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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - rate limit

      - 429

      - login


      **Objetivo de esta lección:** Limitar intentos login por IP/usuario con
      respuesta 429 documentada.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Rate limit login
    xp: 10
    cuerpo: |-
      ```ts
      // p.ej. 5 intentos / 15 min por IP+email en POST /auth/login → 429
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tests + commit
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- rate-limit
      git add projects/m17-vitrina
      git commit -m "feat(m17): L27 rate limit login"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Rate limit en login», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Rate limit en login
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Rate limit solo en memoria sin doc de
      multi-instancia."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Limitar intentos login por IP/usuario con respuesta 429 documentada.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “429 sin test."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`POST /auth/login` responde 429 tras ráfaga; test o script lo demuestra.'
      - 'Commit `docs(m17): L27 rate-limit-en-login`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
