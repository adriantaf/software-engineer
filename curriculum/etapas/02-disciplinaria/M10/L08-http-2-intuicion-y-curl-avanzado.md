---
id: L08
materia: M10
orden: 8
titulo: HTTP/2 intuición y curl avanzado
horas: 5
semana: 2
lectura: MDN HTTP/2 + notas Tanenbaum aplicación
evidencia: labs/curl-avanzado.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar timings y, si aplica, que el servidor habla
      HTTP/2.


      Mides antes de opinar. Hoy `curl` deja de ser solo `-v`.
  - id: s2
    tipo: ejemplo
    titulo: 1. Formato de timing
    xp: 10
    cuerpo: >-
      ```bash

      curl -o /dev/null -s -w 'dns:%{time_namelookup} connect:%{time_connect}
      tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total}
      code:%{http_code}\n' \
        https://example.com
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "HTTP/2 intuición y curl avanzado" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/curl-avanzado.md
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

      `curl --http1.1 -sI https://example.com | head -5`
    comandoEsperado:
      - 'curl --http1.1 -sI https://example.com | head -5'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl --http1.1 -sI https://example.com | head -5'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Documentar timings y, si aplica, que el servidor habla HTTP/2.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. HTTP versión
    xp: 10
    cuerpo: >-
      ```bash

      curl --http1.1 -sI https://example.com | head -5

      curl --http2 -sI https://example.com | head -5

      ```


      ¿Aparece `HTTP/2`? Anota. Si no, documenta el límite del servidor — no
      inventes.
  - id: s7
    tipo: explicacion
    titulo: 3. Flags útiles
    xp: 10
    cuerpo: >-
      Practica y anota: `-H`, `-d`, `-X`, `-L` (follow redirect),
      `--fail-with-body` (si tu curl lo tiene), `-A` User-Agent.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/curl-avanzado.md` con timings (`curl -w`) y comparación HTTP/1.1
        vs HTTP/2 si el servidor lo ofrece.
      - Semana 2 consolidada en README (DNS + HTTP).
      - 'Commit `docs(m10): l08 curl avanzado`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — HTTP/2 intuición y curl avanzado

**~5.0 h · Semana 2**

Mides antes de opinar. Hoy `curl` deja de ser solo `-v`.

## Objetivo

Documentar timings y, si aplica, que el servidor habla HTTP/2.

## Pasos

### 1. Formato de timing (45 min)

```bash
curl -o /dev/null -s -w 'dns:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total} code:%{http_code}\n' \
  https://example.com
```

Copia 3 corridas a `labs/curl-avanzado.md` e interpreta cada campo.

### 2. HTTP versión (45 min)

```bash
curl --http1.1 -sI https://example.com | head -5
curl --http2 -sI https://example.com | head -5
```

¿Aparece `HTTP/2`? Anota. Si no, documenta el límite del servidor — no inventes.

### 3. Flags útiles (40 min)

Practica y anota: `-H`, `-d`, `-X`, `-L` (follow redirect), `--fail-with-body` (si tu curl lo tiene), `-A` User-Agent.

### 4. Cierre semana 2 (40 min)

Índice en README: L05–L08 hechos. Checklist P1 sigue abierta hasta TLS.

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l08 curl avanzado"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Multiplexión HTTP/2; curl -w timings; --http1.1 vs --http2 | [MDN · HTTP/2](https://developer.mozilla.org/es/docs/Glossary/HTTP_2) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/curl-avanzado.md` con timings (`curl -w`) y comparación HTTP/1.1 vs HTTP/2 si el servidor lo ofrece.
2. Semana 2 consolidada en README (DNS + HTTP).
3. Commit `docs(m10): l08 curl avanzado`.

## Errores comunes

- Asumir que HTTP/2 “cifra” (sigue necesitando TLS en la práctica web).
- Optimizar micro-timings sin hipótesis.
- Olvidar `-o /dev/null` y llenar el repo de HTML.

## Siguiente

[L09 — TLS: handshake y qué protege en tránsito](L09-tls-handshake-y-que-protege-en-transito.md)
