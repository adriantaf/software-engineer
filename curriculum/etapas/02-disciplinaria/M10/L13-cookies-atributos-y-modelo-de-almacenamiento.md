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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La sesión del dueño del salón vivirá en cookies o en headers. Hoy eliges
      atributos a conciencia.


      **Objetivo de esta lección:** Documentar el modelo de cookie de sesión
      para Vitrina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura MDN
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI https://example.com | grep -i set-cookie || true
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Lab observación
    xp: 10
    cuerpo: >-
      ```bash

      curl -sI https://example.com | grep -i set-cookie || true

      ```


      Si no hay cookies, inventa un ejemplo realista en la bitácora y analiza
      cada flag.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cookies: atributos y modelo de almacenamiento», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cookies: atributos y
          modelo de almacena…
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

      `curl -sI https://example.com | grep -i set-cookie || true`
    comandoEsperado:
      - 'curl -sI https://example.com | grep -i set-cookie || true'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sI https://example.com | grep -i set-cookie || true'
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
        texto: Documentar el modelo de cookie de sesión para Vitrina.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Decisión producto
    xp: 10
    cuerpo: >-
      En `labs/cookies.md`: Justifica cada flag para owner/staff. Contrasta con
      token en `Authorization` header.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
