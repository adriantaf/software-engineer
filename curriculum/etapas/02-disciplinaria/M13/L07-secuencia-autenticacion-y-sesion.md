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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin una secuencia de auth, el resto de diagramas asume magia. Hoy dibujas
      login y validación de sesión.


      **Objetivo de esta lección:** `diagramas/secuencia-auth.md` con Mermaid
      del flujo UC-01.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Decide mecanismo
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Secuencia feliz + fallo
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

      En `diagramas/secuencia-auth.md`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Secuencia: autenticación y sesión», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Secuencia:
          autenticación y sesión
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
      ¿Es recomendable en esta lección? “Secuencia donde el browser “guarda el
      rol” y la API confía ciegamente."
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
        texto: '`diagramas/secuencia-auth.md` con Mermaid del flujo UC-01.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Notas de seguridad
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
