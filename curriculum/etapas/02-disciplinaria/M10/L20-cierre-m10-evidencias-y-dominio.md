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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Auditar P1–P3/proyecto y dejar el README listo para
      revisión.


      Cierras la materia como ingeniero: evidencia en git + dominio oral.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m10-redes -type f | sort
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M10 — evidencias y dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: checklist P1–P3 + proyecto verificados
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

      `find projects/m10-redes -type f | sort`
    comandoEsperado:
      - find projects/m10-redes -type f | sort
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find projects/m10-redes -type f | sort'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Auditar P1–P3/proyecto y dejar el README listo para revisión.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Criterios de dominio
    xp: 10
    cuerpo: |-
      Escribe en `projects/m10-redes/dominio-oral.md` respuestas a:

      1. Depurar un timeout (red vs app)
      2. Explicar TLS sin “magia”
      3. Defender tu mapa de superficie
  - id: s7
    tipo: explicacion
    titulo: 3. README final
    xp: 10
    cuerpo: Checklist con casillas marcadas y rutas exactas.
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
