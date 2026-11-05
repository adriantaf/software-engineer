---
id: L10
materia: M10
orden: 10
titulo: Certificados X.509 y cadena de confianza
horas: 5
semana: 3
lectura: Tanenbaum PKI intro + MDN certificados
evidencia: labs/certificados.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El navegador no “confía en example.com”: confía en una CA que firmó un
      leaf con SAN correcto.


      **Objetivo de esta lección:** Inspeccionar un certificado real y explicar
      la cadena.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: openssl s_client
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \
        | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
      ```


      Pega resultado anotado en `labs/certificados.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Cadena
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null |
      head -80

      ```


      Diagrama: leaf → intermediate → root del almacén local.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Certificados X.509 y cadena de confianza», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Certificados X.509 y
          cadena de confianza
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


      `echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \`
    comandoEsperado:
      - >-
        echo | openssl s_client -connect example.com:443 -servername example.com
        2>/dev/null \
      - >-
        echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null
        | head -80
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: echo | openssl s_client -connect example.com:443 -servername
      example.com 2>/dev/null \
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
        texto: Inspeccionar un certificado real y explicar la cadena.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Fallos
    xp: 10
    cuerpo: >-
      Escribe: cert expirado, hostname mismatch, CA desconocida — síntoma en el
      cliente y qué harías en staging de Vitrina.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/certificados.md` con cadena leaf→intermedia→root explicada para un
        sitio real.
      - Salida `openssl s_client` o `curl -v` anotando fechas y SAN.
      - 'Commit `docs(m10): l10 certificados x509`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Certificados X.509 y cadena de confianza

**~5.0 h · Semana 3**

El navegador no “confía en example.com”: confía en una CA que firmó un leaf con SAN correcto.

## Objetivo

Inspeccionar un certificado real y explicar la cadena.

## Pasos

### 1. openssl s_client (60–75 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

Pega resultado anotado en `labs/certificados.md`.

### 2. Cadena (45 min)

```bash
echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null | head -80
```

Diagrama: leaf → intermediate → root del almacén local.

### 3. Fallos (30 min)

Escribe: cert expirado, hostname mismatch, CA desconocida — síntoma en el cliente y qué harías en staging de Vitrina.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/certificados.md
git commit -m "docs(m10): l10 certificados x509"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | X.509, CA intermedia, leaf, validez y CN/SAN | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/certificados.md` con cadena leaf→intermedia→root explicada para un sitio real.
2. Salida `openssl s_client` o `curl -v` anotando fechas y SAN.
3. Commit `docs(m10): l10 certificados x509`.

## Errores comunes

- Confiar en un cert autofirmado en prod “porque es mío”.
- Ignorar SAN y mirar solo CN legacy.
- Subir claves privadas al repo.

## Siguiente

[L11 — Lab openssl y pinning conceptual](L11-lab-openssl-y-pinning-conceptual.md)
