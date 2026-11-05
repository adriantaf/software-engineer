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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Inspeccionar un certificado real y explicar la cadena.


      El navegador no “confía en example.com”: confía en una CA que firmó un
      leaf con SAN correcto.
  - id: s2
    tipo: ejemplo
    titulo: 1. openssl s_client
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \
        | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Certificados X.509 y cadena de confianza" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: labs/certificados.md
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


      `echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \`
    comandoEsperado:
      - >-
        echo | openssl s_client -connect example.com:443 -servername example.com
        2>/dev/null \
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: echo | openssl s_client -connect example.com:443 -servername
      example.com 2>/dev/null \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Inspeccionar un certificado real y explicar la cadena.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Cadena
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null |
      head -80

      ```


      Diagrama: leaf → intermediate → root del almacén local.
  - id: s7
    tipo: explicacion
    titulo: 3. Fallos
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
