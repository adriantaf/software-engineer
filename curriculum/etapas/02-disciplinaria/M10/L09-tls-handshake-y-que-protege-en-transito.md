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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Describir el handshake y delimitar el alcance de protección
      en tránsito.


      Sin TLS, cookies de sesión de Vitrina viajan en claro. Con TLS mal
      entendido, crees que ya terminaste AppSec.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura + esquema
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "TLS: handshake y qué protege en tránsito" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: labs/tls-handshake.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt`
    comandoEsperado:
      - >-
        curl -v https://example.com -o /dev/null 2>&1 | tee
        projects/m10-redes/samples/tls-curl.txt
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Describir el handshake y delimitar el alcance de protección en
          tránsito.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ver en curl
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/samples/tls-curl.txt

      ```


      Resalta: ALPN, versión TLS, “SSL certificate verify ok” (o error).
  - id: s7
    tipo: explicacion
    titulo: 3. Alcance
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
