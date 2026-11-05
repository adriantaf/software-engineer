---
id: L09
materia: M10
orden: 9
titulo: 'TLS: handshake y qué protege en tránsito'
horas: 5
semana: 3
lectura: Tanenbaum seguridad/TLS selecto + MDN TLS
evidencia: labs/tls-handshake.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin TLS, cookies de sesión de Vitrina viajan en claro. Con TLS mal
      entendido, crees que ya terminaste AppSec.


      **Objetivo de esta lección:** Describir el handshake y delimitar el
      alcance de protección en tránsito.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura + esquema
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Ver en curl
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt

      ```


      Resalta: ALPN, versión TLS, “SSL certificate verify ok” (o error).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «TLS: handshake y qué protege en tránsito», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de TLS: handshake y qué
          protege en tránsito
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt`
    comandoEsperado:
      - >-
        curl -v https://example.com -o /dev/null 2>&1 | tee
        projects/m10-redes/samples/tls-curl.txt
      - >-
        git add projects/m10-redes/labs/tls-handshake.md
        projects/m10-redes/samples
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt
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
          Describir el handshake y delimitar el alcance de protección en
          tránsito.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Alcance
    xp: 10
    cuerpo: >-
      Tabla “protege / no protege” con ejemplos del producto (eavesdropping en
      café Wi‑Fi vs XSS en el panel).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/tls-handshake.md` explica handshake en lenguaje ingeniero +
        captura `curl -v` con líneas TLS.
      - >-
        Lista explícita: 3 cosas que TLS protege y 3 que no (XSS, IDOR, BD
        robada…).
      - 'Commit `docs(m10): l09 tls handshake`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — TLS: handshake y qué protege en tránsito

**~5.0 h · Semana 3**

Sin TLS, cookies de sesión de Vitrina viajan en claro. Con TLS mal entendido, crees que ya terminaste AppSec.

## Objetivo

Describir el handshake y delimitar el alcance de protección en tránsito.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/tls-handshake.md`: ClientHello → ServerHello/cert → claves → Application Data. Una figura ASCII basta.

### 2. Ver en curl (45 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/samples/tls-curl.txt
```

Resalta: ALPN, versión TLS, “SSL certificate verify ok” (o error).

### 3. Alcance (45 min)

Tabla “protege / no protege” con ejemplos del producto (eavesdropping en café Wi‑Fi vs XSS en el panel).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/tls-handshake.md projects/m10-redes/samples
git commit -m "docs(m10): l09 tls handshake"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Handshake TLS; confidencialidad e integridad en tránsito; qué NO cubre | [MDN · TLS](https://developer.mozilla.org/es/docs/Glossary/TLS) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/tls-handshake.md` explica handshake en lenguaje ingeniero + captura `curl -v` con líneas TLS.
2. Lista explícita: 3 cosas que TLS protege y 3 que **no** (XSS, IDOR, BD robada…).
3. Commit `docs(m10): l09 tls handshake`.

## Errores comunes

- “HTTPS = seguro contra todo”.
- Pensar que el body JSON ya no necesita authz.
- Confundir certificado inválido con “firewall”.

## Siguiente

[L10 — Certificados X.509 y cadena de confianza](L10-certificados-x-509-y-cadena-de-confianza.md)
