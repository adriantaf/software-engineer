---
id: L16
materia: M10
orden: 16
titulo: Cabeceras de seguridad HTTP
horas: 5
semana: 4
lectura: 'MDN CSP, HSTS, X-Frame-Options / frame-ancestors'
evidencia: labs/security-headers.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Escribir la política inicial de security headers del
      producto.


      Capa barata y visible. Hoy inventarias headers y dejas una checklist para
      M17/M18.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escaneo
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI https://example.com | sed -n '1,40p'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cabeceras de seguridad HTTP" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/security-headers.md
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

      `curl -sI https://example.com | sed -n '1,40p'`
    comandoEsperado:
      - 'curl -sI https://example.com | sed -n ''1,40p'''
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sI https://example.com | sed -n ''1,40p'''
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Escribir la política inicial de security headers del producto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Checklist Vitrina
    xp: 10
    cuerpo: >-
      En `labs/security-headers.md`, para cada header: valor propuesto + riesgo
      si falta. CSP en modo report-only primero está bien — documéntalo.
  - id: s7
    tipo: explicacion
    titulo: 3. Cierre semana 4
    xp: 10
    cuerpo: 'README: L13–L16 hechos; enlace a cookies/CORS/headers.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/security-headers.md` con checklist de headers y valores iniciales
        para Vitrina.
      - '`curl -sI` contra un sitio real anotando cuáles faltan.'
      - 'Commit `docs(m10): l16 security headers`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Cabeceras de seguridad HTTP

**~5.0 h · Semana 4**

Capa barata y visible. Hoy inventarias headers y dejas una checklist para M17/M18.

## Objetivo

Escribir la política inicial de security headers del producto.

## Pasos

### 1. Escaneo (40 min)

```bash
curl -sI https://example.com | sed -n '1,40p'
```

Busca: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.

### 2. Checklist Vitrina (75 min)

En `labs/security-headers.md`, para cada header: valor propuesto + riesgo si falta. CSP en modo report-only primero está bien — documéntalo.

### 3. Cierre semana 4 (30 min)

README: L13–L16 hechos; enlace a cookies/CORS/headers.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l16 security headers"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | HSTS, CSP, X-Content-Type-Options, Referrer-Policy, frame-ancestors | [MDN · Strict-Transport-Security](https://developer.mozilla.org/es/docs/Web/HTTP/Headers/Strict-Transport-Security) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/security-headers.md` con checklist de headers y valores iniciales para Vitrina.
2. `curl -sI` contra un sitio real anotando cuáles faltan.
3. Commit `docs(m10): l16 security headers`.

## Errores comunes

- CSP `unsafe-inline` eterno “para que cargue”.
- HSTS en localhost de desarrollo sin saber cómo deshacerlo.
- Creer que headers reemplazan authz.

## Siguiente

[L17 — Superficie de ataque: endpoints y datos](L17-superficie-de-ataque-endpoints-y-datos.md)
