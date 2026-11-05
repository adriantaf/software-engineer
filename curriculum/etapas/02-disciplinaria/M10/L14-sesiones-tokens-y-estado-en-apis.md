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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar una decisión documentada sesión vs token para el
      piloto single-tenant.


      El panel (origen A) hablará con la API (origen B). Hoy eliges cómo viaja
      la identidad.
  - id: s2
    tipo: ejemplo
    titulo: 1. Modelos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes/labs/sesiones.md
      git commit -m "docs(m10): l14 sesiones tokens"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sesiones, tokens y estado en APIs" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/sesiones.md
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

      `git add projects/m10-redes/labs/sesiones.md`
    comandoEsperado:
      - git add projects/m10-redes/labs/sesiones.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m10-redes/labs/sesiones.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar una decisión documentada sesión vs token para el piloto
          single-tenant.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Amenazas
    xp: 10
    cuerpo: >-
      XSS → robo de token en JS vs cookie HttpOnly; CSRF → SameSite + anti-CSRF;
      replay → TTL corto.
  - id: s7
    tipo: explicacion
    titulo: 3. Decisión piloto
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
