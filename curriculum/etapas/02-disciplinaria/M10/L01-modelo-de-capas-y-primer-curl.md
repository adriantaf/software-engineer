---
id: L01
materia: M10
orden: 1
titulo: Modelo de capas y primer curl
horas: 5
semana: 1
lectura: 'Tanenbaum: intro + capas (modelo OSI/TCP simplificado)'
evidencia: projects/m10-redes/labs/dia1.md + curl -v log
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin mapa de capas, cada error de red se vuelve “el Wi‑Fi está mal”. Hoy
      fijas el diagrama mental que usarás hasta M18.


      **Objetivo de esta lección:** Dejar `projects/m10-redes/` con un lab día
      1: modelo de 5 capas + evidencia de `curl -v` sobre HTTPS.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Revisa el scaffold
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m10-redes
      cat projects/m10-redes/README.md
      mkdir -p projects/m10-redes/{labs,tcp-echo,superficie,samples}
      ```

      No borres la estructura; amplíala.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Modelo de 5 capas
    xp: 10
    cuerpo: >-
      ```bash

      curl -v https://example.com -o /dev/null 2>&1 | tee
      projects/m10-redes/labs/curl-example.log

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Modelo de capas y primer curl», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Modelo de capas y
          primer curl
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

      `ls projects/m10-redes`
    comandoEsperado:
      - ls projects/m10-redes
      - cat projects/m10-redes/README.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: ls projects/m10-redes'
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
          Dejar `projects/m10-redes/` con un lab día 1: modelo de 5 capas +
          evidencia de `curl -v` sobre HTTPS.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Primer `curl -v`
    xp: 10
    cuerpo: >-
      En `dia1.md`, tabla de 4 filas: línea del log → capa → qué significa.
      Compara también: ¿Hay redirección a HTTPS? Anótalo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m10-redes/labs/dia1.md` con diagrama ASCII de 5 capas y qué ve
        `curl -v`.
      - >-
        Log `labs/curl-example.log` (o fragmento anotado) con líneas de
        DNS/TCP/TLS/HTTP resaltadas.
      - 'Commit `docs(m10): l01 capas y primer curl`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Modelo de capas y primer curl

**~5.0 h · Semana 1**

Sin mapa de capas, cada error de red se vuelve “el Wi‑Fi está mal”. Hoy fijas el diagrama mental que usarás hasta M18.

## Objetivo

Dejar `projects/m10-redes/` con un lab día 1: modelo de 5 capas + evidencia de `curl -v` sobre HTTPS.

## Pasos (hazlos en orden)

### 1. Revisa el scaffold (15 min)

```bash
ls projects/m10-redes
cat projects/m10-redes/README.md
mkdir -p projects/m10-redes/{labs,tcp-echo,superficie,samples}
```

No borres la estructura; amplíala.

### 2. Modelo de 5 capas (45–60 min)

En `projects/m10-redes/labs/dia1.md` dibuja ASCII (o Mermaid) con:

1. Aplicación (HTTP)
2. Transporte (TCP/UDP + puerto)
3. Red (IP)
4. Enlace
5. Física (una línea)

Anota **encapsulación**: header de cada capa envuelve el payload de arriba.

### 3. Primer `curl -v` (60–75 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/labs/curl-example.log
```

En `dia1.md`, tabla de 4 filas: línea del log → capa → qué significa. Compara también:

```bash
curl -v http://example.com -o /dev/null 2>&1 | head -40
```

¿Hay redirección a HTTPS? Anótalo.

### 4. Vitrina (20 min)

Párrafo: cuando el panel de Vitrina llame a `https://api…/pedidos`, ¿qué capas deben funcionar antes de que el JSON exista?

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l01 capas y primer curl"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Intro + encapsulación; mapa de 5 capas hacia HTTP | [MDN · Overview of HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Overview) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m10-redes/labs/dia1.md` con diagrama ASCII de 5 capas y qué ve `curl -v`.
2. Log `labs/curl-example.log` (o fragmento anotado) con líneas de DNS/TCP/TLS/HTTP resaltadas.
3. Commit `docs(m10): l01 capas y primer curl`.

## Errores comunes

- Pegar 200 líneas de curl sin marcar qué capa es cada bloque.
- Decir “HTTPS = la app ya es segura” (XSS/IDOR siguen vivos).
- Confundir TLS con cifrado en reposo de la BD.

## Siguiente

[L02 — IP, direccionamiento y enrutamiento intro](L02-ip-direccionamiento-y-enrutamiento-intro.md)
