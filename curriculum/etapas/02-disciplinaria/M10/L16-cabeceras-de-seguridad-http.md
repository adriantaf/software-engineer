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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Capa barata y visible. Hoy inventarias headers y dejas una checklist para
      M17/M18.


      **Objetivo de esta lección:** Escribir la política inicial de security
      headers del producto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escaneo
    xp: 10
    cuerpo: >-
      ```bash

      curl -sI https://example.com | sed -n '1,40p'

      ```


      Busca: `Strict-Transport-Security`, `Content-Security-Policy`,
      `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`,
      `Permissions-Policy`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Checklist Vitrina
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l16 security headers"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cabeceras de seguridad HTTP», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cabeceras de seguridad
          HTTP
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

      `curl -sI https://example.com | sed -n '1,40p'`
    comandoEsperado:
      - 'curl -sI https://example.com | sed -n ''1,40p'''
      - git add projects/m10-redes
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sI https://example.com | sed -n ''1,40p'''
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
        texto: Escribir la política inicial de security headers del producto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cierre semana 4
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
