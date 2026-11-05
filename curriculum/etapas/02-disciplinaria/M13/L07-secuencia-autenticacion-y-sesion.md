---
id: L07
materia: M13
orden: 7
titulo: 'Secuencia: autenticación y sesión'
horas: 5
semana: 2
lectura: 'Larman: diagramas de secuencia; flujo login/sesión'
evidencia: projects/m13-diseno/diagramas/secuencia-auth.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `diagramas/secuencia-auth.md` con Mermaid del flujo UC-01.


      Sin una secuencia de auth, el resto de diagramas asume magia. Hoy dibujas
      login y validación de sesión.
  - id: s2
    tipo: ejemplo
    titulo: 1. Decide mecanismo
    xp: 10
    cuerpo: |-
      ```mermaid
      sequenceDiagram
        participant U as Browser
        participant API as API
        participant DB as PostgreSQL
        U->>API: POST /auth/login {email, password}
        API->>DB: buscar usuario + verificar hash
        alt ok
          API->>API: crear sesión
          API-->>U: 200 + Set-Cookie HttpOnly
        else credenciales inválidas
          API-->>U: 401
        end
        U->>API: GET /me (Cookie)
        API->>API: validar sesión
        API-->>U: 200 {id, rol}
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Secuencia: autenticación y sesión" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m13-diseno/diagramas/secuencia-auth.md
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
      ¿Es buena práctica en esta lección? “Secuencia donde el browser “guarda el
      rol” y la API confía ciegamente."
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
        texto: '`diagramas/secuencia-auth.md` con Mermaid del flujo UC-01.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Secuencia feliz + fallo
    xp: 10
    cuerpo: |-
      En `diagramas/secuencia-auth.md`:

      ```mermaid
      sequenceDiagram
        participant U as Browser
        participant API as API
        participant DB as PostgreSQL
        U->>API: POST /auth/login {email, password}
        API->>DB: buscar usuario + verificar hash
        alt ok
          API->>API: crear sesión
          API-->>U: 200 + Set-Cookie HttpOnly
        else credenciales inválidas
          API-->>U: 401
        end
        U->>API: GET /me (Cookie)
        API->>API: validar sesión
        API-->>U: 200 {id, rol}
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Notas de seguridad
    xp: 10
    cuerpo: >-
      Lista bajo el diagrama: password hasheado (nunca en logs), rate limit
      futuro, no revelar “email no existe” vs “password mal” si tu amenaza lo
      pide (o documenta el trade-off UX).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `secuencia-auth.md` muestra participantes Browser, API, Store/DB y pasos
        de login OK + fallo.
      - 'Queda explícito dónde se crea/valida la sesión (API, no solo front).'
      - 'Commit `docs(m13): secuencia autenticacion y sesion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Secuencia: autenticación y sesión

**~5.0 h · Semana 2**

Sin una secuencia de auth, el resto de diagramas asume magia. Hoy dibujas login y validación de sesión.

## Objetivo

`diagramas/secuencia-auth.md` con Mermaid del flujo UC-01.

## Pasos (hazlos en orden)

### 1. Decide mecanismo (20–30 min)

Piloto recomendado: **sesión server-side o cookie firmada HttpOnly**. Anótalo; el ADR formal es L16.

### 2. Secuencia feliz + fallo (80–100 min)

En `diagramas/secuencia-auth.md`:

```mermaid
sequenceDiagram
  participant U as Browser
  participant API as API
  participant DB as PostgreSQL
  U->>API: POST /auth/login {email, password}
  API->>DB: buscar usuario + verificar hash
  alt ok
    API->>API: crear sesión
    API-->>U: 200 + Set-Cookie HttpOnly
  else credenciales inválidas
    API-->>U: 401
  end
  U->>API: GET /me (Cookie)
  API->>API: validar sesión
  API-->>U: 200 {id, rol}
```

### 3. Notas de seguridad (40 min)

Lista bajo el diagrama: password hasheado (nunca en logs), rate limit futuro, no revelar “email no existe” vs “password mal” si tu amenaza lo pide (o documenta el trade-off UX).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/secuencia-auth.md
git commit -m "docs(m13): secuencia autenticacion y sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Secuencia UML: login, cookie/sesión, fallo 401 | [Mermaid — sequenceDiagram](https://mermaid.js.org/syntax/sequenceDiagram.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `secuencia-auth.md` muestra participantes Browser, API, Store/DB y pasos de login OK + fallo.
2. Queda explícito dónde se crea/valida la sesión (API, no solo front).
3. Commit `docs(m13): secuencia autenticacion y sesion`.

## Errores comunes

- Secuencia donde el browser “guarda el rol” y la API confía ciegamente.
- Olvidar el camino de credenciales inválidas.
- Tokens en localStorage sin justificación (si eliges cookie, dilo en el diagrama).

## Siguiente

[L08 — Secuencia: crear pedido (P2)](L08-secuencia-crear-pedido-p2.md)
