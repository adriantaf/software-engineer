---
id: L15
materia: M10
orden: 15
titulo: 'CORS, preflight y errores típicos'
horas: 5
semana: 4
lectura: MDN CORS
evidencia: labs/cors.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      CORS no autentica usuarios: solo relaja same-origin en el browser. Hoy lo
      configuras sin abrirlo todo.


      **Objetivo de esta lección:** Documentar preflight y una política CORS
      para panel+API de Vitrina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura MDN
    xp: 10
    cuerpo: |-
      ```bash
      curl -v -X OPTIONS https://httpbin.org/anything \
        -H 'Origin: https://app.agenda.local' \
        -H 'Access-Control-Request-Method: POST' \
        -H 'Access-Control-Request-Headers: content-type,authorization'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Simula preflight
    xp: 10
    cuerpo: |-
      ```bash
      curl -v -X OPTIONS https://httpbin.org/anything \
        -H 'Origin: https://app.agenda.local' \
        -H 'Access-Control-Request-Method: POST' \
        -H 'Access-Control-Request-Headers: content-type,authorization'
      ```

      Anota qué respondería **tu** API (orígenes permitidos, métodos, headers).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «CORS, preflight y errores típicos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de CORS, preflight y
          errores típicos
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

      `curl -v -X OPTIONS https://httpbin.org/anything \`
    comandoEsperado:
      - 'curl -v -X OPTIONS https://httpbin.org/anything \'
      - git add projects/m10-redes/labs/cors.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -v -X OPTIONS https://httpbin.org/anything \'
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
        texto: Documentar preflight y una política CORS para panel+API de Vitrina.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Política producto
    xp: 10
    cuerpo: >-
      En `labs/cors.md`: allowlist de orígenes staging/prod; nunca `*` con
      credentials; cómo fallar cerrado.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/cors.md` explica preflight y configuración segura (sin `*` +
        credentials).
      - >-
        Ejemplo de error de consola típico y cómo lo depurarías con curl
        OPTIONS.
      - 'Commit `docs(m10): l15 cors`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — CORS, preflight y errores típicos

**~5.0 h · Semana 4**

CORS no autentica usuarios: solo relaja same-origin en el browser. Hoy lo configuras sin abrirlo todo.

## Objetivo

Documentar preflight y una política CORS para panel+API de Vitrina.

## Pasos

### 1. Lectura MDN (45 min)

Same-origin; simple request vs preflight; `Access-Control-Allow-Credentials`.

### 2. Simula preflight (45 min)

```bash
curl -v -X OPTIONS https://httpbin.org/anything \
  -H 'Origin: https://app.agenda.local' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type,authorization'
```

Anota qué respondería **tu** API (orígenes permitidos, métodos, headers).

### 3. Política producto (45 min)

En `labs/cors.md`: allowlist de orígenes staging/prod; nunca `*` con credentials; cómo fallar cerrado.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cors.md
git commit -m "docs(m10): l15 cors"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Same-origin policy; ACAO; preflight OPTIONS; credenciales | [MDN · CORS](https://developer.mozilla.org/es/docs/Web/HTTP/CORS) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cors.md` explica preflight y configuración segura (sin `*` + credentials).
2. Ejemplo de error de consola típico y cómo lo depurarías con curl OPTIONS.
3. Commit `docs(m10): l15 cors`.

## Errores comunes

- `Access-Control-Allow-Origin: *` con cookies.
- Desactivar CORS en el navegador “para desarrollar”.
- Confundir CORS con authz de negocio.

## Siguiente

[L16 — Cabeceras de seguridad HTTP](L16-cabeceras-de-seguridad-http.md)
