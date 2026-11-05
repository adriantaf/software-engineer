---
id: L13
materia: M10
orden: 13
titulo: 'Cookies: atributos y modelo de almacenamiento'
horas: 5
semana: 4
lectura: MDN Cookies (ES)
evidencia: labs/cookies.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar el modelo de cookie de sesión para Vitrina.


      La sesión del dueño del salón vivirá en cookies o en headers. Hoy eliges
      atributos a conciencia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura MDN
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI https://example.com | grep -i set-cookie || true
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cookies: atributos y modelo de almacenamiento" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: labs/cookies.md
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

      `curl -sI https://example.com | grep -i set-cookie || true`
    comandoEsperado:
      - 'curl -sI https://example.com | grep -i set-cookie || true'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sI https://example.com | grep -i set-cookie || true'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Documentar el modelo de cookie de sesión para Vitrina.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Lab observación
    xp: 10
    cuerpo: >-
      ```bash

      curl -sI https://example.com | grep -i set-cookie || true

      ```


      Si no hay cookies, inventa un ejemplo realista en la bitácora y analiza
      cada flag.
  - id: s7
    tipo: ejemplo
    titulo: 3. Decisión producto
    xp: 10
    cuerpo: |-
      ```text
      Set-Cookie: session=…; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=…
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/cookies.md` tabla de atributos con decisión recomendada para
        sesión Vitrina.
      - Ejemplo `Set-Cookie` redactado (valores ficticios).
      - 'Commit `docs(m10): l13 cookies`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Cookies: atributos y modelo de almacenamiento

**~5.0 h · Semana 4**

La sesión del dueño del salón vivirá en cookies o en headers. Hoy eliges atributos a conciencia.

## Objetivo

Documentar el modelo de cookie de sesión para Vitrina.

## Pasos

### 1. Lectura MDN (50 min)

Subraya Secure, HttpOnly, SameSite=Lax/Strict/None, Domain, Path, Max-Age vs Expires.

### 2. Lab observación (40 min)

```bash
curl -sI https://example.com | grep -i set-cookie || true
```

Si no hay cookies, inventa un ejemplo realista en la bitácora y analiza cada flag.

### 3. Decisión producto (60 min)

En `labs/cookies.md`:

```text
Set-Cookie: session=…; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=…
```

Justifica cada flag para owner/staff. Contrasta con token en `Authorization` header.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cookies.md
git commit -m "docs(m10): l13 cookies"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Set-Cookie; Secure, HttpOnly, SameSite, Path, Domain, Max-Age | [MDN · HTTP cookies](https://developer.mozilla.org/es/docs/Web/HTTP/Cookies) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cookies.md` tabla de atributos con decisión recomendada para sesión Vitrina.
2. Ejemplo `Set-Cookie` redactado (valores ficticios).
3. Commit `docs(m10): l13 cookies`.

## Errores comunes

- Cookie de sesión sin `Secure`/`HttpOnly` en prod.
- `SameSite=None` sin entender CSRF.
- Guardar access tokens de larga vida en `localStorage` “porque es más fácil”.

## Siguiente

[L14 — Sesiones, tokens y estado en APIs](L14-sesiones-tokens-y-estado-en-apis.md)
