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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Mides antes de opinar. Hoy `curl` deja de ser solo `-v`.


      **Objetivo de esta lección:** Documentar timings y, si aplica, que el
      servidor habla HTTP/2.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Formato de timing
    xp: 10
    cuerpo: >-
      ```bash

      curl -o /dev/null -s -w 'dns:%{time_namelookup} connect:%{time_connect}
      tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total}
      code:%{http_code}\n' \
        https://example.com
      ```


      Copia 3 corridas a `labs/curl-avanzado.md` e interpreta cada campo.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: HTTP versión
    xp: 10
    cuerpo: >-
      ```bash

      curl --http1.1 -sI https://example.com | head -5

      curl --http2 -sI https://example.com | head -5

      ```


      ¿Aparece `HTTP/2`? Anota. Si no, documenta el límite del servidor — no
      inventes.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «HTTP/2 intuición y curl avanzado», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de HTTP/2 intuición y curl
          avanzado
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

      `curl --http1.1 -sI https://example.com | head -5`
    comandoEsperado:
      - 'curl --http1.1 -sI https://example.com | head -5'
      - 'curl --http2 -sI https://example.com | head -5'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl --http1.1 -sI https://example.com | head -5'
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
        texto: 'Documentar timings y, si aplica, que el servidor habla HTTP/2.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Flags útiles
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
