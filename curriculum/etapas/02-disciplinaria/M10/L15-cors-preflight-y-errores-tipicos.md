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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar preflight y una política CORS para panel+API de
      Vitrina.


      CORS no autentica usuarios: solo relaja same-origin en el browser. Hoy lo
      configuras sin abrirlo todo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura MDN
    xp: 10
    cuerpo: |-
      ```bash
      curl -v -X OPTIONS https://httpbin.org/anything \
        -H 'Origin: https://app.agenda.local' \
        -H 'Access-Control-Request-Method: POST' \
        -H 'Access-Control-Request-Headers: content-type,authorization'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "CORS, preflight y errores típicos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/cors.md
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

      `curl -v -X OPTIONS https://httpbin.org/anything \`
    comandoEsperado:
      - 'curl -v -X OPTIONS https://httpbin.org/anything \'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -v -X OPTIONS https://httpbin.org/anything \'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Documentar preflight y una política CORS para panel+API de Vitrina.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Simula preflight
    xp: 10
    cuerpo: |-
      ```bash
      curl -v -X OPTIONS https://httpbin.org/anything \
        -H 'Origin: https://app.agenda.local' \
        -H 'Access-Control-Request-Method: POST' \
        -H 'Access-Control-Request-Headers: content-type,authorization'
      ```

      Anota qué respondería **tu** API (orígenes permitidos, métodos, headers).
  - id: s7
    tipo: explicacion
    titulo: 3. Política producto
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
