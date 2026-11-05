---
id: L20
materia: M10
orden: 20
titulo: Cierre M10 — evidencias y dominio
horas: 5
semana: 5
lectura: Ficha M10 completa
evidencia: checklist P1–P3 + proyecto verificados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la materia como ingeniero: evidencia en git + dominio oral.


      **Objetivo de esta lección:** Auditar P1–P3/proyecto y dejar el README
      listo para revisión.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría
    xp: 10
    cuerpo: >-
      ```bash

      find projects/m10-redes -type f | sort

      ```


      Verifica: labs semana 1–4, tls/certs, cookies/cors/headers, `tcp-echo/`,
      `superficie/`, `amenazas-red.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Criterios de dominio
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): cierre materia"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M10 — evidencias y dominio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M10 — evidencias
          y dominio
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

      `find projects/m10-redes -type f | sort`
    comandoEsperado:
      - find projects/m10-redes -type f | sort
      - git add projects/m10-redes
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find projects/m10-redes -type f | sort'
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
        texto: Auditar P1–P3/proyecto y dejar el README listo para revisión.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M10
    xp: 25
    enunciado: >-
      Cierra **Redes de computadoras** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Labs HTTP/DNS/TLS con curl e inspección de certificados'
      - 'P2: Cliente/servidor TCP simple + diagrama de una request'
      - 'P3: Mapa de superficie de ataque de tu API (puertos, headers, cookies)'
      - 'Proyecto: Documentación de red + amenazas del producto web'
      - checklist P1–P3 + proyecto verificados
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          Checklist P1 labs, P2 tcp-echo, P3 superficie, proyecto amenazas —
          todo enlazado en README.
      - id: r3
        criterio: Auto-respuesta escrita a los 3 criterios de dominio de la ficha M10.
      - id: r4
        criterio: 'Commit `docs(m10): cierre materia`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Checklist P1 labs, P2 tcp-echo, P3 superficie, proyecto amenazas — todo
        enlazado en README.
      - Auto-respuesta escrita a los 3 criterios de dominio de la ficha M10.
      - 'Commit `docs(m10): cierre materia`.'
    siguiente: Materia M10 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Cierre M10 — evidencias y dominio

**~5.0 h · Semana 5**

Cierras la materia como ingeniero: evidencia en git + dominio oral.

## Objetivo

Auditar P1–P3/proyecto y dejar el README listo para revisión.

## Pasos

### 1. Auditoría (60 min)

```bash
find projects/m10-redes -type f | sort
```

Verifica: labs semana 1–4, tls/certs, cookies/cors/headers, `tcp-echo/`, `superficie/`, `amenazas-red.md`.

### 2. Criterios de dominio (60 min)

Escribe en `projects/m10-redes/dominio-oral.md` respuestas a:

1. Depurar un timeout (red vs app)
2. Explicar TLS sin “magia”
3. Defender tu mapa de superficie

### 3. README final (40 min)

Checklist con casillas marcadas y rutas exactas.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): cierre materia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Auditoría de evidencia y criterios de dominio de la ficha | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist P1 labs, P2 tcp-echo, P3 superficie, proyecto amenazas — todo enlazado en README.
2. Auto-respuesta escrita a los 3 criterios de dominio de la ficha M10.
3. Commit `docs(m10): cierre materia`.

## Errores comunes

- Marcar dominio sin poder explicar TLS en voz alta.
- Evidencia solo en la cabeza / Discord.
- Dejar `tcp-echo` sin README de uso.

## Siguiente

Cierra la [ficha M10](../M10-redes.md). Siguiente: [M11 — Sistemas operativos](../M11-sistemas-operativos.md).
