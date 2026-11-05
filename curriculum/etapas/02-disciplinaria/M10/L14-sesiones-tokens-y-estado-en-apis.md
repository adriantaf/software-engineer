---
id: L14
materia: M10
orden: 14
titulo: 'Sesiones, tokens y estado en APIs'
horas: 5
semana: 4
lectura: MDN Web Storage vs cookies + OAuth2 vista alta
evidencia: labs/sesiones.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El panel (origen A) hablará con la API (origen B). Hoy eliges cómo viaja
      la identidad.


      **Objetivo de esta lección:** Dejar una decisión documentada sesión vs
      token para el piloto single-tenant.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Modelos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes/labs/sesiones.md
      git commit -m "docs(m10): l14 sesiones tokens"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Amenazas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes/labs/sesiones.md
      git commit -m "docs(m10): l14 sesiones tokens"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sesiones, tokens y estado en APIs», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Sesiones, tokens y
          estado en APIs
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

      `git add projects/m10-redes/labs/sesiones.md`
    comandoEsperado:
      - git add projects/m10-redes/labs/sesiones.md
      - 'git commit -m "docs(m10): l14 sesiones tokens"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m10-redes/labs/sesiones.md'
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
          Dejar una decisión documentada sesión vs token para el piloto
          single-tenant.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Decisión piloto
    xp: 10
    cuerpo: >-
      Elige **un** modelo para M17 y escribe “por qué”. Anota qué cambia cuando
      llegue multi-tenant (M19+).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/sesiones.md` compara sesión+cookie vs Bearer token para Vitrina
        (pros/contras).
      - 'Diagrama: browser → API → store de sesión/Redis/PG.'
      - 'Commit `docs(m10): l14 sesiones tokens`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Sesiones, tokens y estado en APIs

**~5.0 h · Semana 4**

El panel (origen A) hablará con la API (origen B). Hoy eliges cómo viaja la identidad.

## Objetivo

Dejar una decisión documentada sesión vs token para el piloto single-tenant.

## Pasos

### 1. Modelos (50 min)

En `labs/sesiones.md`: (1) session id opaco en cookie HttpOnly; (2) access token Bearer; (3) híbrido access corto + refresh.

### 2. Amenazas (40 min)

XSS → robo de token en JS vs cookie HttpOnly; CSRF → SameSite + anti-CSRF; replay → TTL corto.

### 3. Decisión piloto (50 min)

Elige **un** modelo para M17 y escribe “por qué”. Anota qué cambia cuando llegue multi-tenant (M19+).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/sesiones.md
git commit -m "docs(m10): l14 sesiones tokens"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Sesión server-side vs JWT/opaque token; dónde vive el estado | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/sesiones.md` compara sesión+cookie vs Bearer token para Vitrina (pros/contras).
2. Diagrama: browser → API → store de sesión/Redis/PG.
3. Commit `docs(m10): l14 sesiones tokens`.

## Errores comunes

- JWT eterno en localStorage sin rotación ni revoke.
- Mezclar “stateless” con “sin authz”.
- Olvidar logout / invalidación.

## Siguiente

[L15 — CORS, preflight y errores típicos](L15-cors-preflight-y-errores-tipicos.md)
